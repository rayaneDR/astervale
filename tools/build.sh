#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
set -euo pipefail
mode=${1:?Usage: build.sh baseline|features /absolute/aosp/tree}
tree=${2:?Absolute AOSP checkout required}
[[ "$mode" == baseline || "$mode" == features ]] || { echo 'Unknown mode'; exit 2; }
[[ "$tree" == /* && -f "$tree/build/envsetup.sh" ]] || { echo 'Use an existing absolute Linux source checkout'; exit 2; }
[[ $(uname -s) == Linux && $(uname -m) == x86_64 ]] || { echo 'Linux x86-64 is required'; exit 2; }
mem_kb=$(awk '/MemTotal/ {print $2}' /proc/meminfo)
((mem_kb >= 60000000)) || { echo 'At least 64 GB nominal RAM required; do not build on the Windows 8 GB host'; exit 2; }
free_kb=$(df -Pk "$tree" | awk 'END {print $4}')
((free_kb >= 419430400)) || { echo 'At least 400 GiB free required, 700 GB recommended'; exit 2; }
for tool in repo git python3 java; do command -v "$tool" >/dev/null || { echo "Missing $tool"; exit 2; }; done
cd "$tree"
for path in vendor/samsung/a51/a51-vendor.mk vendor/samsung/universal9611-common/universal9611-common-vendor.mk; do
  [[ -s "$path" ]] || { echo "Private extraction required: $path"; exit 2; }
done
mkdir -p out/astervale-evidence
repo manifest -r -o out/astervale-evidence/source.lock.xml
git -C device/samsung/a51 rev-parse HEAD > out/astervale-evidence/device.sha
git -C kernel/samsung/universal9611 rev-parse HEAD > out/astervale-evidence/kernel.sha
release=${AV_RELEASE_CONFIG:-bp4a}
[[ "$release" =~ ^[a-z0-9]+$ ]] || { echo 'Invalid release configuration'; exit 2; }
# Explicit lunch avoids roomservice fetching public proprietary vendor repositories.
set +u
source build/envsetup.sh
if [[ "$mode" == baseline ]]; then
  lunch "lineage_a51-${release}-userdebug"
else
  [[ -f vendor/astervale/products/astervale_a51.mk ]] || { echo 'Copy android/ to vendor/astervale first'; exit 2; }
  export ASTERVALE_EDITION=${ASTERVALE_EDITION:-lite}
  [[ "$ASTERVALE_EDITION" =~ ^(lite|gaming|full)$ ]] || exit 2
  lunch "astervale_a51-${release}-userdebug"
fi
set -u
build_start=$(date +%s)
m -j"${AV_JOBS:-8}" bacon 2>&1 | tee out/astervale-evidence/build.log
printf '%s\n' "$(( $(date +%s) - build_start ))" > out/astervale-evidence/build-seconds.txt
echo 'Compilation ended. Audit target-files, boot-chain, signing and model assertions before candidate release.'
echo 'No hardware test has been performed by this script.'
