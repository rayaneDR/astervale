# SPDX-License-Identifier: Apache-2.0
ASTERVALE_EDITION ?= lite
ifneq ($(filter $(ASTERVALE_EDITION),lite gaming full),$(ASTERVALE_EDITION))
$(error ASTERVALE_EDITION must be lite, gaming or full)
endif
PRODUCT_SOONG_NAMESPACES += vendor/astervale
PRODUCT_PACKAGES += AsterValePanel AsterValeTheme
PRODUCT_SYSTEM_EXT_PROPERTIES += ro.astervale.version=0.1.0-source ro.astervale.edition=$(ASTERVALE_EDITION)
# Edition selection is scaffold only: no GApps, root daemon or unverified sysfs writes.
PRODUCT_COPY_FILES += vendor/astervale/permissions/privapp-permissions-astervale.xml:$(TARGET_COPY_OUT_SYSTEM_EXT)/etc/permissions/privapp-permissions-astervale.xml
