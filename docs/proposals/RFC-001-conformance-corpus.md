# RFC-001 — Reposition `AEC-Fundamentals` as an openBIM conformance corpus

> **상태: DRAFT — 논의용 제안서이며 아직 채택된 방침이 아닙니다. (Status: DRAFT — proposal for discussion, NOT an adopted decision.)**
> This document restates an external review's proposal in a structured form so the maintainers (Mossland) can discuss it, e.g. as a GitHub Issue. Nothing here changes the license, deletes assets, or commits the project to this direction.

## 1. Context / 배경

`AEC-Fundamentals`는 스스로를 "디지털 트윈을 위한 AEC 데이터 허브"로 표방하지만, 실제 내용은 6개 도메인(Planning / Regulation / Structure / Materials / Construction / MEP)의 **입문 학습 노트**입니다. 정작 디지털 트윈의 핵심 개방형 표준(IFC · IDS · BCF · COBie · bSDD · ISO 19650 · ISO 16739)은 거의 다루지 않습니다.

- 콘텐츠 문서 58개(한 29 + 영 29) 중 외부 출처 URL이 있는 문서 10개, 참고문헌 섹션이 있는 문서 14개.
- 저장소 용량의 ~99.9%가 이미지(171개, 458MB)이며 상당수가 표시 크기 대비 과대하고 권리 근거가 불명확 (별첨 `../asset-audit/IMAGE-AUDIT.md`).
- CI · 이슈 · PR · 태그 · 거버넌스 없음 *(2026-07-12 remediation 이전 기준. 이후 Issue #7 개설 및 최소 CI가 추가됨.)*.

## 2. Problem / 문제

"교과서형 노트"는 이미 시중에 많고, 이 저장소만의 고유 가치를 만들기 어렵습니다. 또한 법규·수치·시뮬레이션 규칙을 RAG/모델 학습 근거로 쓰기엔 출처·검수 체계가 없어 신뢰성 리스크가 있습니다.

## 3. Proposal / 제안

문서를 더 쓰는 대신, **아무도 제공하지 않는 산출물 = 검증 데이터(conformance corpus)** 로 재설계.

> **정의:** conformance corpus = 정상 데이터 + 일부러 틀린 데이터 + 자동검사 정답을 함께 제공하는 적합성 시험 자료 집합. 소프트웨어의 테스트 스위트를 "건물 데이터"에 적용한 것.

핵심 질문: **설계 모델(IFC)의 정보가 BMS·디지털 트윈 운영 모델로 정확히 인계되는가?** 이를 자동으로 검증할 수 있는 pass/fail 데이터셋을 제공한다.

### 저장소 경계 (제안)

> **경계 주의:** 원안 MVP는 `open-sdb`가 이미 선언한 BIM→운영 handoff·identifier provenance·integration validation과 겹칩니다. 아래처럼 명확히 분리합니다.

| 저장소 | 고유 역할 |
| :--- | :--- |
| `AEC-Fundamentals` | AEC **의미 요구사항**, IDS profile, **IFC pass/fail fixture**, 출처가 있는 domain rule |
| `open-sdb` | `IFC ↔ Brick/Haystack/BMS/BEM` crosswalk, adapter, **identifier provenance**, integration pipeline |
| `open-sde` | mandate, PDP/PEP, runtime assurance, actuation audit |
| `FACADE` | 실제 요구사항·비식별 fixture 제공과 downstream 검증 |

## 4. MVP — `AECF-HVAC-Semantics-0.1` (범위 축소)

> **원안은 IFC·IDS·Brick·Haystack·gbXML·COBie를 한꺼번에 다뤄 `open-sdb`와 중복·과대했습니다.** 첫 MVP는 **IFC + IDS 검증만** 남기고, Brick/Haystack/BMS 인계와 crosswalk는 `open-sdb`로 넘깁니다.

2-zone 소형 오피스의 AHU–VAV 계통을 대상으로 (**MVP-0 범위**):

```text
profiles/aecf-hvac-semantics-0.1/{profile.yaml, requirements.ids, sources.yaml}
cases/small-office-vav/
├── design/model.ifc              # 합성 2-zone AHU–VAV, IFC4X3_ADD2
├── pass/model.ifc                # 정상 (IDS 통과)
├── fail/{missing-prop,bad-unit,dup-id,broken-rel,...}.ifc   # 단일 결함 4~6개
└── expected/results.json         # deterministic rule ID + 기대결과
validator/   tests/   .github/workflows/   docs/primer-legacy/
```

- 최소 검증 항목(MVP-0): 필수 property 누락, 잘못된 단위, 중복/소실 `GlobalId`, `AHU→VAV→zone` 관계 단절, 센서-설비 미연결 — 전부 **IDS 1.0 + IFC 스키마 검증**으로 판정.
- 도구: **IfcOpenShell / IfcTester** 버전 고정, clean clone에서 실행되는 GitHub Actions, 생성경위·라이선스 manifest, openBIM·HVAC 전문가 검토 기록.
- **이후 확장**(별도 case): `IFC GlobalId ↔ Brick URI ↔ BMS point ID ↔ COBie name` crosswalk, gbXML/에너지 — 단, 인계·통합 검증은 `open-sdb` 소관.

## 5. Standards baseline (2026)

> **MVP-0에서 normative(필수)로 두는 것은 `IFC4X3_ADD2 / ISO 16739-1:2024`와 `IDS v1.0.0`뿐입니다.** 나머지(COBie·Brick·Haystack·gbXML·BCF 등)는 informative/후속이며, 실제 인계 검증은 `open-sdb` 소관입니다.

| 계층 | 기준 |
| :--- | :--- |
| 정보관리 | ISO 19650, ISO 7817-1:2024 (LOIN) |
| 설계 모델 | IFC 4.3 ADD2 / ISO 16739-1:2024 |
| 정보요구 검증 | IDS 1.0, bSDD |
| 이슈 교환 | BCF 3.0 |
| 자산 인계 | NBIMS-US V4 / COBie V3 |
| 운영 의미 모델 | Brick 1.4.4, Haystack 4 |
| BIM→BEM | gbXML 8.01 |
| watchlist | Brick 1.5 RC, Haystack 5/Xeto, IFC 5 |

## 6. Migration of existing docs / 기존 문서 처리

삭제하지 않고 `docs/primer-legacy/`로 이동 + 검수 상태 front matter 부여:

```yaml
id: aecf-mep-103
locale: ko
status: unreviewed          # unreviewed | domain-reviewed | source-verified | deprecated | quarantined
jurisdiction: KR
effective_date: 2026-06-22
reviewed_by: null
source_ids: [kr-iaq-act-rule-appendix-2]
```

추가 규칙: `normative requirement` / `engineering heuristic` / `author insight` 구분; 법규는 조문·별표·시행일·관할 필수; 영문은 한국어 canonical 문서의 source hash 기록(번역 drift 검사); 이미지엔 `creator/source_url/license/generated_with/sha256` 기록.

## 7. Licensing / 라이선스

현행 저장소 전체 `CC BY-NC-SA 4.0`은 상업적 이용을 막아 OSI 기준 오픈소스가 아니며, 외부 이미지·표준 발췌까지 동일 라이선스로 덮을 수 없음. 상세 권고는 `./LICENSING.md`.

## 8. Roadmap & decision gate

| 기간 | 작업 | 완료 기준 |
| :--- | :--- | :--- |
| 1–2주 | 신규 문서 중단, 오류·출처·권리 감사 | 58문서·171이미지에 상태 부여 |
| 3–4주 | README·파일명·CI·라이선스 구조 정비 | link/media/lang-pair 검사 CI 통과 |
| 5–8주 | `AECF-HVAC-Semantics-0.1` 구현 | IFC/IDS/Brick pass/fail 자동검증 |
| **60일 Gate** | 유지 판정 | fixture 실패 시 검수 문서만 `open-sdb`로 이전 후 archive |

## 9. Needs external review / 외부 감수 필요 (이 RFC의 전제)

- **라이선스 재설정**: 기여자 동의 + 원본 권리 확인이 선행되어야 함 (법무 판단).
- **이미지 저작권**: ArchDaily·블로그·교재 출처 이미지의 재배포 가능 여부 확인 (파일별).
- **도메인·법규 사실검증**: 법정 수치·시행일·시뮬레이션 규칙은 유자격 전문가/1차 법령 확인 필요.
- **IFC/IDS/Brick fixture**: 실제 openBIM 저작 도구·검증기·전문 지식 필요 — 문서 세션에서 급조하면 안 됨.

---
*Source: 이 제안은 사용자가 제공한 외부 리뷰(2026-07-13)를 구조화한 것입니다. 채택 여부는 Mossland의 결정입니다.*
