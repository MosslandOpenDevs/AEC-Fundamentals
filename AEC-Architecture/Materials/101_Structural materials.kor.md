# 🏗️ Structural Materials (구조 재료)

> <strong>Document Info</strong>
> * <strong>분류 (Category):</strong> 건축 / 구조 핵심 (Architecture / Structural Core)
> * <strong>타겟 시스템 (Target System):</strong> 구조 해석 (FEM), 물량 산출 (QTO), 물리 엔진 (Physics Engine)
> * <strong>최종 업데이트 (Last Updated):</strong> 2026-02-02
> * <strong>핵심 키워드 (Keywords):</strong> `콘크리트 위계(Concrete Hierarchy)`, `데이터 정합성(Data Integrity)`, `열용량(Thermal Mass)`, `LCA`

---

<div align="center">

# 01. 구조 재료의 데이터 계층 (Concrete Hierarchy)

### "Code as Material: 물리적 속성을 가진 데이터 객체"

</div>

---

<br>

디지털 트윈에서 건축 재료는 단순한 3D 텍스처가 아닙니다.

에너지 시뮬레이션의 <strong>경계 조건(Boundary Condition)</strong>이자, 탄소 배출량 알고리즘의 신뢰도를 결정하는 <strong>데이터 객체(Data Entity)</strong>입니다.

<br>

#### 1. 데이터 구성 로직 (Composition Logic)

이 3가지 재료는 별개의 물질이 아니라, <strong>상속(Inheritance)</strong> 관계를 가집니다. 데이터 스키마 설계 시 아래의 포함 관계를 이해해야 합니다.

<div align="center">

| Level 1 (Base) | Level 2 (Surface) | Level 3 (Core) |
| :--- | :--- | :--- |
| <strong>시멘트 페이스트</strong> | <strong>몰탈 (Mortar)</strong> | <strong>콘크리트 (Concrete)</strong> |
| `Water` + `Cement` | `Paste` + `Sand` (잔골재) | `Mortar` + `Gravel` (굵은골재) |
| 접착제 (Binder) | 마감 및 조정 (Interface) | 구조체 (Load-bearing) |

</div>

> <strong>💡 Dev Note:</strong> 자갈(Gravel)의 유무는 이 객체가 <strong>구조체(Structure)</strong>인지 <strong>마감재(Finish)</strong>인지를 결정하는 `Boolean` 값과 같습니다.

<br>

#### 2. 재료별 물리적 속성과 데이터 포인트

<strong>① 시멘트 페이스트 (Cement Paste)</strong>
* <strong>물리적 특징 (Physics):</strong> 유동성이 높음. 골재 없음.
* <strong>데이터 포인트 (Data Point):</strong>
    * `Hydration Heat` (수화열):
        - 계산상 역할 (Computational Role): 
          시멘트 경화 과정에서 발생하는 내부 열원으로 작용하며, 매스 콘크리트 초기 온도 상승 및 온도 균열 해석에 직접적인 영향을 줌.
    * `Carbon Intensity` (탄소 배출 계수):
        - 계산상 역할 (Computational Role): 
          LCA 계산에서 단위 부피당 탄소 배출량을 결정하며, 시멘트 100% 구성으로 가장 높은 탄소 기여도를 가짐.
* <strong>주요 용도 (Usage):</strong> 타일 줄눈(Grout), 미세 균열 보수

<br>

<strong>② 몰탈 (Mortar)</strong>
* <strong>물리적 특징 (Physics):</strong> 표면이 매끄러움. 벽돌 접착이나 바닥 수평용.
* <strong>데이터 포인트 (Data Point):</strong>
    * `Layer Depth` (층 두께):
        - 계산상 역할 (Computational Role): 
          보통 20~30mm의 얇은 층으로 모델링되며, 구조적·열적 영향은 제한적인 표면 레이어로 취급됨.
    * `Roughness` (표면 거칠기, $k_s$):
        - 계산상 역할 (Computational Role): 
          CFD 해석에서 벽면 마찰 손실을 결정하며, 거칠기 값이 낮아 유체 흐름 저항이 작게 계산됨.
* <strong>주요 용도 (Usage):</strong> 벽돌 조적(Masonry), 바닥 미장(Smoothing), 타일 접착

<br>

<strong>③ 콘크리트 (Concrete)</strong>
* <strong>물리적 특징 (Physics):</strong> 굵은골재가 맞물려 압축력을 견딤.
* <strong>데이터 포인트 (Data Point):</strong>
    * `Mass` (질량):
        - 계산상 역할 (Computational Role): 
          2,300 ~ 2,400 kg/m³의 자중(Self-weight)으로 작용하며, 구조 해석에서 주요 하중 입력값이 됨.
    * `Specific Heat` (비열):
        - 계산상 역할 (Computational Role): 
          열을 저장하고 방출하는 능력(Thermal Mass)을 결정하며, 실내 온도 지연(Time Lag)과 에너지 부하 산정에 영향을 줌.
* <strong>주요 용도 (Usage):</strong> 기둥(Column), 보(Beam), 슬래브(Slab), 기초(Foundation)

<br>

---

#### 3. 재료 데이터 구분이 필수적인 이유 (Critical Reasons)

<strong>① 에너지 시뮬레이션: "열용량의 주체가 다르다"</strong>

재료의 특성에 따라 시뮬레이션의 <strong>시간축(Time Step)</strong>과 <strong>공간축(Space)</strong> 설정을 달리해야 합니다.

* <strong>Simulation Logic:</strong>
    * <strong>콘크리트:</strong> 거대한 <strong>축열체(Thermal Battery)</strong>로 작용 (Time Lag 형성)
    * <strong>몰탈:</strong> 축열 성능이 거의 없는 얇은 <strong>피부(Skin)</strong> 레이어

> <strong>⚠️ Risk:</strong> 벽체를 `Mortar`로 잘못 매핑할 경우, 열 저장 능력이 '0'에 가깝게 계산되어 <strong>냉난방 설비가 과다 설계(Over-spec)</strong> 됩니다.

<br>

<strong>② 디지털 트윈 & LCA: "탄소 데이터 알고리즘 오류"</strong>

* <strong>Logic:</strong> $\text{Total Carbon} = \text{Volume}(\text{m}^3) \times \text{Carbon Factor}(\text{kgCO}_2\text{e/m}^3)$
* <strong>Fact:</strong> 시멘트 함량 차이로 인해 콘크리트와 몰탈의 탄소 계수는 서로 다릅니다.

> <strong>⚠️ Risk:</strong> 바닥 미장(`Mortar`)을 구조체(`Concrete`) 계수로 계산할 경우, 실제보다 탄소 배출량이 적게 산정되는 <strong>그린워싱(Greenwashing)</strong> 오류가 발생합니다.