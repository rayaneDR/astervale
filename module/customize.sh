#!/system/bin/sh
# SPDX-License-Identifier: Apache-2.0
ui_print 'AsterVale preview module — hardware untested'
model=$(getprop ro.product.model)
sdk=$(getprop ro.build.version.sdk)
[ "$model" = 'SM-A515F' ] || abort 'Initial support is SM-A515F only.'
[ "$sdk" = '36' ] || abort 'Initial layer target is Android 16 / API 36 only.'
ui_print 'No partition flashing, boot image replacement, thermal or clock changes.'
ui_print 'Install APK separately. All debloat operations are manual and reversible.'
set_perm_recursive "$MODPATH" 0 0 0755 0644
set_perm "$MODPATH/manage.sh" 0 0 0755
set_perm "$MODPATH/uninstall.sh" 0 0 0755
