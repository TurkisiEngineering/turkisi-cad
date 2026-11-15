"""Manual dovetail positioning slide with lead screw and handwheel.

build123d 0.11.1 rebuild of girdi/spec.md.
Units: INCH. Global frame exactly as in spec section 1 (+Y up, Z = travel, z = 0 at the
far end face of the base, screw axis x = 0, y = Y0). Every part is built in place.

Run:  python model.py            -> writes final.step (AP214, inch) next to this script
      python model.py --check    -> also prints the measurement table (see measure.py)
"""
import copy
import math
import sys
from pathlib import Path

from build123d import (
    Axis, Box, Compound, Cylinder, Edge, Face, Helix, Line, Location, Plane, Polyline,
    ThreePointArc, Unit, Vector, Wire, export_step, revolve, sweep, Align, Solid, Part,
)

# --------------------------------------------------------------------------------------
# Parameters (inch)
# --------------------------------------------------------------------------------------
Y0 = 0.0424438                 # screw axis height (y); x = 0
# P01 base
BASE_L = 4.0
BASE_W = 2.5
BASE_YBOT = Y0 - 0.437         # -0.39456 mounting face
BASE_YTOP = Y0 + 0.313         # 0.35544
WAY_TOP_HALF = 0.66249         # dovetail opening half width at base top
WAY_FLOOR_Y = Y0 - 0.062       # -0.01956
WAY_FLOOR_HALF = 0.87900       # dovetail floor half width (undercut, 60 deg flanks)
GROOVE_HALF = 0.562            # centre groove half width
GROOVE_FLOOR_Y = Y0 - 0.177    # -0.13456
MOUNT_HOLES_XZ = [(-0.343, 0.5), (0.343, 3.5)]
CSK_DIA = 0.385
CSK_BOT_Y = -0.24212           # 82 deg countersink bottom
MOUNT_HOLE_DIA = 0.198
END_HOLE_X = 1.031
END_HOLE_Y = WAY_FLOOR_Y       # -0.01956
END_HOLE_DIA = 0.164           # major dia of the #8 thread (not modelled)
END_HOLE_DEPTH = 0.625
# P02 carriage
CAR_Z0, CAR_Z1 = 1.5, 4.0
CAR_TOP_Y = Y0 + 0.368         # 0.41044
CAR_TOP_HALF = 0.62308
CAR_UNDER_Y = Y0 - 0.049       # -0.00656
CAR_FLANK_BOT_HALF = 0.86383
CHAN_BOT_HALF = 0.56452
CHAN_TOP_HALF = 0.43750
CHAN_CEIL_Y = Y0 + 0.171       # 0.21344
CROWN_R = 0.312
CROWN_C = (0.0, -0.05356)
CROWN_X = 0.16142
STRIP_Z = [(1.6, 2.1), (3.4, 3.9)]
STRIP_ROUND_R = 0.01
NUT_Z = 2.75
NUT_DIA = 0.995
TOP_HOLES_Z = [1.718, 2.156, 3.344, 3.78]
TOP_HOLE_DIA = 0.164
F5_P1, F5_P2 = (0.59562, -0.00656), (0.56437, -0.00631)   # source sliver plane (+X side)
F5_Z = [(1.5, 2.3125), (3.1875, 4.0)]
# P03 drive nut
NUT_YBOT = -0.11156
# P04 end block
EB_Z0, EB_Z1 = 4.0, 4.625
EB_YBOT, EB_YTOP = -0.38456, 0.40544
EB_CLEAR_DIA = 0.201
EB_BORE = [(4.0, 4.155, 0.28125), (4.155, 4.375, 0.339), (4.375, 4.625, 0.375)]  # (z0, z1, dia)
# P05 end plate
EP_Z0, EP_Z1 = -0.062, 0.0
EP_YBOT, EP_YTOP = -0.38456, 0.35544
EP_HOLE_DIA = 0.185
# P06 lead screw
LS_Z0, LS_ZT, LS_Z1 = 0.5, 4.0, 5.0     # start, end of thread section, shaft end
LS_MAJOR_R = 0.125
LS_CHAMFER_R0 = 0.08711                 # end-face radius of 30 deg end chamfer
LS_CHAMFER_Z = 0.56563
LS_SHAFT_R = 0.109
PITCH = 0.05
ROOT_R = 0.09252
ROOT_HALF_LAND = 0.003125
FLANK_ANGLE = 30.0                      # from radial direction
GROOVE_OUT_R = 0.13                     # groove tool continued past the crest (< pitch overlap)
ROOT_Z_PHASE = 0.515625                 # root centre at theta = 0
GROOVE_START_K = -2                     # sweep starts fully outside the z = 0.5 end
GROOVE_END_K, GROOVE_END_THETA = 69, 270.0   # stops at theta 270, root centre z = 4.003125
GROOVE_CHUNK_TURNS = 8.0                # sweep split in chunks (robust booleans)
# P07 handwheel
HW_PROFILE = [(4.687, 0), (4.687, 0.335), (5.062, 0.335), (5.062, 0.855), (5.082, 0.875),
              (5.417, 0.875), (5.437, 0.855), (5.437, 0)]
