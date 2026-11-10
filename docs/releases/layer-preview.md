# AsterVale layer 0.1.0 preview

**Experimental APK and optional root-manager module. Not a ROM or recovery ZIP. All Android behavior is untested on SM-A515F hardware.**

Built source includes original home/app drawer preview, Rill multilingual local command routing with explicit action confirmation, on-device-only Android speech integration, offline-voice TTS selection, and optional draggable Seed/Pebble/Kite companion with stop controls. Companion-specific power, thermals, accessibility and gestures require owner tests. The long-press listening/thinking/speaking menu entries are visual demonstrations, not a live model.

99 curated text rules across 11 language/script variants, with a runnable 125-case host benchmark. This is not an LLM or speech-quality benchmark. Known misses are published in the benchmark table. Complete global UI localization, general question answering, built-in speech packs, notification summaries, automatic game/video hiding, cloud BYOK, icon-pack/widget support and privileged tuning are incomplete.

The optional module only supports SM-A515F / API 36 and changes no settings automatically. It offers read-only hardware inventory and explicit reversible disabling of printing or the Lineage recorder. Do not install it in recovery/Odin; use a compatible root manager. CPU/GPU/thermal/ZRAM/background-process tuning remains disabled.

The APK is signed with an Android debug/test certificate and uses a preview application ID. It is not production-signed; CI's ephemeral debug keys may require uninstall/reinstall between artifacts. Back up any preview data first. No API keys, signing keys, Google apps or Samsung blobs are bundled.

See INSTALL.md, PLAN_B.md, LANGUAGE_BENCHMARK.md and OWNER_TEST_TEMPLATE.md. No AsterVale baseline boot, performance gain, 60-fps result, battery improvement or OTA success is claimed.
