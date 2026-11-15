"""P01 Spanner - hook spanner wrench for side-slot round nuts (P17).

build123d 0.11.1. Units: inches. Global frame per spec.md:
plate between Y=-0.06..+0.06, outline in XZ plane, handle along +X, Z<=0.
Run:  python spanner.py   -> writes final.step next to this script.
"""
from math import tan, radians, sqrt
from pathlib import Path

from build123d import (
    Vector, Edge, Wire, Face, Solid, Plane, Axis, Location, Pos, Box, Cylinder,
    Mode, export_step, import_step, Unit,
)

# ---------------------------------------------------------------- parameters
T = 0.12                      # plate thickness (Y)
Y0 = -T / 2                   # plate lower face

# handle
X_HEAD_TOP = -1.354007        # start of handle top edge (Z=0)
X_END_C = 1.970605            # handle end semicircle centre X
R_END = 0.194895              # handle end radius (= half handle width)
W_HANDLE = 2 * R_END          # 0.389790 handle width
Z_MID = -R_END                # handle mid-height

# head
X_NECK = -0.703984            # end of handle bottom edge
R_NECK = 0.468750             # concave neck arc (15/32)
P_NECK_END = (-1.024250, -0.516259)
R_BACK = 0.707013             # outer back of head
C_BACK = (-1.507307, 0.0)
P_BACK_END = (-2.159435, -0.273121)
R_TIP = 0.078125              # hook tip round (5/64)
C_TIP = (-2.087375, -0.242941)
P_TIP_END = (-2.104284, -0.166668)
P_HOOK_TOP = (-1.931443, -0.128350)
P_PIN_TIP = (-1.864243, -0.193720)
P_PIN_UNDER = (-1.922674, -0.215905)
R_JAW = 0.3125                # jaw radius (fits 0.625 dia nut)
C_JAW = (-1.696750, 0.0)
P_JAW_END = (-1.411824, -0.128350)

# hanging slot
SLOT_C1 = 1.918717
SLOT_C2 = 1.944702
SLOT_R = 0.064965

# edge rounds and run-out
R_ROUND = 0.015625            # 1/64
X_ROUND_START = -0.441484     # full round starts here
RUNOUT_ANGLE = 10.0           # cone half-angle, deg
X_RUNOUT = -0.478189          # run-out back to sharp


def P(x, z):
    return Vector(x, 0, z)


def arc_mid(c, r, a, b, convex_dir=None):
    """Point on circle (c,r) halfway (by angle) between points a and b, short way."""
    ca, cb = Vector(*a) - Vector(*c), Vector(*b) - Vector(*c)
    m = (ca.normalized() + cb.normalized()).normalized() * r
    return (c[0] + m.X, c[1] + m.Y)


# ---------------------------------------------------------------- F1 outline
def outline_face():
    e = []
    e.append(Edge.make_line(P(X_HEAD_TOP, 0), P(X_END_C, 0)))                       # 1
    e.append(Edge.make_three_point_arc(P(X_END_C, 0), P(X_END_C + R_END, Z_MID),
                                       P(X_END_C, -W_HANDLE)))                      # 2
    e.append(Edge.make_line(P(X_END_C, -W_HANDLE), P(X_NECK, -W_HANDLE)))           # 3
    c_neck = (X_NECK, -W_HANDLE - R_NECK)
    m = arc_mid(c_neck, R_NECK, (X_NECK, -W_HANDLE), P_NECK_END)
    e.append(Edge.make_three_point_arc(P(X_NECK, -W_HANDLE), P(*m), P(*P_NECK_END)))  # 4
    e.append(Edge.make_three_point_arc(P(*P_NECK_END), P(C_BACK[0], -R_BACK),
                                       P(*P_BACK_END)))                             # 5
    e.append(Edge.make_three_point_arc(P(*P_BACK_END), P(C_TIP[0] - R_TIP, C_TIP[1]),
                                       P(*P_TIP_END)))                              # 6 (leftmost pt)
    e.append(Edge.make_line(P(*P_TIP_END), P(*P_HOOK_TOP)))                         # 7
    e.append(Edge.make_line(P(*P_HOOK_TOP), P(*P_PIN_TIP)))                         # 8
    e.append(Edge.make_line(P(*P_PIN_TIP), P(*P_PIN_UNDER)))                        # 9
    m = arc_mid(C_JAW, R_JAW, P_PIN_UNDER, P_JAW_END)
    e.append(Edge.make_three_point_arc(P(*P_PIN_UNDER), P(*m), P(*P_JAW_END)))      # 10
    e.append(Edge.make_line(P(*P_JAW_END), P(X_HEAD_TOP, 0)))                       # 11
    return Face(Wire(e))


