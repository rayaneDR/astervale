#!/system/bin/sh
# SPDX-License-Identifier: Apache-2.0
module_path=${0%/*}
state_path="$module_path/disabled-by-astervale.txt"
[ -f "$state_path" ] || exit 0
while IFS= read -r package; do
  case "$package" in com.android.printspooler|org.lineageos.recorder) pm enable --user 0 "$package" ;; esac
done < "$state_path"
