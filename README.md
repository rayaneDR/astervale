# AsterVale

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
| Standalone home + drawer | built / untested | APK compiled and linted; hardware untested; not a complete Launcher3 fork |
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

Read [known issues](docs/KNOWN_ISSUES.md), [STATUS](STATUS.md), [design system](DESIGN.md), [base research](docs/BASE_RESEARCH.md), [feature ranking](docs/FEATURE_RESEARCH.md), [local AI research](docs/AI_RESEARCH.md), [Plan A build notes](docs/BUILD.md), [recovery](docs/RECOVERY.md), [validation](docs/VALIDATION.md) and [contributing](CONTRIBUTING.md).

## Build the APK for free

Use JDK 21, Android SDK 36 / Build Tools 36 and the checked-in Gradle wrapper. `gradlew.bat --no-daemon :layer:assembleDebug` on Windows, or `bash gradlew --no-daemon :layer:assembleDebug` on Linux. This compiles only the small app, not AOSP. `python tools/package_layer.py` packages the optional module and copies an existing built APK into `dist/`. All generated binaries stay outside Git.

Initial APKs use a debug/test certificate and preview ID; CI artifacts can have different test certificates. They are not a production updater channel. No secrets, Samsung blobs or Google apps are included. [Full licensing notices](NOTICE): original source Apache-2.0, upstream kernel GPLv2, fonts OFL. Independent project, unaffiliated with Samsung, Google, Apple or LineageOS.
