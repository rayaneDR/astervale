# Skills, tools and provenance

Used existing Impeccable for design/context/visual checks, find-skills and skill-installer for discovery and reviewed installation, Sites guidance for local static preview (owner explicitly chose GitHub Pages hosting), and Composio/GitHub for authorized repository/Pages operations. No unrelated PDF/document/image-generation pipeline is needed for a source/app project; original logos/wallpapers are authored geometry.

Installed:
- OpenAI `playwright` skill, from openai/skills; SKILL.md, shell wrapper and CLI reference read before use. `@playwright/cli` installed project-locally with `--ignore-scripts`; browser QA used the existing Chrome installation. No unreviewed npm lifecycle installer ran. Exact dependency integrity is in package-lock.json.
- Official Android `litert-lm` skill, from android/skills, installed as `android-litert-lm` after reading its SKILL.md. It guides future optional CPU-model lifecycle and memory handling; it does not mean a model is implemented. Available in the next turn. No downloaded scripts from this skill were executed.
- Temurin OpenJDK 21.0.13+9, official Adoptium release archive, SHA256 `a4dbaa05fca4bd89d84584e58c459bd732efebb1722af80ab13c6516832004f9`, verified before extraction to ignored `tools/bin/`.

Reused existing Android SDK 36/Build Tools 36, ADB/fastboot, cached Gradle 8.14.3, Git, Node and Python. Downloaded official repo launcher for inspection only; did not execute it or sync AOSP. Checked Android official CLI/AI skills and Anthropic/OpenAI collections; did not run their install-one-liners. No third-party model, firmware or proprietary vendor repo was downloaded. No paid runner or cloud account was created. No network blocker requires changing account security settings.

Failures: absent kernel lineage-23.2 branch resolved through actual manifest; Heimdall latest-release endpoint 404; initial Playwright bundled-browser version absent, resolved with installed Chrome; JDK25/Gradle mismatch resolved by verified JDK21. Never install a random binary mirror to bypass these failures.
