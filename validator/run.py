#!/usr/bin/env python3
"""Conformance runner for AECF-HVAC-Handover-0.1.

Validates every case model under cases/small-office-vav/{pass,fail}/ against the
profile IDS with ifctester, then checks the result matches expected/results.json:

  - pass/*.ifc  must satisfy every specification (no failed specs);
  - fail/*.ifc  must fail exactly the specifications listed in expected/results.json.

Usage:
  python validator/run.py            # check against expected/results.json (CI mode)
  python validator/run.py --write    # (re)generate expected/results.json from actual
"""
import json, os, sys, glob

import ifcopenshell
from ifctester import ids

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDS_PATH = os.path.join(ROOT, "profiles", "aecf-hvac-handover-0.1", "requirements.ids")
CASE_DIR = os.path.join(ROOT, "cases", "small-office-vav")
EXPECTED = os.path.join(CASE_DIR, "expected", "results.json")


def failed_specs(model_path):
    model = ifcopenshell.open(model_path)
    doc = ids.open(IDS_PATH)
    doc.validate(model)
    return sorted(s.name for s in doc.specifications if not s.status)


def discover():
    cases = {}
    for kind in ("pass", "fail"):
        for p in sorted(glob.glob(os.path.join(CASE_DIR, kind, "*.ifc"))):
            rel = os.path.relpath(p, CASE_DIR).replace(os.sep, "/")
            cases[rel] = kind
    return cases


def run(write=False):
    cases = discover()
    expected = {} if write else json.load(open(EXPECTED)).get("cases", {})
    results, ok = {}, True
    for rel, kind in cases.items():
        fs = failed_specs(os.path.join(CASE_DIR, rel))
        verdict = "pass" if not fs else "fail"
        results[rel] = {"expected": kind, "failed_specs": fs}
        # structural invariant
        structural = (kind == "pass" and verdict == "pass") or (kind == "fail" and verdict == "fail")
        # match against recorded expectation (verdict + which specs)
        exp = expected.get(rel)
        matches = write or (exp is not None and exp.get("failed_specs", []) == fs and exp.get("expected") == kind)
        good = structural and matches
        ok = ok and good
        flag = "OK " if good else "❌ "
        print(f"  {flag}[{verdict:4s}] {rel:34s} failed={fs}")

    if write:
        os.makedirs(os.path.dirname(EXPECTED), exist_ok=True)
        json.dump({"profile": "aecf-hvac-handover-0.1", "cases": results},
                  open(EXPECTED, "w"), indent=2, ensure_ascii=False)
        open(EXPECTED, "a").write("\n")
        print(f"\nwrote {os.path.relpath(EXPECTED, ROOT)} ({len(results)} cases)")
        return 0
    print("\n✓ conformance corpus matches expected results" if ok
          else "\n✗ conformance mismatch — see ❌ rows above")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(run(write="--write" in sys.argv[1:]))
