// SPDX-License-Identifier: Apache-2.0
import java.nio.file.*;
import org.astervale.panel.IntentEngine;
public final class SafetyTests {
    public static void main(String[] args)throws Exception{
        IntentEngine e=new IntentEngine(Files.newBufferedReader(Path.of(args[0])));
        String[][] negatives={{"en","don't open wifi"},{"en","Open Wi-Fi and Bluetooth"},{"en","Explain the word battery"},{"en","\"open wifi\""},{"ar","لا تشغل الواي فاي"},{"ary","ماتحلش الويفي"},{"ary-Latn","mat 7ell wifi"},{"fr","N’ouvre pas le Wi-Fi"},{"es","No abras Wi-Fi"},{"pt","Não abras o Wi-Fi"},{"ru","Не открывай вайфай"},{"tr","Wifi açma"},{"hi","वाईफाई मत खोलो"},{"zh","不要打开无线网络"}};
        for(String[] p:negatives)if(e.parse(p[1],p[0]).action()!=IntentEngine.Action.UNKNOWN)throw new AssertionError("Unsafe route: "+p[0]+" "+p[1]);
        if(e.parse("3afak coupe le wifi","en").action()!=IntentEngine.Action.WIFI)throw new AssertionError("Code switch regression");
        if(!e.parse("3afak coupe le wifi","en").language().equals("ary-Latn"))throw new AssertionError("Arabizi routing regression");
        if(e.parse("turn on do not disturb","en").action()!=IntentEngine.Action.DND)throw new AssertionError("DND polarity regression");
        System.out.println("17 safety/routing assertions passed on host JVM; Android actions remain untested.");
    }
}
