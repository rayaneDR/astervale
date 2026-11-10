"""Download public reference metadata/images for inspection only; never product assets."""
from pathlib import Path
from html.parser import HTMLParser
import json,urllib.request,urllib.parse,concurrent.futures
ROOT=Path(__file__).resolve().parents[1];out=ROOT/'research/ui';out.mkdir(parents=True,exist_ok=True)
SOURCES={
 'apple27':'https://developer.apple.com/news/?id=e2lxw9l1',
 'apple-materials':'https://developer.apple.com/design/human-interface-guidelines/materials',
 'apple-refinements':'https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/',
 'material-expressive':'https://blog.google/products-and-platforms/platforms/android/material-3-expressive-android-wearos-launch/',
 'oneui':'https://developer.samsung.com/one-ui/index.html',
 'hyperos':'https://www.mi.com/global/hyperos',
 'dribbble-control':'https://dribbble.com/shots/26175703-Apple-Liquid-Glass-iOS-26-Control-Center-UI-Kit',
 'behance-glass':'https://www.behance.net/gallery/228076573/SmartHomeX-iOS-26-Glassmorphic-Dashboard-UI',
 'mobbin':'https://mobbin.com/browse/ios/apps',
 'emil-motion':'https://emilkowal.ski/ui/good-vs-great-animations',
}
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 AsterVale-design-research'}),timeout=35) as r:return r.read()
class Metadata(HTMLParser):
    def __init__(self):super().__init__();self.images=[]
    def handle_starttag(self,tag,attributes):
        a=dict(attributes)
        if tag=='meta' and a.get('property')=='og:image':self.images.append(a.get('content'))
        if tag=='img' and ('image' in a.get('class','') or 'hero' in a.get('class','')):
            src=a.get('src')
            if src and not src.startswith('data:'):self.images.append(src)
def fetch(item):
    name,url=item
    try:
        data=get(url);(out/(name+'.html')).write_bytes(data)
        meta=Metadata();meta.feed(data.decode('utf-8',errors='replace'))
        record={'name':name,'url':url,'status':'fetched','image_candidates':meta.images[:5]}
        if meta.images:
            image_url=urllib.parse.urljoin(url,meta.images[0]);payload=get(image_url)
            (out/(name+'.image')).write_bytes(payload);record['reference_image']=str(out/(name+'.image'))
        return record
    except Exception as e:return {'name':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:results=list(pool.map(fetch,SOURCES.items()))
(out/'sources.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
