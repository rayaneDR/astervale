"""Fetch source evidence and original-source assets. Does not execute downloads."""
from research import get, ROOT, OUT
import json, pathlib

urls = {
 'community.xml': 'https://raw.githubusercontent.com/Exynos9611Development/local_manifests/lineage-23.2/common.xml',
 'a51.dependencies.json': 'https://raw.githubusercontent.com/Exynos9611Development/android_device_samsung_a51/lineage-23.2/lineage.dependencies',
 'a51.BoardConfig.mk': 'https://raw.githubusercontent.com/Exynos9611Development/android_device_samsung_a51/lineage-23.2/BoardConfig.mk',
 'common.BoardConfig.mk': 'https://raw.githubusercontent.com/Exynos9611Development/android_device_samsung_universal9611-common/lineage-23.2/BoardConfigCommon.mk',
 'a51.product.mk': 'https://raw.githubusercontent.com/Exynos9611Development/android_device_samsung_a51/lineage-23.2/lineage_a51.mk',
 'a51.proprietary-list.txt': 'https://raw.githubusercontent.com/Exynos9611Development/android_device_samsung_a51/lineage-23.2/proprietary-files.txt',
 'a51.extract.py': 'https://raw.githubusercontent.com/Exynos9611Development/android_device_samsung_a51/lineage-23.2/extract-files.py',
 'a51.releasetools.py': 'https://raw.githubusercontent.com/Exynos9611Development/android_device_samsung_a51/lineage-23.2/releasetools/releasetools.py',
 'common.releasetools.py': 'https://raw.githubusercontent.com/Exynos9611Development/android_device_samsung_universal9611-common/lineage-23.2/releasetools/releasetools.py',
 'lineage-manifest.xml': 'https://raw.githubusercontent.com/LineageOS/android/lineage-23.2/default.xml',
 'heimdall-repo.json': 'https://api.github.com/repos/Benjamin-Dobell/Heimdall',
 'kernel-branches.json': 'https://api.github.com/repos/Exynos9611Development/android_kernel_samsung_universal9611/branches',
}
for name, url in urls.items():
    try:
        data = get(url); (OUT/name).write_bytes(data); print(name, len(data))
    except Exception as exc:
        print(name, str(exc))

assets = ROOT / 'site' / 'assets'
assets.mkdir(parents=True, exist_ok=True)
for name, url in {
 'Manrope.ttf': 'https://raw.githubusercontent.com/google/fonts/main/ofl/manrope/Manrope%5Bwght%5D.ttf',
 'Manrope-OFL.txt': 'https://raw.githubusercontent.com/google/fonts/main/ofl/manrope/OFL.txt',
 'NotoSansArabic.ttf': 'https://raw.githubusercontent.com/google/fonts/main/ofl/notosansarabic/NotoSansArabic%5Bwdth,wght%5D.ttf',
 'NotoSansArabic-OFL.txt': 'https://raw.githubusercontent.com/google/fonts/main/ofl/notosansarabic/OFL.txt',
}.items():
    try:
        data = get(url); (assets/name).write_bytes(data); print(name, len(data))
    except Exception as exc: print(name, str(exc))

skill = pathlib.Path.home() / '.codex/skills/playwright'
if not skill.exists():
    for source, dest in [('playwright-skill.txt','SKILL.md'), ('playwright-wrapper.txt','scripts/playwright_cli.sh'), ('playwright-reference.txt','references/cli.md')]:
        target = skill / dest
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((OUT/source).read_bytes())
    print('Installed reviewed OpenAI Playwright skill', skill)
