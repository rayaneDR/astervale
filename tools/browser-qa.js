async (page) => {
  const failures=[];
  const check=(condition,message)=>{if(!condition)failures.push(message);};
  await page.setViewportSize({width:1440,height:1000});
  await page.goto('http://127.0.0.1:4173/preview.html');
  await page.locator('#reset-demo').click();
  const ids=['lock','home','drawer','notifications','controls','settings','gaming','assistant','setup'];
  for(const id of ids){
    await page.locator(`#screen-nav [data-screen="${id}"]`).click();
    check(await page.locator(`#phone-screen.${id}`).count()===1,`Screen ${id} absent`);
    const geometry=await page.locator('#phone-screen').evaluate(el=>({scroll:el.scrollWidth,width:el.clientWidth}));
    check(geometry.scroll<=geometry.width+1,`${id}: horizontal phone overflow ${geometry.scroll}/${geometry.width}`);
    await page.screenshot({path:`output/playwright/${id}.png`});
  }
  await page.locator('#screen-nav [data-screen="assistant"]').click();
  check(await page.locator('[data-action="propose:battery"]').isDisabled(),'Assistant not disabled by default');
  await page.locator('[data-action="toggle:assistant"]').click();
  await page.locator('[data-action="propose:battery"]').click();
  check(await page.locator('.action-preview').count()===1,'No action preview');
  await page.locator('[data-action="cancel"]').click();
  check(await page.locator('.action-preview').count()===0,'Cancel failed');
  await page.locator('[data-action="propose:battery"]').click();
  await page.locator('[data-action="confirm"]').click();
  check(await page.evaluate(()=>JSON.parse(localStorage.getItem('astervale-preview')).profile)==='Battery saver','Confirmed choice not saved');
  await page.locator('#screen-nav [data-screen="drawer"]').click();
  await page.locator('#app-search').fill('not-a-real-app');
  check(await page.locator('#no-apps').isVisible(),'Search empty state absent');
  await page.locator('#app-search').fill('camera');
  check(await page.locator('#app-grid .app-button').count()===1,'Drawer search failed');
  await page.locator('#screen-nav [data-screen="controls"]').click();
  await page.locator('[data-action="toggle:bluetooth"]').click();
  check(await page.locator('[data-action="toggle:bluetooth"]').getAttribute('aria-pressed')==='true','Quick toggle failed');
  await page.locator('#theme-dark').click();
  check(await page.locator('#phone.dark').count()===1,'Dark theme failed');
  await page.locator('#locale').selectOption('ar');
  await page.locator('#text-scale').selectOption('2');
  await page.locator('#reduce-motion').check();
  check(await page.locator('#phone').getAttribute('dir')==='rtl','RTL direction failed');
  for(const id of ids){
    await page.locator(`#screen-nav [data-screen="${id}"]`).click();
    const g=await page.locator('#phone-screen').evaluate(el=>({scroll:el.scrollWidth,width:el.clientWidth}));
    check(g.scroll<=g.width+1,`${id}: 200% RTL horizontal overflow ${g.scroll}/${g.width}`);
  }
  await page.screenshot({path:'output/playwright/rtl-large-dark.png'});
  await page.locator('#reset-demo').click();
  await page.locator('#screen-nav [data-screen="home"]').click();
  await page.screenshot({path:'output/playwright/desktop.png'});
  await page.setViewportSize({width:390,height:844});
  check(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'390px page overflow');
  await page.screenshot({path:'output/playwright/mobile.png',fullPage:true});
  await page.goto('http://127.0.0.1:4173/');
  check(await page.locator('h1').innerText()==='A little\nmore life.','Landing title missing');
  await page.screenshot({path:'output/playwright/landing-mobile.png',fullPage:true});
  await page.setViewportSize({width:1440,height:1000});
  await page.screenshot({path:'output/playwright/landing-desktop.png',fullPage:true});
  const external=await page.evaluate(()=>performance.getEntriesByType('resource').filter(r=>!r.name.startsWith(location.origin)).map(r=>r.name));
  check(external.length===0,`Unexpected external resources: ${external}`);
  console.log(JSON.stringify({screens:ids.length,checks:'screen render, overflow, assistant consent/cancel/confirm, persistence, search, controls, theme, RTL/200%, reduced motion, mobile, local resources',failures},null,2));
  if(failures.length)throw new Error(failures.join('; '));
}
