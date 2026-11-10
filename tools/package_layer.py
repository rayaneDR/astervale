"""Create manager-installable module ZIP, never a ROM or recovery update ZIP."""
from pathlib import Path
import hashlib,zipfile,json,shutil
ROOT=Path(__file__).resolve().parents[1]
def package():
    out=ROOT/'dist';out.mkdir(exist_ok=True)
    target=out/'AsterVale-optional-module-0.1.0-preview.zip'
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
        for source in sorted((ROOT/'module').glob('*')):
            if source.is_file():z.writestr(source.name,source.read_bytes().replace(b'\r\n',b'\n'))
        z.writestr('capabilities.sh',(ROOT/'tools/capabilities.sh').read_bytes().replace(b'\r\n',b'\n'))
    apk=ROOT/'layer/build/outputs/apk/debug/layer-debug.apk'
    if apk.exists():shutil.copy2(apk,out/'AsterVale-layer-0.1.0-preview.apk')
    artifacts=[]
    for p in sorted(out.glob('*')):
        if p.suffix not in ['.apk','.zip']:continue
        artifacts.append({'filename':p.name,'bytes':p.stat().st_size,'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest(),'label':'built','hardware':'untested','kind':'apk' if p.suffix=='.apk' else 'optional-root-module-not-rom'})
    (out/'artifacts.json').write_text(json.dumps(artifacts,indent=2)+'\n')
    (out/'SHA256SUMS').write_text(''.join(f"{a['sha256']}  {a['filename']}\n" for a in artifacts))
    print(json.dumps(artifacts,indent=2))
if __name__=='__main__':package()
