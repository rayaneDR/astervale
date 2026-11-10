// SPDX-License-Identifier: Apache-2.0
package org.astervale.panel;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.provider.Settings;
import android.view.View;
import android.view.WindowInsets;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.Spinner;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

/** Local action panel. No network, shell executor or exported privileged service. */
public final class PanelActivity extends Activity {
    private SharedPreferences preferences;
    private LinearLayout content;
    private EditText packageInput;
    private Spinner profile;
    private Button batteryAction, dndAction, launchAction;
    private boolean enabled;
    private static final String[] PROFILE_IDS = {"balanced", "battery", "gaming"};

    @Override public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        preferences = getSharedPreferences("panel", MODE_PRIVATE);
        enabled = preferences.getBoolean("local_assistant", false);
        getWindow().setDecorFitsSystemWindows(false);
        ScrollView scroll = new ScrollView(this);
        content = new LinearLayout(this);
        content.setOrientation(LinearLayout.VERTICAL);
        content.setLayoutDirection(View.LAYOUT_DIRECTION_LOCALE);
        content.setPadding(dp(24), dp(24), dp(24), dp(24));
        scroll.addView(content);
        scroll.setOnApplyWindowInsetsListener((view, insets) -> {
            android.graphics.Insets bars = insets.getInsets(WindowInsets.Type.systemBars() | WindowInsets.Type.ime());
            view.setPadding(bars.left, bars.top, bars.right, bars.bottom);
            return insets;
        });
        setContentView(scroll);
        text(R.string.app_name, 24);
        text(R.string.title, 32);
        text(R.string.untested, 14);
        text(R.string.profile, 20);
        packageInput = new EditText(this);
        packageInput.setHint(R.string.package_hint);
        packageInput.setSingleLine(true);
        packageInput.setInputType(android.text.InputType.TYPE_CLASS_TEXT | android.text.InputType.TYPE_TEXT_VARIATION_VISIBLE_PASSWORD);
        add(packageInput);
        profile = new Spinner(this);
        profile.setAdapter(new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item,
            new String[]{getString(R.string.balanced), getString(R.string.battery), getString(R.string.gaming)}));
        add(profile);
        button(R.string.save_profile, () -> {
            String target = validPackage();
            if (target == null) return;
            preferences.edit().putString("profile:" + target, PROFILE_IDS[profile.getSelectedItemPosition()]).apply();
            toast(R.string.saved);
        });
        text(R.string.profile_notice, 14);
        Switch consent = new Switch(this);
        consent.setText(R.string.assistant);
        consent.setChecked(enabled);
        add(consent);
        text(R.string.assistant_notice, 14);
        batteryAction = button(R.string.open_battery, () -> propose(R.string.action_battery,
            new Intent(Settings.ACTION_BATTERY_SAVER_SETTINGS)));
        dndAction = button(R.string.open_dnd, () -> propose(R.string.action_dnd,
            new Intent(Settings.ACTION_NOTIFICATION_POLICY_ACCESS_SETTINGS)));
        launchAction = button(R.string.open_app, () -> {
            String target = validPackage();
            if (target == null) return;
            Intent launch = getPackageManager().getLaunchIntentForPackage(target);
            if (launch == null) { toast(R.string.invalid_package); return; }
            propose(R.string.action_launch, launch);
        });
        consent.setOnCheckedChangeListener((v, checked) -> {
            enabled = checked;
            preferences.edit().putBoolean("local_assistant", checked).apply();
            updateActions();
        });
        updateActions();
    }
    private String validPackage() {
        String value = packageInput.getText().toString().trim();
        if (!value.matches("[A-Za-z][A-Za-z0-9_]*(\\.[A-Za-z][A-Za-z0-9_]*)+")
                || getPackageManager().getLaunchIntentForPackage(value) == null) {
            packageInput.setError(getString(R.string.invalid_package)); return null;
        }
        return value;
    }
    private void propose(int explanation, Intent intent) {
        if (!enabled) return;
        // Copy the exact intent before confirmation; no external input or model commands.
        final Intent proposed = new Intent(intent);
        new AlertDialog.Builder(this).setTitle(R.string.action_title)
            .setMessage(getString(explanation) + (proposed.getComponent() == null ? "" : "\n" + proposed.getComponent().getPackageName()))
            .setNegativeButton(R.string.cancel, null)
            .setPositiveButton(R.string.confirm, (dialog, which) -> {
                if (!enabled) return;
                try { startActivity(proposed); }
                catch (ActivityNotFoundException | SecurityException exception) { toast(R.string.unavailable); }
            }).show();
    }
    private void updateActions() {
        batteryAction.setEnabled(enabled); dndAction.setEnabled(enabled); launchAction.setEnabled(enabled);
    }
    private void text(int id, float size) {
        TextView view = new TextView(this); view.setText(id); view.setTextSize(size);
        view.setPadding(0, dp(12), 0, dp(8)); add(view);
    }
    private Button button(int id, Runnable action) {
        Button view = new Button(this); view.setText(id); view.setOnClickListener(v -> action.run()); add(view); return view;
    }
    private void add(View view) {
        LinearLayout.LayoutParams layout = new LinearLayout.LayoutParams(-1, -2);
        layout.bottomMargin = dp(8); view.setMinimumHeight(dp(48)); content.addView(view, layout);
    }
    private int dp(int value) { return Math.round(value * getResources().getDisplayMetrics().density); }
    private void toast(int id) { Toast.makeText(this, id, Toast.LENGTH_LONG).show(); }
}
