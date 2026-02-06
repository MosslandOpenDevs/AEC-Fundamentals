
# Architectural Drawings

Architectural drawings are technical documents used to communicate design intent and construction standards in a shared language across the entire team. Therefore, when reading drawings, it is important to first understand what each drawing is showing and what decisions it supports (site plan / floor plan / elevation / section / detail / schedule). This chapter first summarizes the basic types of drawings, then explains how to interpret line weights and colors in CAD drawings, and finally introduces common abbreviations frequently found on drawings.

---

# 도면의 종류

## Site Plan

<img src="101-103_img/site-plan.jpg" style="width:80%;">

(ArchDaily, White Brick House/PLAN Architects office, https://www.archdaily.com/1037251/white-brick-house-plan-architects-office)

A site plan includes the site boundary, adjacent roads, access points, parking circulation, levels (external GL), and the scope and boundaries of landscape/civil works. Rather than focusing on the building’s internal configuration, it primarily shows the relationship between the building and its surroundings (approach, circulation, and exterior space planning).
In practice, the site plan is where key conditions are checked first—such as whether access is intuitive, whether vehicle routes conflict, and whether site level references are clearly defined.

## Floor Plan

<img src="101-103_img/first-floor-plan.jpg" style="width:80%;">

(ArchDaily, White Brick House/PLAN Architects office, https://www.archdaily.com/1037251/white-brick-house-plan-architects-office)

A floor plan is often the first drawing people think of when they hear “architectural drawing.” It shows the spatial layout, circulation, dimensions, walls/doors/windows, and core components (stairs, elevators, restrooms, shafts). It is also typically the first drawing where detailed work begins in the design process.
Because elevations, sections, and details are difficult to finalize reliably until the floor plan is confirmed, the floor plan functions as a baseline drawing for the entire project.

## Elevation

<img src="101-103_img/front-elevation.jpg" style="width:80%;">

(ArchDaily, White Brick House/PLAN Architects office, https://www.archdaily.com/1037251/white-brick-house-plan-architects-office)

An elevation shows what the building will look like from the outside. You can review façade composition, window proportions, and elevation levels (floor lines), and it organizes elements that shape the building’s overall impression—such as material segmentation and repetition, and the proportions of openings (windows).
In practice, reviews typically focus on floor-line alignment, window datum lines, and consistency of material boundaries.

## Section

<img src="101-103_img/section.jpg" style="width:80%;">

(ArchDaily, White Brick House/PLAN Architects office, https://www.archdaily.com/1037251/white-brick-house-plan-architects-office)

A section represents the building as if it were cut in a specific direction. It allows you to verify floor-to-floor height and ceiling height, floor/slab thickness, service zones (ducts/pipes), and structural depth. Because vertical clearances that are not visible in plans—especially ceiling plenum space for services—are revealed in sections, they are essential drawings for clash checks and for determining floor heights.

## Detail / Blow-up

<img src="101-103_img/detail.jpg" style="width:80%;">

(metalocus, ALVARO LAMAS Gaviones de piedra para unas viviendas adosadas por Gino Guarnieri y Roberto Mascazzini, 
https://www.metalocus.es/es/noticias/gaviones-de-piedra-para-unas-viviendas-adosadas-por-gino-guarnieri-y-roberto-mascazzini)

A detail drawing enlarges areas that are hard to confirm in overall drawings—such as exterior wall-to-slab joints, window perimeters, roof waterproofing/parapets, restroom waterproofing, and floor level changes/thresholds—to show construction details for specific parts. In practice, details often determine performance-critical areas directly tied to defects (waterproofing, insulation, airtightness, thermal bridging, etc.), so it is important to develop them to a level where the construction method can be clearly explained.

## Schedule Drawings

<img src="101-103_img/schedule.png.jpg" style="width:80%;">

(M.T.COPELAND TECHNOLOGIES, https://mtcopeland.com/blog/what-are-window-and-door-schedules-in-blueprints/)

Schedule drawings list items such as window schedules, door schedules, finish schedules, hardware schedules, and room name schedules in table form. Because drawing symbols (tags) must match the codes in the schedule precisely to reduce confusion in quantity takeoffs, estimating, and procurement, practitioners pay special attention to omissions and duplicates.

---

# Checking CAD Drawings

When producing drawings, line thickness varies depending on the purpose of the line (section lines, elevation lines, centerlines, etc.). This is a convention (a standard rule) used to convey the priority and meaning of information to the reader. The same principle applies when drafting with CAD software: lines are commonly differentiated by color, and when plotting (printing), each color is mapped to a specific line weight.

Below is an example of a commonly used line-color standard table in CAD files. Smaller numbers indicate thinner lines and larger numbers indicate thicker lines. More important elements are drawn heavier so they can be distinguished at a glance.

| Color No. | Line-weight name |  Plot color | Screen color | Use                                                                                                 |
| --------: | :--------------: | :---------: | :----------- | :-------------------------------------------------------------------------------------------------- |
|         1 |       No. 1      |    Black    | Red          | Thin lines, centerlines                                                                             |
|         2 |       No. 5      |    Black    | Yellow       | Structural elements, major section lines; important elements such as boundary lines                 |
|         3 |       No. 4      |    Black    | Green        | Text, symbols; non-load-bearing walls (masonry)                                                     |
|         4 |       No. 2      |    Black    | Cyan         | Finish lines, elevation lines, furniture; demountable partitions; elevators, sanitary fixtures, MEP |
|         5 |       No. 1      |    Black    | Blue         | Reserved                                                                                            |
|         6 |       No. 1      |    Black    | Magenta      | Reserved                                                                                            |
|         7 |       No. 3      |    Black    | White        | Windows (including frames); dimension lines and leaders; revision clouds                            |
|         8 |       No. 1      |    Black    | Dark gray    | Hatching; site-related—roads, parking, people, landscape, vehicles                                  |
|         9 |       No. 1      |    Black    | Light gray   | Reserved                                                                                            |
|       10+ |         –        | Black/Color | –            | Reserved                                                                                            |



# Drawing Abbreviations

When reviewing drawings, you will repeatedly encounter English abbreviations. Abbreviations are used to keep drawings concise and to speed up communication, but if standards are not aligned, they can cause confusion instead. In particular, abbreviations related to levels, datums/grids, and dimensions directly affect cross-discipline coordination, so their meanings should be clarified early in the project and used consistently.

Below is a categorized list of the most basic and commonly used abbreviations in architectural drawings.

## Level-Related Abbreviations

A level defines the reference point used to describe height. Even for the “same” fifth floor, different level references can change floor-to-floor height, ceiling height, and service clearances. For that reason, level abbreviations must be understood accurately.

- EL (Elevation Level)

An absolute elevation referenced to mean sea level. Commonly used when reviewing relationships to the site and surrounding infrastructure, and for checking exterior levels.

GL (Ground Level)

- GL (Ground Level)

The ground level. Used as an exterior reference height in a project, and the exact benchmark may be defined differently depending on the facility. If GL is ambiguous on the site plan or external circulation drawings, slope, drainage, and access planning can become unstable.

- FL (Finish Level)

The finished level. Refers to the reference height after interior floor finishes are completed, and FL is often used as the basis for indicating floor levels on drawings. In practice, it ties directly to decisions such as threshold steps, finish thickness, and accessibility ramps.
- SL (Slab Level)

The structural level. Used when defining floors based on the top of slab. Because the difference between FL and SL corresponds to finish thickness and floor-system allowance, it is critical for MEP clash checks.

## Grid / Datum Line Abbreviations
When structural, architectural, and MEP drawings are coordinated, the grid is one of the first references to check.


GRID / G (Grid Line)

Reference lines for structure and planning. Typically labeled with numbers (1, 2, 3…) and letters (X, Y…), and used as the basis for column locations and major wall layouts.

CL (Center Line)

A centerline. Indicates the center of a wall, column, equipment, etc. Because dimensional errors can be significant depending on whether dimensions are taken from faces or from centerlines, the drawing intent should be confirmed together with the notation.

## Dimension and Geometry Abbreviations

DIM (Dimension)

치수 표기 자체를 의미하거나 치수 관련 주기를 가리킬 때 사용합니다.

Ø / DIA (Diameter)

Diameter notation for circular elements (e.g., Ø150). Used for pipes/ducts as well as handrails, circular columns, and other round components.

R (Radius)

Radius notation (e.g., R50). Used for curved surfaces, rounding, and curved walls.

TYP (Typical)

Indicates a repeated condition. Drawings are simplified by showing the condition once and marking it as TYP. However, any exceptions must be noted separately.

## 창호부호

Drawings use various codes related to windows and doors to indicate material and type (window/door/fire door/shutter, etc.) in a compact form. Understanding this system makes it much easier to distinguish openings quickly on plans and elevations, and to coordinate with schedules (window/door schedules), finish schedules, and cost estimates. In this document, the symbols used for window/door coding are organized based on KSF 1502.

| Material                  | Material code | Window (W) | Door (D) | Fire Door (FD) | Shutter (S) | Fire Shutter (FS) | Grille (G) | Frame (F) |
| ------------------------- | :-----------: | :--------: | :------: | :------------: | :---------: | :---------------: | :--------: | :-------: |
| Aluminum alloy            |       A       |     AW     |    AD    |        –       |      AS     |         –         |     AG     |     AF    |
| Plastic (synthetic resin) |       P       |     PW     |    PD    |        –       |      –      |         –         |      –     |     PF    |
| Steel                     |       S       |     SW     |    SD    |       FSD      |      SS     |        FSS        |     SG     |     SF    |
| Stainless steel           |       SS      |     SSW    |    SSD   |      FSSD      |     SSS     |         –         |     SSG    |    SSF    |
| Wood                      |       W       |     WW     |    WD    |        –       |      –      |         –         |     WG     |     WF    |

Other Common Drawing Conventions그 외 도면에서 자주 보이는 표기 관례

NTS (Not To Scale)

Means “not to scale.” In detail drawings or concept diagrams, actual dimensions must be verified using dimension lines rather than by measuring the drawing.

REV (Revision)

Indicates a revision/change. Often appears with revision clouds or revision marks and is used to quickly identify the scope of changes.

---

## 참고 자료

- 한국건축사협회, 건축도면 공동표준지침 1.1
- 한국건축사협회, 건축도면 공동표준지침 부속서 8 건축 도면약어목록 1.1