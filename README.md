# AEC Domain Archive: Engineering Foundations for Digital Twins

**A Centralized Repository of Core AEC Documentation and Field Insights for Digital Synchronization.**

<p align="left">
  <img src="https://img.shields.io/badge/Domains-6-1f6feb" alt="6 Domains">
  <img src="https://img.shields.io/badge/Topics-29-2ea043" alt="29 Topics">
  <img src="https://img.shields.io/badge/Docs-58%20(KO%2BEN)-2ea043" alt="58 documents, Korean + English">
  <img src="https://img.shields.io/badge/Languages-KO%20%2B%20EN-8957e5" alt="Korean + English">
  <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey" alt="CC BY-NC-SA 4.0">
</p>

---

## 🏗️ Abstract

`AEC-Fundamentals`는 물리적 건축 자산의 디지털 전환을 지원하기 위해 **AEC(Architecture, Engineering, Construction) 전 영역의 핵심 지식을 체계적으로 구조화한 도메인 아카이브**입니다. 본 저장소는 파편화된 건축 법규, 구조 역학, 시공 프로세스 및 설비 계통의 실무 지식을 엔지니어링 관점에서 재정리하여, 디지털 트윈 구축을 위한 필수 데이터 리소스 허브 역할을 수행합니다.

`AEC-Fundamentals` is a **centralized AEC domain archive** that systematizes core knowledge across the architecture, engineering, and construction lifecycles. By consolidating fragmented insights—from regulatory constraints and structural mechanics to field-proven construction processes—this repository serves as a technical resource hub for building high-fidelity digital twins.

> 모든 **지식 문서**(29개 주제 · 58개 파일)는 한국어(`.kor.md`)와 영어(`.eng.md`)로 병기됩니다. `docs/`의 거버넌스·감사 문서는 예외입니다.
> Every **knowledge document** (29 topics · 58 files) is provided in both Korean (`.kor.md`) and English (`.eng.md`). Governance/audit docs under `docs/` are the exception.

---

## 🎯 Strategic Objectives

* **Knowledge Assetization:** 파편화된 건축 실무 지식의 체계적 자산화 및 공유
* **Technical Grounding:** 디지털 트윈 모델의 현실 정합성을 뒷받침하는 기술적 근거 제공
* **Cross-Domain Collaboration:** 건축 도메인과 소프트웨어 엔지니어링 간의 원활한 협업을 위한 표준 가이드라인 구축
* **Practical Reference:** 현장 용어 및 실무 프로세스에 기반한 실전 엔지니어링 리소스 제공

---

## 🏛️ Technical Pillars

| Phase | Technical Domain | Key Focus Areas |
| :--- | :--- | :--- |
| **01** | **Structural Logic & Regulation** | 하중 흐름, 구조 시스템(RC/Steel), 법적 매스 규제 및 사선제한 |
| **02** | **Spatial Planning & Materials** | 동선 및 공간 위계, 재료별 열관류율 및 물성 데이터, 단열/방수 공법 |
| **03** | **Construction Lifecycle** | 현장 실무 용어, 기초/골조 공정, 시공 오차 관리 및 하자 분석 |
| **04** | **System Integration (MEP)** | HVAC 계통도, 전력 계통 및 통신 네트워크, CFD/에너지 해석 모델 연계 |

---

## 🗂️ Documentation Index · 문서 인덱스

> 각 문서는 한국어(KO)와 영어(EN) 버전으로 연결됩니다. · Each entry links to its Korean (KO) and English (EN) version.

### `01` · Structural Logic & Regulation · 구조 논리와 법규

<details open>
<summary><b>구조 · Structure</b></summary>