# P08 crank handle
CRANK_Y = Y0 - 0.631                    # -0.58856
# H1 button-head screw
H1_SHANK_L = 0.6871
H1_SHANK_R = 0.082
H1_HEAD_R = 0.187
H1_HEAD_H = 0.1
H1_POSES = {
    "H1-a": ((END_HOLE_X, END_HOLE_Y, 4.625), (1, 0, 0), (0, 0, 1)),
    "H1-b": ((-END_HOLE_X, END_HOLE_Y, 4.625), (1, 0, 0), (0, 0, 1)),
    "H1-c": ((END_HOLE_X, END_HOLE_Y, -0.062), (1, 0, 0), (0, 0, -1)),
    "H1-d": ((-END_HOLE_X, END_HOLE_Y, -0.062), (1, 0, 0), (0, 0, -1)),
}
BIG = 10.0


# --------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------
def arc_mid(c, p, q, r=None):
    """Midpoint of the minor arc centred at c from p to q (2D)."""
    a0 = math.atan2(p[1] - c[1], p[0] - c[0])
    a1 = math.atan2(q[1] - c[1], q[0] - c[0])
    d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
    am = a0 + d / 2
    if r is None:
        r = 0.5 * (math.dist(c, p) + math.dist(c, q))
    return (c[0] + r * math.cos(am), c[1] + r * math.sin(am))


def profile_face(segs, to3d):
    """segs: list of ('L', p) or ('A', centre, p) in 2D, starting point = first ('L', p).
    to3d maps a 2D point to a 3D Vector. Returns a planar Face."""
    edges = []
    cur = segs[0][1]
    start = cur
    for s in segs[1:] + [("L", start)]:
        if s[0] == "L":
            nxt = s[1]
            if math.dist(cur, nxt) > 1e-9:
                edges.append(Edge.make_line(to3d(cur), to3d(nxt)))
        elif s[0] == "S":                      # exact arc sampled into a B-spline
            c, nxt = s[1], s[2]
            r0 = math.dist(c, cur)
            r1 = math.dist(c, nxt)
            a0 = math.atan2(cur[1] - c[1], cur[0] - c[0])
            a1 = math.atan2(nxt[1] - c[1], nxt[0] - c[0])
            d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
            n = 48
            pts = [cur] + [(c[0] + (r0 + (r1 - r0) * i / n) * math.cos(a0 + d * i / n),
                            c[1] + (r0 + (r1 - r0) * i / n) * math.sin(a0 + d * i / n))
                           for i in range(1, n)] + [nxt]
            edges.append(Edge.make_spline([to3d(p) for p in pts]))
        elif s[0] == "A":
            c, nxt = s[1], s[2]
            m = s[3] if len(s) > 3 else arc_mid(c, cur, nxt)
            edges.append(Edge.make_three_point_arc(to3d(cur), to3d(m), to3d(nxt)))
        cur = nxt
    return Face(Wire(edges))


def xy_extrude(segs, z0, z1):
    """Cross-section in (x, y), extruded along +Z from z0 to z1."""
    f = profile_face(segs, lambda p: Vector(p[0], p[1], z0))
    return Solid.extrude(f, Vector(0, 0, z1 - z0))


def poly(pts):
    return [("L", p) for p in pts]


