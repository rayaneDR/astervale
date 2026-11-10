"""Resolve official action tags to verified commit IDs before workflow execution."""
from research import get, ROOT, OUT
import concurrent.futures,json,re
versions={'checkout':'v4','setup-java':'v4','upload-artifact':'v4','configure-pages':'v5','upload-pages-artifact':'v3','deploy-pages':'v4'}
def pin(item):
    name,tag=item
    sha=json.loads(get(f'https://api.github.com/repos/actions/{name}/commits/{tag}'))['sha']
    (OUT/f'action-{name}.yml').write_bytes(get(f'https://raw.githubusercontent.com/actions/{name}/{sha}/action.yml'))
    return name,tag,sha
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:locked=list(pool.map(pin,versions.items()))
for p in (ROOT/'.github/workflows').glob('*.yml'):
    text=p.read_text()
    for name,tag,sha in locked:text=re.sub(r'actions/'+re.escape(name)+r'@[A-Za-z0-9._-]+',f'actions/{name}@{sha}',text)
    p.write_text(text)
(ROOT/'docs/ACTION_PINS.json').write_text(json.dumps([{'repository':f'actions/{name}','source_tag':tag,'commit':sha} for name,tag,sha in locked],indent=2)+'\n')
print(json.dumps(locked))