| 문서 · Document | 언어 · Lang |
| :--- | :---: |
| 하중의 종류와 흐름 <br> <sub>Load Flow & System</sub> | [KO](AEC-Architecture/Structure/101_Load%20flow%20and%20system.kor.md) · [EN](AEC-Architecture/Structure/101_Load%20flow%20and%20system.eng.md) |
| 구조 시스템과 데이터 토폴로지 <br> <sub>Structural System &amp; Data Topology</sub> | [KO](AEC-Architecture/Structure/102_Structural%20system%20%26%20data%20topology.kor.md) · [EN](AEC-Architecture/Structure/102_Structural%20system%20%26%20data%20topology.eng.md) |
| 재료 물성과 시뮬레이션 응답 <br> <sub>Material Properties &amp; Simulation Response</sub> | [KO](AEC-Architecture/Structure/103_Material%20properties%20%26%20simulation%20response.kor.md) · [EN](AEC-Architecture/Structure/103_Material%20properties%20%26%20simulation%20response.eng.md) |

</details>

<details open>
<summary><b>법규 · Regulation</b></summary>

| 문서 · Document | 언어 · Lang |
| :--- | :---: |
| 건축 법규는 왜 필요한가? <br> <sub>Why So Many Regulations?</sub> | [KO](AEC-Architecture/Regulation/101_Why%20do%20we%20need%20so%20many%20regulations%20in%20architecture%EF%BC%9F.kor.md) · [EN](AEC-Architecture/Regulation/101_Why%20do%20we%20need%20so%20many%20regulations%20in%20architecture%EF%BC%9F.eng.md) |
| 건축 법규의 전체 구조 <br> <sub>Structure of Building Regulation</sub> | [KO](AEC-Architecture/Regulation/102_A%20glance%20at%20the%20entire%20structure%20of%20building%20regulation.kor.md) · [EN](AEC-Architecture/Regulation/102_A%20glance%20at%20the%20entire%20structure%20of%20building%20regulation.eng.md) |
| 건축법 5대 핵심 개념 <br> <sub>Five Key Concepts in Building Code</sub> | [KO](AEC-Architecture/Regulation/103_Five%20key%20concepts%20covered%20in%20building%20code.kor.md) · [EN](AEC-Architecture/Regulation/103_Five%20key%20concepts%20covered%20in%20building%20code.eng.md) |
| 용도지역·지구·구역 <br> <sub>Use Zones, Districts &amp; Areas</sub> | [KO](AEC-Architecture/Regulation/104_Use%20zones%2C%20districts%2C%20and%20areas%2C%20why%20are%20they%20so%20complicated%EF%BC%9F.kor.md) · [EN](AEC-Architecture/Regulation/104_Use%20zones%2C%20districts%2C%20and%20areas%2C%20why%20are%20they%20so%20complicated%EF%BC%9F.eng.md) |
| 건축 인허가 절차 <br> <sub>The Building Permit Process</sub> | [KO](AEC-Architecture/Regulation/105_The%20building%20permit%20process%20actually%20goes%20like%20this.kor.md) · [EN](AEC-Architecture/Regulation/105_The%20building%20permit%20process%20actually%20goes%20like%20this.eng.md) |

</details>

### `02` · Spatial Planning & Materials · 공간 계획과 재료

<details open>
<summary><b>계획 · Planning</b></summary>

| 문서 · Document | 언어 · Lang |
| :--- | :---: |
| 건축계획이란? <br> <sub>What Is Architectural Planning?</sub> | [KO](AEC-Architecture/Planning/101_Introduction.kor.md) · [EN](AEC-Architecture/Planning/101_Introduction.eng.md) |
| 건축 도면 읽기 <br> <sub>Architectural Drawings</sub> | [KO](AEC-Architecture/Planning/102_Plan%20reading.kor.md) · [EN](AEC-Architecture/Planning/102_Plan%20reading.eng.md) |
| 용도별 계획 <br> <sub>Program-Specific Planning</sub> | [KO](AEC-Architecture/Planning/103_Special%20part.kor.md) · [EN](AEC-Architecture/Planning/103_Special%20part.eng.md) |
| 공간의 기본 단위 <br> <sub>Basic Unit of Space</sub> | [KO](AEC-Architecture/Planning/201_Basic%20unit%20of%20space.kor.md) · [EN](AEC-Architecture/Planning/201_Basic%20unit%20of%20space.eng.md) |
| 평면도 읽는 개념 <br> <sub>Reading the Floor Plan</sub> | [KO](AEC-Architecture/Planning/202_At%20least%20a%20concept%20of%20seeing%20the%20floor%20plan.kor.md) · [EN](AEC-Architecture/Planning/202_At%20least%20a%20concept%20of%20seeing%20the%20floor%20plan.eng.md) |
| 동선 계획 <br> <sub>Circulation Plan</sub> | [KO](AEC-Architecture/Planning/203_Circulation%20plan.kor.md) · [EN](AEC-Architecture/Planning/203_Circulation%20plan.eng.md) |

