# Base selection — checked 2026-11-10

Primary-source review, not hardware certification.

| Base | Evidence | Decision |
| --- | --- | --- |
| Community LineageOS 23.2 | [Exynos9611Development](https://github.com/Exynos9611Development) reports A16 QPR2 stable; public device/common/kernel source | Selected: minimal feature surface and paired trees |
| crDroid 12 | [A51 page](https://crdroid.net/a51/12) lists Android 16, 12.11, 2026-08-22, and currently marks unsupported | Useful reference; do not build our identity on its customization stack |
| Matrixx | [A51 tree](https://github.com/Matrixx-Devices/device_samsung_a51); [main manifest](https://github.com/ProjectMatrixx/android) archived September 7, 2026 | Avoid archived base despite previous A51 support |
| Evolution X | [upstream](https://github.com/Evolution-X) lists Android 16 and 17 work | No confirmed matched A51 build baseline from sources inspected; more integration work |
| PixelExperience | [project](https://github.com/PixelExperience) | No maintained Android 16 A51 baseline verified; not selected |
| /e/OS unofficial | [device documentation](https://doc.e.foundation/devices) | No matched current Android 16 A51 source/build pair verified; not selected |
| GrassKernel | [older kernel repository](https://github.com/Exynos9611Development/android_kernel_samsung_universal9611-old) | Historical alternative; selected kernel comes from current community manifest |

Inspected [community manifest](https://github.com/Exynos9611Development/local_manifests/blob/lineage-23.2/common.xml) uses kernel `AOSP`, not `lineage-23.2`. Our generated source lock records exact commits and omits all proprietary vendor projects and unrelated devices. Full framework reproducibility still requires `repo manifest -r` after sync; a pinned root manifest alone does not freeze its branch-valued dependencies.

Upstream [A51 BoardConfig](https://github.com/Exynos9611Development/android_device_samsung_a51/blob/lineage-23.2/BoardConfig.mk) overrides common releasetools. Inspected device install-end writes dtbo; inspected common install-end also writes vbmeta. This requires boot-chain review: it is not safe to assume the hooks compose. No unconditional vbmeta patch is enabled here. Read exact target-files and compare the generated updater-script before first candidate flashing.

Android 17: a 4.14 version string alone does not prove compatibility or impossibility. Verify eBPF/backports, cgroup layout/freezer, VINTF, graphics/media HALs, SELinux and recovery first. Baseline Android 16 must boot before spending rental time on a forward port. Kernel version must be read from pinned Makefile/build output; never infer it from a branch name.

Keep base Trebuchet/Launcher3 for M1. [Lawnchair](https://github.com/LawnchairLauncher/lawnchair) is an optional later launcher; preserve its GPL license when forking. Theme/features live in `android/`, mounted at `vendor/astervale`, not in Samsung trees. Device capability adapters gate all hardware operations.
