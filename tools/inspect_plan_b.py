"""Inspect public build feeds and tool metadata without executing remote code."""
from research import get, OUT, ROOT
import json, pathlib
for name,url in {
 'ota-a51.json':'https://api.github.com/repos/Exynos9611Development/OTA/contents/a51?ref=lineage',
 'jdk.json':'https://api.adoptium.net/v3/assets/latest/21/hotspot?architecture=x64&image_type=jdk&os=windows&vendor=eclipse',
 'android-skills.json':'https://api.github.com/repos/android/skills/git/trees/main?recursive=1',
 'anthropic-skills.json':'https://api.github.com/repos/anthropics/skills/contents/skills',
}.items():
    try:
        data=get(url);(OUT/name).write_bytes(data)
        if name=='ota-a51.json': print(data.decode()[:6000])
        elif name=='jdk.json':
            item=json.loads(data)[0]['binary']['package'];print('JDK',item['link'],item['checksum'])
        else:
            data=json.loads(data)
            paths=[x.get('path',x.get('name')) for x in (data.get('tree',[]) if isinstance(data,dict) else data)]
            print(name,[p for p in paths if 'SKILL' in p or '/' not in p][:30])
    except Exception as e:print(name,e)
