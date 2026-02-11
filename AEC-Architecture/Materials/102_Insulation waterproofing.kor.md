# 🛡️ Performance Materials (성능 재료)

> <strong>Document Info</strong>
> * <strong>분류 (Category):</strong> 건축 / 성능 레이어 (Architecture / Performance Layer)
> * <strong>타겟 시스템 (Target System):</strong> 에너지 시뮬레이션 (EnergyPlus), 시설 관리 (FM)
> * <strong>최종 업데이트 (Last Updated):</strong> 2026-02-02
> * <strong>핵심 키워드 (Keywords):</strong> `열전도율(Thermal Conductivity)`, `단열재(Insulation)`, `방수재(Waterproofing)`, `리스크 관리(Risk Management)`

---

<div align="center">

# 02. 성능 재료의 데이터 정의 (Performance Layer)

### "Invisible but Critical: 에너지와 유지보수의 핵심 변수"

</div>

---

<br>

## 1. Overview

이 문서는 마감재 뒤에 숨겨져 보이지 않지만(Invisible), 디지털 트윈의 <strong>물리적 성능(Physics Performance)</strong>을 결정짓는 핵심 레이어에 대한 데이터 정의서입니다.

* <strong>단열재 (Insulation):</strong> 에너지 해석 알고리즘의 저항값($R$-Value) 변수
* <strong>방수재 (Waterproofing):</strong> 유지보수 시뮬레이션 및 IoT 센서 배치의 타겟 포인트

<br>

---

## 2. Insulation (단열재): Energy Variables

단열재는 단순한 두께(Geometry)가 아닌, <strong>열전도율(Thermal Conductivity, $k$)</strong> 속성을 가진 객체로 정의되어야 합니다.

### 2.1 Physics Parameter Definition
에너지 시뮬레이션(EnergyPlus) 입력 시 다음 공식을 따릅니다.

$$\huge U = \frac{1}{\sum (d_i / k_i) + R_s}$$

* <strong>$k$ (Thermal Conductivity, W/mK):</strong> 재료 고유의 열 전달 계수. (<strong>낮을수록 우수함.</strong> 📉)
* <strong>$d$ (Thickness, m):</strong> 모델링 두께.
* <strong>$U$ (U-Value):</strong> 최종 열관류율.

### 2.2 Material Database (LOD 300 Specification)

#### Type A: PF Board (페놀폼)
<div align="center">
  <img src="./assets/images/insulation_pf_board.png" width="70%" alt="PF Board">
</div>

* <strong>Property ($k$):</strong> <strong>0.020 W/mK</strong> (<strong>최고 성능.</strong>)
* <strong>Features:</strong>
    * 얇은 두께로 법적 단열 기준 충족 가능.
    * <strong>Sim Note:</strong> 습기에 취약하므로 외기 직접 노출 부위 설정 시 Performance Decay(성능 저하) 계수 적용 고려.

#### Type B: Rigid Polyurethane (경질 우레탄폼)
<div align="center">
  <img src="./assets/images/insulation_rigid_polyurethane.png" width="70%" alt="Rigid Polyurethane">
</div>

* <strong>Property ($k$):</strong> <strong>0.023 W/mK</strong> (<strong>고성능.</strong>)
* <strong>Features:</strong>
    * 스프레이 발포 시공 시 기밀성(Airtightness) 우수.
    * <strong>Sim Note:</strong> 틈새가 없어 열교(Thermal Bridge) 발생 확률이 가장 낮음.

#### Type C: EPS (비드법 보온판 / 스티로폼)
<div align="center">
  <img src="./assets/images/insulation_eps.png" width="70%" alt="EPS">
</div>

* <strong>Property ($k$):</strong> <strong>0.034 W/mK</strong> (<strong>일반 성능</strong>)
* <strong>Features:</strong>
    * 백색(1종)보다 흑연을 함유한 회색(2종)이 단열 성능 우수.
    * <strong>Sim Note:</strong> 장기 사용 시 경년 변화(Aging) 변수 적용 필요.

#### Type D: Glass Wool (그라스울)
<div align="center">
  <img src="./assets/images/insulation_glass_wool.png" width="70%" alt="Glass Wool">
</div>

* <strong>Property ($k$):</strong> <strong>0.038 W/mK</strong> (<strong>내화/흡음</strong>)
* <strong>Features:</strong>
    * 유리섬유 재질로 <strong>불연(Fire Safety).</strong>
    * <strong>Sim Note:</strong> 단열 성능 외에 <strong>흡음 계수(NRC)</strong> 데이터 매핑 시 음향 시뮬레이션 활용 가능.

<br>

---

## 3. Waterproofing (방수재): Risk Data

방수 레이어는 LCA(Life Cycle Assessment) 관점에서 <strong>리스크 관리 데이터(Risk Management Data)</strong>로 분류됩니다.

### 3.1 Method & Risk Factor

| Method | Type | Pros | Risk Factor (Simulation Variable) |
|:---:|:---|:---|:---|
| <strong>우레탄 도막</strong><br>(Liquid Applied) | 액체 도포 후 경화 | 이음매(Joint) 없음<br>복잡한 형상에 적합 | <strong>Thickness Uniformity (두께 균일성)</strong><br>👉 시공 숙련도에 따른 편차 데이터 보정 필요 |
| <strong>시트 방수</strong><br>(Sheet Membrane) | 공장 제조 시트 부착 | 두께 일정<br>품질 예측 용이 | <strong>Joint Length (조인트 길이)</strong><br>👉 시트 간 겹침 부위가 누수 원인의 90%<br>👉 유지보수 리스크 산출 공식: $Risk \propto Length_{joint}$ |

### 3.2 Critical Points (IoT Sensor Hotspots)

<strong>누수 감지 센서(Leakage Sensor)</strong>를 배치해야 하는 우선순위 <strong>좌표(Coordinate)</strong>입니다.

1.  <strong>Drain Area (드레인 주변)</strong> `Priority: High`
    * <strong>Reason:</strong> 이질재(콘크리트-배관) 접합부의 열수축팽창 계수 차이로 인한 틈새 발생.
2.  <strong>Parapet Corner (파라펫 코너)</strong> `Priority: Medium`
    * <strong>Reason:</strong> 옥상 난간과 바닥의 구조적 거동 차이에 의한 크랙(Crack) 집중 구간.
3.  <strong>Pipe Penetration (설비 관통부)</strong> `Priority: High`
    * <strong>Reason:</strong> 슬래브를 관통하는 파이프의 진동(Vibration)으로 방수층 파단 위험.

<br>

---

> <strong>Engineer's Note</strong>
> * <strong>단열재(Insulation)</strong>는 연속적인 <strong>실수(Float)</strong> 값입니다. ($k \downarrow = \text{효율} \uparrow$)
> * <strong>방수재(Waterproofing)</strong>는 <strong>이진(Boolean)</strong> 상태 (누수: True/False)로 정의되지만, 실패 확률은 <strong>접합부 복잡도(Joint Complexity)</strong>에 비례합니다.