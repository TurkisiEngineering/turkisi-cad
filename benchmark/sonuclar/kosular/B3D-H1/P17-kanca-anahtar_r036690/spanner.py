"""P01 Spanner - hook spanner wrench (spec P17). Units: inch. build123d 0.11.1.

Outline in global XZ plane, extruded symmetric along Y (Y = -T/2 .. +T/2).
Run:  python spanner.py   ->  writes final.step next to this script.
"""
import math
from pathlib import Path
from build123d import *

# ---------------- parameters (inch) ----------------
T = 0.12                      # plate thickness (Y)
H_W = 0.389790                # handle width
X_HEAD = -1.354007            # start of handle top edge (end of step 11)
X_END = 1.970605              # centre x of semicircular handle end
R_END = H_W / 2               # 0.194895 handle end radius
Z_MID = -R_END                # handle mid height
X_NECK = -0.703984            # end of handle bottom edge
R_NECK = 0.468750             # concave neck arc (15/32)
C_NECK = (-0.703984, -0.858540)
P_NECK_END = (-1.024250, -0.516259)
R_BACK = 0.707013             # outer back of head
C_BACK = (-1.507307, 0.0)
P_BACK_END = (-2.159435, -0.273121)
R_TIP = 0.078125              # hook tip round (5/64)
C_TIP = (-2.087375, -0.242941)
P_TIP_END = (-2.104284, -0.166668)
X_LEFT = -2.165500            # leftmost point
P_HOOK_TOP = (-1.931443, -0.128350)
P_PIN_TIP = (-1.864243, -0.193720)
P_PIN_UNDER = (-1.922674, -0.215905)
R_JAW = 0.312500              # jaw radius (5/16) -> 0.625 nut
C_JAW = (-1.696750, 0.0)
P_JAW_END = (-1.411824, -0.128350)

# slot F2
SLOT_C1 = 1.918717
SLOT_C2 = 1.944702
SLOT_R = 0.064965
SLOT_ZC = Z_MID

# rounds F3/F4
R_RND = 0.015625              # edge round (1/64)
X_RND_START = -0.441484       # straight round starts (full radius)
RUNOUT_HALF_ANGLE = 10.0      # deg, conical run-out
X_RUNOUT_END = -0.478189      # run-out back to sharp edge


def P(x, z):
    return Vector(x, 0, z)


def arc_mid(c, r, p0, p1, ccw):
    """Midpoint of arc about centre c from p0 to p1 (in x,z), ccw sense seen in (x,z)."""
    a0 = math.atan2(p0[1] - c[1], p0[0] - c[0])
    a1 = math.atan2(p1[1] - c[1], p1[0] - c[0])
    if ccw:
        while a1 <= a0:
            a1 += 2 * math.pi
    else:
        while a1 >= a0:
            a1 -= 2 * math.pi
    am = (a0 + a1) / 2
    return (c[0] + r * math.cos(am), c[1] + r * math.sin(am))


