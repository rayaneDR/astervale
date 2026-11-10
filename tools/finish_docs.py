"""Update project truth after Plan B implementation; no claims inferred from source."""
from pathlib import Path
import shutil,json
ROOT=Path(__file__).resolve().parents[1]

(ROOT/'README.md').write_text('''# AsterVale

An original, zero-budget Android 16 layer project for Samsung Galaxy A51 **SM-A515F / a51 / Exynos 9611**.

**Plan B is the default: a standalone APK and optional root-manager module over an existing community ROM. Hardware behavior is untested. No full AsterVale ROM has been compiled.**

![Browser prototype, not Android screenshot](docs/screenshots/desktop.png)

## Try it

- [Interactive design preview](https://rayanedr.github.io/astervale/preview.html)
- [Website](https://rayanedr.github.io/astervale/)
- [Layer prereleases](https://github.com/rayaneDR/astervale/releases)
- [Installation and removal](docs/INSTALL.md)

The nine-screen browser prototype supports light/dark, Arabic/RTL, text scaling, quick-setting demos, per-game profile preferences and assistant consent/confirmation. It reads no real notifications, device settings or API keys. Locally: `python -m http.server 4173 --directory site --bind 127.0.0.1`.

## What exists

| Component | Artifact label | Evidence / limitation |
| --- | --- | --- |
| Original design + web prototype | built | Browser flow checks, screenshots; not native SystemUI |
| Standalone home + drawer | untested | Native source; check validation report for APK build result; not a complete Launcher3 fork |
| Rill local command assistant | built / untested | Actual Java matcher tested on host; Android actions/voice untested |
| Floating Seed / Pebble / Kite companion | untested | Drag/edge snap/tap/menu, optional overlay; no screen reading |
| Optional root-manager module | built / untested | Packaged; explicit reversible debloat only, no boot-time tuning |
| Game profiles | untested | Preferences only; no CPU/GPU/thermal changes or FPS claims |
| On-device speech / offline TTS | untested | Android service/voice availability required; no bundled ASR model |
| Model/cloud integration | untested | Not implemented; no general-purpose LLM or cloud requests |
| Global localization | untested | 11 language/script command variants, Arabic panel resources; full app translation incomplete |
| Full ROM and OTA | untested | Pinned source preparation; no adequate free builder or owner firmware/test evidence |

Rill defaults to English and has a conservative local intent router with explanations in English, Arabic, Moroccan Darija Arabic/Arabizi, French, Spanish, Portuguese, Russian, Turkish, Hindi and Chinese. [Actual 125-case text benchmark with failures](docs/LANGUAGE_BENCHMARK.md). This does not establish speech quality, general language support or A51 latency.

The [upstream community feed](https://github.com/Exynos9611Development/OTA/blob/lineage/a51/ota.json) lists a February 14, 2026 LineageOS 23.2 A51 build. Its download responded HTTP 200 with the expected byte count on 2026-11-10. We have not downloaded, flashed or tested it. It is about nine months old, so it is not advertised as a recent security baseline. See [Plan B and its limits](docs/PLAN_B.md).

Read [STATUS](STATUS.md), [design system](DESIGN.md), [base research](docs/BASE_RESEARCH.md), [feature ranking](docs/FEATURE_RESEARCH.md), [local AI research](docs/AI_RESEARCH.md), [Plan A build notes](docs/BUILD.md), [recovery](docs/RECOVERY.md), [validation](docs/VALIDATION.md) and [contributing](CONTRIBUTING.md).

## Build the APK for free

Use JDK 21, Android SDK 36 / Build Tools 36 and the checked-in Gradle wrapper. `gradlew.bat --no-daemon :layer:assembleDebug` on Windows, or `bash gradlew --no-daemon :layer:assembleDebug` on Linux. This compiles only the small app, not AOSP. `python tools/package_layer.py` packages the optional module and copies an existing built APK into `dist/`. All generated binaries stay outside Git.

Initial APKs use a debug/test certificate and preview ID; CI artifacts can have different test certificates. They are not a production updater channel. No secrets, Samsung blobs or Google apps are included. [Full licensing notices](NOTICE): original source Apache-2.0, upstream kernel GPLv2, fonts OFL. Independent project, unaffiliated with Samsung, Google, Apple or LineageOS.
''',encoding='utf-8')