def revolve_zr(segs, ax_x, ax_y):
    """Revolve profile given in (z, r) about the axis parallel to Z through (ax_x, ax_y)."""
    f = profile_face(segs, lambda p: Vector(ax_x + p[1], ax_y, p[0]))
    return Solid.revolve(f, 360, Axis((ax_x, ax_y, 0), (0, 0, 1)))


def zcyl(r, z0, z1, x, y):
    return Solid.make_cylinder(r, z1 - z0, Plane(origin=(x, y, z0), z_dir=(0, 0, 1)))


def ycyl(r, y0, y1, x, z):
    return Solid.make_cylinder(r, y1 - y0, Plane(origin=(x, y0, z), x_dir=(1, 0, 0), z_dir=(0, 1, 0)))


def box(x0, x1, y0, y1, z0, z1):
    return Solid.make_box(x1 - x0, y1 - y0, z1 - z0, Plane(origin=(x0, y0, z0)))


# --------------------------------------------------------------------------------------
# P01 Base
# --------------------------------------------------------------------------------------
def make_base():
    sec = [(-BASE_W / 2, BASE_YBOT), (BASE_W / 2, BASE_YBOT), (BASE_W / 2, BASE_YTOP),
           (WAY_TOP_HALF, BASE_YTOP), (WAY_FLOOR_HALF, WAY_FLOOR_Y), (GROOVE_HALF, WAY_FLOOR_Y),
           (GROOVE_HALF, GROOVE_FLOOR_Y), (-GROOVE_HALF, GROOVE_FLOOR_Y),
           (-GROOVE_HALF, WAY_FLOOR_Y), (-WAY_FLOOR_HALF, WAY_FLOOR_Y),
           (-WAY_TOP_HALF, BASE_YTOP), (-BASE_W / 2, BASE_YTOP)]
    base = xy_extrude(poly(sec), 0.0, BASE_L)
    # F2 countersunk mounting holes (axis // Y). Tool profile in (y, r), extended a bit
    # into the groove air above and below the underside.
    for hx, hz in MOUNT_HOLES_XZ:
        prof = [(GROOVE_FLOOR_Y + 0.05, 0), (GROOVE_FLOOR_Y + 0.05, CSK_DIA / 2),
                (GROOVE_FLOOR_Y, CSK_DIA / 2), (CSK_BOT_Y, MOUNT_HOLE_DIA / 2),
                (BASE_YBOT - 0.05, MOUNT_HOLE_DIA / 2), (BASE_YBOT - 0.05, 0)]
        f = profile_face(poly(prof), lambda p, hx=hx, hz=hz: Vector(hx + p[1], p[0], hz))
        tool = Solid.revolve(f, 360, Axis((hx, 0, hz), (0, 1, 0)))
        base = base - tool
    # F3 end holes (axis // Z), flat bottoms
    for sx in (-1, 1):
        base = base - zcyl(END_HOLE_DIA / 2, -0.1, END_HOLE_DEPTH, sx * END_HOLE_X, END_HOLE_Y)
        base = base - zcyl(END_HOLE_DIA / 2, BASE_L - END_HOLE_DEPTH, BASE_L + 0.1,
                           sx * END_HOLE_X, END_HOLE_Y)
    return base


