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
| Own crosswalk / self-authored data | **CC0** or **ODC-BY** *(after legal review)* | individual facts are generally not copyrightable, **but** their selection/arrangement can be (and some jurisdictions grant a *sui generis* **database right**); ODC-BY covers the DB layer, **not** the rights to individual records inside it |
| Existing docs | **keep current CC BY-NC-SA until re-licensed** | re-license only after rights-holders are identified (see below) |
| Third-party images / standard excerpts | **include only with proof of redistribution rights; otherwise remove or link-only** | attribution alone does **not** grant redistribution; keep the original license per file |

**Standards principle:** do **not** copy ISO/standard text, tables, or definitions into the corpus/RAG. Keep only the **standard number + clause reference** plus **independently authored** requirements.

Mechanism (REUSE-compliant): a top-level `LICENSE` for code, a `LICENSES/` folder, **SPDX headers** in source files, and a **`REUSE.toml`** for assets that can't carry a header (note: `.reuse/dep5` is deprecated as of [REUSE 3.3](https://reuse.software/spec-3.3/)). Per-image rights live in `../asset-audit/image-manifest.csv`.

A ready-to-activate **scaffold** (verbatim license texts + a proposed `REUSE.toml`) is in [`./licensing-scaffold/`](./licensing-scaffold/) — it is inert until the decision is made and rights are cleared.

## Blocking prerequisites (external review)

- [ ] **Identify the actual copyright holders** (not merely "all contributors") — under employment/contractor agreements the company may hold the rights — then obtain consent to re-license.
- [ ] Verify, per image, whether it may be redistributed at all (many may need removal/replacement/link-only).
- [ ] Legal confirmation of the split incl. database-right exposure, esp. if `open-sdb`/`open-sde` will consume this data.

*Source: structured from the external review provided 2026-07-13. Decision belongs to Mossland.*
