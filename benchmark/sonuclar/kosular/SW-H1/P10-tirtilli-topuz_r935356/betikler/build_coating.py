"""P02 Grip coating -> teslim/P02_coating.SLDPRT (spec bolum 5). P01_core.SLDPRT gerekir (S4 cikarma)."""
import math, os
from swcom import *
from build_core import arc_mid

P = dict(
    T_coat=0.06, Z_coat_bot=-0.18, Z_coat_flat_top=0.5, Z_liner_top=0.26, Z_ceiling=0.35,
    R_outer=1.26, R_scallop_out=0.27, R_liner=1.05, R_scallop_liner=0.45, R_plan_round=0.1,
    R_rim_in=1.11, R_scallop_in=0.39, R_scallop_pcd=1.39, R_edge_round=0.06,
    R_dome_out=2.230085, Dome_cx=0.124593, Dome_cz=-1.524424, R_cap_start=1.06, Z_coat_top=0.68,
    R_open_low=0.421954, Z_open_low=0.62, R_open_top=0.461925, Z_open_cone_top=0.674670,
)


def sel_face_at(pt, x, y, z, append):
    return pt.ext.SelectByID2("", "FACE", x * IN, y * IN, z * IN, append, 0, None, 0)


def build(sw, core_path=None):
    pt = Part(sw, "P02_coating")
    pt.equations(P)
    zb, zt = P["Z_coat_bot"], P["Z_coat_flat_top"]
    # S1 lobed cup
    pl = pt.plane_z(zb)
    pt.sketch(pl); pt.plan(outline(P["R_outer"], P["R_scallop_out"], P["R_plan_round"], P["R_scallop_pcd"]), zb)
    pt.end_sketch("SK_S1_Lo"); pt.extrude("S1a_OuterPrism", zt - zb)
    pt.sketch(pl); pt.plan(outline(P["R_liner"], P["R_scallop_liner"], P["R_plan_round"], P["R_scallop_pcd"]), zb)
    pt.end_sketch("SK_S1_Li"); pt.extrude("S1b_InnerCut", P["Z_liner_top"] - zb, cut=True)
    pt.report("S1")
    # S2 edge rounds R0.06: all edges of bottom face (outer+inner loop) and top face (outer loop)
    pt.m.ClearSelection2(True)
    ok1 = sel_face_at(pt, 1.15, 0, zb, False)
    ok2 = sel_face_at(pt, 0.7, 0, zt, True)
    print("fillet face sel", ok1, ok2)
    r = P["R_edge_round"] * IN
    f = pt.fm.FeatureFillet3(195, r, 0, 0, 0, 0, 0, None, None, None, None, None, None, None)
    assert f is not None, "fillet fail"
    setname(f, "S2_EdgeRounds")
    pt.report("S2")
    # S3 dome cap
    pt.sketch("Top Plane")
    dc = (P["Dome_cx"], P["Dome_cz"])
    a = (P["R_cap_start"], zt); b = (P["R_open_top"], P["Z_coat_top"])
    pt.rz_profile([(0, zt), ('L', a), ('A', arc_mid(dc, P["R_dome_out"], a, b), b), ('L', (0, P["Z_coat_top"])), ('L', (0, zt))])
    pt.end_sketch("SK_S3_cap"); pt.revolve("S3_DomeCap")
    # S4 cuts: Lci prism z 0.26..0.35
    pl2 = pt.plane_z(P["Z_liner_top"])
    pt.sketch(pl2); pt.plan(outline(P["R_rim_in"], P["R_scallop_in"], 0, P["R_scallop_pcd"]), P["Z_liner_top"])
    pt.end_sketch("SK_S4_Lci"); pt.extrude("S4a_CeilingFree", P["Z_ceiling"] - P["Z_liner_top"], cut=True)
    # top opening
    pt.sketch("Top Plane")
    pt.rz_profile([(0, 0.2), ('L', (P["R_open_low"], 0.2)), ('L', (P["R_open_low"], P["Z_open_low"])),
                   ('L', (P["R_open_top"], P["Z_open_cone_top"])), ('L', (P["R_open_top"], 0.8)), ('L', (0, 0.8)),
                   ('L', (0, 0.2))])
    pt.end_sketch("SK_S4_opening"); pt.revolve("S4b_TopOpening", cut=True)
    pt.report("S4b")
    # subtract the finished core (inserted part body, then Combine-subtract)
    core_path = core_path or os.path.join(OUT, "P01_core.SLDPRT")
    fi = pt.pd.InsertPart3(core_path, C.swInsertPartImportSolids, "")
    assert fi is not None, "insert part fail"
    setname(fi, "S4c_CoreTool")
    bs = pt.bodies()
    main = [x for x in bs if x.GetBodyBox()[5] > 0.67 * IN][0]
    tool = [x for x in bs if x.GetBodyBox()[2] < -0.6 * IN][0]
    pt.m.ClearSelection2(True)
    fc = pt.fm.InsertCombineFeature(C.SWBODYCUT, main, VARR_D([tool]))
    assert fc is not None, "combine fail"
    setname(fc, "S4c_SubtractCore")
    r = pt.report("P02 final")
    pt.save("P02_coating.SLDPRT")
    return pt, r


if __name__ == "__main__":
    build(app())
