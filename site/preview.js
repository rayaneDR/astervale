'use strict';
(() => {
  const $ = s => document.querySelector(s);
  const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const icons = {
    home:'M3 11 12 3l9 8v10h-6v-7H9v7H3Z', settings:'M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8M9 3h6l1 3 3 1 2 5-2 5-3 1-1 3H9l-1-3-3-1-2-5 2-5 3-1Z',
    search:'M10.5 3a7.5 7.5 0 1 0 0 15 7.5 7.5 0 0 0 0-15M16 16l5 5', camera:'M3 7h5l2-3h4l2 3h5v14H3ZM12 10a4 4 0 1 0 0 8 4 4 0 0 0 0-8',
    phone:'M5 3h4l1 6-3 2a15 15 0 0 0 6 6l2-3 6 1v4c0 2-2 3-4 2C9 19 5 15 3 7c-1-2 0-4 2-4Z', messages:'M3 4h18v13H9l-6 4ZM7 9h10M7 13h6',
    browser:'M3 12a9 9 0 1 0 18 0 9 9 0 0 0-18 0M3 12h18M12 3c-5 5-5 13 0 18 5-5 5-13 0-18', game:'M7 7h10c3 0 4 3 5 9 1 5-4 5-6 1H8c-2 4-7 4-6-1 1-6 2-9 5-9ZM5 12h6M8 9v6M16 11h.1M19 14h.1',
    agent:'M12 3v4M10 3h4M5 8h14v12H5ZM2 12h3M19 12h3M9 12v2M15 12v2M9 17h6', wifi:'M2 8a16 16 0 0 1 20 0M5 12a11 11 0 0 1 14 0M8 16a6 6 0 0 1 8 0M12 20h.1',
    bluetooth:'M7 7l10 10-5 4V3l5 4L7 17', moon:'M20 15A9 9 0 0 1 9 4a9 9 0 1 0 11 11Z', sun:'M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8M12 1v3M12 20v3M1 12h3M20 12h3M4 4l2 2M18 18l2 2M20 4l-2 2M6 18l-2 2',
    battery:'M2 7h18v10H2ZM22 10v4M6 10v4M10 10v4M14 10v4', arrow:'m9 5 7 7-7 7', back:'m15 5-7 7 7 7', lock:'M6 10h12v11H6ZM8 10V7a4 4 0 0 1 8 0v3',
    music:'M9 17V5l11-2v12M9 6l11-2M9 17a3 3 0 1 0-6 0 3 3 0 0 0 6 0M20 15a3 3 0 1 0-6 0 3 3 0 0 0 6 0', calendar:'M3 5h18v16H3ZM7 2v6M17 2v6M3 10h18M7 14h3M14 14h3',
    files:'M3 6h7l2 3h9v12H3ZM3 6V3h7l2 3h9v3', mail:'M3 5h18v14H3ZM3 5l9 8 9-8', clock:'M3 12a9 9 0 1 0 18 0 9 9 0 0 0-18 0M12 7v6l4 2', shield:'M12 2 3 6v6c0 5 9 10 9 10s9-5 9-10V6ZM8 12l3 3 5-6',
    volume:'M3 9h4l5-5v16l-5-5H3ZM16 8c3 2 3 6 0 8M19 5c5 4 5 10 0 14', grid:'M3 3h6v6H3ZM15 3h6v6h-6ZM3 15h6v6H3ZM15 15h6v6h-6', airplane:'M2 12l8-2V3l2-2 2 2v7l8 2v3l-8-1v5l3 2v1l-5-1-5 1v-1l3-2v-5l-8 1Z', check:'m5 12 4 4L20 5'
  };
  const icon = n => `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="${icons[n] || icons.grid}"/></svg>`;
  const translations = {
    'Lock screen':'شاشة القفل','Home':'الرئيسية','App drawer':'التطبيقات','Notifications':'الإشعارات','Control center':'مركز التحكم','Settings':'الإعدادات','Game Mode':'وضع الألعاب','Assistant':'المساعد','First boot':'الإعداد الأول',
    'Good morning':'صباح الخير','Tuesday, November 10':'الثلاثاء، ١٠ نوفمبر','A little room to breathe.':'مساحة للهدوء.','Your day, at your pace.':'يومك، على إيقاعك.','All apps':'كل التطبيقات','Search apps':'البحث في التطبيقات','Phone':'الهاتف','Messages':'الرسائل','Camera':'الكاميرا','Browser':'المتصفح','Music':'الموسيقى','Calendar':'التقويم','Files':'الملفات','Clock':'الساعة','Mail':'البريد','Open app drawer':'فتح قائمة التطبيقات','Unlock preview':'فتح المعاينة','Welcome home.':'أهلًا بك.','Make this phone yours.':'اجعل هذا الهاتف لك.','Continue':'متابعة','Back':'رجوع','Appearance':'المظهر','Privacy':'الخصوصية','Battery':'البطارية','Sound':'الصوت','Balanced':'متوازن','Battery saver':'توفير الطاقة','Gaming':'ألعاب','Apply':'تطبيق','Cancel':'إلغاء','Your phone, thoughtfully.':'هاتفك، بعناية.','No cloud connection':'لا اتصال سحابي','Local preview only':'معاينة محلية فقط','Focus':'التركيز','Bluetooth':'بلوتوث','Airplane mode':'وضع الطيران','Dark theme':'المظهر الداكن','Brightness':'السطوع','Finish setup':'إنهاء الإعداد','Language':'اللغة','Nothing here yet.':'لا شيء هنا بعد.','Clear all':'مسح الكل','Device metrics unavailable':'قياسات الجهاز غير متاحة','Demo notifications':'إشعارات تجريبية','Per-app profile':'ملف خاص بالتطبيق','Select a game':'اختيار لعبة','Protect the temperature.':'حماية درجة الحرارة.','Choose a quieter evening.':'اختر أمسية أهدأ.','Allow local assistant preview':'السماح بمعاينة المساعد المحلي','Use battery saver':'استخدم توفير الطاقة','Open settings':'فتح الإعدادات','Change preview theme':'تغيير مظهر المعاينة','Keep thermal protection':'الإبقاء على الحماية الحرارية','Block interruptions':'منع المقاطعات','Show metric overlay':'إظهار قياسات الأداء','Icon shape':'شكل الأيقونات','Rounded':'مستدير','Square':'مربع','Compact':'مضغوط','Permission required':'إذن مطلوب'
  };
  const defaults = {theme:'light',lang:'en',scale:'1',motion:false,wifi:true,bluetooth:false,focus:false,airplane:false,brightness:68,profile:'Balanced',game:'demo.racer',profiles:{},overlay:false,assistant:false,icons:'Rounded',notifications:true,setup:0};
  let state;
  try {state={...defaults,...JSON.parse(localStorage.getItem('astervale-preview') || '{}')};} catch {state={...defaults};}
  // Constrain persisted input before it reaches markup or style values.
  state.theme=['light','dark'].includes(state.theme)?state.theme:'light';
  state.lang=['en','ar'].includes(state.lang)?state.lang:'en';
  state.scale=['1','1.3','2'].includes(String(state.scale))?String(state.scale):'1';
  state.profile=['Balanced','Battery saver','Gaming'].includes(state.profile)?state.profile:'Balanced';
  state.setup=Number.isInteger(state.setup)&&state.setup>=0&&state.setup<=2?state.setup:0;
  state.icons=['Rounded','Square','Compact'].includes(state.icons)?state.icons:'Rounded';
  state.game=['demo.racer','demo.puzzle'].includes(state.game)?state.game:'demo.racer';
  for(const key of ['motion','wifi','bluetooth','focus','airplane','overlay','assistant','notifications'])state[key]=typeof state[key]==='boolean'?state[key]:defaults[key];
  state.profiles=state.profiles && typeof state.profiles==='object' && !Array.isArray(state.profiles)?state.profiles:{};
  state.brightness=Math.min(100,Math.max(10,Number(state.brightness)||68));
  const t=s=>state.lang==='ar'?(translations[s] || s):s;
  const screens=[['lock','Lock screen','A quiet first glance. Private notifications stay private.'],['home','Home','A quiet home for the things you reach for.'],['drawer','App drawer','Your apps, without the clutter. Search or browse.'],['notifications','Notifications','A useful pause. Grouped, readable and easy to clear.'],['controls','Control center','The essentials, within reach. Every control is a browser demo.'],['settings','Settings','A familiar structure with a little more personality.'],['gaming','Game Mode','Choose a profile. Thermal protection always has the final say.'],['assistant','Assistant','Understand the action before you allow it. No network calls.'],['setup','First boot','A considered welcome, with privacy choices up front.']];
  let current=new URLSearchParams(location.search).get('screen') || 'home';
  if(!screens.some(s=>s[0]===current))current='home';
  const embedded=new URLSearchParams(location.search).get('embed')==='1';
  if(embedded)document.body.classList.add('embedded');
  let pending=null, toastTimer;
  function save(){try{localStorage.setItem('astervale-preview',JSON.stringify(state));}catch{/* Private mode can disable storage. */}}
  function toast(msg){const n=$('#snackbar');n.textContent=msg;n.classList.add('visible');clearTimeout(toastTimer);toastTimer=setTimeout(()=>n.classList.remove('visible'),2800);}
  function button(text,action,cls='primary'){return `<button class="button ${cls}" data-action="${action}">${esc(t(text))}</button>`;}
  function row(name,sub,ico,action,end='arrow'){return `<button class="row" data-action="${action}">${icon(ico)}<span class="row-text"><strong>${esc(t(name))}</strong><small>${esc(t(sub))}</small></span>${end==='arrow'?icon('arrow'):`<span class="switch ${state[end]?'on':''}" aria-hidden="true"></span>`}</button>`;}
  function toggle(name,key,ico,sub='Preview setting'){return `<button class="row" role="switch" aria-checked="${!!state[key]}" data-action="toggle:${key}" aria-label="${esc(t(name))}">${icon(ico)}<span class="row-text"><strong>${esc(t(name))}</strong><small>${esc(t(sub))}</small></span><span class="switch ${state[key]?'on':''}" aria-hidden="true"></span></button>`;}
  const apps=[['Phone','phone','green'],['Messages','messages','sand'],['Camera','camera','clay'],['Browser','browser','green'],['Settings','settings','sand'],['Game Mode','game','green'],['Assistant','agent','clay'],['Music','music','sand'],['Calendar','calendar','sand'],['Files','files','green'],['Clock','clock','clay'],['Mail','mail','sand']];
  const app=(a)=>`<button class="app-button" data-action="app:${esc(a[0])}" aria-label="${esc(t(a[0]))}"><span class="app-symbol ${a[2]}">${icon(a[1])}</span><span class="app-label">${esc(t(a[0]))}</span></button>`;
  const heading=(title,sub)=>`<h2>${esc(t(title))}</h2><p class="subheading">${esc(t(sub))}</p>`;
  function screen(){
    switch(current){
    case 'home':return `<p class="greeting">${t('Good morning')}</p><div class="clock">09:41</div><p class="date">${t('Tuesday, November 10')}</p><div class="home-widget"><h3>${t('A little room to breathe.')}</h3><p>${t('Your day, at your pace.')}</p></div><div class="home-space"></div><div class="apps">${apps.slice(4,8).map(app).join('')}</div><div class="dock">${apps.slice(0,4).map(app).join('')}</div><button class="drawer-hint" data-screen="drawer">${icon('grid')}<br>${t('Open app drawer')}</button>`;
    case 'lock':return `<div class="lock-mark">${icon('lock')}</div><p class="date">${t('Tuesday, November 10')}</p><div class="clock">09:41</div><p>${t('Choose a quieter evening.')}</p><div class="lock-note">${icon('shield')}<p>${state.lang==='ar'?'محتوى الإشعارات مخفي حتى فتح القفل.':'Notification content stays hidden until you unlock.'}</p><small>${t('Local preview only')}</small></div><div class="lock-bottom">${button('Unlock preview','screen:home')}</div>`;
    case 'drawer':return `${heading('All apps','Your phone, thoughtfully.')}<label class="search">${icon('search')}<input id="app-search" placeholder="${t('Search apps')}" aria-label="${t('Search apps')}" autocomplete="off"></label><div class="apps drawer-grid" id="app-grid">${apps.map(app).join('')}</div><p id="no-apps" class="empty" hidden>${t('Nothing here yet.')}</p>`;
    case 'controls':return `${heading('Control center','Local preview only')}<div class="quick-grid">${[['wifi','Wi-Fi','wifi'],['bluetooth','Bluetooth','bluetooth'],['focus','Focus','moon'],['airplane','Airplane mode','airplane']].map(([key,name,ic])=>`<button class="quick-tile ${state[key]?'active':''}" aria-pressed="${!!state[key]}" data-action="toggle:${key}">${icon(ic)}<span>${t(name)}</span><small style="color:inherit">${state[key]?(state.lang==='ar'?'مفعّل':'On'):(state.lang==='ar'?'متوقف':'Off')}</small></button>`).join('')}</div><label class="brightness-label" for="brightness">${icon('sun')}${t('Brightness')} <output>${state.brightness}%</output></label><input id="brightness" type="range" min="10" max="100" value="${state.brightness}"><div class="surface">${row('Music','No media playing','music','media')}</div>${button('Notifications','screen:notifications','outline')}<p class="info-note">${state.lang==='ar'?'هذه عناصر معاينة، ولا تغيّر إعدادات الهاتف.':'These controls change the preview, not your phone settings.'}</p>`;
    case 'notifications':return `${heading('Notifications','Demo notifications')}<button class="outline" data-screen="controls">${t('Control center')}</button><p class="section-title">${state.lang==='ar'?'اليوم':'Today'}</p>${state.notifications?`<article class="notification"><div class="notification-head">${icon('calendar')}AsterVale · ${state.lang==='ar'?'عرض تجريبي':'Demo'}</div><strong>${t('A little room to breathe.')}</strong><p>${state.lang==='ar'?'حان وقت استراحة صغيرة.':'A reminder to take a small pause.'}</p></article><article class="notification"><div class="notification-head">${icon('messages')}${t('Messages')} · ${state.lang==='ar'?'عرض تجريبي':'Demo'}</div><strong>${state.lang==='ar'?'معاينة خاصة':'A private preview'}</strong><p>${state.lang==='ar'?'لا تتم قراءة أي إشعارات حقيقية.':'No real notifications are read by this prototype.'}</p></article><div class="notify-actions"><button data-action="clear-notifications">${t('Clear all')}</button><button data-screen="assistant">${t('Assistant')} ${icon('arrow')}</button></div>`:`<div class="empty">${icon('check')}<p>${t('Nothing here yet.')}</p>${button('Reset preview','restore-notifications','outline')}</div>`}`;
    case 'settings':return `${heading('Settings','Your phone, thoughtfully.')}<div class="surface"><h3>AsterVale</h3><small>Android 16 · SM-A515F<br>${state.lang==='ar'?'تصميم تجريبي · لم يتم بناء النظام':'Design preview · ROM not built'}</small></div><p class="section-title">${t('Appearance')}</p><div class="surface">${toggle('Dark theme','darkToggle','moon',state.theme==='dark'?'Dark':'Light')}${row('Icon shape',state.icons,'grid','shape')}${row('Game Mode',state.profile,'game','screen:gaming')}${row('Assistant',state.assistant?'Local preview only':'Off by default','agent','screen:assistant')}</div><p class="section-title">${state.lang==='ar'?'الأساسيات':'Everyday essentials'}</p><div class="surface">${row('Battery','Device metrics unavailable','battery','screen:gaming')}${row('Sound','Volume and interruptions','volume','screen:controls')}${row('Privacy','No cloud connection','shield','privacy')}</div>`;
    case 'gaming':return `${heading('Game Mode','Protect the temperature.')}<label for="game-app">${t('Select a game')}</label><select id="game-app"><option value="demo.racer" ${state.game==='demo.racer'?'selected':''}>${state.lang==='ar'?'لعبة سباق تجريبية':'Demo racer'}</option><option value="demo.puzzle" ${state.game==='demo.puzzle'?'selected':''}>${state.lang==='ar'?'لعبة ألغاز تجريبية':'Demo puzzle'}</option></select><p class="section-title">${t('Per-app profile')}</p><div class="profile-select">${['Battery saver','Balanced','Gaming'].map(p=>`<button aria-pressed="${(state.profiles[state.game]||state.profile)===p}" data-action="profile:${p}">${t(p)}</button>`).join('')}</div><p class="info-note">${state.lang==='ar'?'يُحفظ الاختيار لهذه اللعبة في المتصفح فقط. ضبط المعالج والرسوم غير مفعّل.':'Choice saved for this demo game in your browser. CPU and GPU tuning is not enabled.'}</p><div class="metric-pair"><div><strong>— FPS</strong><small>${t('Device metrics unavailable')}</small></div><div><strong>— °C</strong><small>${state.lang==='ar'?'لا اتصال بالجهاز':'No device connected'}</small></div></div><div class="surface">${toggle('Block interruptions','focus','moon')}${toggle('Show metric overlay','overlay','game')}${row('Keep thermal protection','Always preserved','shield','thermal')}</div>${button('Apply','apply-profile')}<p class="info-note">${state.lang==='ar'?'لم تُقَس زيادة الأداء أو استهلاك البطارية.':'No performance gain or battery improvement has been measured.'}</p>`;
    case 'assistant':return `${heading('Assistant','Your phone, thoughtfully.')}<div class="agent-symbol">${icon('agent')}</div><h3>${state.lang==='ar'?'أنت تختار. وأنا أوضّح.':'You choose. I explain.'}</h3><p class="info-note">${state.lang==='ar'?'معاينة محلية فقط. لا نموذج ذكاء اصطناعي، ولا إرسال للبيانات.':'A local interaction demo. No AI model, API key or data transmission.'}</p>${toggle('Allow local assistant preview','assistant','shield','Off by default')}<p class="section-title">${state.lang==='ar'?'جرّب إجراءً':'Try an action'}</p><button class="prompt" data-action="propose:battery" ${!state.assistant?'disabled':''}>${icon('battery')} ${t('Use battery saver')}</button><button class="prompt" data-action="propose:settings" ${!state.assistant?'disabled':''}>${icon('settings')} ${t('Open settings')}</button><button class="prompt" data-action="propose:theme" ${!state.assistant?'disabled':''}>${icon('moon')} ${t('Change preview theme')}</button>${pending?`<div class="action-preview"><strong>${state.lang==='ar'?'الإجراء المقترح':'Proposed action'}</strong><p>${esc(t(pending==='battery'?'Use battery saver':pending==='settings'?'Open settings':'Change preview theme'))}</p><small>${state.lang==='ar'?'ينطبق على المعاينة فقط.':'Applies to this browser preview only.'}</small><div class="actions"><button data-action="cancel">${t('Cancel')}</button><button data-action="confirm" class="primary">${t('Apply')}</button></div></div>`:''}<p class="info-note">${t('No cloud connection')} · BYOK ${state.lang==='ar'?'غير مدمج بعد':'integration pending'}</p>`;
    case 'setup':return `<div class="setup"><img class="setup-mark" src="assets/mark.svg" alt="AsterVale"><p class="setup-step">${state.setup+1} / 3</p><h2>${t(state.setup===0?'Welcome home.':state.setup===1?'Make this phone yours.':'Your phone, thoughtfully.')}</h2>${state.setup===0?`<p>${state.lang==='ar'?'بداية هادئة لهاتف تعرفه جيدًا.':'A fresh start for a phone you know by heart.'}</p><label>${t('Language')}<select id="setup-lang"><option value="en" ${state.lang==='en'?'selected':''}>English</option><option value="ar" ${state.lang==='ar'?'selected':''}>العربية</option></select></label>`:state.setup===1?`<p>${state.lang==='ar'?'اختر مظهرًا، ويمكنك تغييره لاحقًا.':'Choose a starting point. You can change it later.'}</p><div class="segmented"><button data-action="theme:light" aria-pressed="${state.theme==='light'}">${state.lang==='ar'?'فاتح':'Light'}</button><button data-action="theme:dark" aria-pressed="${state.theme==='dark'}">${state.lang==='ar'?'داكن':'Dark'}</button></div>`:`<p>${state.lang==='ar'?'لا يُفعّل المساعد تلقائيًا، ولا تُرسَل البيانات.':'The assistant stays off by default. No data leaves this preview.'}</p><label class="check-row"><input type="checkbox" id="setup-consent" ${state.assistant?'checked':''}>${t('Allow local assistant preview')}</label><p class="info-note">${state.lang==='ar'?'لا استعادة حساب أو تثبيت تطبيقات في هذه المعاينة.':'Account restoration and app installation are not part of this prototype.'}</p>`}${button(state.setup===2?'Finish setup':'Continue','setup-next')}${state.setup?button('Back','setup-back','outline'):''}</div>`;
    }
  }
  function render(){
    const phone=$('#phone');state.darkToggle=state.theme==='dark';
    phone.classList.toggle('dark',state.theme==='dark');phone.classList.toggle('has-wallpaper',['home','lock'].includes(current));
    phone.style.setProperty('--scale',state.scale);phone.dir=state.lang==='ar'?'rtl':'ltr';phone.lang=state.lang;
    document.body.classList.toggle('reduced',!!state.motion);
    $('#theme-light').setAttribute('aria-pressed',String(state.theme==='light'));$('#theme-dark').setAttribute('aria-pressed',String(state.theme==='dark'));
    $('#locale').value=state.lang;$('#text-scale').value=state.scale;$('#reduce-motion').checked=!!state.motion;
    $('#screen-nav').innerHTML=screens.map(([id,name])=>`<button data-screen="${id}" aria-current="${id===current}">${esc(t(name))}<span aria-hidden="true">↗</span></button>`).join('');
    $('#screen-description').textContent=screens.find(s=>s[0]===current)[2];
    const el=$('#phone-screen');el.className=`phone-screen ${current}`;el.innerHTML=`<div class="screen-content">${screen()}</div>`;
    // Icon-shape customization is a browser design control, not an installed icon pack.
    el.querySelectorAll('.app-symbol').forEach(n=>n.style.borderRadius=state.icons==='Square'?'5px':state.icons==='Compact'?'12px':'16px');
    save();
  }
  function navigate(id){if(!screens.some(s=>s[0]===id))return;current=id;pending=null;render();$('#phone-screen').scrollTop=0;}
  function action(a){
    const [kind,...parts]=a.split(':');const value=parts.join(':');
    if(kind==='screen')return navigate(value);
    if(kind==='app'){const dest={'Settings':'settings','Game Mode':'gaming','Assistant':'assistant'}[value];if(dest)return navigate(dest);return toast(`${t(value)} · ${state.lang==='ar'?'تشغيل التطبيقات غير متاح في المتصفح':'app launch is not available in a browser'}`);}
    if(kind==='toggle'){
      if(!['wifi','bluetooth','focus','airplane','overlay','assistant','darkToggle'].includes(value))return;
      if(value==='darkToggle')state.theme=state.theme==='light'?'dark':'light';else state[value]=!state[value];
      if(value==='assistant'&&!state.assistant)pending=null;
      if(value==='overlay')toast(state.lang==='ar'?'قياسات الأداء غير متاحة دون الجهاز.':'Overlay requested; real FPS and temperature are unavailable.');
    }else if(kind==='profile'){if(!['Balanced','Battery saver','Gaming'].includes(value))return;state.profile=value;state.profiles[state.game]=value;
    }else if(kind==='theme')state.theme=value==='dark'?'dark':'light';
    else if(a==='apply-profile')return toast(state.lang==='ar'?'حُفظ ملف اللعبة التجريبية. لم تُغيّر ترددات الجهاز.':'Demo game profile saved. No device clocks changed.');
    else if(a==='clear-notifications')state.notifications=false;
    else if(a==='restore-notifications')state.notifications=true;
    else if(a==='shape'){const shapes=['Rounded','Square','Compact'];state.icons=shapes[(shapes.indexOf(state.icons)+1)%shapes.length];toast(`${t('Icon shape')}: ${t(state.icons)}`);}
    else if(kind==='propose'&&state.assistant){if(['battery','settings','theme'].includes(value))pending=value;}
    else if(a==='cancel')pending=null;
    else if(a==='confirm'&&state.assistant&&pending){const p=pending;pending=null;if(p==='settings')return navigate('settings');if(p==='battery')state.profile='Battery saver';if(p==='theme')state.theme=state.theme==='light'?'dark':'light';toast(state.lang==='ar'?'تم تطبيق الإجراء على المعاينة فقط.':'Confirmed action applied to preview only.');}
    else if(a==='setup-next'){if(state.setup<2)state.setup++;else{state.setup=0;return navigate('home');}}
    else if(a==='setup-back')state.setup=Math.max(0,state.setup-1);
    else if(a==='thermal')return toast(state.lang==='ar'?'لا يمكن تعطيل حماية الحرارة.':'Thermal protection stays enabled. No hardware tuning implemented.');
    else if(a==='privacy')return toast(state.lang==='ar'?'لا إرسال للبيانات، ولا وصول للإشعارات.':'No network requests, API keys or notification access.');
    else if(a==='media')return toast(state.lang==='ar'?'لا توجد وسائط قيد التشغيل.':'No media is playing in this demo.');
    render();
  }
  document.addEventListener('click',e=>{const s=e.target.closest('[data-screen]');if(s)return navigate(s.dataset.screen);const a=e.target.closest('[data-action]');if(a&&!a.disabled)action(a.dataset.action);});
  document.addEventListener('input',e=>{
    if(e.target.id==='app-search'){const q=e.target.value.trim().toLocaleLowerCase();const list=apps.filter(a=>`${a[0]} ${t(a[0])}`.toLocaleLowerCase().includes(q));$('#app-grid').innerHTML=list.map(app).join('');$('#no-apps').hidden=!!list.length;}
    if(e.target.id==='brightness'){state.brightness=Number(e.target.value);document.querySelector('.brightness-label output').textContent=`${state.brightness}%`;save();}
  });
  document.addEventListener('change',e=>{
    if(['locale','setup-lang'].includes(e.target.id)){state.lang=e.target.value;render();}
    if(e.target.id==='text-scale'){state.scale=e.target.value;render();}
    if(e.target.id==='reduce-motion'){state.motion=e.target.checked;render();}
    if(e.target.id==='game-app'){state.game=e.target.value;render();}
    if(e.target.id==='setup-consent'){state.assistant=e.target.checked;save();}
  });
  $('#theme-light').onclick=()=>action('theme:light');$('#theme-dark').onclick=()=>action('theme:dark');
  $('#go-home').onclick=()=>navigate('home');
  $('#reset-demo').onclick=()=>{state={...defaults,profiles:{}};pending=null;render();toast('Preview reset.');};
  // Gesture shortcuts always have equivalent labelled buttons.
  let start=null;$('#phone').addEventListener('pointerdown',e=>{if(e.target.closest('button,input,select'))return;start={x:e.clientX,y:e.clientY};});
  $('#phone').addEventListener('pointerup',e=>{if(!start)return;const dy=e.clientY-start.y,dx=e.clientX-start.x;start=null;if(Math.abs(dx)>80||Math.abs(dy)<100)return;if(dy<0&&['home','lock'].includes(current))navigate(current==='lock'?'home':'drawer');else if(dy>0&&current==='home')navigate('controls');});
  document.addEventListener('keydown',e=>{if(e.key==='Escape')navigate('home');});
  render();
})();
