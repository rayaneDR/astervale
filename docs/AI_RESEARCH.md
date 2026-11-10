# Rill: local AI component decision

Rill is a working English name and an original Seed/Pebble/Kite character family. Default UI/tool IDs are English. The current artifact is a **local command router**, not a general-purpose LLM. All A51 speech quality/speed/peak RAM/battery measurements are **untested**.

| Component | Source / license | Size / resource evidence | Decision |
| --- | --- | --- | --- |
| Android on-device recognition | [SpeechRecognizer API](https://developer.android.com/reference/android/speech/SpeechRecognizer) | API 31+ availability and language packs depend on the installed service | Implement explicit on-device-only, no online fallback; may be unavailable on vanilla Lineage |
| Vosk small per-language models | [official model list](https://alphacephei.com/vosk/models) | Typically ~50 MB disk and ~300 MB runtime per upstream; model licenses vary | Good optional command-STT adapter; not bundled or benchmarked; no verified Darija small pack |
| whisper.cpp multilingual tiny/base | [upstream](https://github.com/ggml-org/whisper.cpp) MIT | Current upstream table: tiny 75 MiB / ~273 MB, base 142 MiB / ~388 MB, small 466 MiB / ~852 MB | Tiny/base candidate CPU adapter, push-to-talk only, unload after idle; table is upstream, not A51 measurement |
| Moroccan Whisper small | [TaloCreations model card](https://huggingface.co/TaloCreations/whisper-darija-finetuned) declares Apache-2.0 | Small-class model; conversion/runtime and derived license chain require review | Candidate Darija comparison, not a quality guarantee |
| MaghrebVoice | [author model card](https://huggingface.co/Ayoub-Laachir/MaghrebVoice) declares Apache-2.0 | Large-v3 class, unsuitable to assume lightweight | Reject as default for 4 GB A51 |
| Darija flight-domain fine-tune | [author model card](https://huggingface.co/ayoubelfallah1/whisper-darija-v4) | Domain-specific reported WER, no phone-command benchmark | Do not transfer its score to general Darija commands |
| Atlas-Chat-2B | [original model](https://huggingface.co/MBZUAI-Paris/Atlas-Chat-2B), Gemma terms | 2B weights, KV cache and runtime memory beyond file size; third-party quantizations not automatically trusted | Experimental 6 GB option only after conversion/license audit; no default on 4 GB |
| Qwen3-0.6B | [original model](https://huggingface.co/Qwen/Qwen3-0.6B), Apache-2.0 | Official full weights ~1.5 GB; quantized size/runtime depend on format/context | Optional CPU candidate; Darija quality unverified; not loaded in current build |
| LiteRT-LM | [Google runtime](https://github.com/google-ai-edge/LiteRT-LM) | Reviewed official Android skill: model outside APK, background init, single owner, close once | Useful future engine; no GPU/NPU assumption for Mali-G72 |
| llama.cpp | [upstream](https://github.com/ggml-org/llama.cpp), MIT | Android CPU path; tokens/s highly hardware/model dependent | Alternate optional runtime; no bundled model |
| Android TTS | [API](https://developer.android.com/reference/android/speech/tts/TextToSpeech) | Installed voices expose network requirement and locale | Select only offline voices; text fallback if exact language unavailable |
| Piper | [current project](https://github.com/OHF-Voice/piper1-gpl) | Runtime GPL licensing and each voice's license must be reviewed | Not bundled; no unverified Darija voice claim |

MLC/MediaPipe GPU deployment adds toolchain/device coverage cost without proven A51 benefit; evaluate only after a small CPU baseline. Do not infer Mali support from another SoC benchmark. Original models are not downloaded in this session, avoiding several GB of unneeded files and accidental license acceptance.

## Language protocol

`commands.tsv` holds 99 locale/action rules with localized explanations for English, Arabic, natural-draft Moroccan Darija Arabic script and Arabizi, French, Spanish, Portuguese, Russian, Turkish, Hindi and Chinese. Rule/phrase matching is limited language routing; it is not universal detection. Selected language resolves shared words; Arabizi markers can take precedence. Mixed or negated requests are rejected or require clarification. Some code-switching works, some fails; see exact corpus results.

`assistant/benchmark.tsv` contains development text fixtures, including negative and compound examples. `docs/LANGUAGE_BENCHMARK.md` executes the actual Java matcher. It is a host-side text benchmark only. Native-speaker review, unseen-user commands and real recorded speech per locale remain required. Success on this small authored corpus does not make a language fully supported.

Hardware benchmark plan: at least 50 unseen typed and 50 spoken commands per locale, at least 3 speakers and quiet/noisy variants, separate code-switched and Arabizi sets. Report intent precision/recall, abstention, unsafe-action false positives, language routing, speech WER/CER (Darija orthographic alternatives documented), TTS intelligibility ratings, p50/p95 end-to-end time, peak PSS and 20-minute battery/thermal test. All model providers are untrusted action proposers and cannot execute arbitrary code.

No wake word or continuous microphone. No model loaded at idle. Session chat clears on process death; external engines have separate privacy behavior. Future model manager must verify hash/format/license and show disk/RAM estimate, cancellation and unload controls. Cloud BYOK remains absent/off until an explicit consent and encrypted-secret transport is implemented.
