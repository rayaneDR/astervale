// SPDX-License-Identifier: Apache-2.0
package org.astervale.panel;

import android.app.*;
import android.content.*;
import android.graphics.*;
import android.os.*;
import android.provider.Settings;
import android.view.*;
import android.widget.PopupMenu;

/** Original low-draw-rate companion. No screen access, game detection or microphone. */
public final class BubbleService extends Service {
    private WindowManager manager;
    private WindowManager.LayoutParams layout;
    private Companion view;
    private final Handler handler=new Handler(Looper.getMainLooper());
    private boolean screenOn=true,attached=false;
    private String state="idle";
    private int character=0;
    private final Runnable blink=new Runnable(){public void run(){if(screenOn&&view!=null){view.blink=!view.blink;view.invalidate();handler.postDelayed(this,view.blink?140:5000);}}};
    private final BroadcastReceiver receiver=new BroadcastReceiver(){@Override public void onReceive(Context c,Intent i){
        String a=i.getAction();
        if(Intent.ACTION_SCREEN_OFF.equals(a)){screenOn=false;handler.removeCallbacks(blink);if(view!=null)view.setVisibility(View.GONE);state="sleepy";}
        else if(Intent.ACTION_SCREEN_ON.equals(a)){screenOn=true;state="idle";if(view!=null)view.setVisibility(View.VISIBLE);handler.post(blink);}
        else if(Intent.ACTION_BATTERY_LOW.equals(a)){state="sleepy";if(view!=null)view.invalidate();}
        else if(Intent.ACTION_POWER_CONNECTED.equals(a)){state="happy";if(view!=null)view.invalidate();}
        else if(Intent.ACTION_POWER_DISCONNECTED.equals(a)){state="idle";if(view!=null)view.invalidate();}
    }};
    @Override public void onCreate(){
        super.onCreate();manager=getSystemService(WindowManager.class);
        NotificationManager notifications=getSystemService(NotificationManager.class);
        notifications.createNotificationChannel(new NotificationChannel("companion","Rill companion",NotificationManager.IMPORTANCE_LOW));
        PendingIntent stop=PendingIntent.getService(this,1,new Intent(this,BubbleService.class).setAction("STOP"),PendingIntent.FLAG_IMMUTABLE|PendingIntent.FLAG_UPDATE_CURRENT);
        PendingIntent open=PendingIntent.getActivity(this,2,new Intent(this,RillActivity.class),PendingIntent.FLAG_IMMUTABLE|PendingIntent.FLAG_UPDATE_CURRENT);
        startForeground(17,new Notification.Builder(this,"companion").setSmallIcon(android.R.drawable.ic_dialog_info).setContentTitle("Rill companion is visible").setContentText("No screen reading or continuous microphone. Tap Stop to hide.").setContentIntent(open).addAction(new Notification.Action.Builder(null,"Stop",stop).build()).setOngoing(true).build());
        IntentFilter f=new IntentFilter();f.addAction(Intent.ACTION_SCREEN_OFF);f.addAction(Intent.ACTION_SCREEN_ON);f.addAction(Intent.ACTION_BATTERY_LOW);f.addAction(Intent.ACTION_POWER_CONNECTED);f.addAction(Intent.ACTION_POWER_DISCONNECTED);
        if(Build.VERSION.SDK_INT>=33)registerReceiver(receiver,f,Context.RECEIVER_NOT_EXPORTED);else registerReceiver(receiver,f);
    }
    @Override public int onStartCommand(Intent intent,int flags,int id){
        if(intent==null||"STOP".equals(intent.getAction())||!Settings.canDrawOverlays(this)){stopSelf();return START_NOT_STICKY;}
        character=Math.max(0,Math.min(2,intent.getIntExtra("character",0)));
        int size=Math.max(48,Math.min(88,intent.getIntExtra("size",60)));
        int pixels=Math.round(size*getResources().getDisplayMetrics().density);
        if(attached){manager.removeView(view);attached=false;}
        layout=new WindowManager.LayoutParams(pixels,pixels,WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY,WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE,PixelFormat.TRANSLUCENT);
        layout.gravity=Gravity.TOP|Gravity.LEFT;layout.x=8;layout.y=240;
        layout.alpha=Math.max(.35f,Math.min(1f,intent.getIntExtra("opacity",90)/100f));
        view=new Companion();view.setContentDescription("Rill companion. Tap to open, drag to move, long press for state menu, double tap to hide.");
        try{manager.addView(view,layout);attached=true;handler.removeCallbacks(blink);handler.postDelayed(blink,5000);}catch(RuntimeException e){stopSelf();}
        return START_NOT_STICKY;
    }
    private void menu(){
        PopupMenu menu=new PopupMenu(this,view);String[] options={"Open Rill","Hide companion","Idle","Listening (visual demo)","Thinking (visual demo)","Speaking (visual demo)","Happy","Sleepy"};
        for(int n=0;n<options.length;n++)menu.getMenu().add(0,n,n,options[n]);
        menu.setOnMenuItemClickListener(item->{int n=item.getItemId();if(n==0)open();else if(n==1)stopSelf();else{state=new String[]{"idle","listening","thinking","speaking","happy","sleepy"}[n-2];view.invalidate();}return true;});menu.show();
    }
    private void open(){startActivity(new Intent(this,RillActivity.class).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK));}
    private final class Companion extends View {
        private final Paint paint=new Paint(Paint.ANTI_ALIAS_FLAG);
        boolean blink=false;
        private float downX,downY;private int startX,startY;private boolean dragged;
        private final GestureDetector gestures;
        Companion(){super(BubbleService.this);setImportantForAccessibility(View.IMPORTANT_FOR_ACCESSIBILITY_YES);setFocusable(true);
            gestures=new GestureDetector(BubbleService.this,new GestureDetector.SimpleOnGestureListener(){
                @Override public boolean onDown(MotionEvent e){return true;}
                @Override public boolean onSingleTapConfirmed(MotionEvent e){if(!dragged){performClick();open();}return true;}
                @Override public boolean onDoubleTap(MotionEvent e){stopSelf();return true;}
                @Override public void onLongPress(MotionEvent e){if(!dragged)menu();}
            });
        }
        @Override public boolean performClick(){super.performClick();return true;}
        @Override public boolean onTouchEvent(MotionEvent e){
            if(e.getActionMasked()==MotionEvent.ACTION_DOWN){downX=e.getRawX();downY=e.getRawY();startX=layout.x;startY=layout.y;dragged=false;}
            if(e.getActionMasked()==MotionEvent.ACTION_MOVE){float dx=e.getRawX()-downX,dy=e.getRawY()-downY;if(Math.hypot(dx,dy)>12)dragged=true;if(dragged){Rect bounds=manager.getCurrentWindowMetrics().getBounds();layout.x=Math.max(0,Math.min(bounds.width()-getWidth(),startX+(int)dx));layout.y=Math.max(0,Math.min(bounds.height()-getHeight(),startY+(int)dy));manager.updateViewLayout(this,layout);}}
            if(e.getActionMasked()==MotionEvent.ACTION_UP&&dragged){int width=manager.getCurrentWindowMetrics().getBounds().width();layout.x=layout.x<width/2?0:width-getWidth();manager.updateViewLayout(this,layout);}
            gestures.onTouchEvent(e);return true;
        }
        @Override protected void onDraw(Canvas c){
            super.onDraw(c);float w=getWidth(),h=getHeight();
            paint.setColor(character==1?Color.rgb(175,112,85):character==2?Color.rgb(104,119,152):Ui.GREEN);
            if(character==2){Path k=new Path();k.moveTo(w*.5f,h*.08f);k.lineTo(w*.92f,h*.5f);k.lineTo(w*.5f,h*.92f);k.lineTo(w*.08f,h*.5f);k.close();c.drawPath(k,paint);}else c.drawRoundRect(w*.06f,h*.06f,w*.94f,h*.94f,character==1?w*.3f:w*.42f,h*.42f,paint);
            paint.setColor(Color.rgb(245,241,233));float eyeY=h*.43f;
            if(blink||state.equals("sleepy")){paint.setStrokeWidth(w*.04f);c.drawLine(w*.3f,eyeY,w*.4f,eyeY,paint);c.drawLine(w*.6f,eyeY,w*.7f,eyeY,paint);}else{c.drawCircle(w*.35f,eyeY,w*.045f,paint);c.drawCircle(w*.65f,eyeY,w*.045f,paint);}
            paint.setStyle(Paint.Style.STROKE);paint.setStrokeWidth(w*.03f);
            if(state.equals("speaking")||state.equals("listening"))c.drawOval(w*.43f,h*.56f,w*.57f,h*.7f,paint);
            else c.drawArc(w*.36f,h*.48f,w*.64f,h*.72f,state.equals("happy")?0:20,140,false,paint);
            paint.setStyle(Paint.Style.FILL);
            if(state.equals("thinking")){for(int n=0;n<3;n++)c.drawCircle(w*(.4f+.1f*n),h*.23f,w*.02f,paint);}
        }
    }
    @Override public void onDestroy(){handler.removeCallbacksAndMessages(null);try{unregisterReceiver(receiver);}catch(IllegalArgumentException ignored){}if(attached&&view!=null){manager.removeView(view);attached=false;}stopForeground(STOP_FOREGROUND_REMOVE);super.onDestroy();}
    @Override public IBinder onBind(Intent i){return null;}
}
