"""Original small command lexicon and human-authored text fixtures, not recorded speech."""
from pathlib import Path
import csv,json
ROOT=Path(__file__).resolve().parents[1]
# Language / command keyword alternatives / local explanation prefix.
languages={
 'en':(['wi-?fi|wireless network','bluetooth','battery|power sav','settings|preferences','brightness|screen light','volume|sound level','do not disturb|focus mode','alarm','timer|countdown'],'I can open the relevant Android controls. Review and make the change there.'),
 'ar':(['واي فاي|واي.?فاي|الواي فاي','بلوتوث|البلوتوث','بطاري|توفير الطاق','الإعدادات|الاعدادات','سطوع|إضاءة الشاشة','صوت|الصوت','عدم الإزعاج|عدم الازعاج','منبه|المنبه','مؤقت|المؤقت'],'يمكنني فتح عناصر التحكم المناسبة في أندرويد. راجع التغيير ونفّذه هناك.'),
 'ary':(['الويفي|ويفي|الوايفاي','البلوتوت|بلوتوت','الباطري|باطري|توفير البطارية','ليبارامتر|البارامتر|الإعدادات','الضو|ضو الشاشة','الصوت|صوت التليفون','بلا صداع|بلا ازعاج','ريفي|الريفي','كونطور|مينوتور'],'نقدر نحل ليك الإعدادات ديال هاد الحاجة. شوف التغيير وديرو نتا تما.'),
 'ary-Latn':(['wifi|l?wifi','blotot|bloutout|bluetooth','batri|batterie|battery','parametr|settings|reglages','daw|do dyal|brightness','sot|sout|volume','bla sda3|dnd','reveil|alarm','minuteur|timer'],'N9der n7ell lik settings dyal had l7aja. Chof ttbdil w diro nta temma.'),
 'fr':(['wi-?fi|reseau sans fil|réseau sans fil','bluetooth','batterie|économie d.énergie','paramètres|parametres|réglages','luminosité|luminosite','volume|niveau sonore','ne pas déranger|mode concentration','réveil|reveil|alarme','minuteur|compte à rebours'],'Je peux ouvrir les commandes Android correspondantes. Vérifiez et effectuez le changement vous-même.'),
 'es':(['wi-?fi|red inalámbrica','bluetooth','batería|bateria|ahorro de energía','ajustes|configuración','brillo|luz de pantalla','volumen|nivel de sonido','no molestar','alarma|despertador','temporizador|cuenta atrás'],'Puedo abrir los controles de Android. Revisa y realiza el cambio allí.'),
 'pt':(['wi-?fi|rede sem fios','bluetooth','bateria|poupança de energia','definições|configurações','brilho|luz da tela','volume|nível de som','não perturbar','alarme|despertador','temporizador|contagem regressiva'],'Posso abrir os controlos do Android. Reveja e faça a alteração aí.'),
 'ru':(['вай.?фай|беспроводн','блютуз','батаре|энергосбереж','настройки','яркост','громкост','не беспокоить','будильник','таймер'],'Я могу открыть нужные настройки Android. Проверьте и измените их самостоятельно.'),
 'tr':(['wi-?fi|kablosuz','bluetooth','pil|batarya|güç tasarrufu','ayarlar','parlaklık','ses düzeyi|ses seviyesi','rahatsız etme','alarm','zamanlayıcı|geri sayım'],'İlgili Android denetimlerini açabilirim. Değişikliği orada gözden geçirip uygulayın.'),
 'hi':(['वाई.?फाई|वाइफाइ','ब्लूटूथ','बैटरी|ऊर्जा बचत','सेटिंग','चमक|रोशनी','आवाज़|आवाज|वॉल्यूम','परेशान न करें','अलार्म','टाइमर'],'मैं Android के संबंधित नियंत्रण खोल सकता हूँ। वहाँ बदलाव जाँचें और खुद लागू करें।'),
 'zh':(['无线网络|无线网|wifi','蓝牙','电池|省电','设置','亮度','音量','勿扰|专注模式','闹钟','计时器|倒计时'],'我可以打开相应的 Android 控制项。请在那里检查并自行更改。'),
}
actions=['WIFI','BLUETOOTH','BATTERY','SETTINGS','BRIGHTNESS','VOLUME','DND','ALARM','TIMER']
asset=ROOT/'layer/src/main/assets';asset.mkdir(parents=True,exist_ok=True)
with (asset/'commands.tsv').open('w',encoding='utf-8',newline='') as file:
    file.write('# locale\taction\tregex\tEnglish tool IDs, localized explanation; curated command routing only\n')
    for lang,(patterns,reply) in languages.items():
        for action,pattern in zip(actions,patterns):
            # Exact phrase boundaries for Latin short tokens reduce accidental substring activation.
            expression='(?:'+pattern+')'
            if lang in ['en','fr','es','pt','tr','ary-Latn']:expression=r'(?<![\p{L}\p{N}])'+expression+r'(?![\p{L}\p{N}])'
            file.write('\t'.join([lang,action,expression,reply])+'\n')

