// SPDX-License-Identifier: Apache-2.0
package org.astervale.panel;

import android.app.Activity;
import android.content.Intent;
import android.content.pm.ResolveInfo;
import android.os.Bundle;
import android.provider.Settings;
import android.widget.*;
import android.text.Editable;
import android.text.TextWatcher;
import java.text.DateFormat;
import java.util.*;

/** Original lightweight home preview. Base ROM Trebuchet remains available as fallback. */
public final class LayerHomeActivity extends Activity {
    private LinearLayout root, apps;
    @Override public void onCreate(Bundle b){super.onCreate(b);home();}
    private void home(){
        root=Ui.page(this);
        Ui.text(this,root,"AsterVale",18);
        Ui.text(this,root,DateFormat.getTimeInstance(DateFormat.SHORT).format(new Date()),64);
        Ui.text(this,root,DateFormat.getDateInstance(DateFormat.FULL).format(new Date()),16);
        Ui.text(this,root,"A little room to breathe.",28);
        Ui.text(this,root,"Preview layer · hardware untested",14);
        Ui.button(this,root,"All apps",this::drawer);
        Ui.button(this,root,"Rill · local assistant",()->startActivity(new Intent(this,RillActivity.class)));
        Ui.button(this,root,"Game profiles",()->startActivity(new Intent(this,PanelActivity.class)));
        Ui.button(this,root,"System settings",()->startActivity(new Intent(Settings.ACTION_SETTINGS)));
        Ui.button(this,root,"Choose default home",()->startActivity(new Intent(Settings.ACTION_HOME_SETTINGS)));
        Ui.text(this,root,"This original home prototype does not replace SystemUI, lockscreen or the ROM’s Settings app. Switch back to Trebuchet at any time.",14);
    }
    private void drawer(){
        root=Ui.page(this);Ui.text(this,root,"All apps",32);
        Ui.button(this,root,"Home",this::home);
        EditText search=new EditText(this);search.setHint("Search apps");search.setSingleLine(true);root.addView(search);
        apps=new LinearLayout(this);apps.setOrientation(1);root.addView(apps);
        Intent query=new Intent(Intent.ACTION_MAIN).addCategory(Intent.CATEGORY_LAUNCHER);
        List<ResolveInfo> installed=new ArrayList<>(getPackageManager().queryIntentActivities(query,0));
        installed.sort(new ResolveInfo.DisplayNameComparator(getPackageManager()));
        Runnable populate=()->{
            apps.removeAllViews();String term=search.getText().toString().toLowerCase(Locale.ROOT);
            for(ResolveInfo info:installed){String label=info.loadLabel(getPackageManager()).toString();if(!label.toLowerCase(Locale.ROOT).contains(term))continue;
                Ui.button(this,apps,label,()->{Intent i=new Intent(Intent.ACTION_MAIN).addCategory(Intent.CATEGORY_LAUNCHER).setClassName(info.activityInfo.packageName,info.activityInfo.name);try{startActivity(i);}catch(RuntimeException e){Toast.makeText(this,"App unavailable",Toast.LENGTH_SHORT).show();}});
            }
        };
        search.addTextChangedListener(new TextWatcher(){public void beforeTextChanged(CharSequence s,int st,int c,int a){}public void onTextChanged(CharSequence s,int st,int before,int count){populate.run();}public void afterTextChanged(Editable e){}});
        populate.run();
    }
}
