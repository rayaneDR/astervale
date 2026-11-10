from pathlib import Path
import json,shutil
ROOT=Path(__file__).resolve().parents[1]
release='https://github.com/rayaneDR/astervale/releases/tag/v0.1.0-layer-preview'
p=ROOT/'STATUS.md';s=p.read_text(encoding='utf-8')
s=s.replace('layer packaging in progress','APK and optional module packaged')
s=s.replace('First Java app compilation found missing PopupMenu import; corrected and rebuilding.','First Java compilation found a missing PopupMenu import; corrected. Lint caught two layout-constant errors; corrected. Final local assembleDebug + lintDebug succeeded.')
s=s.replace('1. Finish APK compilation/lint and publish preview artifacts with hashes and exact limitations.','1. Owner test the published preview using docs/INSTALL.md; APK compile, lint and signature verification completed. No hardware milestone is considered passed.')
s=s.replace('- Native standalone home, Rill command panel, profile preferences and optional three-character companion source.','- Built standalone APK with original home, Rill command panel, profile preferences and optional three-character companion. Test certificate verified; hardware untested.')
s=s.replace('- GitHub Pages enabled with free standard-runner workflow. Deployment result recorded separately in validation.','- GitHub Pages deployed successfully; public preview HTTP 200. Free standard-runner APK/source checks passed. Initial invalid setup-java pin was corrected against the official repository.')
p.write_text(s,encoding='utf-8')
p=ROOT/'README.md';s=p.read_text(encoding='utf-8').replace('| Standalone home + drawer | untested | Native source; check validation report for APK build result; not a complete Launcher3 fork |','| Standalone home + drawer | built / untested | APK compiled and linted; hardware untested; not a complete Launcher3 fork |')
s=s.replace('Read [STATUS](STATUS.md),','Read [known issues](docs/KNOWN_ISSUES.md), [STATUS](STATUS.md),')
p.write_text(s,encoding='utf-8')
p=ROOT/'docs/VALIDATION.md'
p.write_text('''# Validation — 2026-11-10 owner-local date

## Actual results

- Windows local build: JDK 21.0.13+9, Gradle 8.14.3, AGP 8.13.2, SDK/Build Tools 36. `:layer:assembleDebug :layer:lintDebug` completed **BUILD SUCCESSFUL** after fixing the missing import and layout-constant errors. Final run: 1m31s, 45 tasks (23 executed, 22 up-to-date). This is app compilation only.
- APK signature: Android `apksigner verify --verbose` passed, APK Signature Scheme v2, one signer, debug/test certificate. No SourceStamp or production trust chain claimed.
- Android lint: zero errors. Remaining warnings document the deliberate Android 16 target rather than Android 17 and hardcoded/incomplete localization. No blanket lint suppression or baseline hid errors.
- Source contracts: six tests passed (no proprietary vendor sync, no app Internet/screen/SMS privileges, no module flash/sysfs/autorun writes, XML parse, language fixtures, no external web script).
- Actual Java intent engine: 125 host development text cases; see LANGUAGE_BENCHMARK.md for language counts and failures. 17 additional negation/compound/quoted/code-switch safety assertions passed. Neither test proves arbitrary-language understanding or phone execution.
- Browser Chrome QA: all nine screens, assistant disabled/consent/cancel/confirm, stored profile, drawer search/empty state, quick toggles, light/dark, Arabic RTL, 200% text, reduced-motion option, 390px page overflow, local-only resources. Initial lock clock overflow fixed. Browser console: zero errors/warnings. Actual captures in docs/screenshots; none are native screenshots.
- Design detector ran: cream-palette warning intentionally matches recorded mineral direction; small functional labels were enlarged. These advisories do not establish native accessibility compliance.
- Public website workflow succeeded and preview returned HTTP 200. Source/APK GitHub Actions run [42921769183](https://github.com/rayaneDR/astervale/actions/runs/42921769183) succeeded on a standard free runner. This proves small-APK build feasibility, not AOSP capacity.
- Upstream community ROM: feed inspected and release HEAD returned HTTP 200 / 1,092,215,327 bytes. No ZIP download/hash verification, flash or boot test performed.

## Untested

Android installation/rendering, launcher behavior, overlay gestures/lifecycle, on-device speech availability/quality, TTS, hardware services, frame rate, thermals, battery, performance profiles, module install/remove/debloat restore, full ROM boot, SELinux runtime and OTA. No owner test report exists. No general model benchmark exists. See KNOWN_ISSUES.md.
''',encoding='utf-8')
for name in ['desktop','mobile','landing-desktop','landing-mobile','assistant','gaming','controls','rtl-large-dark']:
    p=ROOT/f'output/playwright/{name}.png'
    if p.exists():shutil.copy2(p,ROOT/f'docs/screenshots/{name}.png')
p=ROOT/'site/index.html';s=p.read_text(encoding='utf-8')
s=s.replace('The first release is source and design work. There is no flashable AsterVale ZIP yet.','The first layer preview includes a small experimental APK, an optional module and original art assets. No full AsterVale ROM has been compiled.')
s=s.replace('<a class="button primary" href="https://github.com/rayaneDR/astervale">Follow the project ↗</a>','<a class="button primary" href="'+release+'">Get the layer preview ↗</a>')
p.write_text(s,encoding='utf-8')
p=ROOT/'CHANGELOG.md';s=p.read_text(encoding='utf-8')
s=s.replace('No compiled ROM/APK, device test result or downloadable flashable release.','Standalone preview APK compiled and linted; optional root-manager module and original art pack built. No compiled full ROM or device test result. Plan B is the default under the zero-budget replacement brief.')
p.write_text(s,encoding='utf-8')
print('Final evidence and release-facing documentation updated.')
