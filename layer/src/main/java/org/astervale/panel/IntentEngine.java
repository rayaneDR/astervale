// SPDX-License-Identifier: Apache-2.0
package org.astervale.panel;
import java.io.*;
import java.text.Normalizer;
import java.util.*;
import java.util.regex.Pattern;

/** Conservative multilingual route matcher, NOT a language model or general language detector. */
public final class IntentEngine {
    public enum Action { WIFI, BLUETOOTH, BATTERY, SETTINGS, BRIGHTNESS, VOLUME, DND, ALARM, TIMER, UNKNOWN }
    public record Result(Action action,String language,String explanation) {}
    private record Rule(String lang,Action action,Pattern pattern,String reply) {}
    private final List<Rule> rules=new ArrayList<>();
    private static final Pattern NEGATION=Pattern.compile("(?iu)(\\b(don't|dont|do not|never|not|ne|pas|no|non|nao|não|nicht|yapma|açma|degil|mat|machi)\\b|لا ت|لا ا|ما .*ش|مات|متفتح|(?<!\\p{L})не\\s|नहीं|मत |不要|别|لا تشغل)");
    public IntentEngine(Reader input) throws IOException {
        try(BufferedReader reader=new BufferedReader(input)){String line;while((line=reader.readLine())!=null){
            if(line.trim().isEmpty()||line.startsWith("#"))continue;String[] p=line.split("\t",4);if(p.length!=4)throw new IOException("Invalid rule row");
            rules.add(new Rule(p[0],Action.valueOf(p[1]),Pattern.compile(p[2],Pattern.CASE_INSENSITIVE|Pattern.UNICODE_CASE),p[3]));
        }}
    }
    public Result parse(String raw,String preferredLocale){
        String value=Normalizer.normalize(raw,Normalizer.Form.NFKC).toLowerCase(Locale.ROOT).replace('’','\'').trim();
        String polarity=value.replace("do not disturb","").replace("ne pas déranger","").replace("no molestar","").replace("não perturbar","").replace("не беспокоить","");
        if(value.length()>512||value.isEmpty()||NEGATION.matcher(polarity).find())return unknown(preferredLocale);
        if(value.matches(".*\\b(and|then|puis|et|word|article|quoted|definition|meaning|explain|why)\\b.*")||value.contains("\""))return unknown(preferredLocale);
        LinkedHashMap<Action,List<Rule>> hits=new LinkedHashMap<>();
        for(Rule r:rules)if(r.pattern.matcher(value).find())hits.computeIfAbsent(r.action,k->new ArrayList<>()).add(r);
        // Generic settings words may qualify a specific control (for example 蓝牙设置).
        if(hits.size()>1)hits.remove(Action.SETTINGS);
        // Multiple actions require clarification. Do not infer an action from a compound request.
        if(hits.size()!=1)return unknown(preferredLocale);
        List<Rule> choices=hits.values().iterator().next();
        Rule selected=choices.stream().filter(r->r.lang.equals(preferredLocale)).findFirst().orElse(choices.get(0));
        // Arabizi/code-switch hints are deterministic; low-resource detection stays explicit.
        if(value.matches(".*(3afak|3afek|bghit|7ell|7al|ch3el|tfi|safi|dyali).*")){
            for(Rule r:rules)if(r.lang.equals("ary-Latn")&&r.action==selected.action){selected=r;break;}
        }
        return new Result(selected.action,selected.lang,selected.reply);
    }
    private static Result unknown(String lang){
        String reply=switch(lang){
            case "ar" -> "لم أفهم إجراءً واحدًا بوضوح. أعد صياغته أو اختره من الإعدادات.";
            case "ary" -> "ما فهمتش شنو بغيتي بالضبط. عاودها ولا اختار من الإعدادات.";
            case "ary-Latn" -> "Ma fhemtch chno bghiti bddabt. 3awedha wla khtar mn settings.";
            case "fr" -> "Je n’ai pas compris une seule action claire. Reformulez ou ouvrez les réglages.";
            case "es" -> "No entendí una acción clara. Reformula o abre los ajustes.";
            case "pt" -> "Não entendi uma ação clara. Reformule ou abra as definições.";
            case "ru" -> "Не удалось определить одно действие. Переформулируйте запрос.";
            case "tr" -> "Tek bir eylem anlaşılmadı. Lütfen yeniden ifade edin.";
            case "hi" -> "एक स्पष्ट कार्रवाई नहीं समझ आई। कृपया दोबारा कहें।";
            case "zh" -> "无法确定单个操作。请换一种说法，或打开设置。";
            default -> "I could not identify one clear action. Rephrase or use settings. No action was taken.";
        };return new Result(Action.UNKNOWN,lang,reply);
    }
}
