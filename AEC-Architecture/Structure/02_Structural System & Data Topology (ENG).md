# 02 Structural System & Data Topology

### Wall Structure vs. Rahmen Structure: Differences in Simulation Boundary Conditions and Data Hierarchy

---

In the Digital Twin construction phase, identifying the **Structural System** means more than just geometric modeling.

The structural system is the highest-level **Physical Constraint** that determines the **thermal bridge lines** for energy analysis, **obstacles** for airflow analysis, and the **modifiable range** of BIM data.

<br>

| **1. Wall Structure** | **2. Rahmen Structure (Rigid Frame)** |
| :--- | :--- |
| **Linear Constraint**<br>Closed Data Cell | **Point Constraint**<br>Flexible Field |
| **[Definition]**<br>**Bearing Walls**, which support vertical loads, partition the space and simultaneously act as the structural body. | **[Definition]**<br>Columns and Beams combine to form a 3D frame. The walls are **Non-bearing walls** that do not carry loads. |
| <img src="./assets/images/structure_wall_iso.png" width="100%"> | <img src="./assets/images/structure_rahmen_iso.png" width="100%"> |
| **[Analysis] Closed Boundary**<br><br><li>**Energy Analysis**: Every corner where exterior and interior walls meet becomes a **Linear Thermal Bridge**.</li><br><li>**Airflow Analysis**: Airflow is blocked by bearing walls, forcing **Room-based independent grid** partitioning.</li> | **[Analysis] Open Boundary**<br><br><li>**Energy Analysis**: Structure is separated from the envelope, making **Openings (Windows) and Curtain Walls** the key variables.</li><br><li>**Airflow Analysis**: Analyzed as a massive **Open Plan**, where columns act as **Obstacles** splitting the fluid flow.</li> |
| <img src="./assets/images/sim_closed_boundary.png" width="100%"> | <img src="./assets/images/sim_open_field.png" width="100%"> |
| **[Data] Static Zone**<br><br><li>BIM Wall Attribute = **`Structural`** (Fixed)</li><li>Since Room boundaries are permanently fixed, the data model flexibility during the operation phase is low.</li> | **[Data] Dynamic Layer**<br><br><li>BIM Wall Attribute = **`Architectural`** (Variable)</li><li>Sensor data is mapped to invariant **Columns (Anchors)**, and wall information is editable at any time.</li> |
| <img src="./assets/images/data_static_zone.png" width="100%"> | <img src="./assets/images/data_dynamic_grid.png" width="100%"> |
| 💡 **Insight**<br>Minimum Modeling Unit: **Fixed Room** | 💡 **Insight**<br>Minimum Modeling Unit: **Coordinate Grid** |
| <div align="center"><br><h3>🔻 Summary: Wall</h3></div> | <div align="center"><br><h3>Summary: Rahmen 🔻</h3></div> |
| <div align="center"><b>[Constraint]</b><br>Linear Constraint</div> | <div align="center"><b>[Constraint]</b><br>Point Constraint</div> |
| <div align="center"><b>[BIM Hierarchy]</b><br>Wall = Structure (Immutable)</div> | <div align="center"><b>[BIM Hierarchy]</b><br>Wall = Architecture (Mutable)</div> |
| <div align="center"><b>[Energy Sim]</b><br>Thermal Bridge Mgmt</div> | <div align="center"><b>[Energy Sim]</b><br>Envelope (Skin) Performance</div> |
| <div align="center"><b>[Airflow Sim]</b><br>Compartment (Partitioned)</div> | <div align="center"><b>[Airflow Sim]</b><br>Open Field (Open Plan)</div> |

<br>

### Conclusion

Understanding the building's structural form is akin to understanding the **shape of the vessel that holds the data**. When building performance analysis models and digital twins, ensure that the **Data Hierarchy** is correctly set according to the target building's structural system.