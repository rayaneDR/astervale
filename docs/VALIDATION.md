# Validation — 2026-11-10 owner-local date

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
