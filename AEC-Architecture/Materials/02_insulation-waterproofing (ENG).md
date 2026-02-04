# 🛡️ Performance Materials

> **Document Info**
> * **Category:** Architecture / Performance Layer
> * **Target System:** Energy Simulation (EnergyPlus), Facility Management (FM)
> * **Last Updated:** 2026-02-02
> * **Keywords:** `Thermal Conductivity`, `Insulation`, `Waterproofing`, `Risk Management`

---

<div align="center">

# 02. Data Definition of Performance Layer

### "Invisible but Critical: Core Variables for Energy & Maintenance"

</div>

---

<br>

## 1. Overview

This document serves as a data definition guide for the "Invisible" core layer hidden behind finishing materials, which determines the <strong>Physics Performance</strong> of the Digital Twin.

* **Insulation:** Resistance variable ($R$-Value) for energy analysis algorithms.
* **Waterproofing:** Target points for maintenance simulation and IoT sensor deployment.

<br>

---

## 2. Insulation: Energy Variables

Insulation must be defined not merely as geometry (thickness), but as an object possessing the <strong>Thermal Conductivity ($k$)</strong> property.

### 2.1 Physics Parameter Definition
For Energy Simulation (e.g., EnergyPlus), the following formula applies:

$$\huge U = \frac{1}{\sum (d_i / k_i) + R_s}$$

* **$k$ (Thermal Conductivity, W/mK):** The material's inherent heat transfer coefficient. (<strong>Lower is Better.</strong> 📉)
* **$d$ (Thickness, m):** Modeled thickness.
* **$U$ (U-Value):** The resulting thermal transmittance of the assembly.

### 2.2 Material Database (LOD 300 Specification)

#### Type A: PF Board (Phenolic Foam)
<div align="center">
  <img src="./asstes/images/insulation_pf_board.png" width="70%" alt="PF Board">
</div>

* **Property ($k$):** <strong>0.020 W/mK</strong> (<strong>Highest Performance.</strong>)
* **Features:**
    * Can meet legal insulation standards with a thin profile.
    * <strong>Sim Note:</strong> Vulnerable to moisture; consider applying a 'Performance Decay' coefficient if set in areas directly exposed to external air.

#### Type B: Rigid Polyurethane
<div align="center">
  <img src="./asstes/images/insulation_rigid_polyurethane.png" width="70%" alt="Rigid Polyurethane">
</div>

* **Property ($k$):** <strong>0.023 W/mK</strong> (<strong>High Performance.</strong>)
* **Features:**
    * Excellent <strong>Airtightness</strong> when spray-applied.
    * <strong>Sim Note:</strong> Lowest probability of <strong>Thermal Bridge</strong> occurrence due to gap-free application.

#### Type C: EPS (Expanded Polystyrene)
<div align="center">
  <img src="./asstes/images/insulation_eps.png" width="70%" alt="EPS">
</div>

* **Property ($k$):** <strong>0.034 W/mK</strong> (<strong>Standard Performance</strong>)
* **Features:**
    * Graphite-enhanced (Type 2, Grey) offers better thermal performance than standard White (Type 1).
    * <strong>Sim Note:</strong> Requires application of an <strong>Aging</strong> variable for long-term usage analysis.

#### Type D: Glass Wool
<div align="center">
  <img src="./asstes/images/insulation_glass_wool.png" width="70%" alt="Glass Wool">
</div>

* **Property ($k$):** <strong>0.038 W/mK</strong> (<strong>Fire Resistant/Acoustic</strong>)
* **Features:**
    * Made of fiberglass; <strong>Non-combustible (Fire Safety).</strong>
    * <strong>Sim Note:</strong> Can be used for acoustic simulation by mapping <strong>NRC (Noise Reduction Coefficient)</strong> data in addition to thermal properties.

<br>

---

## 3. Waterproofing: Risk Data

The Waterproofing layer is classified as <strong>Risk Management Data</strong> from an LCA (Life Cycle Assessment) perspective.

### 3.1 Method & Risk Factor

| Method | Type | Pros | Risk Factor (Simulation Variable) |
|:---:|:---|:---|:---|
| <strong>Liquid Applied</strong><br>(Urethane) | Applied as liquid, then cured | No Joints<br>Suitable for complex shapes | <strong>Thickness Uniformity</strong><br>👉 Data calibration required based on workmanship/skill level |
| <strong>Sheet Membrane</strong><br>(Asphalt/Rubber) | Pre-manufactured sheet attachment | Uniform thickness<br>Predictable quality | <strong>Joint Length</strong><br>👉 Overlap joints account for 90% of leaks<br>👉 Maintenance Risk Formula: $Risk \propto Length_{joint}$ |

### 3.2 Critical Points (IoT Sensor Hotspots)

Priority <strong>Coordinates</strong> for placing <strong>Leakage Sensors</strong> in the Digital Twin control system.

1.  <strong>Drain Area</strong> `Priority: High`
    * <strong>Reason:</strong> Gaps occur due to differences in thermal expansion/contraction coefficients at the junction of heterogeneous materials (Concrete-Pipe).
2.  <strong>Parapet Corner</strong> `Priority: Medium`
    * <strong>Reason:</strong> High concentration of <strong>Cracks</strong> due to differences in structural behavior between the roof railing and the floor.
3.  <strong>Pipe Penetration</strong> `Priority: High`
    * <strong>Reason:</strong> Risk of waterproofing layer rupture caused by pipe <strong>Vibration</strong>.

<br>

---

> **Engineer's Note**
> * <strong>Insulation</strong> is a continuous <strong>Float</strong> value. ($k \downarrow = Efficiency \uparrow$)
> * <strong>Waterproofing</strong> functions as a <strong>Boolean</strong> state (Leak: True/False), but the failure probability correlates with <strong>Joint Complexity</strong>.