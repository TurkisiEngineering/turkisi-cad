"""Features shared by base (P01) and lid (P02)."""
from params import *


def outer_shell(P, z_open, s, tag):
    """Outer shell from the open (parting-side) plane z_open going in direction s (-1 base, +1 lid).
    1) rounded slab (R_EDGE perimeter round, sphere corners) near the closed face
    2) ruled loft between outline S at z_open and the constant-radius outline 0.35 further."""
    h_wall = 0.35                              # loft height (to the axis plane of the R0.1 round)
    z_round = z_open + s * h_wall              # = -0.35 base / 0.38 lid
    z_face = z_open + s * 0.45                 # closed face (-0.45 / 0.48)
    z_slab = z_round - s * 0.05                # slab starts 0.05 inside the loft
    pl = P.pz(z_slab)
    P.begin(pl, "%s_SK_slab" % tag)
    P.rrect(EDGE_C_HX + R_EDGE, EDGE_C_HY + R_EDGE, R_EDGE, z_slab)
    P.end()
    P.extrude(abs(z_face - z_slab), up=(s > 0), name="%s_Slab" % tag)
    P.fillet([(0.0, -(EDGE_C_HY + R_EDGE), z_face)], R_EDGE, name="%s_PerimeterRound_R0.1" % tag)
    P.param("R_EDGE", R_EDGE, "%s_PerimeterRound_R0.1" % tag, "perimeter round radius")

    # loft (constant corner radius, corner centres move diagonally with the 3 deg draft)
    d = h_wall * T3
    pl2 = P.pz(z_round)
    P.begin(P.pz(z_open), "%s_SK_outlineS" % tag)
    P.rrect(W_HALF, L_HALF, R_CORNER, z_open)
    sk1 = P.end()
    P.begin(pl2, "%s_SK_outlineS_drafted" % tag)
    P.rrect(W_HALF - d, L_HALF - d, R_CORNER, z_round)
    sk2 = P.end()
    P.loft(sk1, (0.0, -L_HALF, z_open), sk2, (0.0, -(L_HALF - d), z_round), name="%s_OuterWall_Loft3deg" % tag)
    P.param("W_HALF", W_HALF, "%s_SK_outlineS" % tag, "outline S half width X")
    P.param("L_HALF", L_HALF, "%s_SK_outlineS" % tag, "outline S half length Y")
    P.param("R_CORNER", R_CORNER, "%s_SK_outlineS / _drafted" % tag, "vertical corner radius (constant)")
    P.param("DRAFT_OUT", DRAFT_OUT, "%s_SK_outlineS_drafted" % tag, "outer wall draft deg (offset 0.35*tan3)")


def cavity(P, z_open, s, tag, z_floor):
    pl = P.pz(z_open)
    P.begin(pl, "%s_SK_cavityC" % tag)
    a = CAV_CHAMF - CAV_HY   # 0.75062
    b = CAV_CHAMF - CAV_HX   # 1.02562
    pts = [(CAV_HX, -b), (CAV_HX, b), (a, CAV_HY), (-a, CAV_HY), (-CAV_HX, b), (-CAV_HX, -b),
           (-a, -CAV_HY), (a, -CAV_HY)]
    P.poly(pts, z_open)
    P.end()
    depth = abs(z_floor - z_open)
    P.extrude(depth, up=(s > 0), cut=True, draft=DRAFT_IN, outward=False, name="%s_Cavity_1deg" % tag)
    P.param("CAV_HX", CAV_HX, "%s_SK_cavityC" % tag, "cavity half width at open side")
    P.param("CAV_HY", CAV_HY, "%s_SK_cavityC" % tag, "cavity half length at open side")
    P.param("CAV_CHAMF", CAV_CHAMF, "%s_SK_cavityC" % tag, "corner chamfer line |x|+|y|")
    P.param("CAV_DEPTH", depth, "%s_Cavity_1deg" % tag, "cavity depth")
    P.param("DRAFT_IN", DRAFT_IN, "%s_Cavity_1deg" % tag, "cavity draft deg")
    # fillets floor/ceiling to the four straight walls only
    off = depth * T1
    hx, hy = CAV_HX - off, CAV_HY - off
    pts = [(hx, 0, z_floor), (-hx, 0, z_floor), (0, hy, z_floor), (0, -hy, z_floor)]
    P.fillet(pts, R_CAV_FILLET, name="%s_FloorFillet_R0.03" % tag, propagate=False)
    P.param("R_CAV_FILLET", R_CAV_FILLET, "%s_FloorFillet_R0.03" % tag, "floor/ceiling fillet")


def label(P, z_face, s, tag):
    """label ring groove 0.01 deep into the outer face z_face (s = direction into the part)"""
    pl = P.pz(z_face)
    P.begin(pl, "%s_SK_label" % tag)
    P.rect(-LABEL_OUT[0], -LABEL_OUT[1], LABEL_OUT[0], LABEL_OUT[1], z_face)
    P.rect(-LABEL_IN[0], -LABEL_IN[1], LABEL_IN[0], LABEL_IN[1], z_face)
    P.end()
    P.extrude(LABEL_DEPTH, up=(s > 0), cut=True, name="%s_LabelRecess" % tag)
    P.param("LABEL_OUT", "%.3f x %.3f half" % LABEL_OUT, "%s_SK_label" % tag, "label groove outer")
    P.param("LABEL_IN", "%.3f x %.3f half" % LABEL_IN, "%s_SK_label" % tag, "label groove inner")
    P.param("LABEL_DEPTH", LABEL_DEPTH, "%s_LabelRecess" % tag, "label groove depth")


def cross(arm, half):
    """12-vertex cross polygon (ribs along +/-X and +/-Y)"""
    return [(arm, -half), (arm, half), (half, half), (half, arm), (-half, arm), (-half, half),
            (-arm, half), (-arm, -half), (-half, -half), (-half, -arm), (half, -arm), (half, -half)]
