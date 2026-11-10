# AsterVale design system

Direction chosen under the owner's explicit autonomous-design instruction: mineral warmth and quiet, generous composition. The interface should feel personal without spending the A51's frame budget on effects.

## Roles
| Role | Light | Dark |
| --- | --- | --- |
| Canvas | #f5f1e9 | #151d1b |
| Surface | #fffdf8 | #202c28 |
| Text | #20382f | #edf3e9 |
| Secondary | #53665b | #b5c6b9 |
| Accent | #315b45 | #b5d3a3 |
| On accent | #ffffff | #152b20 |
| Outline | #c5cbbf | #65776a |
| Error | #a52328 | #ffb4ab |

Manrope variable (SIL OFL) is the Latin face; Noto Sans Arabic (SIL OFL) supplies Arabic. Self-hosted fonts with included licenses; Android system body text remains Roboto until the font-overlay path is compiled and reviewed. Headline 36/42 sp, title 24/30, body 16/24, label 14/20. Large clock 78/80. Weight 400–700. Never compress text to fit; allow wrapping and scrolling at 200%.

4 dp base spacing; 8, 12, 16, 24, 32, 48 dp steps. Insets 24 dp; rows at least 56 dp; interactive targets at least 48 dp. Panels 16 dp radius; small icons 12 dp; phone corners are hardware framing only. Custom icons use a consistent 1.7 px line and 24 px grid, with labels. Accent is used for state, not decoration.

Wallpaper: original intersecting mineral arcs, authored geometry, no copied images. Distinct moss, clay, sand and pale lime tones. Geometry is static; no live shaders. The translucent shade gets an opaque tonal fallback by default; blur is opt-in only after measured device evidence. AOD defaults off for power and burn-in evaluation.

Motion: 160 ms state changes and 240 ms panel entrance, cubic-bezier(.16,1,.3,1). Animate opacity/transform only. Interruptible; no elastic overshoot. System remove-animations and browser prefers-reduced-motion collapse transitions. Target 60 Hz / 16.7 ms frame budget, measured using Perfetto and FrameTimeline; no device measurements yet. Effects are removed if repeated matched traces regress p95/p99 or thermal stability.

## Surface brief
Prototype operates as a screen workbench: screen index, central phone, inspector and explicit implementation status. The landing page introduces the actual source project and links to the preview, build instructions and release state. Nine screens: lock, home, drawer, notifications, controls, settings, gaming, assistant, setup. No network in the prototype, no API-key collection, no simulated measurement presented as real.

Android port keeps predictive Back, insets, notification privacy and normal permission flows. Use Launcher3/Trebuchet already in Lineage for initial bring-up; evaluate Lawnchair later rather than replacing a working launcher before baseline proof. SystemUI/Settings patches follow base-boot testing, not a claim that CSS equals a native port.
