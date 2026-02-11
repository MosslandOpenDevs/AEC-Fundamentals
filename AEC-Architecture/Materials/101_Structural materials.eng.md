# 🏗️ Structural Materials

> <strong>Document Info</strong>
> * <strong>Category:</strong> Architecture / Structural Core
> * <strong>Target System:</strong> Structural Analysis (FEM), Quantity Take-off (QTO), Physics Engine
> * <strong>Last Updated:</strong> 2026-02-02
> * <strong>Keywords:</strong> `Concrete Hierarchy`, `Data Integrity`, `Thermal Mass`, `LCA`

---

<div align="center">

# 01. Data Hierarchy of Structural Materials (Concrete Hierarchy)

### "Code as Material: Data Objects with Physical Properties"

</div>

---

<br>

In Digital Twins, architectural materials are not merely 3D textures.

They serve as <strong>Boundary Conditions</strong> for energy simulation and <strong>Data Entities</strong> that determine the reliability of carbon emission algorithms.

<br>

#### 1. Composition Logic

These three materials are not separate substances but share an <strong>Inheritance</strong> relationship.
When designing a data schema, one must understand the inclusion relationship below.

<div align="center">

| Level 1 (Base) | Level 2 (Surface) | Level 3 (Core) |
| :--- | :--- | :--- |
| <strong>Cement Paste</strong> | <strong>Mortar</strong> | <strong>Concrete</strong> |
| `Water` + `Cement` | `Paste` + `Sand` (Fine Agg.) | `Mortar` + `Gravel` (Coarse Agg.) |
| Binder | Interface | Load-bearing Structure |

</div>

> <strong>💡 Dev Note:</strong> The presence of Gravel acts as a `Boolean` value that determines whether this object is a <strong>Structure</strong> or a <strong>Finish</strong>.

<br>

#### 2. Material Properties & Data Points

<strong>① Cement Paste</strong>
* <strong>Physics:</strong> High fluidity. No aggregates.
* <strong>Data Point:</strong>
    * `Hydration Heat`:
        - Computational Role: 
          Acts as an internal heat source during the cement curing process; directly influences early temperature rise and thermal crack analysis in mass concrete.
    * `Carbon Intensity`:
        - Computational Role: 
          Determines carbon emissions per unit volume in LCA calculations; has the highest carbon contribution due to 100% cement composition.
* <strong>Usage:</strong> Tile Grout, Micro-crack Repair

<br>

<strong>② Mortar</strong>
* <strong>Physics:</strong> Smooth surface. Used for brick bonding or floor leveling.
* <strong>Data Point:</strong>
    * `Layer Depth`:
        - Computational Role: 
          Modeled as a thin layer (typically 20~30mm); treated as a surface layer with limited structural or thermal impact.
    * `Roughness` ($k_s$):
        - Computational Role: 
          Determines wall friction loss in CFD analysis; lower roughness values result in calculated lower fluid flow resistance.
* <strong>Usage:</strong> Brick Masonry, Floor Smoothing (Screed), Tile Bonding

<br>

<strong>③ Concrete</strong>
* <strong>Physics:</strong> Coarse aggregates interlock to withstand compressive forces.
* <strong>Data Point:</strong>
    * `Mass` (Density):
        - Computational Role: 
          Acts as self-weight (2,300 ~ 2,400 kg/m³); serves as the primary load input in structural analysis.
    * `Specific Heat`:
        - Computational Role: 
          Determines the ability to store and release heat (Thermal Mass); influences indoor temperature Time Lag and energy load calculations.
* <strong>Usage:</strong> Column, Beam, Slab, Foundation

<br>

---

#### 3. Critical Reasons for Data Distinction

<strong>① Energy Simulation: "Different Entities of Heat Capacity"</strong>

Depending on the material properties, the simulation <strong>Time Step</strong> and <strong>Space</strong> settings must be adjusted.

* <strong>Simulation Logic:</strong>
    * <strong>Concrete:</strong> Acts as a massive <strong>Thermal Battery</strong> (Creates Time Lag).
    * <strong>Mortar:</strong> Acts merely as a thin <strong>Skin</strong> layer with negligible thermal storage.

> <strong>⚠️ Risk:</strong> If a wall is incorrectly mapped as `Mortar`, the heat storage capacity is calculated as near '0', resulting in an <strong>Over-spec HVAC design</strong>.

<br>

<strong>② Digital Twin & LCA: "Carbon Data Algorithm Errors"</strong>

* <strong>Logic:</strong> 
  $\text{Total Carbon} = \text{Volume}(\text{m}^3) \times \text{Carbon Factor}(\text{kgCO}_2\text{e/m}^3)$
* <strong>Fact:</strong> 
  Due to differences in cement content, the carbon coefficients for Concrete and Mortar are different.

> <strong>⚠️ Risk:</strong> If floor screed (`Mortar`) is calculated using the coefficient for the structure (`Concrete`), the carbon emissions will be underestimated, leading to a <strong>Greenwashing</strong> error.