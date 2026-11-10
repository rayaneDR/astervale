from pathlib import Path
import subprocess,shutil,json
root=Path(__file__).resolve().parents[1]
targets=[('dribbble','https://dribbble.com/shots/26161490-Control-Center-iOS-26-Apple-Liquid-Glass-UI'),('behance','https://www.behance.net/gallery/227972619/iOS-26-A-Framer-Remix'),('mobbin','https://mobbin.com/discover/apps/ios')]
code='async (page)=>{await page.setViewportSize({width:1440,height:1000});const results=[];for(const [name,url] of '+json.dumps(targets)+'){try{await page.goto(url,{waitUntil:"domcontentloaded",timeout:25000});await page.screenshot({path:"research/ui/"+name+"-browser.png"});results.push({name,title:await page.title(),text:(await page.locator("body").innerText()).slice(0,700)});}catch(e){results.push({name,error:String(e)});}}console.log(JSON.stringify(results));}'
result=subprocess.run([shutil.which('node'),str(root/'node_modules/@playwright/cli/playwright-cli.js'),'run-code',code],cwd=root,capture_output=True)
(root/'research/ui/browser-observations.txt').write_bytes(result.stdout+result.stderr)
print((result.stdout+result.stderr).decode('utf-8',errors='replace')[-2000:])