# --------------------------------------------------------------------------------------
# P02 Carriage (with integral wear strips)
# --------------------------------------------------------------------------------------
def make_carriage():
    segs = [("L", (-CAR_TOP_HALF, CAR_TOP_Y)),
            ("L", (CAR_TOP_HALF, CAR_TOP_Y)),
            ("L", (CAR_FLANK_BOT_HALF, CAR_UNDER_Y)),
            ("L", (CHAN_BOT_HALF, CAR_UNDER_Y)),
            ("L", (CHAN_TOP_HALF, CHAN_CEIL_Y)),
            ("L", (CROWN_X, CHAN_CEIL_Y)),
            ("A", CROWN_C, (-CROWN_X, CHAN_CEIL_Y), (0.0, CROWN_C[1] + CROWN_R)),
            ("L", (-CHAN_TOP_HALF, CHAN_CEIL_Y)),
            ("L", (-CHAN_BOT_HALF, CAR_UNDER_Y)),
            ("L", (-CAR_FLANK_BOT_HALF, CAR_UNDER_Y))]
    car = xy_extrude(segs, CAR_Z0, CAR_Z1)
    # F2 wear strips (+X profile, mirrored for -X)
    rc = (0.86210, WAY_FLOOR_Y + STRIP_ROUND_R)
    for sx in (1, -1):
        m = lambda p, sx=sx: (sx * p[0], p[1])
        strip = [("L", m((0.56542, CAR_UNDER_Y))),
                 ("L", m((0.56542, WAY_FLOOR_Y))),
                 ("L", m((0.86210, WAY_FLOOR_Y))),
                 ("A", m(rc), m((0.87076, -0.00456))),
                 ("L", m((0.66291, BASE_YTOP))),
                 ("L", m((0.65685, 0.35194))),
                 ("L", m((CAR_FLANK_BOT_HALF, CAR_UNDER_Y)))]
        for z0, z1 in STRIP_Z:
            car = car + xy_extrude(strip, z0, z1)
    # F3 nut bore, F4 top holes (through all Y)
    car = car - ycyl(NUT_DIA / 2, -1, 1, 0.0, NUT_Z)
    for hz in TOP_HOLES_Z:
        car = car - ycyl(TOP_HOLE_DIA / 2, -1, 1, 0.0, hz)
    # F5 source artefact (+X only): wedge sliver between y = CAR_UNDER_Y and the plane through
    # (0.59562, -0.00656) and (0.56437, -0.00631); cut after the strips are joined, which leaves
    # a 0.00025 in wedge gap above the +X strips (this reproduces the source surface area).
    (ax, ay), (bx, by) = F5_P1, F5_P2
    slope = (by - ay) / (bx - ax)
    x_in = 0.50                                    # well inside the channel air
    tri = [(ax, CAR_UNDER_Y), (ax + (x_in - ax), CAR_UNDER_Y), (x_in, ay + slope * (x_in - ax))]
    for z0, z1 in F5_Z:
        car = car - xy_extrude(poly(tri), z0, z1)
    return car


# --------------------------------------------------------------------------------------
# P03 drive nut, P04 end block, P05 end plate
# --------------------------------------------------------------------------------------
def make_nut():
    return ycyl(NUT_DIA / 2, NUT_YBOT, CAR_TOP_Y, 0.0, NUT_Z)


def make_end_block():
    eb = box(-BASE_W / 2, BASE_W / 2, EB_YBOT, EB_YTOP, EB_Z0, EB_Z1)
    for sx in (-1, 1):
        eb = eb - zcyl(EB_CLEAR_DIA / 2, EB_Z0 - 0.1, EB_Z1 + 0.1, sx * END_HOLE_X, END_HOLE_Y)
    for z0, z1, d in EB_BORE:
        eb = eb - zcyl(d / 2, z0 - (0.1 if z0 == EB_Z0 else 0), z1 + (0.1 if z1 == EB_Z1 else 0), 0.0, Y0)
    return eb


def make_end_plate():
    ep = box(-BASE_W / 2, BASE_W / 2, EP_YBOT, EP_YTOP, EP_Z0, EP_Z1)
    for sx in (-1, 1):
        ep = ep - zcyl(EP_HOLE_DIA / 2, EP_Z0 - 0.1, EP_Z1 + 0.1, sx * END_HOLE_X, END_HOLE_Y)
    return ep


# --------------------------------------------------------------------------------------
# P06 lead screw with modelled helical groove
# --------------------------------------------------------------------------------------
def make_lead_screw():
    blank = revolve_zr(poly([(LS_Z0, 0), (LS_Z0, LS_CHAMFER_R0), (LS_CHAMFER_Z, LS_MAJOR_R),
                             (LS_ZT, LS_MAJOR_R), (LS_ZT, 0)]), 0.0, Y0)
    # Cut the groove in an axially longer cylinder (sweep caps / crossings of the end faces
    # make OCCT booleans fail silently), then intersect with the true blank (chamfer, z <= 4).
    work = zcyl(LS_MAJOR_R, LS_Z0 - 0.3, LS_ZT + 0.3, 0.0, Y0)
    tanf = math.tan(math.radians(FLANK_ANGLE))
    hw_out = ROOT_HALF_LAND + (GROOVE_OUT_R - ROOT_R) * tanf
    z_start = ROOT_Z_PHASE + PITCH * GROOVE_START_K           # theta = 0
    total_turns = (GROOVE_END_K - GROOVE_START_K) + GROOVE_END_THETA / 360.0
    done = 0.0
    while done < total_turns - 1e-9:
        n = min(GROOVE_CHUNK_TURNS, total_turns - done)
        z0 = z_start + done * PITCH
        helix = Helix(PITCH, PITCH * n, ROOT_R, center=(0, Y0, z0), direction=(0, 0, 1))
        prof = Face(Wire.make_polygon(
            [Vector(r, Y0, z0 + dz) for r, dz in
             [(ROOT_R, -ROOT_HALF_LAND), (ROOT_R, ROOT_HALF_LAND),
              (GROOVE_OUT_R, hw_out), (GROOVE_OUT_R, -hw_out)]], close=True))
        groove = sweep(prof, helix, is_frenet=True)
        work = work - groove
        done += n
    threaded = work & blank
    shaft = zcyl(LS_SHAFT_R, LS_ZT, LS_Z1, 0.0, Y0)
    s = threaded + shaft
    return s.solids()[0] if len(s.solids()) == 1 else s


