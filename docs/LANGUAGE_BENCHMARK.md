# Text-route benchmark

Executed on Windows JVM, not A51. Synthetic human-authored fixtures, no recorded speech; curated keyword matcher, no LLM. Does not establish general language quality, speech WER, phone latency, RAM or battery.

| Language | Correct / cases | A51 speech / TTS / LLM |
| --- | --- | --- |
| en | 13 / 13 | untested |
| ar | 11 / 11 | untested |
| ary | 11 / 11 | untested |
| ary-Latn | 11 / 12 | untested |
| fr | 12 / 12 | untested |
| es | 11 / 11 | untested |
| pt | 11 / 11 | untested |
| ru | 11 / 11 | untested |
| tr | 7 / 11 | untested |
| hi | 11 / 11 | untested |
| zh | 11 / 11 | untested |

## Failures

| Language | Input | Expected | Actual |
| --- | --- | --- | --- |
| ary-Latn | bghit n9ess lbatri | BATTERY | UNKNOWN |
| tr | Ayarları açar mısın | SETTINGS | UNKNOWN |
| tr | Parlaklığı azalt | BRIGHTNESS | UNKNOWN |
| tr | Ses seviyesini yükselt | VOLUME | UNKNOWN |
| tr | Alarmı aç | ALARM | UNKNOWN |

Negation, quoted text, inflected words and code-switching require broader tests. Tool execution always needs confirmation, including matched routes.

Host batch elapsed (not device latency): 121 ms
