# Contributing

Keep one feature per commit; preserve base-boot changes separately from visual/product changes. Every Android change must state its build evidence and `untested` or `tested by owner` status. Use `python -m unittest discover -s tests -v` and `node --check site/app.js` / `node --check site/preview.js` for source checks. Browser evidence is not native proof.

Never commit proprietary blobs, EFS, firmware archives, signing/API keys or personal logs. New dependencies must have source/revision/license recorded and scripts reviewed before execution. Preserve upstream notices; kernel changes remain GPLv2 and released kernels require corresponding complete source/config/toolchain information. Submit owner reports using `docs/OWNER_TEST_TEMPLATE.md`.
