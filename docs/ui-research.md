# UI research → AsterVale redesign

Research completed **before prototype redesign**, 2026-11-10 (owner-local date). This report separates observed guidance, anecdotal feedback and our design decisions. No third-party assets, SF fonts or Apple icons will ship.

## References studied

| Reference | What informed the design |
| --- | --- |
| [Apple's iOS/iPadOS/macOS 27 design kits, June 2026](https://developer.apple.com/news/?id=e2lxw9l1) | Current-era reference, not an assumption that iOS 26 is latest. Inspected the public component image: concentrated controls, pill groups, soft edge lighting and strong text hierarchy. |
| [Apple 2026 design refinements](https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/) | Legibility, consistency and user-adjustable transparency are explicit priorities. |
| [HIG Materials](https://developer.apple.com/design/human-interface-guidelines/materials) | Glass distinguishes floating controls/navigation; content needs quieter material. Avoid a translucent card on every surface. |
| [Adopting Liquid Glass](https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass) and [iOS 26 screen resources](https://developer.apple.com/design/whats-new/) | Home/lock/control-center/widget/notification family, concentric shapes, appearance variants. Borrow hierarchy and cohesion, not branded components. |
| [HIG Layout](https://developer.apple.com/design/human-interface-guidelines/layout.md), [Typography](https://developer.apple.com/design/human-interface-guidelines/typography.md), [Icon Composer](https://developer.apple.com/icon-composer/) | Alignment, adaptable text roles, optically balanced simple icons. Open-font substitute required; no exported Apple assets. |
| [Designing Fluid Interfaces, WWDC18](https://developer.apple.com/videos/play/wwdc2018/803/) | Direct feedback, continuous manipulation and interruptible motion. Motion should preserve the relationship between source and destination. |
| [Material 3 Expressive announcement](https://blog.google/products-and-platforms/platforms/android/material-3-expressive-android-wearos-launch/) and [motion overview](https://m3.material.io/styles/motion/overview/how-it-works) | Reviewed public multi-screen image: emphasis through scale/shape/color, configurable controls and responsive feedback. Keep Android semantics; avoid importing every expressive flourish onto old hardware. |
| [One UI principles](https://developer.samsung.com/one-ui/index.html), [layout](https://developer.samsung.com/one-ui/layout/basic.html), [motion](https://developer.samsung.com/one-ui/motion/basic.html), [scalable typography](https://developer.samsung.com/one-ui/accessibility/layout-and-typo.html) | Separate the viewing area from reachable actions; preserve 200% text scaling and predictable navigation. |
| [HyperOS 4 public design showcase](https://www.mi.com/global/hyperos) | Inspected the official widget image: large readable values, soft depth and grouped glanceable information. Our icons/wallpaper remain original. Its device performance claims do not transfer to A51. |
| [Lawnchair 16 source](https://github.com/LawnchairLauncher/lawnchair), [theming documentation](https://github.com/LawnchairLauncher/docs/blob/main/help/core-features/theming-and-icons.md), [crDroid Settings source](https://github.com/crdroidandroid/android_packages_apps_crDroidSettings) | Preserve icon packs, per-icon choices, font/color settings and an app drawer rather than treating iOS similarity as loss of Android customization. |
| [Glass Launcher listing and current reviews](https://play.google.com/store/apps/details?hl=en-US&id=com.luutinhit.launcherios) | Users discuss visual appeal, widgets, customization and ads. These are individual reports, not independent RAM/power measurements. Keep AsterVale ad-free and don't copy listing performance claims. |
| [Dribbble control-center study](https://dribbble.com/shots/26175703-Apple-Liquid-Glass-iOS-26-Control-Center-UI-Kit), [second control-center concept](https://dribbble.com/shots/26161490-Control-Center-iOS-26-Apple-Liquid-Glass-UI), [Behance glass dashboard](https://www.behance.net/gallery/228076573/SmartHomeX-iOS-26-Glassmorphic-Dashboard-UI), [Mobbin iOS collection](https://mobbin.com/discover/apps/ios) | Discovery references only: Dribbble's text was accessible but browser image did not render; Behance returned 403/400; Mobbin exposed login/navigation rather than its screen library. No claim to have inspected gated flows or downloaded kits. Official public reference images above provide the visual evidence. |
| [Emil Kowalski: Good vs Great Animations](https://emilkowal.ski/ui/good-vs-great-animations) | Source-aware origins, deliberate curves, slower inspection and motion only where it helps. |
| [Lineage UI customization discussion, 2026](https://www.reddit.com/r/LineageOS/comments/1vh26sp/how_much_customisation_within_lineageos_ui/), [Quick Settings complaint](https://www.reddit.com/r/LineageOS/comments/vfv867/), [favorite features discussion](https://www.reddit.com/r/LineageOS/comments/d93zki/whats_your_favourite_lineageos_feature/) | Anecdotal and mixed-age evidence: desire for customization/low bloat, frustration with extra taps/large tiles and inconsistent toggles. Treat as hypotheses to test, not a representative survey or verification of commenters' platform claims. |

## Feel to borrow

1. **Wallpaper-backed depth:** the home/lock screen is a coherent scene; control surfaces float above it. Glass gets a visible edge and a restrained offset shadow, not just opacity.
2. **A disciplined hierarchy:** thin large lock clock; compact home widgets; regular app grid and four-place dock; grouped settings rows with readable secondary text. Stop repeating the same generic card on every screen.
3. **Controls with physical weight:** clearly selected connectivity buttons, comfortable sliders, local press response and a sheet that comes from its trigger. Preserve labels and state meaning.
4. **Quiet content, expressive controls:** settings/chat content stays near-solid. Translucency is limited to the dock, quick controls and floating chrome. Nothing refracts or animates continually.

## What we aim to do better than iOS

These are design goals, **not tested superiority claims**: preserve an app drawer, selectable icon shapes/layouts and per-app profiles; expose opaque/reduced-motion choices; retain Android Back and explicit control labels; preview assistant actions and their permissions; make Arabic/RTL and large text part of initial validation. A51-friendly opaque rendering is the default. No fake benchmarks or a permission-eating imitation lockscreen.

## Final design decisions

| System | Decision |
| --- | --- |
| Palette | Pearl canvas `#f2f3f5`, white content `#ffffff`, graphite ink `#1c2824`, secondary `#56635e`; original moss accent `#28604c`, on-accent white. Dark: `#111b18` / `#1e2b26`, ink `#f2f6f3`, accent `#bfdab5`. Wallpaper: original lagoon/moss/pearl/clay folds. |
| Material | Opaque content; bounded frosted appearance for floating controls. Optional 12px static backdrop blur in the browser, never animated. Manual opaque control plus automatic fallback for reduced-transparency, reduced-data, low-memory hints or sustained sampled frame delay. Browser sampling is not an A51 performance result. |
| Type | Existing OFL Manrope + Noto Sans Arabic. Body 15–17, labels ≥12, title 30–34, lock clock 82–96 at default scale. Size-specific tracking, tabular numerals for metrics; 200% text wraps/scrolls. No SF font. |
| Icons | Original 24px vectors, ~1.7px stroke for controls; app icons have distinct colored fields and a subtle top highlight, not SF Symbols or copied app logos. |
| Geometry | 4px spacing base; 8/12/16/24/32 steps; phone content inset 22–24. App icons 54px; touch targets ≥48. Rows 58–66. Content panels 20–24 radius; control modules 26; dock 30; concentric inner radii. The explicit iOS-inspired brief justifies these larger radii. |
| Motion | Press 110ms, control state 160ms, panel entrance 240ms, exit 180ms. `cubic-bezier(.23,1,.32,1)` for response and `cubic-bezier(.32,.72,0,1)` for drawer travel. Transform/opacity only; cancel prior WAAPI transitions. No motion for keyboard navigation; reduced motion uses a short fade. Gesture spring work is deferred rather than imitating a velocity-aware spring with fixed keyframes. |

## Screen-by-screen acceptance

| Screen | Reference feel / concrete redesign check |
| --- | --- |
| Lock | Large airy clock, quiet date, private notification stack, reachable bottom shortcuts; no duplicate giant CTA dominating the screen. |
| Home | Two glanceable original widgets, balanced colored app grid, grounded translucent dock, wallpaper breathing room. |
| Drawer | Clear search and regular icons, grouped favorites/all apps, no wall of identical flat tiles. |
| Notifications | Smaller header controls, a coherent stacked hierarchy, legible opaque message content and reachable clear action. |
| Controls | Connectivity group, media module, distinct brightness/volume controls and secondary actions; selected state works without color alone. |
| Settings | Large title + search, recognizable identity row, grouped colored category glyphs, aligned chevrons and row rhythm. |
| Game Mode | Restrained dark performance panel, per-app selector, honest unavailable metrics and prominent thermal protection. No pretend FPS. |
| Rill | Original companion identity, chat-like space and an action preview that explains permission/scope before application. |
| Setup | Spacious original brand entrance, short progressive choices, language/theme/privacy controls, reachable continuation. |

## Tooling and verification

Using existing Apple Design / Animate / Impeccable guidance and reviewed OpenAI Playwright tooling. Installed Anthropic `webapp-testing` after reading SKILL.md and `with_server.py`; only its `--help` ran, since our server already exists. The skill's black-box-first suggestion conflicts with the owner's read-before-run rule, so the owner's rule wins. It is available in the next turn.

Next: implement only after this report is committed; capture all nine actual browser screens in light, dark and RTL/large-text states; inspect their rendered composition against the checks above, fix failures and publish a linked gallery. Hardware smoothness and native parity remain untested.
