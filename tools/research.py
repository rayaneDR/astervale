"""Read public upstream metadata; never downloads proprietary vendor repositories."""
import concurrent.futures, hashlib, json, pathlib, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'research'
OUT.mkdir(exist_ok=True)

def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'AsterVale-source-audit'})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read()

JOBS = {
    'community-manifest': 'https://api.github.com/repos/Exynos9611Development/local_manifests/contents?ref=lineage-23.2',
    'a51-head': 'https://api.github.com/repos/Exynos9611Development/android_device_samsung_a51/branches/lineage-23.2',
    'common-head': 'https://api.github.com/repos/Exynos9611Development/android_device_samsung_universal9611-common/branches/lineage-23.2',
    'kernel-head': 'https://api.github.com/repos/Exynos9611Development/android_kernel_samsung_universal9611/branches/lineage-23.2',
    'a51-tree': 'https://api.github.com/repos/Exynos9611Development/android_device_samsung_a51/git/trees/lineage-23.2?recursive=1',
    'playwright-skill': 'https://raw.githubusercontent.com/openai/skills/main/skills/.curated/playwright/SKILL.md',
    'playwright-wrapper': 'https://raw.githubusercontent.com/openai/skills/main/skills/.curated/playwright/scripts/playwright_cli.sh',
    'playwright-reference': 'https://raw.githubusercontent.com/openai/skills/main/skills/.curated/playwright/references/cli.md',
    'repo-launcher': 'https://storage.googleapis.com/git-repo-downloads/repo',
    'heimdall-release': 'https://api.github.com/repos/Benjamin-Dobell/Heimdall/releases/latest',
    'lawnchair': 'https://api.github.com/repos/LawnchairLauncher/lawnchair',
}

def fetch(item):
    name, url = item
    try:
        data = get(url)
        (OUT / (name + '.txt')).write_bytes(data)
        return {'name': name, 'url': url, 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
    except Exception as exc:
        return {'name': name, 'url': url, 'error': str(exc)}

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(fetch, JOBS.items()))
    (OUT / 'downloads.json').write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results, indent=2))