</details>

<details open>
<summary><b>재료 · Materials</b></summary>

| 문서 · Document | 언어 · Lang |
| :--- | :---: |
| 구조 재료 <br> <sub>Structural Materials</sub> | [KO](AEC-Architecture/Materials/101_Structural%20materials.kor.md) · [EN](AEC-Architecture/Materials/101_Structural%20materials.eng.md) |
| 성능 재료 (단열·방수) <br> <sub>Performance Materials (Insulation &amp; Waterproofing)</sub> | [KO](AEC-Architecture/Materials/102_Insulation%20waterproofing.kor.md) · [EN](AEC-Architecture/Materials/102_Insulation%20waterproofing.eng.md) |
| 마감 재료 <br> <sub>Finishing Materials</sub> | [KO](AEC-Architecture/Materials/103_Finishing%20materials.kor.md) · [EN](AEC-Architecture/Materials/103_Finishing%20materials.eng.md) |

</details>

### `03` · Construction Lifecycle · 시공 생애주기

<details open>
<summary><b>시공 · Construction</b></summary>

| 문서 · Document | 언어 · Lang |
| :--- | :---: |
| 건축이란? (용어와 역사) <br> <sub>Construction Terms &amp; History</sub> | [KO](AEC-Architecture/Construction/101_Construction%20terms%20and%20history.kor.md) · [EN](AEC-Architecture/Construction/101_Construction%20terms%20and%20history.eng.md) |
| 건축 용어 <br> <sub>Architectural Terms</sub> | [KO](AEC-Architecture/Construction/201_Architectural%20Terms.kor.md) · [EN](AEC-Architecture/Construction/201_Architectural%20Terms.eng.md) |
| 기초공사란? <br> <sub>What Is Foundation Work?</sub> | [KO](AEC-Architecture/Construction/202_What%20is%20foundation%20work.kor.md) · [EN](AEC-Architecture/Construction/202_What%20is%20foundation%20work.eng.md) |
| 골조공사란? <br> <sub>Structural Framework Construction</sub> | [KO](AEC-Architecture/Construction/203_Structure%20frame%20work.kor.md) · [EN](AEC-Architecture/Construction/203_Structure%20frame%20work.eng.md) |
| 건축시공과 계약 체계 <br> <sub>Construction Contract System</sub> | [KO](AEC-Architecture/Construction/301_Construction%20contract%20system.kor.md) · [EN](AEC-Architecture/Construction/301_Construction%20contract%20system.eng.md) |
| 건축 공사의 흐름 <br> <sub>Flow of Building Construction</sub> | [KO](AEC-Architecture/Construction/302_Structural%20construction%20flow.kor.md) · [EN](AEC-Architecture/Construction/302_Structural%20construction%20flow.eng.md) |
| 마감 공정 로직 <br> <sub>Finishing Process Logic</sub> | [KO](AEC-Architecture/Construction/401_finishing-process-logic.kor.md) · [EN](AEC-Architecture/Construction/401_finishing-process-logic.eng.md) |

</details>

### `04` · System Integration (MEP) · 설비 통합

<details open>
<summary><b>설비 · MEP</b></summary>

