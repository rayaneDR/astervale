# Linux build plan

## Capacity and cost

[AOSP](https://source.android.com/docs/setup/start/requirements) documents 64 GB RAM and 400 GB free disk. Use Linux x86-64, Ubuntu 22.04/24.04 compatible with pinned Lineage dependencies, 16+ vCPU, **64 GB RAM and 700 GB free SSD** including logs/caches/target-files. GPU unnecessary. Budget first sync/build **8–24 hours**, incremental **1–4 hours** as planning estimates, not measured results; failed iterations add cost.

Standard public [GitHub runners](https://docs.github.com/en/actions/reference/runners/github-hosted-runners) list 16 GB RAM / 14 GB SSD. They run web/source checks here; they cannot be claimed as a full ROM host. Do not use swap and disk-cleaner tricks as evidence of fit.

Compared [Hetzner cloud](https://www.hetzner.com/cloud/) and [dedicated EX](https://www.hetzner.com/dedicated-rootserver/matrix-ex/): live pages did not expose a stable complete numeric checkout quote in our captured text. No invented low price or claim of global cheapest. For repeated builds, request a 64 GB / 2× NVMe dedicated quote, include setup fees and minimum billing; compare actual availability.

Lowest verified hourly candidate in this comparison is **Scaleway GP1-M**, 16 vCPU / 64 GB, listed **€0.38352/hour** on the [official pricing page](https://www.scaleway.com/fr/tarifs/virtual-instances/). Capacity in [official specifications](https://www.scaleway.com/en/docs/instances/reference-content/choosing-instance-type/) is x64. Storage must be quoted separately; do not assume legacy included storage. The [June 2026 rate change](https://www.scaleway.com/en/blog/a-transparent-update-on-scaleway-pricing/) lists low-latency block storage at €0.00013/GB/hour. At 700 GB this adds €0.091/hour: illustrative total **€0.47452/hour**, **€3.80–€11.39 for 8–24 hours**, before VAT, IP, egress, retained storage and failed builds. Verify checkout availability and storage billing tier before renting. This is a costed candidate, not proof of cheapest worldwide.

No account, payment or remote host has been created. Keep cloud spending inside a funded account selected by the owner. Stop/delete rented compute after copying artifacts; stopped disks/IPs may still incur charges.

## Bring-up sequence

1. On the provisioned host install official Ubuntu build prerequisites following the pinned Lineage branch documentation. `tools/build.sh` checks capacity/tools; it does not execute downloaded install scripts.
2. Download official [repo launcher](https://gerrit.googlesource.com/git-repo/+/refs/heads/main/README.md), inspect/signature-check using repo documentation before executing. A copy is downloaded locally under ignored research for review, not run.
3. `repo init -u https://github.com/LineageOS/android -b lineage-23.2 --git-lfs` in an empty build directory. Copy `manifests/a51.xml` into `.repo/local_manifests/`. Sync with `repo sync -c -j8 --no-clone-bundle --no-tags`.
4. Save `repo manifest -r -o source.lock.xml`. Keep it with artifacts. Avoid `breakfast` roomservice auto-downloads: use explicit `lunch` after all required sources are present.
5. Copy this repo's `android/` into `vendor/astervale`. It is deliberately outside device source. Use an owner-controlled local checkout or explicit source copy, never a vendor blob repo.
6. Inspect `device/samsung/{a51,universal9611-common}/extract-files.py`, helper imports and fixup scripts in full. Use those pinned scripts with the private firmware dump. They generate private vendor makefiles/binaries. Do not run the downloaded extraction snapshot here. Follow `docs/BLOBS.md`.
7. Read `board-info.txt`, phone bootloader/baseband and donor requirements. Review dtbo/vbmeta behavior and recovery partition limits. Build **unchanged** `lineage_a51` M1 first using `tools/build.sh baseline /absolute/build/tree`.
8. After baseline owner proof, use `tools/build.sh features /absolute/build/tree` for the separate AsterVale product. Lunch release configuration defaults to `bp4a`; verify against the synced branch before use. Failed lunch/build is a blocker, never a flashable milestone.
9. Use release signing keys kept off Git and audit generated updater-script/SELinux/VINTF/size. CI release workflow intentionally cannot manufacture a zip from source files. See release notes templates and `tools/release_gate.py`.

Editions: Lite includes base + control panel; Gaming adds profile UX when integrated; Full adds optional agent panel. Currently these are package-selection source scaffolds, not built variants. Vanilla first. GApps is deferred pending redistributability, partition fit, SetupWizard integration and licensing review; no Google apps are bundled.
