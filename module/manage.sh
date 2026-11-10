#!/system/bin/sh
# SPDX-License-Identifier: Apache-2.0
set -eu
[ "$(id -u)" = 0 ] || { echo 'Root required for optional debloat. APK does not need root.'; exit 1; }
[ "$(getprop ro.product.model)" = 'SM-A515F' ] || exit 1
module_path=${0%/*}
state_path="$module_path/disabled-by-astervale.txt"
operation=${1:-help}
choice=${2:-}
case "$choice" in
  printing) package='com.android.printspooler' ;;
  recorder) package='org.lineageos.recorder' ;;
  '') package='' ;;
  *) echo 'Unsupported choice. Only printing and recorder are allowlisted.'; exit 2 ;;
esac
case "$operation" in
  inventory)
    echo 'Read-only CPU/GPU capability inventory. No hardware tuning enabled.'
    sh "$module_path/capabilities.sh"
    ;;
  disable)
    [ -n "$package" ] || exit 2
    if pm list packages -d --user 0 | grep -Fxq "package:$package"; then echo 'Already disabled; not claiming ownership.'; exit 0; fi
    pm list packages --user 0 | grep -Fxq "package:$package" || { echo 'Not installed.'; exit 2; }
    # Journal before mutation so interrupted commands remain recoverable.
    touch "$state_path"
    grep -Fxq "$package" "$state_path" || printf '%s\n' "$package" >> "$state_path"
    pm disable-user --user 0 "$package"
    echo "Disabled $package for user 0; data retained. Restore using: sh $module_path/manage.sh restore $choice"
    ;;
  restore)
    [ -n "$package" ] || exit 2
    [ -f "$state_path" ] && grep -Fxq "$package" "$state_path" || { echo 'No AsterVale-owned disable recorded.'; exit 2; }
    pm enable --user 0 "$package"
    grep -Fxv "$package" "$state_path" > "$state_path.tmp" || true
    mv "$state_path.tmp" "$state_path"
    ;;
  help)
    echo 'inventory | disable printing|recorder | restore printing|recorder'
    echo 'No clocks, thermal thresholds, ZRAM, process limits or RAM cleaners are changed.'
    ;;
  *) echo 'Unknown operation'; exit 2 ;;
esac
