// SPDX-License-Identifier: Apache-2.0
package org.astervale.panel;

import android.Manifest;
import android.app.*;
import android.content.*;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.*;
import android.provider.*;
import android.speech.*;
import android.speech.tts.*;
import android.widget.*;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

/** Offline rule assistant. No INTERNET permission, no screen/notification access. */
public final class RillActivity extends Activity implements RecognitionListener {
    private LinearLayout page;
    private TextView transcript, usage;
    private EditText input;
    private Spinner language, character;
    private SeekBar bubbleSize, bubbleOpacity;
    private IntentEngine engine;
    private SpeechRecognizer recognizer;
    private TextToSpeech tts;
    private boolean ttsReady;
    private IntentEngine.Result pending;
    private final StringBuilder history=new StringBuilder();
    private static final String[] LOCALES={"en","ar","ary","ary-Latn","fr","es","pt","ru","tr","hi","zh"};
    private static final String[] NAMES={"English","العربية","الدارجة المغربية","Darija · Arabizi","Français","Español","Português","Русский","Türkçe","हिन्दी","中文"};
    @Override public void onCreate(Bundle b){
        super.onCreate(b);
        page=Ui.page(this);
        Ui.text(this,page,"Rill",38);
        Ui.text(this,page,"A little help. On your terms.",18);
        Ui.text(this,page,"Local command router · no cloud · Android behavior untested",13);
        try{engine=new IntentEngine(new InputStreamReader(getAssets().open("commands.tsv"),StandardCharsets.UTF_8));}
        catch(IOException e){Ui.text(this,page,"Command data unavailable. No actions enabled.",16);return;}
        language=new Spinner(this);language.setAdapter(new ArrayAdapter<>(this,android.R.layout.simple_spinner_dropdown_item,NAMES));page.addView(language);
        input=new EditText(this);input.setHint("Type a phone command in your language");input.setMinLines(2);page.addView(input);
        Ui.button(this,page,"Review command",()->handle(input.getText().toString()));
        Ui.button(this,page,"Talk · on-device speech only",this::listen);
        transcript=Ui.text(this,page,"No command yet. History is session-only and can be cleared.",15);
        Ui.button(this,page,"Clear history",()->{history.setLength(0);transcript.setText("");pending=null;});
        Ui.text(this,page,"Companion",24);
        Ui.text(this,page,"An optional original character. Draw-over-apps and notification permissions are requested only when you enable it. No accessibility service or screen reading.",14);
        character=new Spinner(this);character.setAdapter(new ArrayAdapter<>(this,android.R.layout.simple_spinner_dropdown_item,new String[]{"Seed","Pebble","Kite"}));page.addView(character);
        Ui.text(this,page,"Bubble size",14);bubbleSize=new SeekBar(this);bubbleSize.setMin(48);bubbleSize.setMax(88);bubbleSize.setProgress(60);page.addView(bubbleSize);
        Ui.text(this,page,"Opacity",14);bubbleOpacity=new SeekBar(this);bubbleOpacity.setMin(35);bubbleOpacity.setMax(100);bubbleOpacity.setProgress(90);page.addView(bubbleOpacity);
        Ui.button(this,page,"Enable / update companion",this::enableBubble);
        Ui.button(this,page,"Hide companion",()->stopService(new Intent(this,BubbleService.class)));
        Ui.text(this,page,"Model manager",24);
        Ui.text(this,page,"No language model is loaded or downloaded. Offline speech depends on an installed on-device recognition service. Downloadable Whisper/Vosk/LLM adapters are not integrated. Darija speech and voices are untested. Cloud mode is absent and off.",14);
        usage=Ui.text(this,page,"",14);refreshUsage();
        Ui.button(this,page,"Refresh memory / battery information",this::refreshUsage);
        tts=new TextToSpeech(this,status->{ttsReady=status==TextToSpeech.SUCCESS;});
    }
    private String preferred(){return LOCALES[language.getSelectedItemPosition()];}
    private void append(String s){history.append(s).append("\n\n");if(history.length()>12000)history.delete(0,history.length()-10000);transcript.setText(history.toString());}
    private void handle(String command){
        if(engine==null)return;
        pending=engine.parse(command,preferred());
        append("You: "+command+"\nRill ["+pending.language()+"]: "+pending.explanation());
        if(pending.action()==IntentEngine.Action.UNKNOWN){speak(pending.explanation(),pending.language());return;}
        final IntentEngine.Result proposed=pending;
        new AlertDialog.Builder(this).setTitle("Review action · "+proposed.action().name())
            .setMessage(proposed.explanation()+"\n\nNo setting changes automatically. Android will show its own controls. Alarm/timer opens its editor without inferred parameters.")
            .setNegativeButton(R.string.cancel,(d,w)->pending=null)
            .setPositiveButton(R.string.confirm,(d,w)->{pending=null;dispatch(proposed);}).show();
    }
    private void dispatch(IntentEngine.Result result){
        Intent action=switch(result.action()){
            case WIFI -> new Intent(Settings.Panel.ACTION_WIFI);
            case BLUETOOTH -> new Intent(Settings.ACTION_BLUETOOTH_SETTINGS);
            case BATTERY -> new Intent(Settings.ACTION_BATTERY_SAVER_SETTINGS);
            case SETTINGS -> new Intent(Settings.ACTION_SETTINGS);
            case BRIGHTNESS -> new Intent(Settings.ACTION_DISPLAY_SETTINGS);
            case VOLUME -> new Intent(Settings.Panel.ACTION_VOLUME);
            case DND -> new Intent(Settings.ACTION_NOTIFICATION_POLICY_ACCESS_SETTINGS);
            case ALARM -> new Intent(AlarmClock.ACTION_SHOW_ALARMS);
            case TIMER -> new Intent(AlarmClock.ACTION_SET_TIMER).putExtra(AlarmClock.EXTRA_SKIP_UI,false);
            default -> null;
        };
        if(action==null)return;
        try{startActivity(action);speak(result.explanation(),result.language());}
        catch(ActivityNotFoundException|SecurityException e){append("Rill: This Android control is unavailable. No action completed.");}
    }
    private void listen(){
        if(!SpeechRecognizer.isOnDeviceRecognitionAvailable(this)){append("Rill: No on-device speech service is installed. Type a command; online speech will not be used.");return;}
        if(checkSelfPermission(Manifest.permission.RECORD_AUDIO)!=PackageManager.PERMISSION_GRANTED){requestPermissions(new String[]{Manifest.permission.RECORD_AUDIO},41);return;}
        if(recognizer!=null){recognizer.cancel();recognizer.destroy();}
        recognizer=SpeechRecognizer.createOnDeviceSpeechRecognizer(this);recognizer.setRecognitionListener(this);
        Intent request=new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            .putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            .putExtra(RecognizerIntent.EXTRA_LANGUAGE,preferred()).putExtra(RecognizerIntent.EXTRA_PREFER_OFFLINE,true);
        append("Rill: Listening once using on-device speech. Selected language: "+preferred());
        try{recognizer.startListening(request);}catch(RuntimeException e){append("Rill: On-device speech could not start. Type instead.");}
    }
    private void speak(String text,String lang){
        if(!ttsReady||tts==null)return;
        Set<Voice> voices=tts.getVoices();if(voices==null)return;
        String requested=Locale.forLanguageTag(lang).getLanguage();
        Voice offline=voices.stream().filter(v->!v.isNetworkConnectionRequired()&&v.getLocale().getLanguage().equals(requested)).findFirst().orElse(null);
        if(offline==null){append("Rill: No installed offline voice for "+lang+". Text response kept in your language.");return;}
        tts.setVoice(offline);tts.speak(text,TextToSpeech.QUEUE_FLUSH,null,"rill-local");
    }
    private void enableBubble(){
        if(!Settings.canDrawOverlays(this)){
            new AlertDialog.Builder(this).setTitle("Allow companion overlay?")
                .setMessage("Rill needs Draw over other apps to show its bubble. It cannot read the screen. Return here and tap Enable after granting it.")
                .setNegativeButton(R.string.cancel,null).setPositiveButton(R.string.confirm,(d,w)->startActivity(new Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION,Uri.parse("package:"+getPackageName())))).show();return;
        }
        if(Build.VERSION.SDK_INT>=33&&checkSelfPermission(Manifest.permission.POST_NOTIFICATIONS)!=PackageManager.PERMISSION_GRANTED){requestPermissions(new String[]{Manifest.permission.POST_NOTIFICATIONS},42);return;}
        Intent start=new Intent(this,BubbleService.class).putExtra("size",bubbleSize.getProgress()).putExtra("opacity",bubbleOpacity.getProgress()).putExtra("character",character.getSelectedItemPosition());
        try{startForegroundService(start);}catch(RuntimeException e){append("Rill: Companion could not start. Check system overlay/background restrictions.");}
    }
    private void refreshUsage(){
        android.os.Debug.MemoryInfo info=new android.os.Debug.MemoryInfo();android.os.Debug.getMemoryInfo(info);
        usage.setText("Current app-process PSS: "+info.getTotalPss()+" KiB. Includes UI and companion (same process). Sample at "+java.text.DateFormat.getTimeInstance().format(new Date())+".\nCompanion-specific battery cost: unmeasured. CPU/FPS/temperature: unmeasured. No zero-drain claim.");
    }
    @Override protected void onStop(){super.onStop();if(recognizer!=null){recognizer.cancel();recognizer.destroy();recognizer=null;}if(tts!=null)tts.stop();}
    @Override protected void onDestroy(){if(recognizer!=null)recognizer.destroy();if(tts!=null){tts.stop();tts.shutdown();}super.onDestroy();}
    @Override public void onReadyForSpeech(Bundle p){} @Override public void onBeginningOfSpeech(){} @Override public void onRmsChanged(float r){} @Override public void onBufferReceived(byte[] b){} @Override public void onEndOfSpeech(){}
    @Override public void onError(int e){append("Rill: On-device speech error "+e+". No cloud fallback. Type instead.");}
    @Override public void onResults(Bundle results){ArrayList<String> list=results.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION);if(list!=null&&!list.isEmpty()){input.setText(list.get(0));handle(list.get(0));}}
    @Override public void onPartialResults(Bundle p){} @Override public void onEvent(int t,Bundle p){}
}
