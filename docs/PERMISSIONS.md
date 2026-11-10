# Control methods and permissions

| Method | What it needs | Current use / limit |
| --- | --- | --- |
| Normal Android intents/panels | User APK, explicit confirmation | Implemented routes to Wi-Fi/volume panels, other settings and alarm/timer UI. Does not silently toggle restricted radios or close other apps |
| Home role | Owner chooses default home | Optional minimal launcher; base Trebuchet retained |
| Companion overlay | Draw over apps + foreground notification permission | Optional bubble only. No screen capture, accessibility tree, notification access or background mic |
| Voice | Runtime microphone + installed on-device service | One explicit session; service may be absent on vanilla ROM. No online fallback |
| TTS | Installed offline voice for selected language | Select only voices marked non-network; no guaranteed Darija voice |
| Notification listener | Owner separately enables service | Not implemented or requested |
| Accessibility | Owner separately enables narrowly scoped service | Not implemented; do not claim it can freely toggle everything or circumvent Android restrictions |
| Shizuku | Owner starts service via authorized ADB/wireless debugging; per-app authorization | Not integrated. ADB grant is not root or platform signature |
| Root module | Existing compatible root manager | Optional explicit two-package debloat only, no tuning daemon or installed APK privilege escalation |
| Full-ROM privileged app | Platform build/signing + appropriate allowlists/SELinux | Separate Soong source; not the installed Plan B APK and not a grant of arbitrary permissions |

Calls/messages, app force-stop, broad settings writes and model-proposed actions must use a bounded adapter and explicit confirmation. Current app has no INTERNET, QUERY_ALL_PACKAGES, SMS, call-log, notification or screen-reading permission. The timer editor uses normal SET_ALARM permission with its own UI, not a silently created inferred timer.
