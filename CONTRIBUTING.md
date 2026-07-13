# Contributing to AEC-Fundamentals

Thanks for contributing. This repo is a bilingual AEC knowledge base; consistency and
render-correctness matter because the docs are read on GitHub and may feed downstream
tools. Please skim this before opening a PR.

## Repository layout

- Knowledge docs live under `AEC-Architecture/<Domain>/` — `Construction`, `MEP`,
  `Materials`, `Planning`, `Regulation`, `Structure`.
- Every topic is a **pair**: `NNN_Title.kor.md` (Korean) **and** `NNN_Title.eng.md`
  (English). Both are required; keep filenames identical except the language suffix.
- Images go in the topic's sibling `*_img/` or `assets/images/` folder.
- Governance/analysis lives under `docs/` (`docs/asset-audit/`, `docs/proposals/`).

## Markdown rules (these are CI-enforced — see below)

1. **Korean bold ending in `)` followed by a letter does NOT render.**
   `**용어(English)**한글` shows literal `**`. Move the paren outside the bold:
   `**용어**(English)한글`. (CommonMark flanking: a closing `**` after punctuation
   must be followed by whitespace or punctuation.)
2. **Leave a blank line after a standalone `<img …>`.** Without it, the `<img>` starts
   an HTML block that swallows the next paragraph, so its Markdown (e.g. `**bold**`)
   won't render.
3. **Leave a blank line before a `---` thematic break.** A paragraph immediately
   followed by `---` becomes a SETEXT `<h2>` and the rule disappears.
4. Use a space after `#` in headings; keep table columns consistent.
5. Text files use **LF** line endings (no CRLF).
6. Korean-language citations in a `# Reference` list stay in Korean — do not translate
   the titles of Korean-language sources.

## Run the checks locally

```bash
python scripts/check_docs.py
```

This is exactly what CI (`.github/workflows/docs-checks.yml`) runs on every push/PR:
bold-flanking render safety, `<img>` HTML-block traps, SETEXT headings, KO/EN pair
completeness, relative link/image resolution, and CRLF. It uses only the Python
standard library.

## Images

- Record every image in [`docs/asset-audit/image-manifest.csv`](docs/asset-audit/image-manifest.csv):
  `creator`, `source_url`, `license`, and (for AI images) `generated_with`.
- **Do not add third-party images without proof of redistribution rights.** Attribution
  alone is not permission. When in doubt, link out instead of embedding.
- Keep images near their display size (avoid multi-MB / multi-thousand-px files).

## Document status (front-matter scheme)

New or reviewed docs should carry a status. GitHub renders leading YAML front-matter
as a table:

```yaml
---
status: unreviewed        # unreviewed | domain-reviewed | source-verified | deprecated
locale: ko                # ko | en
jurisdiction: KR          # for legal/regulatory content
effective_date: 2026-06-22
reviewed_by: null
source_ids: []
---
```

Legal figures (codes, thresholds) must cite the clause/appendix and effective date, and
must not be used for compliance or model training until `status: source-verified`. Docs
that are still unverified carry an explicit banner at the top (see `MEP/103`,
`Structure/102`, `Construction/301`).

## Licensing (in flux)

The project is discussing a per-content-type license split — see
[`docs/proposals/LICENSING.md`](docs/proposals/LICENSING.md) and
[Issue #7](https://github.com/MosslandOpenDevs/AEC-Fundamentals/issues/7). Until that is
decided, existing content remains under the current repository license, and third-party
material keeps its original license.

## Pull requests

- Keep KO and EN in sync when you change one side.
- Make sure `python scripts/check_docs.py` passes.
- Reference the relevant issue; for proposals, comment on Issue #7.
