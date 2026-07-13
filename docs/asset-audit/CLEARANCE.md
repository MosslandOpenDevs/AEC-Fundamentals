# 🔐 Image Rights Clearance — triage

> Provisional, **evidence-based** triage of all 171 images to accelerate a human rights review. `clearance_status` is set from measurable evidence (filename, format, alpha channel, colour complexity, in-image credits, and spot visual inspection). **It is NOT a legal determination** — every image still needs a person to confirm `creator` / `source_url` / `license` in `image-manifest.csv` before the repo can be treated as rights-clean.

## Buckets
| clearance_status | files | MiB | meaning | action |
| :--- | ---: | ---: | :--- | :--- |
| `third-party-HIGH-RISK` | 15 | 6 | real photos / real project drawings, unknown source | **Remove, replace, or link-out** unless redistribution permission is obtained |
| `design-partner-AETHRION` | 15 | 33 | in-image credit assigns rights to **AETHRION** | Confirm the AETHRION agreement (commission/licence); record licence |
| `review-needed-photo` | 19 | 29 | photo-like JPEG, source unclear (photo vs AI) | **Human view required** — classify then clear |
| `review-needed` | 4 | 8 | ambiguous | Human view required |
| `ai-or-original-illustration` | 23 | 31 | AI-generated or self-authored illustrations | Record `generated_with` + confirm the tool's terms allow redistribution |
| `likely-original-diagram` | 95 | 351 | technical diagrams made in a design tool (alpha/flat PNG) | Confirm original (or AI tool); low risk |

## 🚩 Key findings

- **AETHRION owns the `Regulation/` image set.** `Regulation Intro Image.jpg` (and the chapter infographics such as `03-2.jpg`) carry the in-image line **“본 저작물 권한은 AETHRION에 있습니다”** ("rights to this work belong to AETHRION"). Treat all 15 `Regulation/assets/images/*` as a commissioned third party — confirm the licence/assignment with AETHRION.

- **The Planning drawing set is a real project.** `site-plan.jpg`, `first-floor-plan.jpg`, `front-elevation.jpg`, `section.jpg`, `detail.jpg` are professional drawings of an actual building (scale bars, VOID call-outs) — almost certainly published elsewhere (ArchDaily-style). High removal/replacement risk.

- **Famous-building photos are third-party.** `pantheon.jpg`, `big-ben.jpg`, `baroque.jpg`, `brighton.jpg`, `florence-cathedral.jpg`, `greece.jpg`, `rococo.jpg`, `the-white-house.jpg`.

- **Le Corbusier Modulor** (`Corbusier Modulor color..jpg`, `modulor.png`) is copyrighted (FLC/ADAGP).

- The concept PNGs (e.g. `gothic.png`) are **AI-generated** — `gothic.png` shows the tell-tale “cellings” typo. Low copyright risk, but record the tool and its terms.

## HIGH-RISK — remove / replace / license before public release

- `AEC-Architecture/Planning/101-103_img/modulor.png` — Le Corbusier Modulor — copyrighted (FLC/ADAGP)
- `AEC-Architecture/Construction/01_img/brighton.jpg` — real-building photograph (unknown source)
- `AEC-Architecture/Construction/01_img/florence-cathedral.jpg` — real-building photograph (unknown source)
- `AEC-Architecture/Construction/01_img/rococo.jpg` — real-building photograph (unknown source)
- `AEC-Architecture/Construction/01_img/baroque.jpg` — real-building photograph (unknown source)
- `AEC-Architecture/Planning/101-103_img/Corbusier Modulor color..jpg` — Le Corbusier Modulor — copyrighted (FLC/ADAGP)
- `AEC-Architecture/Construction/01_img/the-white-house.jpg` — real-building photograph (unknown source)
- `AEC-Architecture/Construction/01_img/greece.jpg` — real-building photograph (unknown source)
- `AEC-Architecture/Planning/101-103_img/first-floor-plan.jpg` — real architectural project drawing (viewed) — likely ArchDaily-style
- `AEC-Architecture/Construction/01_img/pantheon.jpg` — real-building photograph (unknown source)
- `AEC-Architecture/Construction/01_img/big-ben.jpg` — real-building photograph (unknown source)
- `AEC-Architecture/Planning/101-103_img/site-plan.jpg` — real architectural project drawing (viewed) — likely ArchDaily-style
- `AEC-Architecture/Planning/101-103_img/section.jpg` — real architectural project drawing (viewed) — likely ArchDaily-style
- `AEC-Architecture/Planning/101-103_img/front-elevation.jpg` — real architectural project drawing (viewed) — likely ArchDaily-style
- `AEC-Architecture/Planning/101-103_img/detail.jpg` — real architectural project drawing (viewed) — likely ArchDaily-style

## AETHRION-owned — confirm agreement

- `AEC-Architecture/Regulation/assets/images/03-2.jpg`
- `AEC-Architecture/Regulation/assets/images/03-2_ENG.jpg`
- `AEC-Architecture/Regulation/assets/images/03-3.jpg`
- `AEC-Architecture/Regulation/assets/images/03-3_ENG.jpg`
- `AEC-Architecture/Regulation/assets/images/04-1.jpg`
- `AEC-Architecture/Regulation/assets/images/04-1_ENG.jpg`
- `AEC-Architecture/Regulation/assets/images/04-2.jpg`
- `AEC-Architecture/Regulation/assets/images/04-2_ENG.jpg`
- `AEC-Architecture/Regulation/assets/images/04-3.jpg`
- `AEC-Architecture/Regulation/assets/images/5-0.jpg`
- `AEC-Architecture/Regulation/assets/images/5-0_ENG.jpg`
- `AEC-Architecture/Regulation/assets/images/5-2.jpg`
- `AEC-Architecture/Regulation/assets/images/5-2_ENG.jpg`
- `AEC-Architecture/Regulation/assets/images/Regulation Intro Image.jpg`
- `AEC-Architecture/Regulation/assets/images/Regulation Intro Image_ENG.jpg`

## Needs a human look (photo vs AI)

- `AEC-Architecture/Planning/201-203_img/01_image1.jpg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/SpaceComposition.jpg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/01_image2.jpg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/Basic unit of space.jpg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/Circulation plan.jpg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/FlowPlan.jpg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/FloorPlan.jpg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/plan.jpg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/Corridor_image.jpg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Construction/202_img/5.jpeg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/Lowlevel.jpg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Construction/202_img/3.jpeg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/Room_image.jpg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Construction/202_img/1.jpeg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Construction/202_img/4.jpeg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Construction/202_img/2.jpeg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/Highlevel.jpg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Structure/assets/images/material_concept_compare.png` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Planning/101-103_img/bubble.jpg` — photo-like JPEG — verify source (photo vs AI)
- `AEC-Architecture/Construction/401_img/finishing_waterproofing_03.png` — ambiguous
- `AEC-Architecture/Construction/301-302_img/BAR.png` — ambiguous
- `AEC-Architecture/Construction/301-302_img/formwork.png` — ambiguous
- `AEC-Architecture/Planning/201-203_img/Circulation plan1.png` — ambiguous

## Recommended order

1. Confirm the **AETHRION** licence (covers 15 files at once).
2. Resolve the **15 HIGH-RISK** files: obtain permission, replace with an owned/original or CC0 asset, or link out.
3. Human-review the **23** `review-needed*` files.
4. For AI images, record `generated_with` and confirm the tool's redistribution terms.
5. Fill `creator/source_url/license` in `image-manifest.csv`; set `status: cleared` per row.
6. Only after clearance: compress survivors + one history rewrite (see IMAGE-AUDIT.md).
