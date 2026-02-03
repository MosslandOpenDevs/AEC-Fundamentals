---
title: "Digital Twin Material Guide: 03. Structure Types & Data Topology"
date: 2026-02-02
category: Architecture / Structure
tags: [Wall Structure, Rahmen, Simulation, Data Hierarchy, Thermal Bridge]
description: "Comparison of simulation boundary conditions and data hierarchy between Wall and Rahmen structures"
---

# 🏗️ Structural System & Data Topology

> **Document Info**
> * **Category:** Architecture / Structural System
> * **Target System:** Energy Analysis, Airflow Analysis (CFD), BIM Data Management
> * **Last Updated:** 2026-02-02
> * **Keywords:** `Wall vs Rahmen`, `Physical Constraint`, `Thermal Bridge`, `Data Hierarchy`

---

<div align="center">

# 02 Structural System & Data Topology

### Wall vs. Rahmen Structure: Differences in Simulation Boundary Conditions and Data Hierarchy

</div>

---

<br>

Identifying the **Structural System** during the Digital Twin construction phase means more than just simple geometric modeling.

The structural system is the highest-level <strong>Physical Constraint</strong> that determines the <strong>Thermal Bridge lines</strong> for energy analysis, the <strong>Obstacles</strong> for airflow analysis, and the <strong>Modifiable Scope</strong> of BIM data.

<br>

<div align="center">

| <strong>1. Wall Structure</strong> | <strong>2. Rahmen Structure</strong> |
| :--- | :--- |
| <strong>Linear Constraint</strong><br>Closed Data Cell | <strong>Point Constraint</strong><br>Flexible Field |
| <strong>[Definition]</strong><br><strong>Bearing Walls</strong> support vertical loads, acting as both space dividers and structural entities simultaneously. | <strong>[Definition]</strong><br>Columns and Beams combine to form a 3D frame, while walls are <strong>Non-load bearing</strong> elements. |
| <img src="./assets/images/structure_wall_iso.png" width="100%" alt="Wall Structure Isometric"> | <img src="./assets/images/structure_rahmen_iso.png" width="100%" alt="Rahmen Structure Isometric"> |
| <strong>[Analytical View] Analytically Closed</strong><br><br><li><strong>Energy</strong>: All corners where exterior and interior walls meet become <strong>Linear Thermal Bridges</strong>.</li><br><li><strong>Airflow</strong>: Airflow is blocked by bearing walls, enforcing <strong>Room-based independent grid</strong> partitioning.</li> | <strong>[Analytical View] Analytically Open</strong><br><br><li><strong>Energy</strong>: Structure is separated from the skin. <strong>Window & Curtain Wall</strong> properties become key variables.</li><br><li><strong>Airflow</strong>: Analyzed as a massive <strong>Open Plan</strong>, where columns act as <strong>Obstacles</strong> splitting the flow.</li> |
| <img src="./assets/images/sim_closed_boundary.png" width="100%" alt="Simulation Closed Boundary"> | <img src="./assets/images/sim_open_field.png" width="100%" alt="Simulation Open Field"> |
| <strong>[Data] Static Zone</strong><br><br><li>BIM Wall Attribute = <strong>`Structural`</strong> (Fixed)</li><li>Room boundaries are permanently fixed, resulting in low flexibility for the O&M data model.</li> | <strong>[Data] Dynamic Layer</strong><br><br><li>BIM Wall Attribute = <strong>`Architectural`</strong> (Variable)</li><li>Sensor data is mapped to immutable <strong>Columns (Anchors)</strong>, while wall info is modifiable.</li> |
| <img src="./assets/images/data_static_zone.png" width="100%" alt="Static Data Zone"> | <img src="./assets/images/data_dynamic_grid.png" width="100%" alt="Dynamic Data Grid"> |
| 💡 <strong>Insight</strong><br>Min. Modeling Unit: <strong>Fixed Room</strong> | 💡 <strong>Insight</strong><br>Min. Modeling Unit: <strong>Coordinate Grid</strong> |
| <div align="center"><br><h3>🔻 Summary: Wall</h3></div> | <div align="center"><br><h3>Summary: Rahmen 🔻</h3></div> |
| <div align="center"><b>[Constraint]</b><br>Linear Constraint</div> | <div align="center"><b>[Constraint]</b><br>Point Constraint</div> |
| <div align="center"><b>[BIM Hierarchy]</b><br>Wall = Structure (Immutable)</div> | <div align="center"><b>[BIM Hierarchy]</b><br>Wall = Architecture (Mutable)</div> |
| <div align="center"><b>[Energy Analysis]</b><br>Thermal Bridge Management</div> | <div align="center"><b>[Energy Analysis]</b><br>Skin Performance Management</div> |
| <div align="center"><b>[Airflow Analysis]</b><br>Compartment (Partitioned)</div> | <div align="center"><b>[Airflow Analysis]</b><br>Open Field (Open Plan)</div> |

</div>

<br><br>

<div align="center">

### Conclusion

<br>

Understanding the building's structural system is akin to understanding the <strong>shape of the vessel</strong> that holds the data.

When building performance analysis models and Digital Twins, please set the correct <strong>Data Hierarchy</strong> according to the target building's structural format.

</div>