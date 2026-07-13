# 🔐 Image Rights Clearance — triage (clearance 0/171)

> **Status: TRIAGED, not cleared.** All 171 images are `status=unreviewed`; **0 are cleared**, and `source_url`/`license` are empty for every file. `clearance_status` below is a *provisional, evidence-based* label (filename, format, alpha, colour complexity, in-image notices, spot visual inspection) to speed a human review — **not a legal determination**. Each file still needs a person to confirm `creator`/`source_url`/`license` in `image-manifest.csv`.

## Buckets
| clearance_status | files | MiB | meaning | action |
| :--- | ---: | ---: | :--- | :--- |
| `third-party-HIGH-RISK` | 15 | 6 | real photos / real project drawings, source unknown | **Remove, replace, or link-out** unless redistribution permission is obtained |
| `third-party-aethrion-notice` | 15 | 33 | carry an in-image rights notice naming **AETHRION** | Confirm the AETHRION agreement (rights chain, redistribution, sublicense) |
| `review-needed-photo` | 19 | 29 | photo-like JPEG, source unclear | **Human view required** — classify then clear |
| `review-needed` | 4 | 8 | ambiguous | Human view required |
| `suspected-ai-generated` | 12 | 27 | filename `Generated Image …` | Confirm the generating tool + that its terms allow redistribution |
| `suspected-ai-illustration` | 11 | 4 | concept illustration with AI hallmarks (e.g. typos) | Confirm tool/authorship; record `generated_with` |
| `creator-unknown-likely-project` | 95 | 351 | design-tool diagram; **creator unknown, likely project-created** | Confirm authorship (in-house vs AI vs third party) |

## 🚩 Key evidence (to confirm, not conclusions)

- **AETHRION rights notice detected** on the `Regulation/` image set (15 files). `Regulation Intro Image.jpg` and the chapter infographics (`03-2.jpg`, …) carry the in-image line **“본 저작물 권한은 AETHRION에 있습니다”** ("rights to this work belong to AETHRION"). This detects a third-party rights holder; it does **not** establish what the project may redistribute — confirm the AETHRION agreement.

- **A real project's drawings.** `site-plan.jpg`, `first-floor-plan.jpg`, `front-elevation.jpg`, `section.jpg`, `detail.jpg` are professional drawings of an actual building (scale bars, VOID call-outs — viewed). Likely published elsewhere; high removal/replacement risk.

- Famous-building photos (`pantheon`, `big-ben`, …) and **Le Corbusier Modulor** are third-party.

- Concept PNGs (`gothic.png`, …) are **suspected AI-generated** (`gothic.png` shows a `cellings` typo). Record the tool; do not assume the terms permit redistribution.

## HIGH-RISK — remove / replace / license before any public release

- `AEC-Architecture/Planning/101-103_img/modulor.png` — Le Corbusier Modulor — likely copyrighted (FLC/ADAGP)
- `AEC-Architecture/Construction/01_img/brighton.jpg` — real-building photograph, source unknown
- `AEC-Architecture/Construction/01_img/florence-cathedral.jpg` — real-building photograph, source unknown
- `AEC-Architecture/Construction/01_img/rococo.jpg` — real-building photograph, source unknown
- `AEC-Architecture/Construction/01_img/baroque.jpg` — real-building photograph, source unknown
- `AEC-Architecture/Planning/101-103_img/Corbusier Modulor color..jpg` — Le Corbusier Modulor — likely copyrighted (FLC/ADAGP)
- `AEC-Architecture/Construction/01_img/the-white-house.jpg` — real-building photograph, source unknown
- `AEC-Architecture/Construction/01_img/greece.jpg` — real-building photograph, source unknown
- `AEC-Architecture/Planning/101-103_img/first-floor-plan.jpg` — real architectural project drawing (viewed); source unknown
- `AEC-Architecture/Construction/01_img/pantheon.jpg` — real-building photograph, source unknown
- `AEC-Architecture/Construction/01_img/big-ben.jpg` — real-building photograph, source unknown
- `AEC-Architecture/Planning/101-103_img/site-plan.jpg` — real architectural project drawing (viewed); source unknown
- `AEC-Architecture/Planning/101-103_img/section.jpg` — real architectural project drawing (viewed); source unknown
- `AEC-Architecture/Planning/101-103_img/front-elevation.jpg` — real architectural project drawing (viewed); source unknown
- `AEC-Architecture/Planning/101-103_img/detail.jpg` — real architectural project drawing (viewed); source unknown

## AETHRION rights notice — confirm the agreement

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

## Needs a human look

- `AEC-Architecture/Planning/201-203_img/01_image1.jpg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/SpaceComposition.jpg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/01_image2.jpg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/Basic unit of space.jpg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/Circulation plan.jpg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/FlowPlan.jpg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/FloorPlan.jpg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/plan.jpg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/Corridor_image.jpg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Construction/202_img/5.jpeg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/Lowlevel.jpg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Construction/202_img/3.jpeg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/Room_image.jpg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Construction/202_img/1.jpeg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Construction/202_img/4.jpeg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Construction/202_img/2.jpeg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Planning/201-203_img/Highlevel.jpg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Structure/assets/images/material_concept_compare.png` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Planning/101-103_img/bubble.jpg` — photo-like JPEG; source unknown (photo vs AI)
- `AEC-Architecture/Construction/401_img/finishing_waterproofing_03.png` — ambiguous
- `AEC-Architecture/Construction/301-302_img/BAR.png` — ambiguous
- `AEC-Architecture/Construction/301-302_img/formwork.png` — ambiguous
- `AEC-Architecture/Planning/201-203_img/Circulation plan1.png` — ambiguous

## Recommended order

1. Confirm the **AETHRION** agreement (covers 15 files).
2. Resolve the **15 HIGH-RISK** files (permission / replace with owned-or-CC0 / link-out).
3. Human-review the **23** `review-needed*` files and the `creator-unknown-likely-project` set.
4. For AI images, record `generated_with` + confirm the tool's terms.
5. Fill `creator/source_url/license` per row; set `status: cleared`.
6. Only after clearance: compress survivors + one history rewrite (see IMAGE-AUDIT.md).
