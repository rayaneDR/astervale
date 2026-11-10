# Installable layer preview

**APK and optional root module are separate. Neither is a ROM. Hardware behavior is untested.** Keep the existing launcher and recovery route.

1. Verify SHA256 against the exact release's SHA256SUMS. The initial APK uses a debug/test certificate and a `.preview` application ID; it is an experimental preview, not a production-signed updater channel. Do not grant unrelated privileges.
2. Install the APK using Android's normal installer or `adb -s SERIAL install AsterVale-layer-0.1.0-preview.apk`. Open AsterVale Preview. Default home selection is optional; the Home settings button lets you return to Trebuchet.
3. Open Rill. Typed commands run a local curated rule matcher. Review the proposed Android control before continuing. There is no model or cloud connection. History is kept in memory only.
4. Voice uses `createOnDeviceSpeechRecognizer` only when Android reports availability; grant microphone permission only if you want voice. There is no online fallback. Select the language; full speech auto-detection/code-switching is not implemented. TTS only selects installed voices marked as not requiring network. External speech engines remain separate software whose behavior cannot be certified here.
5. Companion is optional: Enable asks for Draw over apps, then notification permission. Tap Enable again after granting. Tap bubble to open Rill, drag to move, long press for the menu, double-tap or notification Stop to hide. Size/opacity and original Seed/Pebble/Kite choices are in Rill. The listening/thinking/speaking menu entries are visual demos; the bubble does not continuously record or infer. Idle blinking pauses when screen off. Automatic game/video hiding and notification reactions are pending.
6. Optional module: install the ZIP from a compatible Magisk manager's module installer only. **Do not sideload it in recovery or Odin.** It asserts SM-A515F / API 36, installs no APK or privileged framework files and changes no tuning on boot. KernelSU compatibility is untested; do not assume it. Remove it through the same manager to restore AsterVale-owned debloat changes.

Optional manual root commands after reviewing the scripts:

```sh
sh /data/adb/modules/astervale_layer/manage.sh inventory
sh /data/adb/modules/astervale_layer/manage.sh disable printing
sh /data/adb/modules/astervale_layer/manage.sh restore printing
```

Only printing and the Lineage recorder are allowlisted. No uninstall/data deletion. Already-disabled packages are not claimed. No CPU/GPU/thermal/ZRAM writes exist. The APK's saved Game Mode choices are preferences, not evidence of performance tuning.

The separate art pack contains an original 1080×2400 wallpaper, two WAV sounds and a boot-animation asset. Select wallpaper/sounds manually if desired. **The art pack and its inner bootanimation.zip are not flashable packages.** Boot-animation installation is deferred until the exact ROM mount path and rollback are reviewed.

Uninstall the APK normally; stop the companion and select Trebuchet before uninstalling if you made AsterVale your home. Revoke overlay/microphone permissions through Android Settings. AsterVale never changes boot, recovery, vbmeta, system partition or bootloader lock state in Plan B.