def build():
    p_top0 = (X_HEAD, 0.0)
    p_top1 = (X_END, 0.0)
    p_bot1 = (X_END, -H_W)
    p_bot0 = (X_NECK, -H_W)

    e = []
    e.append(Edge.make_line(P(*p_top0), P(*p_top1)))                              # 1
    e.append(Edge.make_three_point_arc(P(*p_top1), P(X_END + R_END, Z_MID), P(*p_bot1)))  # 2
    e.append(Edge.make_line(P(*p_bot1), P(*p_bot0)))                              # 3
    m4 = arc_mid(C_NECK, R_NECK, p_bot0, P_NECK_END, ccw=True)
    e.append(Edge.make_three_point_arc(P(*p_bot0), P(*m4), P(*P_NECK_END)))        # 4
    e.append(Edge.make_three_point_arc(P(*P_NECK_END), P(C_BACK[0], -R_BACK), P(*P_BACK_END)))  # 5
    e.append(Edge.make_three_point_arc(P(*P_BACK_END), P(X_LEFT, C_TIP[1]), P(*P_TIP_END)))     # 6
    e.append(Edge.make_line(P(*P_TIP_END), P(*P_HOOK_TOP)))                        # 7
    e.append(Edge.make_line(P(*P_HOOK_TOP), P(*P_PIN_TIP)))                        # 8
    e.append(Edge.make_line(P(*P_PIN_TIP), P(*P_PIN_UNDER)))                       # 9
    m10 = arc_mid(C_JAW, R_JAW, P_PIN_UNDER, P_JAW_END, ccw=True)
    e.append(Edge.make_three_point_arc(P(*P_PIN_UNDER), P(*m10), P(*P_JAW_END)))   # 10
    e.append(Edge.make_line(P(*P_JAW_END), P(*p_top0)))                            # 11

    face = Face(Wire(e))
    body = extrude(face, amount=T / 2, both=True)

    # F2 obround slot through Y
    slot_face = Plane.XZ * Pos((SLOT_C1 + SLOT_C2) / 2, SLOT_ZC) * SlotCenterToCenter(
        SLOT_C2 - SLOT_C1, 2 * SLOT_R)
    body -= extrude(slot_face, amount=T, both=True)

    # F3/F4 rounds: removal bodies for the corner (+Y, top) then mirrored
    yc = T / 2 - R_RND            # 0.044375  round centre line Y
    zc = -R_RND                   # -0.015625 round centre line Z (top)
    ext = 0.02                    # overshoot of removal box outside the plate
    tan_a = math.tan(math.radians(RUNOUT_HALF_ANGLE))
    x_cone0 = X_RUNOUT_END - 0.012                # cone extended past sharp point
    r_cone0 = R_RND + tan_a * (X_RND_START - x_cone0)
    x_box0 = X_RUNOUT_END - 0.006

    box = Pos((x_box0 + X_END) / 2, yc + (T / 2 + ext - yc) / 2, zc + (0 + ext - zc) / 2) * Box(
        X_END - x_box0, T / 2 + ext - yc, ext - zc)
    axis_pl = Plane(origin=(X_RND_START, yc, zc), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    cyl = axis_pl * Cylinder(R_RND, X_END - X_RND_START + 0.01,
                             align=(Align.CENTER, Align.CENTER, Align.MIN))
    cone_pl = Plane(origin=(x_cone0, yc, zc), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    cone = cone_pl * Cone(r_cone0, R_RND, X_RND_START - x_cone0,
                          align=(Align.CENTER, Align.CENTER, Align.MIN))
    corner = box - cyl - cone

    # toroidal round around the semicircular end
    rho0 = R_END - R_RND          # 0.179270
    sq = Pos(X_END + rho0 + (R_END + ext - rho0) / 2, yc + (T / 2 + ext - yc) / 2, Z_MID) * \
        Rectangle(R_END + ext - rho0, T / 2 + ext - yc)
    circ = Pos(X_END + rho0, yc, Z_MID) * Circle(R_RND)
    prof = sq - circ                                   # in XY plane at z = Z_MID
    ring = revolve(prof, Axis((X_END, 0, Z_MID), (0, 1, 0)), 360)
    half = Pos(X_END + 1, 0, Z_MID) * Box(2, 1, 2)     # keep x >= X_END
    torus_cut = ring & half

    cut_pos = corner + torus_cut
    # mirror for bottom edge (about z = Z_MID) and for -Y face
    cut_bot = cut_pos.mirror(Plane.XY.offset(Z_MID))
    cuts = [cut_pos, cut_bot, cut_pos.mirror(Plane.XZ), cut_bot.mirror(Plane.XZ)]
    for c in cuts:
        body -= c
    body.label = "P01 Spanner"
    return body


if __name__ == "__main__":
    part = build()
    out = Path(__file__).with_name("final.step")
    export_step(part, str(out))
    s = part.solids()
    bb = part.bounding_box()
    com = part.center(CenterOf.MASS)
    print("solids", len(s), "faces", len(part.faces()), "valid", part.is_valid)
    print("volume %.6f area %.6f" % (part.volume, part.area))
    print("com %.6f %.6f %.6f" % (com.X, com.Y, com.Z))
    print("bbox", bb.min, bb.max)
