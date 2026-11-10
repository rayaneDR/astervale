# Known issues — preview 0.1.0

- No Android runtime or SM-A515F hardware tests. A successful APK compile/signature check does not prove install, launcher behavior, bubble gestures, battery impact or compatibility.
- The home is a minimal original launcher preview, not the full browser design or a Launcher3/Lawnchair fork. Widgets, app-icon packs, gestures and complete native theming remain pending. Keep Trebuchet installed.
- Rill is a deterministic command router, not a general-purpose LLM. No bundled Whisper/Vosk, model runtime, model downloads, notification summaries, cloud BYOK, app closing, direct Wi-Fi/Bluetooth toggles or arbitrary setting writes.
- On-device speech service may be absent in vanilla LineageOS. Offline TTS depends on an installed voice; Darija voice availability is unverified. Text routing is limited; shared words use selected language, and code-switch detection is incomplete.
- Host development benchmark misses an Arabizi battery phrase and Turkish inflections. The fixture set is small and includes author-written templates; no broad per-language quality claim. All A51 speech/model/latency numbers remain untested.
- Companion's listening/thinking/speaking states in the long-press menu are visual demos. Battery/charging/screen-off behavior is source-only until owner tests. Notification reaction, game/video auto-hide, persistent position and accessible non-drag reposition controls need completion.
- App UI localization is incomplete beyond current resources. Language choice affects the command router and speech request; it does not yet translate every native screen. All translations require native-speaker review.
- The optional module supports only SM-A515F / API 36 and only two manual debloat choices. No tuning runs at boot. KernelSU, installation/uninstallation recovery and actual package state restoration are untested.
- Test-signed APKs are not production updates. Different CI debug keys may require uninstall/reinstall. Do not treat the SHA256 file as a substitute for a production signing trust chain.
- No proven free full-ROM host, current donor firmware inventory or owner base-boot report. Upstream February 2026 ROM is available but old; maintainer stability claims do not establish current security or AsterVale compatibility. IMS/VoLTE/VoWiFi and every hardware function remain untested.
- No full-ROM OTA, GApps variants, complete Lite/Gaming/Full builds, native first-boot wizard or tested recovery release. Art-pack ZIPs and bootanimation.zip are not flashable.
