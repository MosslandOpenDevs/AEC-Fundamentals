"""Build the AECF-HVAC-Semantics-0.1 pass model + single-defect fail variants (deterministic)."""
import hashlib, os, sys, ifcopenshell, ifcopenshell.api, ifcopenshell.guid

SCHEMA = "IFC4X3_ADD2"


def guid(name):
    return ifcopenshell.guid.compress(hashlib.md5(name.encode()).hexdigest())


def run(model, hook, **kw):
    return ifcopenshell.api.run(hook, model, **kw)


def build_base():
    m = ifcopenshell.file(schema=SCHEMA)
    project = run(m, "root.create_entity", ifc_class="IfcProject", name="AECF-HVAC-Semantics-0.1")
    project.GlobalId = guid("project")
    run(m, "unit.assign_unit", length={"is_metric": True, "raw": "METERS"})
    ctx = run(m, "context.add_context", context_type="Model")
    run(m, "context.add_context", context_type="Model",
        context_identifier="Body", target_view="MODEL_VIEW", parent=ctx)

    def ent(cls, name, **extra):
        e = run(m, "root.create_entity", ifc_class=cls, name=name)
        e.GlobalId = guid(cls + ":" + name)
        for k, v in extra.items():
            setattr(e, k, v)
        return e

    site = ent("IfcSite", "Site")
    building = ent("IfcBuilding", "Small Office")
    storey = ent("IfcBuildingStorey", "L1")
    run(m, "aggregate.assign_object", products=[site], relating_object=project)
    run(m, "aggregate.assign_object", products=[building], relating_object=site)
    run(m, "aggregate.assign_object", products=[storey], relating_object=building)

    for i in (1, 2):
        z = ent("IfcSpace", f"Zone-{i}")
        run(m, "aggregate.assign_object", products=[z], relating_object=storey)

    ahu = ent("IfcUnitaryEquipment", "AHU-1", PredefinedType="AIRHANDLER")
    vavs, diffs, sensors = [], [], []
    for i in (1, 2):
        vavs.append(ent("IfcAirTerminalBox", f"VAV-{i}", PredefinedType="VARIABLEFLOWPRESSUREINDEPENDANT"))
        diffs.append(ent("IfcAirTerminal", f"Diffuser-{i}", PredefinedType="DIFFUSER"))
        sensors.append(ent("IfcSensor", f"TempSensor-{i}", PredefinedType="TEMPERATURESENSOR"))
    run(m, "spatial.assign_container", products=[ahu] + vavs + diffs + sensors, relating_structure=storey)

    system = ent("IfcDistributionSystem", "AHU-1-AirSystem", PredefinedType="VENTILATION")
    run(m, "system.assign_system", products=[ahu] + vavs + diffs, system=system)

    for i, vav in enumerate(vavs, 1):
        ps = run(m, "pset.add_pset", product=vav, name="AECF_Handover")
        # second property so removing BMS_PointID leaves a valid (non-empty) IfcPropertySet
        run(m, "pset.edit_pset", pset=ps,
            properties={"BMS_PointID": f"VAV-{i:02d}", "ZoneName": f"Zone-{i}"})
    ahu_ps = run(m, "pset.add_pset", product=ahu, name="AECF_Handover")
    run(m, "pset.edit_pset", pset=ahu_ps,
        properties={"DesignAirFlowRate": m.create_entity("IfcVolumetricFlowRateMeasure", 2.5)})
    return m


# ---- helpers to mutate a fresh copy ----
def pset_entity(elem, name):
    for rel in elem.IsDefinedBy or []:
        if rel.is_a("IfcRelDefinesByProperties"):
            pd = rel.RelatingPropertyDefinition
            if pd.is_a("IfcPropertySet") and pd.Name == name:
                return pd
    return None


def psv(pset, name):
    for p in pset.HasProperties or []:
        if p.is_a("IfcPropertySingleValue") and p.Name == name:
            return p
    return None