# --------------------------------------------------------------------------------------
# P07 handwheel, P08 crank handle
# --------------------------------------------------------------------------------------
def make_handwheel():
    return revolve_zr(poly(HW_PROFILE), 0.0, Y0)


def make_crank():
    c1 = (5.87399, 1.34309)
    p1, q1 = (5.59303, 0.125), (6.15495, 0.125)
    c2 = (6.43771, 0.00051)
    p2, q2 = (6.43699, 0.125), (6.5622, 0.0)
    segs = [("L", (5.437, 0.0)), ("L", (5.437, 0.125)), ("L", p1),
            ("A", c1, q1), ("L", (6.43699, 0.125)),
            # end arc: centre 0.00051 off the axis -> an exact revolve is a spindle torus that
            # does not survive STEP round-trip; use a 48-point B-spline of the exact arc instead.
            ("S", c2, q2)]
    return revolve_zr(segs, 0.0, CRANK_Y)


# --------------------------------------------------------------------------------------
# H1 button-head screw
# --------------------------------------------------------------------------------------
def make_h1_local():
    c = (0.05434, -0.05)
    segs = [("L", (0.0, -H1_SHANK_L)), ("L", (H1_SHANK_R, -H1_SHANK_L)), ("L", (H1_SHANK_R, 0.0)),
            ("L", (H1_HEAD_R, 0.0)), ("L", (H1_HEAD_R, 0.02)), ("A", c, (0.05434, H1_HEAD_H)),
            ("L", (0.0, H1_HEAD_H))]
    f = profile_face(segs, lambda p: Vector(p[0], 0.0, p[1]))     # (r, w) -> local (x, z)
    return Solid.revolve(f, 360, Axis((0, 0, 0), (0, 0, 1)))


def place(shape, origin, u, w):
    return shape.moved(Location(Plane(origin=origin, x_dir=u, z_dir=w)))


# --------------------------------------------------------------------------------------
def build():
    parts = {
        "P01_Base": make_base(),
        "P02_Carriage": make_carriage(),
        "P03_Drive_nut": make_nut(),
        "P04_End_block": make_end_block(),
        "P05_End_plate": make_end_plate(),
        "P06_Lead_screw": make_lead_screw(),
        "P07_Handwheel": make_handwheel(),
        "P08_Crank_handle": make_crank(),
    }
    h1 = make_h1_local()
    for name, (o, u, w) in H1_POSES.items():
        parts[name.replace("-", "_")] = place(copy.deepcopy(h1), o, u, w)   # independent bodies
    for name, p in parts.items():
        p.label = name
    return parts


def export(parts, path):
    from OCP.Interface import Interface_Static
    from OCP.STEPControl import STEPControl_Controller
    STEPControl_Controller.Init_s()
    Interface_Static.SetCVal_s("write.step.schema", "AP214IS")
    Interface_Static.SetCVal_s("write.step.unit", "INCH")
    asm = Compound(children=list(parts.values()), label="dovetail_slide")
    export_step(asm, str(path), unit=Unit.IN)


if __name__ == "__main__":
    out = Path(__file__).with_name("final.step")
    parts = build()
    export(parts, out)
    print("written", out)
    if "--check" in sys.argv:
        from measure import report
        report(parts)
