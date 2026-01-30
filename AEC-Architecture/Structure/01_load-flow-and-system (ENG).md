<div align="center">

# Types of Loads and Flow

<img src="./assets/images/structure.png" width="80%" alt="Load Flow Structure Diagram">

<br>

| **Dead Load** | **Live Load** | **Environmental Load** |
| :---: | :---: | :---: |
| **Weight of Slabs, Beams, Columns, Finishes** | **People, Furniture, Equipment, Vehicles, etc.** | **Wind, Snow, Seismic Loads** |
| □ Structure Thickness = Thermal Mass<br>□ Impact on Energy Simulation | □ Occupant Density = Internal Gain<br>□ Directly linked to HVAC Sizing | Varies by Height · Shape · Location |

</div>

<br><br>

<div align="center">

### 1. Slab

<img src="./assets/images/slab_diagram.png" width="80%" alt="Slab Structure Diagram">

<br>

The <strong>thickness and density</strong> of the concrete slab determine the building's thermal inertia.

If the concrete does not retain enough heat, the <strong>Peak Load</strong><br>
in the simulation will be calculated abnormally high.

<br>

> <strong>*Peak Load:</strong> The maximum energy requirement for the hottest or coldest moments, which determines the HVAC system capacity.

</div>

<br><br>

<div align="center">

### 2. Beam

<img src="./assets/images/beam_diagram.png" width="80%" alt="Beam Structure Diagram">

<br>

A <strong>horizontal framework</strong> that connects columns to support slabs.<br>
It transfers loads and prevents building deflection.

<br>

However, from an analysis perspective, it is a <strong>'Hard Constraint'</strong><br>
that determines the routing paths for mechanical ducts and pipes.

<br>

Ignoring beam depth during modeling results in <strong>impossible construction</strong> scenarios in reality<br>
and acts as an <strong>obstacle</strong> that disrupts airflow in CFD analysis.

</div>

<br><br>

<div align="center">

### 3. Column

<img src="./assets/images/column_diagram.png" width="80%" alt="Column Structure Diagram">

<br>

The 'Immutable Data Coordinates' within a variable space.

<br>

While interior walls may change during operation,<br>
columns remain the fixed <strong>Anchor Points</strong> of the space throughout the building's lifecycle.

<br>

They serve as absolute reference coordinates when dividing energy zones<br>
or placing digital twin sensors.<br>
Zones not partitioned based on columns will lose data integrity during future remodeling.

</div>