(ROOT/'STATUS.md').write_text('''# Status — 2026-11-10 (owner-local date)

## Active scope
Replacement master brief accepted. **Zero budget. Plan B default:** APK + optional module over a community ROM. Continue original AsterVale identity, prototype and LineageOS 23.2 sources. No rented/cloud service provisioned. Plan A full ROM remains separate and blocked on proven free resources.

## Done
- Created public GitHub repository rayaneDR/astervale; local feature commits preserve source changes.
- Pinned 16 public hardware/device/kernel projects; proprietary vendor trees excluded. Kernel branch is AOSP, root manifest LineageOS 23.2.
- Verified upstream A51 OTA feed and download HEAD: HTTP 200, 1,092,215,327 bytes for 2026-02-14 build. Maintainer stability claim is not owner proof; build is not recent.
- Original design system, local OFL fonts, original geometry wallpaper/icons and nine-screen prototype.
- Browser flow checks passed after fixing large RTL clock overflow. No browser console errors. Native rendering not tested.
- Native standalone home, Rill command panel, profile preferences and optional three-character companion source.
- 99 text-route rules and 125 development benchmark cases across 11 language/script variants. Report contains misses; no speech/model/device score fabricated.
- Built optional Magisk-manager module package: no autorun tuning, explicit reversible two-package debloat, read-only inventory.
- Local tools: existing Android SDK/Gradle reused; checksum-verified Temurin 21 installed in ignored tools/bin. OpenAI Playwright installed; official Android LiteRT-LM skill installed for future model integration (available next turn).
- GitHub Pages enabled with free standard-runner workflow. Deployment result recorded separately in validation.

## Failed / limitations
- JDK 25 could not run Gradle 8.14.3; corrected to verified JDK 21.
- First Java app compilation found missing PopupMenu import; corrected and rebuilding.
- Full ROM: no adequate free Linux host, owner firmware donor/current bootloader inventory or base-on-phone test result.
- No A51 hardware, speech, thermal, battery, 60 fps, model inference or OTA validation.
- No bundled Whisper/Vosk model, LLM, notification summary, cloud BYOK, automatic game/video hiding or Accessibility/Shizuku broker.
- Global UI translation, actual SystemUI/lockscreen port, icon-pack/widget engine, first-boot native wizard and production signing/update channel remain incomplete.
- Gaming choices are preferences; CPU/GPU/ZRAM/process-limit/thermal writes disabled.
- Heimdall latest-release API returned 404; no unofficial Odin/Heimdall binary installed.

## Milestones under replacement brief
| Milestone | Label | State |
| --- | --- | --- |
| M0 research/design/build path | built | Plan B chosen and cost-free toolchain prepared |
| M1 community base + installable layer | built / untested | Community ZIP availability verified; layer packaging in progress; owner boot proof absent |
| M2 UI layer | built / untested | Browser verified; native home is a minimal preview |
| M3 Rill + companion | built / untested | Host text tests done; native behavior/speech/model quality untested |
| M4 performance/gaming | built / untested | Optional module packaged; hardware tuning and benchmarks pending |
| M5 extras/localization/website | built / untested | Website/release tooling; complete localization/editions pending |

## Next
1. Finish APK compilation/lint and publish preview artifacts with hashes and exact limitations.
2. Owner installs APK optionally, tests ordinary home/actions first, then separately opts into companion. No ROM flashing required for this first preview.
3. Record owner model/firmware and community base test report before describing M1 as working.
4. Review language failures with native speakers; benchmark actual speech on the owner's phone. No language marked fully supported from synthetic fixtures.
5. Finish native localization and UI parity, then measured per-app performance and optional model adapters. Keep thermal protection.
6. Plan A only after a free/community Linux x86-64 host with 64 GB RAM and 700 GB free SSD is actually available. Never spend money.
''',encoding='utf-8')

p=ROOT/'PRODUCT.md';s=p.read_text(encoding='utf-8').replace('Soong Java app and RRO feature layer.','Standalone Java APK with Gradle 8.14.3 / AGP 8.13.2, plus separate future Soong/RRO layer.').replace('remote Linux compilation required.','full-ROM compilation requires a proven free Linux host; no paid services. Standalone APK compilation uses existing Windows SDK and JDK 21.')
p.write_text(s,encoding='utf-8')

p=ROOT/'docs/PLAN_B.md';s=p.read_text(encoding='utf-8').replace('Actual download availability must be checked separately; never assume a JSON URL is live or authentic from the filename alone.','A HEAD request on 2026-11-10 returned HTTP 200 and Content-Length 1,092,215,327. This verifies endpoint availability/size, not package checksum, authenticity or boot behavior; the ROM was not downloaded.')
p.write_text(s,encoding='utf-8')

shots=ROOT/'docs/screenshots';shots.mkdir(exist_ok=True)
for name in ['desktop','mobile','landing-desktop','landing-mobile','assistant','gaming','controls','rtl-large-dark']:
    source=ROOT/f'output/playwright/{name}.png'
    if source.exists():shutil.copy2(source,shots/f'{name}.png')

print('Updated replacement-brief project truth and copied real browser captures.')
