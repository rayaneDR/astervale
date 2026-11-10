# Plan B: the default, zero-budget layer

Owner directive on 2026-11-10: no rentals, purchases, subscriptions or paid runners. Build the APK and module locally on Windows. Full ROM compilation remains Plan A only if a donated/free host is proven adequate. Cloud trials often require billing identity/payment methods and quotas; none is provisioned here.

## Existing community ROM

The [community OTA feed](https://github.com/Exynos9611Development/OTA/blob/lineage/a51/ota.json) inspected on 2026-11-10 advertises `lineage-23.2-20260214-UNOFFICIAL-a51.zip`, 1,092,215,327 bytes, SHA256 `189cc491e9e58526fe8ee1d7f1a137496a722e02384ef07c1b24ca1d4fbe925a`, at the [upstream release URL](https://github.com/Exynos9611Development/OTA/releases/download/20260214/lineage-23.2-20260214-UNOFFICIAL-a51.zip). This feed entry is approximately nine months old, **not a recent-build guarantee**. Maintainers call A16 QPR2 stable on their [organization page](https://github.com/Exynos9611Development); this is a maintainer claim, not our hardware result. A HEAD request on 2026-11-10 returned HTTP 200 and Content-Length 1,092,215,327. This verifies endpoint availability/size, not package checksum, authenticity or boot behavior; the ROM was not downloaded. AsterVale does not redistribute the community ROM or its blobs.

M1 cannot honestly be marked “base working on owner's phone” until the owner reports install/boot results. Do not flash an old/community ROM on the strength of our prototype. Exact firmware/recovery instructions, security patch state and known defects must be read on the matching upstream release and confirmed for SM-A515F. Telephony, IMS/VoLTE/VoWiFi, cameras, UDFPS, encryption and OTA remain untested here.

## Layer architecture

`layer/`: standalone APK, original home preview, Rill local command router, profile-choice panel, optional overlay companion. Installs as a user app; no root, Shizuku or platform signature needed for its basic controls. `android/`: separate Soong/RRO source for a future full ROM. `module/`: optional root-manager package with device/API assertion and manual reversible debloat. No automatic tuning, package disabling or boot-image changes.

## Plan B limits

A normal APK cannot replace trusted SystemUI, real lockscreen, notification shade, Settings home, system boot animation/fonts, grant signature permissions or safely control arbitrary CPU/GPU nodes. Home-role apps can supply the launcher but cannot promise system-wide app transitions or 60 fps. RRO installation does not automatically make it trusted to overlay protected framework resources. Boot/font/theme changes require approved ROM overlay support, root module mounts, or a full source build. We provide candidate RRO source but do not activate framework overrides on an untested phone.

Rill routes Wi-Fi, Bluetooth, brightness, volume, battery, DND, alarms and timers to Android's existing controls after confirmation. It does **not** bypass Android restrictions to silently toggle them. App closing, notification summarization, call/message composition, actual performance changes, automatic game/video detection and model inference are not integrated in this preview. No Accessibility, Shizuku or root bridge is secretly enabled.

The current home is an original minimal implementation, not a Lawnchair fork and not a complete widget/icon-pack launcher. Keep community Trebuchet/Launcher3 installed and selectable. Original browser design precedes a deeper native port; current native UI does not yet match every browser screen.
