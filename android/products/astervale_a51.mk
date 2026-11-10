# SPDX-License-Identifier: Apache-2.0
# Keep device and feature layers separate. No hardware tuning in product props.
$(call inherit-product, device/samsung/a51/lineage_a51.mk)
$(call inherit-product, vendor/astervale/config/common.mk)
PRODUCT_NAME := astervale_a51
PRODUCT_MODEL := SM-A515F
