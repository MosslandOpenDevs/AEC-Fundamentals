# AECF-HVAC-Handover-0.1 — conformance validator (MVP-0)

A small, **real** openBIM conformance corpus: a valid IFC 4.3 model that satisfies an
IDS 1.0 profile, plus single-defect variants that must each fail exactly one
requirement. Everything is validated with [IfcOpenShell / IfcTester](https://docs.ifcopenshell.org/ifctester.html).

> **Scope (RFC-001):** IFC 4.3 + IDS 1.0 only. Brick/Haystack/BMS crosswalk and
> integration validation are out of scope and belong to `open-sdb`.
> **Status:** DRAFT PoC — needs an openBIM/HVAC expert review before it is authoritative.

## Layout

```
profiles/aecf-hvac-handover-0.1/
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
python profiles/aecf-hvac-handover-0.1/build_ids.py profiles/aecf-hvac-handover-0.1/requirements.ids
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
