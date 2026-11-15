"""P01 Base - built in place in the global frame (inch)."""
import sys
from params import *
from common import outer_shell, cavity, label, cross


def build(P, verbose=True):
    rep = (lambda t: P.report(t)) if verbose else (lambda t: None)
    tag = "P01"
    # B1 + B2 outer shell with perimeter round
    outer_shell(P, 0.0, -1, tag)
    rep("shell")
    # B3 + B4 cavity and floor fillets
    cavity(P, 0.0, -1, tag, BASE_FLOOR)
    rep("cavity")

    # B7 corner recesses (4x), cut 0.035 deep, 1 deg draft
    P.begin(P.front, "P01_SK_cornerRecess")
    a = CAV_CHAMF - CAV_HY   # 0.75062
    b = CAV_CHAMF - CAV_HX   # 1.02562
    for sx in (1, -1):
        for sy in (1, -1):
            Q = lambda x, y: (sx * x, sy * y, 0.0)
            P.line(Q(CAV_HX, b), Q(CAV_HX, 1.05))
            P.arc(Q(0.865, 1.05), Q(CAV_HX, 1.05), Q(0.865, 1.07), Q(0.865 - RECESS_R * R2_, 1.05 + RECESS_R * R2_))
            P.line(Q(0.865, 1.07), Q(0.865, 1.14))
            P.line(Q(0.865, 1.14), Q(0.795, 1.14))
            P.arc(Q(0.775, 1.14), Q(0.795, 1.14), Q(0.775, CAV_HY), Q(0.775 + RECESS_R * R2_, 1.14 - RECESS_R * R2_))
            P.line(Q(0.775, CAV_HY), Q(a, CAV_HY))
            P.line(Q(a, CAV_HY), Q(CAV_HX, b))
    P.end()
    P.extrude(RECESS_DEPTH, up=False, cut=True, draft=DRAFT_IN, outward=False, name="P01_CornerRecess_x4")
    P.param("RECESS_DEPTH", RECESS_DEPTH, "P01_CornerRecess_x4", "corner recess depth")
    P.param("RECESS_R", RECESS_R, "P01_SK_cornerRecess", "corner recess arc radius")
    rep("recess")

    # B5 lip z 0..0.03, both faces drafted 3 deg (narrower at the top)
    P.begin(P.front, "P01_SK_lip")
    P.rect(-LIP_IN[0], -LIP_IN[1], LIP_IN[0], LIP_IN[1], 0.0)
    P.rrect(LIP_OUT[0], LIP_OUT[1], LIP_OUT_R, 0.0)
    P.end()
    P.extrude(LIP_H, up=True, draft=DRAFT_OUT, outward=False, name="P01_Lip_3deg")
    P.param("LIP_H", LIP_H, "P01_Lip_3deg", "lip height")
    P.param("LIP_IN", "%.3f x %.3f half" % LIP_IN, "P01_SK_lip", "lip inner boundary (sharp)")
    P.param("LIP_OUT", "%.3f x %.3f half, R%.2f" % (LIP_OUT + (LIP_OUT_R,)), "P01_SK_lip", "lip outer boundary")
    rep("lip")

    # B6 tongue: 4 stadium footprints at z=0.03, 10 deg draft, R0.005 top round, then gap cut
    zt = LIP_H
    P.begin(P.pz(zt), "P01_SK_tongue")
    for sx in (1, -1):
        P.slot_y(sx * TONGUE_X_C, -TONGUE_X_END, TONGUE_X_END, TONGUE_HALF_W, zt)
    for sy in (1, -1):
        P.slot_x(sy * TONGUE_Y_C, -TONGUE_Y_END, TONGUE_Y_END, TONGUE_HALF_W, zt)
    P.end()
    P.extrude(TONGUE_H, up=True, draft=TONGUE_DRAFT, outward=False, name="P01_Tongue_10deg")
    rep("tongue")
    k = TONGUE_HALF_W - TONGUE_H * T10
    ztop = zt + TONGUE_H
    pts = [(TONGUE_X_C + k, 0.5, ztop), (-TONGUE_X_C - k, 0.5, ztop),
           (0.3, TONGUE_Y_C + k, ztop), (0.3, -TONGUE_Y_C - k, ztop)]
    try:
        P.fillet(pts, TONGUE_R, name="P01_TongueRound_R0.005")
        P.param("TONGUE_R", TONGUE_R, "P01_TongueRound_R0.005", "tongue top-edge round")
    except Exception as ex:
        print("tongue round FAILED", ex)
    rep("tongue round")
    P.begin(P.pz(zt), "P01_SK_tongueGap")
    P.rect(0.85, -TONGUE_GAP, 0.92, TONGUE_GAP, zt)
    P.rect(-0.92, -TONGUE_GAP, -0.85, TONGUE_GAP, zt)
    P.end()
    P.extrude(0.05, up=True, cut=True, name="P01_TongueGap")
    for n, v, d in (("TONGUE_H", TONGUE_H, "tongue height"), ("TONGUE_HALF_W", TONGUE_HALF_W, "tongue half width at base"),
                    ("TONGUE_DRAFT", TONGUE_DRAFT, "flank draft deg"), ("TONGUE_X_C", TONGUE_X_C, "X-side centreline"),
                    ("TONGUE_Y_C", TONGUE_Y_C, "Y-side centreline"), ("TONGUE_X_END", TONGUE_X_END, "X-side round end centre |y|"),
                    ("TONGUE_Y_END", TONGUE_Y_END, "Y-side round end centre |x|")):
        P.param(n, v, "P01_SK_tongue / P01_Tongue_10deg", d)
    P.param("TONGUE_GAP", TONGUE_GAP, "P01_SK_tongueGap", "flat ends of X-side segments |y|")
    rep("tongue gap")

    # B8 boss r0.0925 at z=0.03 growing 1 deg downward to the floor
    P.begin(P.pz(BOSS_TOP_BASE), "P01_SK_boss")
    P.circle((0, 0, BOSS_TOP_BASE), BOSS_R)
    P.end()
    P.extrude(BOSS_TOP_BASE - BASE_FLOOR, up=False, draft=DRAFT_IN, outward=True, name="P01_Boss_1deg")
    P.param("BOSS_R", BOSS_R, "P01_SK_boss", "boss radius at top")
    P.param("BOSS_TOP_BASE", BOSS_TOP_BASE, "P01_Boss_1deg", "boss top z")
    rep("boss")

    # B9 ribs: upper cross (to x=0.123, top z=0) and lower cross (to x=0.15221, top z=-0.035)
    P.begin(P.front, "P01_SK_ribUpper")
    P.poly(cross(RIB_STEP_X, RIB_HALF_T), 0.0)
    P.end()
    P.extrude(-BASE_FLOOR, up=False, draft=DRAFT_IN, outward=True, name="P01_RibUpper_1deg")
    hl = RIB_HALF_T - RIB_LOW_Z * T1
    P.begin(P.pz(RIB_LOW_Z), "P01_SK_ribLower")
    P.poly(cross(RIB_END_X, hl), RIB_LOW_Z)
    P.end()
    P.extrude(RIB_LOW_Z - BASE_FLOOR, up=False, draft=DRAFT_IN, outward=True, name="P01_RibLower_1deg")
    P.param("RIB_HALF_T", RIB_HALF_T, "P01_SK_ribUpper", "rib half thickness at z=0")
    P.param("RIB_STEP_X", RIB_STEP_X, "P01_SK_ribUpper", "rib step face")
    P.param("RIB_END_X", RIB_END_X, "P01_SK_ribLower", "rib end face at z=-0.035")
    P.param("RIB_LOW_Z", RIB_LOW_Z, "P01_SK_ribLower", "rib lower top z")
    rep("ribs")

    # B11 screw hole (revolved cut, profile in the YZ plane)
    P.begin(P.right, "P01_SK_screwHole")
    pr = [(0, BASE_Z_BOT), (HOLE_CB_R, BASE_Z_BOT), (HOLE_CB_R, HOLE_CB_Z), (HOLE_R, HOLE_CS_Z),
          (HOLE_R, 0.05), (0, 0.05)]
    for i in range(len(pr)):
        a_, b_ = pr[i], pr[(i + 1) % len(pr)]
        P.line((0, a_[0], a_[1]), (0, b_[0], b_[1]))
    P.cline((0, 0, -0.6), (0, 0, 0.2))
    P.end()
    P.revolve(cut=True, name="P01_ScrewHole")
    P.param("HOLE_CB_R", HOLE_CB_R, "P01_SK_screwHole", "counterbore radius")
    P.param("HOLE_CB_Z", HOLE_CB_Z, "P01_SK_screwHole", "counterbore top z")
    P.param("HOLE_CS_Z", HOLE_CS_Z, "P01_SK_screwHole", "countersink end z (82 deg)")
    P.param("HOLE_R", HOLE_R, "P01_SK_screwHole", "through hole radius")
    rep("hole")

    # B12 label recess on the bottom face
    label(P, BASE_Z_BOT, +1, tag)
    rep("label")

    # B10 rib/boss floor fillets R0.005 (optional, tiny volume)
    return P


R2_ = 0.7071067811865476

if __name__ == "__main__":
    import win32com.client, swlib
    sw = win32com.client.Dispatch("SldWorks.Application")
    P = swlib.Part(sw)
    build(P)
