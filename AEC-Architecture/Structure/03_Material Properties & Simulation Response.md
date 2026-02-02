---
title: "Digital Twin Material Guide: 03. Material Properties & Simulation Response"
date: 2026-02-02
category: Architecture / Structure
tags: [RC, Steel, Thermal Mass, MEP, Energy Simulation]
description: "철근콘크리트(RC)와 철골(Steel) 구조의 열적 거동 및 설비 통합 차이 분석"
---

# 🏗️ Material Properties & Simulation Response

> **Document Info**
> * **분류 (Category):** 건축 / 구조 시스템 (Architecture / Structural System)
> * **타겟 시스템 (Target System):** 에너지 시뮬레이션, HVAC 제어, MEP 라우팅, CFD
> * **최종 업데이트 (Last Updated):** 2026-02-02
> * **핵심 키워드 (Keywords):** `RC vs Steel`, `축열(Thermal Mass)`, `타임 랙(Time Lag)`, `MEP 통합(MEP Integration)`

---

<div align="center">

# 03 Material Properties & Simulation Response

### 철근콘크리트(RC)와 철골(Steel): 열적 거동과 설비 통합의 차이

</div>

---

<br>

구조 재료(Material)의 선택은 단순한 시공 방식을 넘어, <strong>건물의 생체 리듬(Bio-rhythm)</strong>을 결정합니다.

본 챕터에서는 가장 대표적인 두 구조 시스템의 <strong>물리적 성격</strong>을 정의하고, 이를 바탕으로 <strong>에너지 시뮬레이션</strong>과 <strong>MEP(설비) 통합</strong> 관점에서의 차이를 분석합니다.

<br>

## 1. 구조적 개념 (Structural Concept)
**일체식 습식 구조 vs 조립식 건식 구조**

<div align="center">
  <img src="./assets/images/material_concept_compare.png" width="60%" alt="구조 개념 비교">
</div>
<br><br>

<div align="center">

| 구분 | <strong>철근콘크리트 (RC)</strong> | <strong>철골 (Steel Structure)</strong> |
| :--- | :--- | :--- |
| <strong>구성 원리</strong> | <strong>Composite (복합재)</strong><br>콘크리트(압축) + 철근(인장) | <strong>Homogeneous (단일재)</strong><br>고강도 강재(H-Beam 등) |
| <strong>시공 방식</strong> | <strong>Wet Process (습식)</strong><br>현장에서 거푸집에 타설 및 양생 | <strong>Dry Process (건식)</strong><br>공장에서 제작 후 현장 조립(볼트/용접) |
| <strong>물리적 특징</strong> | <strong>Massive & Continuous</strong><br>두껍고 육중하며, 부재가 연속됨 | <strong>Slender & Discrete</strong><br>얇고 길며, 부재가 독립적임 |

</div>

> <strong>Insight</strong>
>
> * <strong>RC</strong>: 현장에서 부어 만드는 <strong>'덩어리(Mass)'</strong> → 열을 많이 머금음
> * <strong>Steel</strong>: 뼈대를 맞추는 <strong>'프레임(Frame)'</strong> → 열에 민감하고 공간이 빔

<br>
<br>

---

<br>

## 2. 열역학적 반응 (Thermodynamic Response)
**Time Lag(지연) vs Quick Response(민감)**

<div align="center">
  <img src="./assets/images/material_thermal_response.png" width="60%" alt="열역학적 반응 비교">
</div>
<br>

건물의 '무게(Mass)'는 열을 다루는 방식에 결정적인 차이를 만듭니다.

> <strong>RC (Concrete)</strong>: `Heavy Mass`
> 콘크리트의 육중한 축열 성능은 외기 온도의 급격한 변화를 흡수하여 <strong>피크 부하를 뒤로 미루는(Time Lag)</strong> 역할을 합니다.

> <strong>Steel</strong>: `Light Mass`
> 열용량이 작아 외기 부하가 실내로 즉각 전달됩니다. 따라서 단열 성능과 <strong>기계 설비의 민첩한 제어</strong>가 필수적입니다.

<div align="center">

| 구분 | <strong>철근콘크리트 (RC)</strong> | <strong>철골 (Steel)</strong> |
| :--- | :--- | :--- |
| <strong>반응 속도</strong> | <strong>Slow (완충)</strong> | <strong>Fast (민감)</strong> |
| <strong>시뮬레이션</strong> | 축열 효과로 인한 부하 이연 | 외피 단열 성능(U-value) 의존 |
| <strong>운영 전략</strong> | 예열/예냉 스케줄링 | 실시간 고효율 제어 |

</div>

<br>
<br>

---

<br>

## 3. 설비 통합과 공간 (MEP Integration)
**매립형 제약(Constraints) vs 오픈형 자유(Flexibility)**

<div align="center">
  <img src="./assets/images/material_mep_integration.png" width="60%" alt="설비 통합 비교">
</div>
<br>

구조체의 형상은 HVAC 설비가 지나갈 <strong>'물리적 길(Routing Path)'</strong>을 결정합니다.

* <strong>RC 구조</strong>: 보(Beam)가 두꺼워 배관 관통이 어렵습니다. 시공 전 <strong>슬리브(Sleeve)</strong> 계획이 없으면 수정이 불가능합니다.
* <strong>철골 구조</strong>: 긴 스팬(Long Span)과 얇은 부재 덕분에 설비 공간 확보가 용이하며, <strong>대공간 기류 해석(CFD)</strong>에 유리합니다.

<div align="center">

| 구분 | <strong>철근콘크리트 (RC)</strong> | <strong>철골 (Steel)</strong> |
| :--- | :--- | :--- |
| <strong>공간 활용</strong> | <strong>Low Flexibility</strong> | <strong>High Flexibility</strong> |
| <strong>MEP 경로</strong> | 슬리브 사전 계획 필수 | 오픈 웹/덕트 관통 용이 |
| <strong>CFD 관점</strong> | 천장고 확보 제약 가능성 | 대공간/자연환기 설계 유리 |

</div>

<br>
<br>

---

<div align="center">

### Conclusion: Simulation Strategy

<br>

재료의 특성에 따라 시뮬레이션의 <strong>시간축(Time Step)</strong>과 <strong>공간축(Space)</strong> 설정을 달리해야 합니다.

<br>

| <strong>Keyword</strong> | <strong>System</strong> | <strong>Action Item</strong> |
| :---: | :---: | :--- |
| <strong>안정성</strong> | `RC Structure` | <strong>축열(Thermal Mass)</strong>을 고려한 예열/예냉 운전 최적화 |
| <strong>민첩성</strong> | `Steel Structure` | <strong>설비 공간(Void)</strong>을 활용한 고성능 공조 및 제어 로직 적용 |

</div>