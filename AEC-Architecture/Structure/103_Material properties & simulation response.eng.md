# 🏗️ Material Properties & Simulation Response

> **Document Info**
> * **Category:** Architecture / Structural System
> * **Target System:** Energy Simulation, HVAC Control, MEP Routing, CFD
> * **Last Updated:** 2026-02-02
> * **Keywords:** `RC vs Steel`, `Thermal Mass`, `Time Lag`, `MEP Integration`

---

<div align="center">

# 03 Material Properties & Simulation Response

### RC vs. Steel: Differences in Thermal Behavior and MEP Integration

</div>

---

<br>

The choice of structural material goes beyond simple construction methods; it determines the **Bio-rhythm of the building**.

This chapter defines the **physical characteristics** of the two most representative structural systems and analyzes their differences from the perspectives of **Energy Simulation** and **MEP (Mechanical, Electrical, Plumbing) Integration**.

<br>

## 1. Structural Concept
**Monolithic Wet Construction vs. Prefabricated Dry Construction**

<div align="center">
  <img src="./assets/images/material_concept_compare.png" width="60%" alt="Material Concept Comparison">
</div>
<br><br>

<div align="center">

| Category | **Reinforced Concrete (RC)** | **Steel Structure** |
| :--- | :--- | :--- |
| **Composition** | **Composite**<br>Concrete (Compression) + Rebar (Tension) | **Homogeneous**<br>High-strength Steel (H-Beam, etc.) |
| **Construction** | **Wet Process**<br>On-site casting into forms & Curing | **Dry Process**<br>Factory fabrication & On-site assembly (Bolt/Weld) |
| **Physical Feature** | **Massive & Continuous**<br>Thick, heavy, and continuous members | **Slender & Discrete**<br>Thin, long, and independent members |

</div>

> **Insight**
>
> * **RC**: A **'Mass'** created on-site → Retains a significant amount of heat.
> * **Steel**: A **'Frame'** assembled from parts → Sensitive to heat, contains void spaces.

<br>
<br>

---

<br>

## 2. Thermodynamic Response
**Time Lag vs. Quick Response**

<div align="center">
  <img src="./assets/images/material_thermal_response.png" width="60%" alt="Thermal Response Diagram">
</div>
<br>

The building's 'Mass' makes a decisive difference in how it handles heat.

> **RC (Concrete)**: `Heavy Mass`
> Concrete's massive thermal storage capacity absorbs rapid changes in outdoor temperature, playing a role in **delaying peak loads (Time Lag)**.

> **Steel**: `Light Mass`
> Low heat capacity causes outdoor loads to transfer immediately to the indoors. Therefore, insulation performance and **agile control of mechanical systems** are essential.

| Category | **Reinforced Concrete (RC)** | **Steel Structure** |
| :--- | :--- | :--- |
| **Response Speed** | **Slow (Buffer)** | **Fast (Sensitive)** |
| **Simulation** | Load shifting via Thermal Mass effect | Dependence on Envelope Insulation (U-value) |
| **Operation Strategy** | Pre-heating/Pre-cooling Scheduling | Real-time High-efficiency Control |

<br>
<br>

---

<br>

## 3. MEP Integration
**Embedded Constraints vs. Open Flexibility**

<div align="center">
  <img src="./assets/images/material_mep_integration.png" width="60%" alt="MEP Integration Diagram">
</div>
<br>

The shape of the structure determines the **'Physical Routing Path'** for HVAC systems.

* **RC Structure**: Thick beams make pipe penetration difficult. Without **Sleeve Planning** prior to construction, modifications are impossible.
* **Steel Structure**: Long spans and thin members make space allocation easy. It is advantageous for **Computational Fluid Dynamics (CFD)** analysis in large spaces.

| Category | **Reinforced Concrete (RC)** | **Steel Structure** |
| :--- | :--- | :--- |
| **Space Flexibility** | **Low Flexibility** | **High Flexibility** |
| **MEP Routing** | Pre-planned Sleeves Essential | Open Web / Duct Penetration Easy |
| **CFD Aspect** | Potential Ceiling Height Constraints | Good for Large Space/Natural Ventilation |

<br>
<br>

---

### Conclusion: Simulation Strategy

Depending on the material properties, the **Time Step** and **Space** settings in the simulation must be adjusted.

<div align="center">

| **Keyword** | **System** | **Action Item** |
| :---: | :---: | :--- |
| **Stability** | `RC Structure` | Optimize operation using **Thermal Mass** (Pre-heating/Cooling) |
| **Agility** | `Steel Structure` | Apply high-performance control logic utilizing **Void Space** |

</div>