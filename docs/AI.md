# Assistant boundary

Default disabled. Native source in this repository supports a local action preview and confirmation only. Remote inference, BYOK storage, notification access and on-device inference are **not implemented**. The prototype never collects API keys and makes no network calls.

Future cloud adapter: HTTPS endpoint selected by the user, AES-GCM secret encryption backed by AndroidKeyStore, no key in resources/logs/backup; per-request preview of exact outbound content and explicit consent, clear endpoint identity, cancellable bounded timeout, no background upload. Revoking consent clears session context and disables requests. Model output and notification text are untrusted data.

Action grammar is a closed enum of validated setting changes, explicit app launches and profile requests. The model cannot execute shell, write arbitrary Settings/sysfs paths, install packages, grant permissions or change protection policy. User reviews the exact proposed action before application. Native notification access would use a separately enabled NotificationListenerService, local redaction and explicit selection before summarization. Never expose notification contents on the lockscreen. Opt-in alone is not blanket permission to transmit all notifications.

No embedded model on the 4 GB edition. A later optional small model must pass measured peak RSS, LMK and sustained thermals on the owner's phone. Network permission is deliberately absent from the current native app until the consent transport is implemented.
