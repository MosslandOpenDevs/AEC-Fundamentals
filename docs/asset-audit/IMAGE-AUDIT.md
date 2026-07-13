# 🖼️ Image Asset Audit

> Auto-generated inventory of raster/vector assets under `AEC-Architecture/`. Use together with `image-manifest.csv`. **Rights columns (creator / source_url / license) are NOT auto-detectable and require human verification.**

## Summary

| Metric | Value |
| :--- | ---: |
| Total images | 171 |
| Total size | **458 MB** (~99.9% of the repo working tree) |
| > 1 MB | 95 |
| > 5 MB | 37 |
| ≥ 4000 px wide | 6 |
| AI-generated (by filename) | 12 (27 MB) |
| Orphan (unreferenced) | 4 |

## By domain

| Domain | Images | Size (MB) |
| :--- | ---: | ---: |
| MEP | 29 | 156.1 |
| Planning | 51 | 93.4 |
| Construction | 54 | 90.3 |
| Materials | 9 | 69.9 |
| Regulation | 15 | 33.2 |
| Structure | 13 | 15.0 |

## ⚠️ Top 20 oversized (compression candidates)

Displayed at ≤100% width but stored at full resolution. Recompress to display size; keep originals as Release assets/LFS if needed.

| Size | Pixels | Displayed | File |
| ---: | :---: | :---: | :--- |
| 42.9 MB | 7950×11746 | 60% | `AEC-Architecture/Planning/201-203_img/core_image.jpg` |
| 9.5 MB | 2656×1600 | 66% | `AEC-Architecture/MEP/101-102_img/101-4.png` |
| 8.9 MB | 2816×1536 | 70% | `AEC-Architecture/Materials/assets/images/insulation_eps.png` |
| 8.9 MB | 2656×1600 | 66% | `AEC-Architecture/MEP/101-102_img/102-1-eng.png` |
| 8.7 MB | 2816×1536 | ? | `AEC-Architecture/MEP/201_img/globe.png` |
| 8.7 MB | 2816×1536 | ? | `AEC-Architecture/MEP/201_img/gate.png` |
| 8.7 MB | 2816×1536 | 70% | `AEC-Architecture/Materials/assets/images/insulation_rigid_polyurethane.png` |
| 8.6 MB | 2816×1536 | ? | `AEC-Architecture/MEP/201_img/check.png` |
| 8.2 MB | 2048×2048 | 80% | `AEC-Architecture/Materials/assets/images/finish_iso.png` |
| 8.1 MB | 2816×1536 | ? | `AEC-Architecture/MEP/201_img/cock.png` |
| 8.0 MB | 2816×1536 | 70% | `AEC-Architecture/Materials/assets/images/insulation_glass_wool.png` |
| 7.9 MB | 2816×1536 | 100% | `AEC-Architecture/Materials/assets/images/facade_iso_stone.png` |
| 7.8 MB | 2816×1536 | ? | `AEC-Architecture/MEP/201_img/flush.png` |
| 7.8 MB | 2816×1536 | ? | `AEC-Architecture/MEP/201_img/butterfly.png` |
| 7.8 MB | 2816×1536 | ? | `AEC-Architecture/MEP/201_img/float.png` |
| 7.6 MB | 2816×1536 | 100% | `AEC-Architecture/Materials/assets/images/facade_iso_brick.png` |
| 7.4 MB | 2816×1536 | ? | `AEC-Architecture/MEP/201_img/floor.png` |
| 7.4 MB | 2816×1536 | ? | `AEC-Architecture/MEP/201_img/Multi.png` |
| 7.3 MB | 2816×1536 | 70% | `AEC-Architecture/Materials/assets/images/insulation_pf_board.png` |
| 7.2 MB | 2816×1536 | ? | `AEC-Architecture/MEP/201_img/insulation.png` |

## 🤖 AI-generated images (filename `Generated Image…`)

These are almost certainly synthetic; confirm the generation tool and record it (`generated_with`). Verify they may be redistributed under the tool's terms.

| Size | File |
| ---: | :--- |
| 6.3 MB | `AEC-Architecture/Construction/201_img/Generated Image February 09, 2026 - 1_53PM.jpeg` |
| 5.1 MB | `AEC-Architecture/Construction/201_img/Generated Image February 09, 2026 - 1_29PM.jpeg` |
| 3.8 MB | `AEC-Architecture/Construction/201_img/Generated Image February 09, 2026 - 1_21PM.jpeg` |
| 3.1 MB | `AEC-Architecture/Construction/201_img/Generated Image February 09, 2026 - 1_18PM.jpeg` |
| 1.7 MB | `AEC-Architecture/Construction/201_img/Generated Image February 09, 2026 - 1_09PM.jpeg` |
| 1.4 MB | `AEC-Architecture/Construction/201_img/Generated Image February 09, 2026 - 1_07PM.jpeg` |
| 1.2 MB | `AEC-Architecture/Construction/201_img/Generated Image February 09, 2026 - 1_02PM.jpeg` |
| 1.2 MB | `AEC-Architecture/Construction/201_img/Generated Image February 09, 2026 - 4_43PM.jpeg` |
| 1.0 MB | `AEC-Architecture/Construction/201_img/Generated Image February 09, 2026 - 2_25PM.jpeg` |
| 0.9 MB | `AEC-Architecture/Construction/201_img/Generated Image February 09, 2026 - 2_10PM.jpeg` |
| 0.7 MB | `AEC-Architecture/Construction/201_img/Generated Image February 09, 2026 - 2_06PM.jpeg` |
| 0.5 MB | `AEC-Architecture/Construction/201_img/Generated Image February 09, 2026 - 12_50PM.jpeg` |

## 🗑️ Orphan images (not referenced by any doc)

Either re-link them in the relevant doc or remove them. **Not deleted automatically** — a broken reference elsewhere is possible.

| Size | File |
| ---: | :--- |
| 3.1 MB | `AEC-Architecture/MEP/101-102_img/101-5.png` |
| 2.3 MB | `AEC-Architecture/Regulation/assets/images/04-3.jpg` |
| 0.5 MB | `AEC-Architecture/Planning/201-203_img/Circulation plan0.png` |
| 0.4 MB | `AEC-Architecture/Planning/201-203_img/Circulation plan1.png` |

## Recommended actions

1. **Fill rights metadata** in `image-manifest.csv` (creator / source_url / license) — highest priority; unverified third-party images cannot be redistributed under the repo license.
2. **Recompress** the oversized list to display resolution (target < ~300 KB each). Expected working-tree reduction: **~458 MB → ~40–60 MB**.
3. **Note:** committing recompressed files does *not* shrink existing git history — that needs a history rewrite (`git filter-repo`), a maintainer decision because it rewrites shared history on a public repo.
4. **Re-link or remove** the 4 orphans; **confirm the tool** for the 12 AI-generated images.
