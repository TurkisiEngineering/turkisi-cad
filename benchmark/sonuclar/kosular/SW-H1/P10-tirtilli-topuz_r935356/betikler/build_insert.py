"""P03 Threaded insert 3/8"-16 -> teslim/P03_insert.SLDPRT (spec bolum 6)."""
import math, sys
from swcom import *

P = dict(
    R_insert_out=0.265625, Z_insert_bot=-0.68, Z_insert_top=-0.18,
    Pitch=0.0625, R_major=0.1875, R_minor=0.146906, Flat=0.0078125, Flank_run=0.0234375,
    Z_root_phase=-0.379218, N_turns=9,
    R_csk=0.21875, Csk_depth=0.03125, csk_angle_deg=90.0,
)


def build(sw, clockwise=False, start_deg=0.0, reversed_=False, save=True):
    pt = Part(sw, "P03_insert")
    pt.equations(P)
    zb, zt, Ro, Rmi, Rma = P["Z_insert_bot"], P["Z_insert_top"], P["R_insert_out"], P["R_minor"], P["R_major"]
    # tube with crest (minor) bore
    pt.sketch("Top Plane")
    pt.rz_profile([(Rmi, zb), ('L', (Ro, zb)), ('L', (Ro, zt)), ('L', (Rmi, zt)), ('L', (Rmi, zb))])
    pt.end_sketch("SK_T1_tube"); pt.revolve("T1_Tube")
    # helix path: start at theta=0, root-flat phase z0 below the insert
    p = P["Pitch"]
    z0 = P["Z_root_phase"] - p * 5          # -0.691718
    pl = pt.plane_z(z0)
    pt.sketch(pl); pt.circle((0, 0, z0), Rma)
    sk = pt.end_sketch("SK_T2_helixbase")
    pt.m.InsertHelix(reversed_, clockwise, False, False, C.swHelixDefinedByPitchAndRevolution,
                     0, p * IN, P["N_turns"], 0, start_deg * DEG)
    hf = pt.m.FeatureByPositionReverse(0)
    setname(hf, "T2_Helix")
    # groove profile (axial half plane theta=0)
    hw_root = P["Flat"] / 2
    hw_crest = hw_root + P["Flank_run"]
    rin = Rmi - 0.015
    pt.sketch("Top Plane")
    pt.rz_profile([(rin, z0 - hw_crest), ('L', (Rmi, z0 - hw_crest)), ('L', (Rma, z0 - hw_root)),
                   ('L', (Rma, z0 + hw_root)), ('L', (Rmi, z0 + hw_crest)), ('L', (rin, z0 + hw_crest)),
                   ('L', (rin, z0 - hw_crest))], axis=False)
    prof = pt.end_sketch("SK_T3_groove")
    pt.m.ClearSelection2(True)
    prof.Select2(False, 1)
    hf.Select2(True, 4)
    f = pt.fm.InsertCutSwept4(False, True, 0, False, False, 0, 0, False, 0, 0, 0, 0, False, True, 0, True,
                              False, False, False)
    assert f is not None, "sweep fail"
    setname(f, "T3_ThreadSweepCut")
    pt.report("T3")
    # countersinks 90deg both ends
    c = P["R_csk"]
    pt.sketch("Top Plane")
    pt.rz_profile([(0, zb - 0.02), ('L', (c + 0.02, zb - 0.02)), ('L', (0.13, zb + (c - 0.13))), ('L', (0, zb + (c - 0.13))),
                   ('L', (0, zb - 0.02))], axis=False)
    pt.rz_profile([(0, zt + 0.02), ('L', (c + 0.02, zt + 0.02)), ('L', (0.13, zt - (c - 0.13))), ('L', (0, zt - (c - 0.13))),
                   ('L', (0, zt + 0.02))])
    pt.end_sketch("SK_T4_csk"); pt.revolve("T4_Countersinks", cut=True)
    r = pt.report("P03 final")
    if save:
        pt.save("P03_insert.SLDPRT")
    return pt, r


if __name__ == "__main__":
    cw = len(sys.argv) > 1 and sys.argv[1] == "cw"
    sa = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
    build(app(), clockwise=cw, start_deg=sa)