# Independent natural requests; intentional negation/compound and unknown challenges included.
requests={
 'en':['Please show Wi-Fi controls','Where can I adjust Bluetooth?','Use battery saver please','Take me to settings','Make the screen brightness lower','Turn the volume down','Start focus mode','Show my alarm','I need a timer','Do not open Wi-Fi','Tell me a joke'],
 'ar':['افتح الواي فاي من فضلك','أريد إعدادات البلوتوث','فعّل توفير الطاقة','افتح الإعدادات','خفّض السطوع','ارفع الصوت','فعّل عدم الإزعاج','أريد المنبه','افتح المؤقت','لا تشغل الواي فاي','ما أخبار الطقس'],
 'ary':['حل ليا الويفي عافاك','شعل البلوتوت','بغيت نوفر الباطري','فين نلقى ليبارامتر','نقص ليا الضو شوية','طلع الصوت عافاك','بغيت التليفون بلا صداع','دير ليا الريفي','حل المينوتور','ماتحلش الويفي','واش غادي تشتي غدا'],
 'ary-Latn':['3afak 7ell wifi','ch3el blotot 3afak','bghit n9ess lbatri','7ell settings dyali','n9ess daw chwia','tla3 sot 3afak','bghit bla sda3','7ell alarm','dir timer 3afak','mat 7ell wifi','3afak coupe le wifi'],
 'fr':['Peux-tu ouvrir le Wi-Fi ?','Ouvre les options Bluetooth','Active l’économie de batterie','Montre les paramètres','Baisse la luminosité','Monte le volume','Active le mode ne pas déranger','Ouvre le réveil','Je veux un minuteur','N’ouvre pas le Wi-Fi','Quel temps demain ?'],
 'es':['Abre el Wi-Fi por favor','Quiero ver Bluetooth','Activa el ahorro de batería','Abre los ajustes','Baja el brillo','Sube el volumen','Activa no molestar','Abre la alarma','Necesito un temporizador','No abras Wi-Fi','Cuéntame un chiste'],
 'pt':['Abre o Wi-Fi por favor','Mostra o Bluetooth','Poupa a bateria','Abre as definições','Reduz o brilho','Aumenta o volume','Ativa não perturbar','Abre o alarme','Preciso de um temporizador','Não abras o Wi-Fi','Como está o tempo?'],
 'ru':['Открой вайфай пожалуйста','Покажи блютуз','Включи энергосбережение','Открой настройки','Уменьши яркость','Увеличь громкость','Включи режим не беспокоить','Открой будильник','Мне нужен таймер','Не открывай вайфай','Расскажи шутку'],
 'tr':['Kablosuz ağ ayarını aç','Bluetooth seçeneklerini göster','Pil tasarrufunu aç','Ayarları açar mısın','Parlaklığı azalt','Ses seviyesini yükselt','Rahatsız etme modunu aç','Alarmı aç','Zamanlayıcı istiyorum','Wifi açma','Bana bir şaka anlat'],
 'hi':['वाईफाई खोलो','ब्लूटूथ दिखाओ','बैटरी बचत चालू करो','सेटिंग खोलो','चमक कम करो','आवाज़ बढ़ाओ','परेशान न करें मोड खोलो','अलार्म खोलो','टाइमर चाहिए','वाईफाई मत खोलो','एक चुटकुला सुनाओ'],
 'zh':['请打开无线网络','打开蓝牙设置','打开省电模式','打开设置','降低亮度','调高音量','开启勿扰模式','打开闹钟','我需要计时器','不要打开无线网络','讲个笑话'],
}
data=ROOT/'assistant';data.mkdir(exist_ok=True)
with (data/'benchmark.tsv').open('w',encoding='utf-8',newline='') as file:
    writer=csv.writer(file,delimiter='\t',lineterminator='\n');writer.writerow(['language','input','expected'])
    for lang,examples in requests.items():
        for i,sentence in enumerate(examples):
            expected=actions[i] if i<9 else 'UNKNOWN'
            if lang=='ary-Latn' and i==10:expected='WIFI'
            writer.writerow([lang,sentence,expected])
    for lang,text in [('en','Open Wi-Fi and Bluetooth'),('ary-Latn','3afak zid volume et luminosité'),('fr','Active Bluetooth puis ouvre les paramètres'),('en','The word battery appears in this article')]:
        writer.writerow([lang,text,'UNKNOWN'])
(data/'LANGUAGES.json').write_text(json.dumps({'default':'en','locales':list(languages),'status':'Curated routing lexicon. Not universal language recognition, speech or LLM benchmark. Native-speaker review pending.','rule_count':len(languages)*len(actions)},indent=2)+'\n')
print('Wrote',len(languages)*len(actions),'rules and',sum(map(len,requests.values()))+4,'evaluation cases')
