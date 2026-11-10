"""Publish reviewed local preview binaries using configured GitHub Git credentials.

Credentials stay in memory, are never printed/written, and go only to GitHub's API.
This fallback handles local binary uploads unsupported by the connected uploader.
"""
from pathlib import Path
import base64,hashlib,json,os,subprocess,urllib.error,urllib.request
ROOT=Path(__file__).resolve().parents[1]
REPO='rayaneDR/astervale'
TAG='v0.1.0-layer-preview'

def main():
    manifest=json.loads((ROOT/'dist/artifacts.json').read_text())
    expected={'AsterVale-layer-0.1.0-preview.apk','AsterVale-optional-module-0.1.0-preview.zip','AsterVale-art-pack-0.1.0-preview.zip'}
    if {a['filename'] for a in manifest}!=expected:raise SystemExit('Unexpected artifact list')
    for a in manifest:
        p=ROOT/'dist'/a['filename']
        if hashlib.file_digest(p.open('rb'),'sha256').hexdigest()!=a['sha256']:raise SystemExit('Artifact checksum mismatch')
    revision=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    env={**os.environ,'GIT_TERMINAL_PROMPT':'0','GCM_INTERACTIVE':'never'}
    result=subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\npath='+REPO+'.git\n\n',cwd=ROOT,env=env,text=True,capture_output=True)
    if result.returncode:raise SystemExit('Configured GitHub credentials unavailable; no credential contents logged')
    credentials=dict(line.split('=',1) for line in result.stdout.splitlines() if '=' in line)
    if not credentials.get('password'):raise SystemExit('No GitHub credential')
    auth='Basic '+base64.b64encode((credentials.get('username','git')+':'+credentials['password']).encode()).decode()
    def api(path,body=None,method=None,binary=False):
        origin='https://uploads.github.com' if binary else 'https://api.github.com'
        data=body if binary else None if body is None else json.dumps(body).encode()
        request=urllib.request.Request(origin+path,data=data,method=method or ('POST' if body is not None else 'GET'),headers={'Authorization':auth,'Accept':'application/vnd.github+json','User-Agent':'AsterVale-preview-publisher','Content-Type':'application/octet-stream' if binary else 'application/json','X-GitHub-Api-Version':'2022-11-28'})
        with urllib.request.urlopen(request,timeout=90) as response:return json.load(response)
    notes=(ROOT/'docs/releases/layer-preview.md').read_text(encoding='utf-8')
    try:release=api('/repos/'+REPO+'/releases/tags/'+TAG)
    except urllib.error.HTTPError as e:
        if e.code!=404:raise
        release=api('/repos/'+REPO+'/releases',{'tag_name':TAG,'target_commitish':revision,'name':'AsterVale 0.1.0 layer preview — hardware untested','body':notes,'draft':False,'prerelease':True,'make_latest':'false'})
    if release.get('target_commitish') not in [revision,'main']:raise SystemExit('Existing tag targets a different revision; refusing overwrite')
    existing={a['name']:a for a in release.get('assets',[])}
    for name in sorted(expected|{'SHA256SUMS','artifacts.json'}):
        path=ROOT/'dist'/name
        if name in existing:
            # Verify state; never replay or replace an uncertain upload.
            with urllib.request.urlopen(existing[name]['browser_download_url']) as response:data=response.read()
            if hashlib.sha256(data).digest()!=hashlib.sha256(path.read_bytes()).digest():raise SystemExit('Existing asset differs; refusing replacement: '+name)
            continue
        asset=api(f'/repos/{REPO}/releases/{release["id"]}/assets?name={name}',path.read_bytes(),binary=True)
        print('Uploaded',asset['name'],asset['size'])
    print('Published',release['html_url'],'commit',revision)

if __name__=='__main__':main()
