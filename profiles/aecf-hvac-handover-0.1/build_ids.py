"""Author the AECF-HVAC-Handover-0.1 IDS (IDS 1.0)."""
from ifctester import ids


def build():
    doc = ids.Ids(
        title="AECF-HVAC-Handover-0.1",
        description="Minimal IFC->operations handover conformance profile (2-zone AHU-VAV).",
        author="aecf@mossland.io",
        version="0.1.0",
    )

    # 1. every space must be named (identifier linkage)
    s1 = ids.Specification(name="Spaces are named", ifcVersion="IFC4X3_ADD2")
    s1.applicability.append(ids.Entity(name="IFCSPACE"))
    s1.requirements.append(ids.Attribute(name="Name"))
    doc.specifications.append(s1)

    # 2. every VAV carries a BMS point id matching VAV-NN
    s2 = ids.Specification(name="VAV has BMS_PointID", ifcVersion="IFC4X3_ADD2")
    s2.applicability.append(ids.Entity(name="IFCAIRTERMINALBOX"))
    s2.requirements.append(ids.Property(
        propertySet="AECF_Handover", baseName="BMS_PointID",
        dataType="IFCLABEL",
        value=ids.Restriction(options={"pattern": "VAV-[0-9]{2}"}, base="string"),
    ))
    doc.specifications.append(s2)

    # 3. AHU design airflow must be a volumetric flow rate (correct unit/datatype)
    s3 = ids.Specification(name="AHU airflow has correct datatype", ifcVersion="IFC4X3_ADD2")
    s3.applicability.append(ids.Entity(name="IFCUNITARYEQUIPMENT"))
    s3.requirements.append(ids.Property(
        propertySet="AECF_Handover", baseName="DesignAirFlowRate",
        dataType="IFCVOLUMETRICFLOWRATEMEASURE",
    ))
    doc.specifications.append(s3)

    # 4. every VAV must belong to a distribution system (AHU->VAV->zone chain)
    s4 = ids.Specification(name="VAV is part of a distribution system", ifcVersion="IFC4X3_ADD2")
    s4.applicability.append(ids.Entity(name="IFCAIRTERMINALBOX"))
    s4.requirements.append(ids.PartOf(name="IFCDISTRIBUTIONSYSTEM", relation="IFCRELASSIGNSTOGROUP"))
    doc.specifications.append(s4)

    return doc


if __name__ == "__main__":
    import sys
    doc = build()
    out = sys.argv[1] if len(sys.argv) > 1 else "requirements.ids"
    doc.to_xml(out)
    print("wrote", out, "with", len(doc.specifications), "specs")
