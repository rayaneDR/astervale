#!/system/bin/sh
# SPDX-License-Identifier: Apache-2.0
# Run manually under adb shell. Read only; no root or permission changes.
echo 'AsterVale capability discovery: no tuning is applied'
for policy in /sys/devices/system/cpu/cpufreq/policy*; do
  [ -d "$policy" ] || continue
  for field in scaling_governor scaling_available_governors scaling_available_frequencies scaling_min_freq scaling_max_freq; do
    [ -r "$policy/$field" ] && { printf '%s: ' "$policy/$field"; cat "$policy/$field"; }
  done
done
for device in /sys/class/devfreq/*; do
  [ -d "$device" ] || continue
  for field in name governor available_governors available_frequencies min_freq max_freq; do
    [ -r "$device/$field" ] && { printf '%s: ' "$device/$field"; cat "$device/$field"; }
  done
done
for zone in /sys/class/thermal/thermal_zone*; do
  [ -r "$zone/type" ] && { printf '%s ' "$zone"; cat "$zone/type"; }
done
cat /proc/swaps
grep -E 'MemTotal|MemAvailable|SwapTotal|SwapFree' /proc/meminfo
