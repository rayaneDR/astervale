# Private extraction contract

Only owner-provided stock SM-A515F firmware or the owner's existing legally obtained installation is a donor. Exact donor/current bootloader compatibility must be verified against the pinned `proprietary-files.txt`, `board-info.txt` and radio stack before extraction. Do not downgrade bootloader binary. Store firmware outside this repository.

On Linux, use the pinned device and common extraction scripts and matching Lineage `tools/extract-utils`; review all imported fixups before running. Record donor filenames + SHA256, firmware build, baseband, bootloader, extraction utility commit and resulting proprietary file hashes in a **private** extraction report. A public report can contain firmware identifiers and hashes, never binaries, keys, EFS or personal data.

Do not clone the public `android_vendor_samsung_*` repositories: public visibility is not a redistribution license. Our local manifest excludes them. Both device-specific and common blobs must exist privately before build. Framework APIs and HAL compatibility remain untested until build and owner tests.
