# Feature contract

`built` means a named artifact was produced; it does not mean hardware tested. `untested` includes planned or uncompiled Android source. `tested by owner` requires an attached dated report and artifact SHA256. No feature currently has the last label.

| Feature | Browser | Android |
| --- | --- | --- |
| Lock/home/drawer | built | untested; base launcher kept, custom port pending |
| Notifications/control center | built | untested; SystemUI changes pending |
| Settings/appearance | built | untested; control-panel source |
| Per-app gaming profiles | built; local demo persistence | untested; native preference selection source |
| DND and app launching | illustrative | untested; Android permission-gated source |
| CPU/GPU/governor tuning | preview explanation only | untested; no writes enabled |
| Thermals/touch/ZRAM/background limits | no device claims | untested; discover and measure first |
| FPS/temperature overlay | clearly demo/unavailable | untested; no FPS source yet |
| AI panel/action preview | built; local demo, no network | untested; local allowlisted actions only |
| BYOK inference/notifications/on-device model | not implemented | untested; deferred |
| Setup wizard | built preview | untested; native replacement pending |
| Light/dark/Arabic/scaling | built preview | untested; native translations/overlay source |
| Boot/wallpaper/sound assets | source assets built | untested; installation pending |
| Lite/Gaming/Full | comparison | untested; product selection source |
| OTA | no downloads available | untested; release gate/feed tooling source |

Performance policy: preserve thermal trip points and SELinux enforcing. No global minimum clock boosts, overclocking, fake refresh rates, arbitrary GPU nodes, disabled thermal daemons, global process caps or clearing app data. Read capability nodes and valid frequency lists first; only adapter-owned paths with stock-value snapshots can be written in a future broker. Apply a per-app lease and restore on exit/crash/reboot/thermal pressure. An adapter missing a capability returns unsupported. No permission to create a universal root command executor.

Collect matched baseline/feature runs with same brightness, refresh rate, battery range, ambient temperature and app version. Warm up; repeat at least five times; report median/p95/p99 frame time, jank %, sustained FPS, thermal status and battery delta with raw traces. Measure cold start, drawer scroll, shade, keyboard and 20-minute game runs. Current numbers: **none**.
