# Status — 2026-11-10 (owner-local date)

## Active scope
Replacement master brief accepted. **Zero budget. Plan B default:** APK + optional module over a community ROM. Continue original AsterVale identity, prototype and LineageOS 23.2 sources. No rented/cloud service provisioned. Plan A full ROM remains separate and blocked on proven free resources.

## Done
- Created public GitHub repository rayaneDR/astervale; local feature commits preserve source changes.
- Pinned 16 public hardware/device/kernel projects; proprietary vendor trees excluded. Kernel branch is AOSP, root manifest LineageOS 23.2.
- Verified upstream A51 OTA feed and download HEAD: HTTP 200, 1,092,215,327 bytes for 2026-02-14 build. Maintainer stability claim is not owner proof; build is not recent.
- Original design system, local OFL fonts, original geometry wallpaper/icons and nine-screen prototype.
- Browser flow checks passed after fixing large RTL clock overflow. No browser console errors. Native rendering not tested.
- Built standalone APK with original home, Rill command panel, profile preferences and optional three-character companion. Test certificate verified; hardware untested.
- 99 text-route rules and 125 development benchmark cases across 11 language/script variants. Report contains misses; no speech/model/device score fabricated.
- Built optional Magisk-manager module package: no autorun tuning, explicit reversible two-package debloat, read-only inventory.
- Local tools: existing Android SDK/Gradle reused; checksum-verified Temurin 21 installed in ignored tools/bin. OpenAI Playwright installed; official Android LiteRT-LM skill installed for future model integration (available next turn).
- GitHub Pages deployed successfully; public preview HTTP 200. Free standard-runner APK/source checks passed. Initial invalid setup-java pin was corrected against the official repository.

## Failed / limitations
- JDK 25 could not run Gradle 8.14.3; corrected to verified JDK 21.
- First Java compilation found a missing PopupMenu import; corrected. Lint caught two layout-constant errors; corrected. Final local assembleDebug + lintDebug succeeded.
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
| M1 community base + installable layer | built / untested | Community ZIP availability verified; APK and optional module packaged; owner boot proof absent |
| M2 UI layer | built / untested | Browser verified; native home is a minimal preview |
| M3 Rill + companion | built / untested | Host text tests done; native behavior/speech/model quality untested |
| M4 performance/gaming | built / untested | Optional module packaged; hardware tuning and benchmarks pending |
| M5 extras/localization/website | built / untested | Website/release tooling; complete localization/editions pending |

## Next
1. Owner test the published preview using docs/INSTALL.md; APK compile, lint and signature verification completed. No hardware milestone is considered passed.
2. Owner installs APK optionally, tests ordinary home/actions first, then separately opts into companion. No ROM flashing required for this first preview.
3. Record owner model/firmware and community base test report before describing M1 as working.
4. Review language failures with native speakers; benchmark actual speech on the owner's phone. No language marked fully supported from synthetic fixtures.
5. Finish native localization and UI parity, then measured per-app performance and optional model adapters. Keep thermal protection.
6. Plan A only after a free/community Linux x86-64 host with 64 GB RAM and 700 GB free SSD is actually available. Never spend money.
