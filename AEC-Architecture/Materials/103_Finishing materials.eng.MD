# 🎨 Finishing Materials

> <strong>Document Info</strong>
> * <strong>Category:</strong> Architecture / Finishing Layer
> * <strong>Target System:</strong> Rendering, Facility Management (FM), BIM/DT Material Library
> * <strong>Last Updated:</strong> 2026-02-02
> * <strong>Keywords:</strong> `Sensory Quality`, `Maintenance`, `Durability`, `Detailing`

---

<div align="center">

# 03. Finishing Layer Data Definition

### "Surface as Data: The final layer that shapes spatial experience"

</div>

---

<br>

## 1. Overview

Finishing materials are the layer users directly experience.  
In a Digital Twin, they are modeled along three axes:

* <strong>Sensory:</strong> color, texture, gloss, reflectance, warm/cool perception
* <strong>Performance:</strong> fire retardant, sound absorption, durability, stain resistance
* <strong>Operations:</strong> maintenance cycle, replacement difficulty, cost

<br>

---

## 2. Internal Finishes

<div align="center">
  <img src="./assets/images/finish_iso.png" width="80%" alt="Interior Finish Iso View">
</div>

> <strong>Concept Note:</strong> The core is visualizing the “sense of space by material.”  
> Even on the same plan, finish combinations change <strong>warmth, brightness, reflectance, and tactility</strong>.

### 2.1 Surface by Location

| Location | Typical Materials | Key Points |
| :--- | :--- | :--- |
| <strong>Floor</strong> | Wood flooring (engineered/laminate), tile, PVC sheet, carpet | durability, footfall feel, acoustics |
| <strong>Wall</strong> | Wallpaper (paper/vinyl), paint, tile, interior film, wood panels | stain control, texture, design |
| <strong>Ceiling</strong> | Gypsum board with wallpaper/paint, acoustic tiles (office), exposed ceiling | lighting plan, reflectance |

### 2.2 Spatial Mood Mapping

* <strong>Wood-based:</strong> warm, stable, suitable for low-to-mid saturation spaces
* <strong>Tile/stone-based:</strong> calm, clean, stronger specular reflection
* <strong>Fabric/carpet:</strong> sound absorption, cozy feel, maintenance-dependent usability

### 2.3 Functional Performance

* <strong>Fire Retardant:</strong> slows ignition and toxic gas release during fire  
  → essential for evacuation safety.
* <strong>Sound Absorption:</strong> reduces reverberation  
  → critical for meeting rooms, auditoriums, studios.
* <strong>Durability:</strong> resistance to scratches, impact, moisture  
  → primary criterion for flooring.

### 2.4 Digital Twin Data Fields

* <strong>`Surface_Roughness`</strong>: visual reflectance / rendering quality
* <strong>`Slip_Resistance`</strong>: floor safety indicator
* <strong>`VOC_Emission`</strong>: indoor air quality metric
* <strong>`Maintenance_Cycle`</strong>: service interval (months/years)
* <strong>`Replace_Cost`</strong>: replacement cost range

<br>

---

## 3. External Finishes

> <strong>Concept Note:</strong> External finishes define a building’s <strong>identity</strong>.  
> Facade imagery should be paired with maintenance data by material type.

### 3.1 Facade Type Classification

<table width="100%">
  <tr>
    <td align="center" width="50%">
      <img src="./assets/images/facade_iso_stone.png" alt="Stone Facade" width="100%">
      <br>
      <b>① Stone Facade</b>
    </td>
    <td align="center" width="50%">
      <img src="./assets/images/facade_iso_metal.png" alt="Metal Facade" width="100%">
      <br>
      <b>② Metal Facade</b>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="./assets/images/facade_iso_glass.png" alt="Glass Facade" width="100%">
      <br>
      <b>③ Glass Facade</b>
    </td>
    <td align="center" width="50%">
      <img src="./assets/images/facade_iso_brick.png" alt="Brick Facade" width="100%">
      <br>
      <b>④ Brick Facade</b>
    </td>
  </tr>
</table>

<br>

| Material | Typical Composition | Look & Feel | Key Management Points |
| :--- | :--- | :--- | :--- |
| <strong>Stone</strong> | granite, marble, limestone | heavy, premium, highly durable | structural load, staining/efflorescence |
| <strong>Metal</strong> | aluminum panels, zinc, steel sheets | modern, refined, easy to fabricate | corrosion protection, joint details |
| <strong>Glass</strong> | curtain wall system | open, high daylight | thermal performance, condensation, sealing |
| <strong>Brick</strong> | facing brick, clay brick | warm, classic, ages well | joint cracking, absorption rate |

### 3.2 Facade Data Fields

* <strong>`Weathering_Rate`</strong>: rate of surface aging (color/texture change)
* <strong>`Thermal_Bridge_Risk`</strong>: thermal bridge risk (esp. metal)
* <strong>`Sealant_Life`</strong>: sealant lifespan (curtain wall critical)
* <strong>`Cleaning_Method`</strong>: cleaning approach (including high-rise access)
* <strong>`Replacement_Panel_Time`</strong>: module replacement time

<br>

---

## 4. Summary

Finishes define <strong>impression + performance + operating cost</strong>.  
In a Digital Twin, “surface” should be treated as an <strong>operational data layer</strong>, not just a texture.
