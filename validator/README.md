# AECF-HVAC-Semantics-0.1 — conformance validator (MVP-0)

A small, **real** openBIM conformance corpus: a valid IFC 4.3 model that satisfies an
IDS 1.0 profile, plus single-defect variants that must each fail exactly one
requirement. Everything is validated with [IfcOpenShell / IfcTester](https://docs.ifcopenshell.org/ifctester.html).

> **Scope (RFC-001):** IFC 4.3 + IDS 1.0 only. Brick/Haystack/BMS crosswalk and
> integration validation are out of scope and belong to `open-sdb`.
> **Status:** DRAFT PoC — needs an openBIM/HVAC expert review before it is authoritative.

## Layout

```
profiles/aecf-hvac-semantics-0.1/
  requirements.ids     # the IDS profile (4 specifications)
  build_ids.py         # regenerates requirements.ids
  profile.yaml         # metadata      sources.yaml  # provenance (synthetic, CC0-proposed)
cases/small-office-vav/
  design/model.ifc     pass/model.ifc          # satisfies every spec
  fail/*.ifc           # five single-defect variants
  expected/results.json# recorded expected outcome per case
validator/
  build_models.py      # regenerates the pass model + fail variants
  run.py               # validates every case and checks it matches expected/results.json
  requirements.txt     # pinned tool versions
```

## Run

```bash
pip install -r validator/requirements.txt
python validator/run.py            # CI mode: assert every case matches expected/results.json
```

Regenerate the fixtures (after editing the builders):

```bash
python profiles/aecf-hvac-semantics-0.1/build_ids.py profiles/aecf-hvac-semantics-0.1/requirements.ids
python validator/build_models.py cases/small-office-vav
python validator/run.py --write    # refresh expected/results.json
```

## What the profile checks

| Specification | Defect variant that must fail it |
| :--- | :--- |
| Spaces are named | `fail/missing-space-name.ifc` |
| VAV has `BMS_PointID` (pattern `VAV-NN`) | `fail/missing-bms-pointid.ifc`, `fail/wrong-pointid-pattern.ifc` |
| AHU `DesignAirFlowRate` datatype = `IfcVolumetricFlowRateMeasure` | `fail/wrong-airflow-datatype.ifc` |
| VAV is part of an `IfcDistributionSystem` | `fail/broken-system.ifc` |

CI: [`.github/workflows/mvp0-conformance.yml`](../.github/workflows/mvp0-conformance.yml).

## Hardening applied

- **No vacuous pass:** every specification has `minOccurs=1`, so an empty model *fails* (it does not pass by having zero applicable entities).
- **Schema-checked:** `run.py` asserts every model (pass *and* fail) is a valid `IFC4X3_ADD2` file via `ifcopenshell.validate` — the fail models violate the IDS, not the IFC schema.
- **Deterministic:** `build_models.py` emits byte-identical files on re-run (fixed GUIDs, fixed STEP header timestamp, sorted unordered SETs).

## Known limitations (why this is a PoC, not an authoritative corpus)

These are **not yet covered** and need design + an openBIM/HVAC expert sign-off before the corpus is treated as authoritative:

- **Entity typing is assumed:** every `IfcAirTerminalBox` is treated as a VAV and every `IfcUnitaryEquipment` as an AHU (no `PredefinedType`/classification gate).
- **No real topology check:** "VAV is part of an `IfcDistributionSystem`" is satisfied by membership in *any* system — the actual **AHU → VAV → zone** chain is not verified (IDS `partOf` cannot express it; needs a custom graph check).
- **`BMS_PointID` is a synthetic requirement example, not a real BMS mapping** — the actual `IFC ↔ Brick/Haystack/BMS` crosswalk and identifier provenance belong to `open-sdb` (see [ADR-001](../docs/proposals/ADR-001-repo-boundaries.md)).
- **Not caught:** duplicate `BMS_PointID`, negative/out-of-range airflow, wrong unit *magnitudes*, and failed-entity counts.
- **Self-consistency risk:** the IDS is authored, run, and its expected results recorded by the same IfcTester family. An independent validator (e.g. a different IDS engine) should cross-check before sign-off.