def slot_face():
    zt, zb = Z_MID + SLOT_R, Z_MID - SLOT_R
    e = [
        Edge.make_line(P(SLOT_C1, zt), P(SLOT_C2, zt)),
        Edge.make_three_point_arc(P(SLOT_C2, zt), P(SLOT_C2 + SLOT_R, Z_MID), P(SLOT_C2, zb)),
        Edge.make_line(P(SLOT_C2, zb), P(SLOT_C1, zb)),
        Edge.make_three_point_arc(P(SLOT_C1, zb), P(SLOT_C1 - SLOT_R, Z_MID), P(SLOT_C1, zt)),
    ]
    return Face(Wire(e))


def extrude_y(face):
    """Extrude a face lying in Y=0 to Y=-T/2..+T/2."""
    f = face.moved(Location((0, Y0, 0)))
    return Solid.extrude(f, Vector(0, T, 0))


# ---------------------------------------------------------------- F3/F4 cutters
BIG = 0.1                      # outward over-size of cutter boxes
YC = T / 2 - R_ROUND           # 0.044375 round centre-line |Y|


def straight_cutter_top_pos():
    """Corner material at (Y=+0.06, Z=0) edge to remove, x from X_RUNOUT to X_END_C."""
    zc = -R_ROUND
    box = Solid.make_box(X_END_C - X_RUNOUT, BIG, BIG,
                         Plane((X_RUNOUT, YC, zc)))
    cyl = Solid.make_cylinder(R_ROUND, X_END_C - X_ROUND_START,
                              Plane((X_ROUND_START, YC, zc), z_dir=(1, 0, 0)))
    r_big = R_ROUND + tan(radians(RUNOUT_ANGLE)) * (X_ROUND_START - X_RUNOUT)
    cone = Solid.make_cone(r_big, R_ROUND, X_ROUND_START - X_RUNOUT,
                           Plane((X_RUNOUT, YC, zc), z_dir=(1, 0, 0)))
    return box - (cyl + cone), r_big


def end_cutter_pos():
    """Corner material around semicircular end on +Y face (toroidal round)."""
    ax_plane = Plane((X_END_C, YC, Z_MID), x_dir=(1, 0, 0), z_dir=(0, 1, 0))
    rc = R_END - R_ROUND       # 0.179270
    ring = (Solid.make_cylinder(R_END + BIG, BIG, ax_plane)
            - Solid.make_cylinder(rc, BIG, ax_plane))
    tor = Solid.make_torus(rc, R_ROUND, ax_plane)
    half = Solid.make_box(BIG * 4, BIG * 2, BIG * 8,
                          Plane((X_END_C, YC - 0.01, Z_MID - BIG * 4)))
    return (ring - tor) & half


def build():
    plate = extrude_y(outline_face()) - extrude_y(slot_face())

    top, r_big = straight_cutter_top_pos()
    end = end_cutter_pos()
    mirror_y = Plane.XZ          # Y -> -Y
    mirror_z = Plane((0, 0, Z_MID), z_dir=(0, 0, 1))  # Z about handle mid-height
    cutters = [top, top.mirror(mirror_z)]
    cutters += [c.mirror(mirror_y) for c in cutters]
    cutters += [end, end.mirror(mirror_y)]
    cut = cutters[0]
    for c in cutters[1:]:
        cut = cut + c
    part = plate - cut
    solids = part.solids()
    assert len(solids) == 1, f"expected one solid, got {len(solids)}"
    s = solids[0]
    s.label = "P01 Spanner"
    return s, r_big


if __name__ == "__main__":
    part, r_big = build()
    out = Path(__file__).with_name("final.step")
    # Write the STEP file natively in inches (CONVERSION_BASED_UNIT 'INCH'),
    # otherwise OCCT rescales to its default write unit (mm).
    from OCP.Interface import Interface_Static
    from OCP.STEPControl import STEPControl_Controller
    STEPControl_Controller.Init_s()
    Interface_Static.SetCVal_s("write.step.unit", "INCH")
    export_step(part, str(out), unit=Unit.IN)
    chk = import_step(str(out))           # importer returns mm
    print(f"STEP re-import: solids {len(chk.solids())}, faces {len(chk.faces())}, "
          f"volume {chk.volume / 25.4**3:.6f} in3")
    bb = part.bounding_box()
    com = part.center()
    print(f"run-out cone large radius = {r_big:.6f} (corner {sqrt(2)*R_ROUND:.6f})")
    print(f"volume {part.volume:.6f}  area {part.area:.6f}  faces {len(part.faces())}")
    print(f"CoM ({com.X:.6f}, {com.Y:.6f}, {com.Z:.6f})")
    print(f"bbox X {bb.min.X:.6f}..{bb.max.X:.6f} Y {bb.min.Y:.6f}..{bb.max.Y:.6f} "
          f"Z {bb.min.Z:.6f}..{bb.max.Z:.6f}")
    print("valid", part.is_valid)
    print("wrote", out)
