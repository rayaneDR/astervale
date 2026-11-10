"""Generate a source-only manifest from the reviewed community manifest."""
import concurrent.futures, json, xml.etree.ElementTree as ET
from research import get, ROOT, OUT

def main():
    original = ET.fromstring((OUT/'community.xml').read_bytes())
    remotes = {r.attrib['name']:r.attrib for r in original.findall('remote')}
    projects = [p.attrib for p in original.findall('project') if not p.attrib['path'].startswith('vendor/') and (not p.attrib['path'].startswith('device/samsung/') or p.attrib['path'] in ['device/samsung/a51','device/samsung/universal9611-common'])]
    def pin(p):
        r=remotes[p['remote']]; branch=p.get('revision',r['revision'])
        owner=r['fetch'].rstrip('/').split('/')[-1]
        data=json.loads(get(f'https://api.github.com/repos/{owner}/{p["name"]}/commits/{branch}'))
        return {**p,'revision':data['sha'],'source_branch':branch,'url':f'https://github.com/{owner}/{p["name"]}'}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        locked=list(pool.map(pin,projects))
    root=ET.Element('manifest')
    for name,r in remotes.items(): ET.SubElement(root,'remote',{'name':'av-'+name,'fetch':r['fetch']})
    base=ET.fromstring((OUT/'lineage-manifest.xml').read_bytes())
    existing={p.attrib.get('path',p.attrib['name']) for p in base.findall('project')}
    for p in locked:
        if p['path'] in existing: ET.SubElement(root,'remove-project',{'path':p['path']})
        ET.SubElement(root,'project',{'path':p['path'],'name':p['name'],'remote':'av-'+p['remote'],'revision':p['revision']})
    ET.indent(root,space='  ')
    target=ROOT/'manifests'; target.mkdir(exist_ok=True)
    (target/'a51.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n'+ET.tostring(root,encoding='unicode')+'\n',encoding='utf-8')
    root_commit=json.loads(get('https://api.github.com/repos/LineageOS/android/commits/lineage-23.2'))['sha']
    (target/'sources.json').write_text(json.dumps({'checked':'2026-11-10','root_manifest':{'url':'https://github.com/LineageOS/android','branch':'lineage-23.2','revision':root_commit},'projects':locked,'note':'Full dependency lock must be generated with repo manifest -r after sync. Proprietary vendor repos intentionally omitted.'},indent=2)+'\n')
    print(f'Pinned {len(locked)} projects. Kernel:',next(p['revision'] for p in locked if p['path'].startswith('kernel/')))

if __name__=='__main__': main()
