# ADR-001 — Repository boundaries (AEC-Fundamentals ↔ open-sdb ↔ open-sde ↔ FACADE)

> **Status: PROPOSED — not acknowledged by the other repositories.** This ADR records the
> intended split so the overlap flagged in review can be closed. It is not binding until
> each named repository's owner acknowledges it (cross-repo issues to be opened).

## Context

The initial MVP (`AECF-HVAC-Handover-0.1`) framed itself around *BIM → operations handover*,
which is exactly what [`open-sdb`](https://github.com/MosslandOpenDevs/open-sdb) already
declares (identifier provenance, integration validation). Same-scope names and a
`BMS_PointID` check made the overlap concrete.

## Decision (proposed)

| Owner | Owns |
| :--- | :--- |
| **AEC-Fundamentals** | AEC meaning/attribute/relationship requirements **inside IFC**, the IDS profile, synthetic pass/fail IFC fixtures, sourced domain rules |
| **open-sdb** | `IFC ↔ Brick/Haystack/BMS/BEM` conversion, external ID mapping & provenance, integration pipeline |
| **open-sde** | mandate, PDP/PEP, runtime assurance, actuation audit — consuming validated state |
| **FACADE** | requirement + de-identified case supplier and downstream acceptance consumer (a project/pilot consumer, **not** a peer public corpus; consortium IP / security / de-identification approvals apply) |

Concretely, in this repo:

1. The profile is renamed `AECF-HVAC-Handover-0.1` → **`AECF-HVAC-Semantics-0.1`** to signal
   *IFC-internal semantics*, not handover.
2. `BMS_PointID` is kept **only as a synthetic project-requirement example** and labelled as
   such in the IDS description. The **real** `IFC ↔ BMS` crosswalk belongs in `open-sdb`
   (recommended future name there: `SDB-HVAC-Handover-0.1`), and moving the check there is the
   preferred end-state.

## Consequences / open items (human gate)

- Open cross-repo issues in `open-sdb`, `open-sde`, and the FACADE tracker to acknowledge this
  split before AECF declares any authoritative release.
- FACADE data flowing into a public corpus needs separate IP / demand-agency / security / 
  de-identification approval.

*Related: [RFC-001](RFC-001-conformance-corpus.md), [Issue #7](https://github.com/MosslandOpenDevs/AEC-Fundamentals/issues/7).*
