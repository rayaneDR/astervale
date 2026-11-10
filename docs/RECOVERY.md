# Recovery and first flashing gate

**There is no AsterVale flashable build yet. Do not flash a source ZIP.** The procedure below is a recovery outline; exact candidate instructions will be generated from its audited recovery and target-files metadata.

Before testing: back up photos, files, authenticator recovery codes, app data and a private device-specific EFS/radio backup using a trusted recovery method. Preserve backups off the phone and never upload EFS. Keep the complete stock **SM-A515F** firmware for the phone's region and current/equal-or-newer bootloader binary. Record USB drivers, cable and working Download Mode entry before changing partitions.

The A51 uses Samsung Download Mode, not a generic fastboot bootloader workflow. Do not use `fastboot flash` instructions intended for Pixels. Use a trusted source for Odin; Samsung does not offer a general official public Odin download here, so no random mirror binary is supplied. Heimdall source is [Benjamin-Dobell/Heimdall](https://github.com/Benjamin-Dobell/Heimdall); A51 compatibility is untested and must be established before it is a recovery dependency.

Return to stock with owner-operated Odin: enter Download Mode using the model's verified key/cable sequence; load matching BL, AP, CP and CSC files in their corresponding fields. Clean CSC typically wipes data; HOME_CSC is not a guaranteed rescue or backup. Keep Re-Partition off; never supply a random PIT or NAND erase. Verify the device model and rollback revision in Odin before Start. Let flashing complete, then follow stock recovery instructions if a reset is required. If Download Mode is unavailable, stop and seek model-specific service recovery.

Do not relock the bootloader with custom partitions. Knox state can remain changed after returning to stock. Neither stock restoration nor custom-ROM testing guarantees IMS/VoLTE, banking apps or DRM functionality.

Candidate first boot requires: correct model/firmware assertions, audited recovery/vbmeta/dtbo install chain, checksums and release signature, owner backup and known stock recovery route. Clean install, encryption/unlock after reboot, SIM/data/calls, Wi-Fi, Bluetooth, cameras, audio, sensors, UDFPS, NFC (if present), suspend/battery, SELinux enforcing and OTA must be reported individually. Missing results remain untested.
