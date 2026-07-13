# Licensing scaffold (DRAFT — not adopted)

> A ready-to-activate [REUSE](https://reuse.software/spec-3.3/)-compliant scaffold for the
> per-content-type license split proposed in [`../LICENSING.md`](../LICENSING.md) and
> [Issue #7](https://github.com/MosslandOpenDevs/AEC-Fundamentals/issues/7).
> **Nothing here changes the repository's effective license.** It is deliberately placed
> under `docs/proposals/` (not the repo root), so no REUSE tool treats it as active config.

## Contents

| File | What it is |
| :--- | :--- |
| `REUSE.example.toml` | proposed path → SPDX license/copyright mapping |
| `LICENSES/*.txt` | **verbatim canonical** license texts (fetched with `reuse download`): `Apache-2.0`, `CC-BY-4.0`, `CC0-1.0`, and the current `CC-BY-NC-SA-4.0` |

## Proposed split (mirrors `../LICENSING.md`)

| Material | License |
| :--- | :--- |
| Knowledge docs (`AEC-Architecture/**`) | **keep `CC-BY-NC-SA-4.0`** until formally re-licensed |
| Explanatory / governance docs (`docs/**`, `README.md`, `CONTRIBUTING.md`) | `CC-BY-4.0` |
| Validator / CI / tooling code (`validator/**`, `scripts/**`, `profiles/**/*.py`) | `Apache-2.0` |
| Self-authored synthetic fixtures (`cases/**`, `profiles/**/*.ids`, `*.yaml`) | `CC0-1.0` |
| Third-party / partner images | **per-file; not blanket-licensed** — see [`../../asset-audit/CLEARANCE.md`](../../asset-audit/CLEARANCE.md) |

## SPDX header convention (for new source files)

Once code is confirmed `Apache-2.0`, add a header to each source file so REUSE does not
depend solely on path globs:

```python
# SPDX-FileCopyrightText: 2026 Mossland
# SPDX-License-Identifier: Apache-2.0
```

## How to activate (after the decision + consent)

1. Confirm the Issue #7 licensing decision **and** identify/obtain consent from the actual
   rights-holders (employment/contract may vest rights in the company — see `../LICENSING.md`).
2. Clear every third-party/partner image per-file in
   [`../../asset-audit/image-manifest.csv`](../../asset-audit/image-manifest.csv); confirm the
   **AETHRION** arrangement for `Regulation/assets/images/*`.
3. Move `REUSE.example.toml` → repo-root `REUSE.toml` and `LICENSES/` → repo-root `LICENSES/`.
4. Add annotations (or remove/replace) for the images, add SPDX headers to source files.
5. `pip install reuse && reuse lint` until it reports the project is compliant.

> ⚠️ `reuse lint` will **not** pass until every file (including images) is covered — that is
> intentional: it forces the image-rights clearance to be finished first.
