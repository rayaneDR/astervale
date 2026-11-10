// SPDX-License-Identifier: Apache-2.0
package org.astervale.panel;
import android.app.Activity;
import android.graphics.Color;
import android.graphics.drawable.GradientDrawable;
import android.view.View;
import android.view.WindowInsets;
import android.widget.*;

final class Ui {
    static final int INK=Color.rgb(32,56,47), BG=Color.rgb(245,241,233), GREEN=Color.rgb(49,91,69);
    static int dp(Activity a,int n){return Math.round(n*a.getResources().getDisplayMetrics().density);}
    static LinearLayout page(Activity a){
        a.getWindow().setDecorFitsSystemWindows(false);
        ScrollView scroll=new ScrollView(a);scroll.setFillViewport(true);scroll.setBackgroundColor(BG);
        LinearLayout box=new LinearLayout(a);box.setOrientation(LinearLayout.VERTICAL);box.setPadding(dp(a,24),dp(a,24),dp(a,24),dp(a,28));scroll.addView(box);
        scroll.setOnApplyWindowInsetsListener((v,i)->{android.graphics.Insets b=i.getInsets(WindowInsets.Type.systemBars()|WindowInsets.Type.ime());v.setPadding(b.left,b.top,b.right,b.bottom);return i;});
        a.setContentView(scroll);return box;
    }
    static TextView text(Activity a,LinearLayout box,String s,int sp){TextView t=new TextView(a);t.setText(s);t.setTextColor(INK);t.setTextSize(sp);t.setPadding(0,dp(a,10),0,dp(a,12));box.addView(t);return t;}
    static Button button(Activity a,LinearLayout box,String s,Runnable r){Button b=new Button(a);b.setText(s);b.setAllCaps(false);b.setMinHeight(dp(a,52));b.setTextColor(INK);LinearLayout.LayoutParams p=new LinearLayout.LayoutParams(-1,-2);p.bottomMargin=dp(a,8);box.addView(b,p);b.setOnClickListener(v->r.run());return b;}
    static GradientDrawable shape(int color,int radius){GradientDrawable d=new GradientDrawable();d.setColor(color);d.setCornerRadius(radius);return d;}
}
