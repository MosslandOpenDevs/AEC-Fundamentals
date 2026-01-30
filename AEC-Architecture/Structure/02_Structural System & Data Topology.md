# 02 Structural System & Data Topology

### 벽식 구조와 라멘 구조: 시뮬레이션 경계 조건과 데이터 위계의 차이

---

디지털 트윈 구축 단계에서 구조 형식(Structural System)을 파악하는 것은 단순한 형상 모델링 이상의 의미를 가집니다.

구조 형식은 **에너지 해석의 열교(Thermal Bridge) 라인**, **기류 해석의 유체 흐름 장애물**, 그리고 **BIM 데이터의 수정 가능 범위**를 결정짓는 가장 상위의 **물리적 제약 조건(Physical Constraint)**이기 때문입니다.

<br>

| **1. 벽식 구조 (Wall Structure)** | **2. 라멘 구조 (Rahmen Structure)** |
| :--- | :--- |
| **선형 구속 (Linear Constraint)**<br>닫힌 데이터 셀 (Closed Cell) | **점형 구속 (Point Constraint)**<br>가변적 필드 (Flexible Field) |
| **[Definition]**<br>수직 하중을 지지하는 **내력벽(Bearing Wall)**이 공간을 구획하는 동시에 구조체의 역할을 수행합니다. | **[Definition]**<br>기둥(Column)과 보(Beam)가 결합하여 3차원 프레임을 형성하며, 벽체는 하중을 받지 않는 **비내력벽**입니다. |
| <img src="./assets/images/structure_wall_iso.png" width="100%"> | <img src="./assets/images/structure_rahmen_iso.png" width="100%"> |
| **[Analysis] 해석적 닫힘**<br><br><li>**Energy Analysis**: 외벽과 내벽이 만나는 모든 모서리가 **선형 열교(Linear Thermal Bridge)**가 됩니다.</li><br><li>**Airflow Analysis**: 내력벽에 의해 기류가 차단되어, **Room 단위의 독립 격자** 구획이 강제됩니다.</li> | **[Analysis] 해석적 열림**<br><br><li>**Energy Analysis**: 구조와 외피가 분리되어 **개구부(Window)와 커튼월**의 물성치가 핵심 변수가 됩니다.</li><br><li>**Airflow Analysis**: 거대한 **오픈 플랜(Open Plan)**으로 해석되며, 기둥은 유체 흐름을 가르는 장애물(Obstacle)로 작용합니다.</li> |
| <img src="./assets/images/sim_closed_boundary.png" width="100%"> | <img src="./assets/images/sim_open_field.png" width="100%"> |
| **[Data] 정적 공간 (Static Zone)**<br><br><li>BIM 벽체 속성 = **`Structural`** (고정)</li><li>공간(Room) 경계가 영구 고정되므로, 운영 단계 데이터 모델의 유연성이 낮습니다.</li> | **[Data] 동적 레이어 (Dynamic Layer)**<br><br><li>BIM 벽체 속성 = **`Architectural`** (가변)</li><li>센서 데이터는 변하지 않는 **기둥(Anchor)**에 맵핑되며, 벽체 정보는 언제든 수정 가능합니다.</li> |
| <img src="./assets/images/data_static_zone.png" width="100%"> | <img src="./assets/images/data_dynamic_grid.png" width="100%"> |
| 💡 **Insight**<br>데이터 모델링 최소 단위: **고정된 방 (Room)** | 💡 **Insight**<br>데이터 모델링 최소 단위: **좌표 그리드 (Grid)** |
| <div align="center"><br><h3>🔻 Summary: Wall</h3></div> | <div align="center"><br><h3>Summary: Rahmen 🔻</h3></div> |
| <div align="center"><b>[제약 조건]</b><br>Linear Constraint (선형)</div> | <div align="center"><b>[제약 조건]</b><br>Point Constraint (점형)</div> |
| <div align="center"><b>[BIM 위계]</b><br>Wall = Structure (삭제 불가)</div> | <div align="center"><b>[BIM 위계]</b><br>Wall = Architecture (삭제 가능)</div> |
| <div align="center"><b>[에너지 해석]</b><br>열교(Bridge) 관리 핵심</div> | <div align="center"><b>[에너지 해석]</b><br>외피(Skin) 성능 핵심</div> |
| <div align="center"><b>[기류 해석]</b><br>Compartment (구획된 공간)</div> | <div align="center"><b>[기류 해석]</b><br>Open Field (개방형 공간)</div> |

<br>

### Conclusion

건물의 구조 형식을 이해하는 것은 **데이터가 담길 그릇의 형태**를 이해하는 것과 같습니다. 성능 해석 모델과 디지털 트윈을 구축할 때, 대상 건물의 구조 형식에 맞춰 **데이터의 위계(Hierarchy)**를 올바르게 설정하시기 바랍니다.