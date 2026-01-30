# 03 Material Properties & Simulation Response

### 철근콘크리트(RC)와 철골(Steel): 열적 거동과 설비 통합의 차이

---

구조 재료(Material)의 선택은 단순한 시공 방식을 넘어, **건물의 생체 리듬(Bio-rhythm)**을 결정합니다.

본 챕터에서는 가장 대표적인 두 구조 시스템의 **물리적 성격**을 정의하고, 이를 바탕으로 **에너지 시뮬레이션**과 **MEP(설비) 통합** 관점에서의 차이를 분석합니다.

<br>

## 1. 구조적 개념 (Structural Concept)
**일체식 습식 구조 vs 조립식 건식 구조**

<div align="center">
  <img src="./assets/images/material_concept_compare.png" width="60%">
</div>
<br><br>

<div align="center">

| 구분 | **철근콘크리트 (RC)** | **철골 (Steel Structure)** |
| :--- | :--- | :--- |
| **구성 원리** | **Composite (복합재)**<br>콘크리트(압축) + 철근(인장) | **Homogeneous (단일재)**<br>고강도 강재(H-Beam 등) |
| **시공 방식** | **Wet Process (습식)**<br>현장에서 거푸집에 타설 및 양생 | **Dry Process (건식)**<br>공장에서 제작 후 현장 조립(볼트/용접) |
| **물리적 특징** | **Massive & Continuous**<br>두껍고 육중하며, 부재가 연속됨 | **Slender & Discrete**<br>얇고 길며, 부재가 독립적임 |

</div>

> **Insight**
>
> * **RC**: 현장에서 부어 만드는 **'덩어리(Mass)'** → 열을 많이 머금음
> * **Steel**: 뼈대를 맞추는 **'프레임(Frame)'** → 열에 민감하고 공간이 빔

<br>
<br>

---

<br>

## 2. 열역학적 반응 (Thermodynamic Response)
**Time Lag(지연) vs Quick Response(민감)**

<div align="center">
  <img src="./assets/images/material_thermal_response.png" width="60%">
</div>
<br>

건물의 '무게(Mass)'는 열을 다루는 방식에 결정적인 차이를 만듭니다.

> **RC (Concrete)**: `Heavy Mass`
> 콘크리트의 육중한 축열 성능은 외기 온도의 급격한 변화를 흡수하여 **피크 부하를 뒤로 미루는(Time Lag)** 역할을 합니다.

> **Steel**: `Light Mass`
> 열용량이 작아 외기 부하가 실내로 즉각 전달됩니다. 따라서 단열 성능과 **기계 설비의 민첩한 제어**가 필수적입니다.

| 구분 | **철근콘크리트 (RC)** | **철골 (Steel)** |
| :--- | :--- | :--- |
| **반응 속도** | **Slow (완충)** | **Fast (민감)** |
| **시뮬레이션** | 축열 효과로 인한 부하 이연 | 외피 단열 성능(U-value) 의존 |
| **운영 전략** | 예열/예냉 스케줄링 | 실시간 고효율 제어 |

<br>
<br>

---

<br>

## 3. 설비 통합과 공간 (MEP Integration)
**매립형 제약(Constraints) vs 오픈형 자유(Flexibility)**

<div align="center">
  <img src="./assets/images/material_mep_integration.png" width="60%">
</div>
<br>

구조체의 형상은 HVAC 설비가 지나갈 **'물리적 길(Routing Path)'**을 결정합니다.

* **RC 구조**: 보(Beam)가 두꺼워 배관 관통이 어렵습니다. 시공 전 **슬리브(Sleeve)** 계획이 없으면 수정이 불가능합니다.
* **철골 구조**: 긴 스팬(Long Span)과 얇은 부재 덕분에 설비 공간 확보가 용이하며, **대공간 기류 해석(CFD)**에 유리합니다.

| 구분 | **철근콘크리트 (RC)** | **철골 (Steel)** |
| :--- | :--- | :--- |
| **공간 활용** | **Low Flexibility** | **High Flexibility** |
| **MEP 경로** | 슬리브 사전 계획 필수 | 오픈 웹/덕트 관통 용이 |
| **CFD 관점** | 천장고 확보 제약 가능성 | 대공간/자연환기 설계 유리 |

<br>
<br>

---

### Conclusion: Simulation Strategy

재료의 특성에 따라 시뮬레이션의 **시간축(Time Step)**과 **공간축(Space)** 설정을 달리해야 합니다.

<div align="center">

| **Keyword** | **System** | **Action Item** |
| :---: | :---: | :--- |
| **안정성** | `RC Structure` | **축열(Thermal Mass)**을 고려한 예열/예냉 운전 최적화 |
| **민첩성** | `Steel Structure` | **설비 공간(Void)**을 활용한 고성능 공조 및 제어 로직 적용 |

</div>