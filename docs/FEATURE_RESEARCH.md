# Feature and interaction decisions

This is a feasibility-ranked design review of public project features, not a fabricated survey or popularity poll. No user-review quotations or universal “most loved” scores are invented.

Sources: [LineageOS](https://lineageos.org/), [crDroid](https://crdroid.net/), [Evolution X](https://github.com/Evolution-X), [archived Matrixx](https://github.com/ProjectMatrixx), [GrapheneOS features](https://grapheneos.org/features), [Samsung One UI principles](https://developer.samsung.com/one-ui/index.html), [Material 3 Expressive](https://m3.material.io/), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [HyperOS](https://www.mi.com/global/hyperos), [Lawnchair](https://github.com/LawnchairLauncher/lawnchair), [Magisk](https://github.com/topjohnwu/Magisk), [KernelSU](https://github.com/tiann/KernelSU).

| Rank | Feature | Why it fits / source influence | Current state |
| --- | --- | --- | --- |
| 1 | Readable home and searchable drawer | Launcher3/Lawnchair familiarity; reachable One UI controls; original mineral visual identity | Browser built, minimal native home source |
| 2 | Explicit, reversible assistant actions | Graphene-style least privilege and visible permission choices | Native rule-route confirmation source |
| 3 | Fast theme/size/RTL choices | Android theming and accessibility; more user choice than a fixed visual preset | Browser built; system/native theme scope incomplete |
| 4 | Per-app profiles with thermal protection | crDroid/Evolution-style customization without uncontrolled tuning | Preference UI only; no speed claims |
| 5 | Optional companion, stopped with one action | A personal character without continuous AI/microphone or 60 Hz idle animation | Native overlay source; runtime untested |
| 6 | Offline command fallback in every target language | Small models need deterministic safe routing and abstention | Corpus + rule tests; no full-language quality claim |
| 7 | Debloat without data deletion | Root modules can change packages but recovery matters more than a large blacklist | Two optional packages, reversible commands |
| 8 | Per-app notification privacy and grouping | Base Android controls already cover much of this; preserve proven behavior | Native SystemUI unchanged; browser concept |
| 9 | Icon packs, grid/widget customization | Lawnchair/Launcher3 ecosystem; meaningful ownership | Browser shapes; complete native support pending |
| 10 | OTA with explicit provenance | ROM/module ecosystems need correct artifact types and rollback | Layer release workflow; full-ROM OTA deferred |

Ideas intentionally deferred: Play Integrity spoofing, fake unlimited backups, aggressive background killing, overclocking/thermal bypass, all-screen blur and always-loaded LLMs. None improves our stable/low-RAM baseline without tradeoffs and proof.

## What we aim to improve

Use iOS-like spacious grouping and continuity, Android's explicit Back/permission model, One UI's reachable interaction area and Material's scalable semantic roles. Add configurable typography, icon shapes, locally inspectable assistant actions and a privacy-preserving fallback when intelligence is unavailable. These are product goals, not a claim of measured superiority over iOS. HyperOS control-center density informs what to avoid on a narrow small-text layout. The original identity uses moss/clay arcs and line icons rather than cloning branded surfaces.

No blur by default. On this layer, adaptive blur cannot be certified or globally controlled; native views remain opaque. Future measured adaptive path must track sustained frame misses and thermal pressure, fall back once with hysteresis, and offer a manual opaque setting. 60 Hz means 16.7 ms per frame; p95/p99, jank and sustained power must be measured on the owner’s A51 before any “60 fps” claim.