| 문서 · Document | 언어 · Lang |
| :--- | :---: |
| 전기·소방·가스 설비 <br> <sub>Electrical, Fire Safety &amp; Gas Systems</sub> | [KO](AEC-Architecture/MEP/03_electrical-fire.kor.md) · [EN](AEC-Architecture/MEP/03_electrical-fire.eng.md) |
| 배관 및 위생 설비 <br> <sub>Plumbing &amp; Sanitation System</sub> | [KO](AEC-Architecture/MEP/101_Plumbing%20and%20Sanitation%20System.kor.md) · [EN](AEC-Architecture/MEP/101_Plumbing%20and%20Sanitation%20System.eng.md) |
| 급기 덕트 설비 <br> <sub>Supply Air Duct System</sub> | [KO](AEC-Architecture/MEP/102_Supply%20Air%20Duct%20System.kor.md) · [EN](AEC-Architecture/MEP/102_Supply%20Air%20Duct%20System.eng.md) |
| 실내 공기질 <br> <sub>Indoor Air Quality</sub> | [KO](AEC-Architecture/MEP/103_Indoor%20air%20quality.kor.md) · [EN](AEC-Architecture/MEP/103_Indoor%20air%20quality.eng.md) |
| 열부하와 실내 공기 <br> <sub>Thermal Loads &amp; Indoor Air</sub> | [KO](AEC-Architecture/MEP/201_Thermal%20loads%20and%20indoor%20air.kor.md) · [EN](AEC-Architecture/MEP/201_Thermal%20loads%20and%20indoor%20air.eng.md) |

</details>

---

## 🧰 Project & Governance Docs

* **Asset audit** — [IMAGE-AUDIT.md](docs/asset-audit/IMAGE-AUDIT.md) · [rights CLEARANCE triage](docs/asset-audit/CLEARANCE.md) · [image-manifest.csv](docs/asset-audit/image-manifest.csv)
* **Proposals (DRAFT)** — [RFC-001: openBIM conformance corpus](docs/proposals/RFC-001-conformance-corpus.md) · [Licensing recommendation](docs/proposals/LICENSING.md) · [license scaffold](docs/proposals/licensing-scaffold/README.md) · discussion in [Issue #7](https://github.com/MosslandOpenDevs/AEC-Fundamentals/issues/7)
* **Conformance PoC (DRAFT)** — [AECF-HVAC-Handover-0.1](validator/README.md): a real IFC 4.3 + IDS 1.0 pass/fail corpus validated in CI (`mvp0-conformance`)

> ⚠️ **신뢰성 안내 / Reliability note:** 일부 문서(`MEP/103`, `Structure/102`, `Construction/301`)는 법정 수치·규칙이 아직 1차 출처로 검증되지 않았습니다. 규정 준수나 모델 학습 근거로 사용하기 전 각 문서 상단의 상태 배너를 확인하세요. — Some documents are not yet source-verified; check the status banner at the top of each before relying on them for compliance or model training.

---

## 🧬 Engineering Rationale

본 아카이브는 디지털 트윈의 **데이터 신뢰성** 확보를 목적으로 합니다.

* **Contextual Accuracy:** 설계 도면을 넘어 실제 시공 프로세스와 법적 제약을 이해할 때 비로소 가치 있는 디지털 모델이 완성됩니다.
* **Informed Simulation:** 재료와 설비의 물리적 메커니즘을 정의하여 시뮬레이션의 예측 정확도를 상향 평준화합니다.
* **Domain Bridging:** BIM(Revit), gbXML 등 표준 포맷의 기반이 되는 건축 논리를 엔지니어링 관점에서 해석합니다.

---

## 👥 Contributors

This archive is developed and maintained by **Mossland**.

---

## 📄 License

Copyright © 2026 **Mossland**.  
This project is licensed under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

> ⚠️ **This blanket license covers Mossland-authored text only.** It does **not** apply to third-party or unverified images (photos, real project drawings, partner/AETHRION assets — see [rights CLEARANCE](docs/asset-audit/CLEARANCE.md)), which retain their own rights and are **0/171 cleared**. A per-content-type license split is proposed but not adopted ([Issue #7](https://github.com/MosslandOpenDevs/AEC-Fundamentals/issues/7)).

<p align="left">
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
    <img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg" alt="CC BY-NC-SA 4.0" height="40">
  </a>
</p>