def mut_missing_space_name(m):
    m.by_type("IfcSpace")[0].Name = None


def mut_missing_bms_pointid(m):
    vav = [e for e in m.by_type("IfcAirTerminalBox") if e.Name == "VAV-1"][0]
    ps = pset_entity(vav, "AECF_Handover")
    ps.HasProperties = tuple(p for p in ps.HasProperties if p.Name != "BMS_PointID")


def mut_wrong_pointid_pattern(m):
    vav = [e for e in m.by_type("IfcAirTerminalBox") if e.Name == "VAV-1"][0]
    psv(pset_entity(vav, "AECF_Handover"), "BMS_PointID").NominalValue = m.create_entity("IfcLabel", "BADID")


def mut_wrong_airflow_datatype(m):
    ahu = m.by_type("IfcUnitaryEquipment")[0]
    psv(pset_entity(ahu, "AECF_Handover"), "DesignAirFlowRate").NominalValue = m.create_entity("IfcReal", 2.5)


def mut_broken_system(m):
    vav = [e for e in m.by_type("IfcAirTerminalBox") if e.Name == "VAV-1"][0]
    for rel in m.by_type("IfcRelAssignsToGroup"):
        if vav in (rel.RelatedObjects or ()):
            rel.RelatedObjects = tuple(o for o in rel.RelatedObjects if o != vav)


FAILS = {
    "missing-space-name": ("Spaces are named", mut_missing_space_name),
    "missing-bms-pointid": ("VAV has BMS_PointID", mut_missing_bms_pointid),
    "wrong-pointid-pattern": ("VAV has BMS_PointID", mut_wrong_pointid_pattern),
    "wrong-airflow-datatype": ("AHU airflow has correct datatype", mut_wrong_airflow_datatype),
    "broken-system": ("VAV is part of a distribution system", mut_broken_system),
}


def finalize(m):
    """Make output byte-deterministic: fixed GUIDs (incl. api-created relationships) and
    a fixed STEP header (no wall-clock timestamp)."""
    from collections import Counter
    seen = Counter()
    for e in m.by_type("IfcRoot"):
        key = f"{e.is_a()}:{e.Name or ''}"
        seen[key] += 1
        e.GlobalId = ifcopenshell.guid.compress(
            hashlib.md5(f"{key}:{seen[key]}".encode()).hexdigest())
    # IFC SETs are unordered but serialize in insertion order; sort membership by the
    # (now deterministic) GlobalId so the written bytes are stable.
    for rel in m.by_type("IfcRelationship"):
        for attr in ("RelatedElements", "RelatedObjects"):
            try:
                val = getattr(rel, attr)
            except Exception:
                continue
            if val and len(val) > 1:
                setattr(rel, attr, tuple(sorted(val, key=lambda o: o.GlobalId or "")))
    for ua in m.by_type("IfcUnitAssignment"):   # Units is also an unordered SET
        if ua.Units and len(ua.Units) > 1:
            ua.Units = tuple(sorted(ua.Units, key=lambda u: u.id()))
    h = m.header
    h.file_name.name = "aecf-hvac-semantics-0.1"
    h.file_name.time_stamp = "2026-01-01T00:00:00"
    h.file_name.author = ["aecf"]
    h.file_name.organization = ["mossland"]
    return m


def write(m, path):
    finalize(m).write(path)


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "cases/small-office-vav"
    os.makedirs(f"{root}/pass", exist_ok=True)
    os.makedirs(f"{root}/fail", exist_ok=True)
    os.makedirs(f"{root}/design", exist_ok=True)
    base = build_base()
    write(base, f"{root}/pass/model.ifc")
    write(build_base(), f"{root}/design/model.ifc")
    print("wrote pass/model.ifc")
    for key, (spec, fn) in FAILS.items():
        m = build_base()
        fn(m)
        write(m, f"{root}/fail/{key}.ifc")
        print(f"wrote fail/{key}.ifc  (should fail: {spec})")
