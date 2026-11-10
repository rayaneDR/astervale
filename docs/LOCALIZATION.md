# Translation and language quality

English is the default for Rill, tool IDs, source and fallback UI. Android panel resources currently include English and Arabic. The rule lexicon/explanations include 11 language/script variants; **full native UI and system localization is incomplete**. Do not label a language fully supported because a few fixtures pass.

Add UI strings to Android `res/values-LOCALE/strings.xml` (use BCP47 qualifiers such as `values-b+ary` and `values-b+ary+Latn` for Darija variants). Use `start`/`end`, locale-aware dates/numbers/plurals, resource arguments rather than string concatenation, 48 dp targets and scalable `sp`. Test actual Android at 1.0/1.3/2.0 font scale and RTL. Browser captures cannot prove native coverage.

Add command rules in `layer/src/main/assets/commands.tsv`: language, fixed action enum, conservative Java regex, localized explanation. Never add shell code or arbitrary setting paths. Add positive, negated, ambiguous, quoted and code-switched examples to `assistant/benchmark.tsv`; run the actual Java matcher. Shared terms use the user's selected language to avoid pretending the matcher can infer every locale from “wifi.”

Moroccan Darija must be reviewed by native speakers, with Arabic and Latin/Arabizi spelling variants, French/English code-switching and naturally spoken phrasing. Current translations are author-written drafts, not native-speaker certification. Record alternatives rather than forcing one spelling. Never substitute word-for-word Modern Standard Arabic as evidence of Darija support.

Separate route accuracy, language identification, ASR WER/CER, TTS intelligibility and A51 resource/latency results. Keep failed cases in the report. Current detailed host results are in LANGUAGE_BENCHMARK.md; all phone speech and LLM results are untested.
