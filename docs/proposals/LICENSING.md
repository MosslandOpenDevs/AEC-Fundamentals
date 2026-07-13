# Licensing recommendation (DRAFT)

> **상태: DRAFT / 권고 — 법무·기여자 검토 전까지 채택되지 않음.**
> This is a recommendation only. Actual re-licensing must NOT proceed without verifying rights to the underlying material and obtaining contributor consent. No `LICENSE` file has been changed by this document.

## Why the current single license is a problem

The repository is currently licensed as a whole under **CC BY-NC-SA 4.0**. Two issues:

1. **It is not open source (OSI sense).** The `NC` (non-commercial) clause forbids commercial use, and the [Open Source Definition](https://opensource.org/osd) does not allow discrimination against fields of use, including commercial use. Presenting the repo as "open source" would be misleading.
2. **You can only license what you hold rights to.** The repo mixes (a) original prose, (b) future validator/CI code, (c) third-party images (ArchDaily / blogs / textbooks) whose rights the project does not own. A blanket repo license cannot cover material the project has no rights to relicense.

## Recommended split (pending review)

| Material | Recommended license | Note |
| :--- | :--- | :--- |
| Validator / CI / tooling code | **Apache-2.0** or **MIT** | OSI-approved; enables reuse incl. commercial |
| Original explanatory docs | **CC BY 4.0** | attribution, no NC restriction |
| Crosswalk / factual data | **CC0** or **ODC-BY** | facts aren't copyrightable; ease reuse |
| Third-party images / standard excerpts | **keep original license + attribution per file** | never re-license others' work |

Mechanism: a top-level `LICENSE` for code + a `LICENSES/` note explaining the per-content-type split, and per-file/near-file attribution for third-party assets (see `../asset-audit/image-manifest.csv`).

## Blocking prerequisites (external review)

- [ ] Inventory contributors and obtain consent to re-license existing contributions.
- [ ] Verify, per image, whether it may be redistributed at all (many may need removal/replacement).
- [ ] Legal confirmation that the chosen split matches the project's goals (esp. if `open-sdb`/`open-sde` will consume this data).

*Source: structured from the external review provided 2026-07-13. Decision belongs to Mossland.*
