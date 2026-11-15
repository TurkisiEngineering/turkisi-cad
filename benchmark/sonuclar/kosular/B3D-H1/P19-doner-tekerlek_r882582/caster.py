"""
Swivel plate caster, 4 in wheel, foot-pedal total lock  --  build123d 0.11.1
Rebuild of girdi/spec.md.  Units: INCH, global frame of spec section 1 (+Y up,
swivel axis = Y axis, wheel axis = line x=1.515, y=-0.75 parallel to Z).

Run:  python caster.py            -> writes final.step (AP214, inch) next to this file
Every body is built in place (identity placement); 12 solids in total.
"""
import math
import os
import sys

from build123d import (Axis, Box, Compound, Cylinder, Edge, Face, GeomType, Location,
                       Plane, Pos, Solid, Unit, Vector, Wire, export_step, extrude,
                       fillet, mirror, revolve)

# ----------------------------------------------------------------------------
# Named parameters (inch)
# ----------------------------------------------------------------------------
# global frame
PLATE_TOP_Y = 2.75            # mounting face
WHEEL_X, WHEEL_Y = 1.515, -0.75   # wheel axis (parallel to Z)
WHEEL_R = 2.0                 # wheel radius (bottom at y = -2.75)

# P01 fork
FORK_HALF_W = 1.029           # outer flat faces z = +/-1.029, crown radius
RIDGE_HALF_W = 1.133          # ridge band top z = +/-1.133, crown ring radius
GAP_HALF_W = 0.83             # inner faces of the legs / crown inner radius
DECK_TOP_Y = 2.464            # flat top of the deck
DECK_CEIL_Y = 2.184           # ceiling of the U
GAP_END_X = 2.4615            # gap end wall (pedal back face)
LEG_END_X = 3.6885            # leg end face
TOP_ARC_C, TOP_ARC_R = (0.13847, -6.14324), 8.622   # convex sloping deck top
CEIL_ARC_R = 8.342            # ceiling arc (concentric with the top arc)
FRONT_ARC_C, FRONT_ARC_R = (-1.46454, -1.09977), 2.5  # concave front edge of legs
KINGPIN_HOLE_R = 0.5          # fork kingpin hole (dia 1.0)
AXLE_BORE_R = 0.3             # fork axle bore (dia 0.6)
FORK_ROUND_R = 0.06           # F10 outer-face / top rounds
FORK_LEGEND_ROUND_R = 0.125   # F10 leg end vertical edges (see build_log)
RIDGE_ROUND_R = 0.04          # F10 ridge top rounds

# P02 top plate
PLATE_HALF_L, PLATE_HALF_W = 1.8125, 1.25   # 3.625 x 2.5
PLATE_T = 0.1
PLATE_CORNER_R = 0.25
SLOT_W = 0.3125
SLOT_X_IN, SLOT_X_OUT, SLOT_Z = 1.40625, 1.53125, 0.875
PRESS_R = 0.75                # pressed centre replaces plate inside r = 0.75

# P03 kingpin
LUG_TOP_Y = 2.6
LUG_BOSS_R, LUG_FILLET_R = 0.063, 0.0394

# P04 / P05
WASHER_R_OUT, WASHER_Y0, WASHER_Y1 = 0.872, 2.464, 2.539
HEX_AF, HEX_Y0, HEX_Y1 = 1.51, 2.539, 2.614

# P06 pedal
STEM_HALF_W = 0.825
FOOT_HALF_W = 1.05
FOOT_X0, FOOT_X1 = 3.6885, 4.2985
FOOT_ROUND_R = 0.04
FOOT_MID_Y = 1.5195           # foot plate side profile symmetric about this height
RIB_R = 0.025
STEM_RIB_HALF_L, FOOT_RIB_HALF_L = 0.675, 0.875
STEM_RIBS = [(2.5865, 2.1107), (2.7115, 2.0682), (2.8365, 2.0334)]
FOOT_RIBS = [(3.7885, 1.7045), (3.8885, 1.7140), (3.9885, 1.7376)]

# wheel
TREAD_RI, TREAD_RO, TREAD_HALF_W, TREAD_ROUND_R = 1.56375, 2.0, 0.625, 0.2
INSERT_RI = 1.51375
CORE_R, CORE_HALF_W = 1.51375, 0.3125
FL_HUB_R = 0.305
FL_RIM_Z = 0.6106             # rim cylinder from z=0.3125 to 0.6106
FL_DISH_R, FL_DISH_CZ = 3.75269, 2.92770   # dish torus (tube radius, centre-circle z)
FL_ROUND_R = 0.02
FL_HUB_ROUND_Z = 0.8049

# H1 axle pin
PIN_R, PIN_HALF_L = 0.3, 1.034

BIG = 20.0


# ----------------------------------------------------------------------------
# Profile helpers
# ----------------------------------------------------------------------------
def _arc_mid(p0, p1, c, d):
    a0 = math.atan2(p0[1] - c[1], p0[0] - c[0])
    a1 = math.atan2(p1[1] - c[1], p1[0] - c[0])
    r = math.hypot(p0[0] - c[0], p0[1] - c[1])
    if d == "ccw":
        da = (a1 - a0) % (2 * math.pi)
    elif d == "cw":
        da = -((a0 - a1) % (2 * math.pi))
    else:  # short way
        da = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
    am = a0 + da / 2
    return (c[0] + r * math.cos(am), c[1] + r * math.sin(am))


def profile(start, segs, to3d):
    """Closed planar face. segs: ('L', p) | ('A', p, centre, 'cw'|'ccw'|None).
    The contour is closed with a line back to start if needed."""
    edges = []
    cur = start
    for s in segs:
        if s[0] == "L":
            edges.append(Edge.make_line(Vector(*to3d(*cur)), Vector(*to3d(*s[1]))))
        else:
            _, p, c, d = s
            m = _arc_mid(cur, p, c, d)
            edges.append(Edge.make_three_point_arc(Vector(*to3d(*cur)), Vector(*to3d(*m)),
                                                   Vector(*to3d(*p))))
        cur = s[1]
    if math.hypot(cur[0] - start[0], cur[1] - start[1]) > 1e-9:
        edges.append(Edge.make_line(Vector(*to3d(*cur)), Vector(*to3d(*start))))
    return Face(Wire(edges))


XY = lambda a, b: (a, b, 0.0)                       # side view / (r, y) half-section


def XZ(y0):                                           # top view at height y0
    return lambda a, b: (a, y0, b)


WH = lambda rho, z: (WHEEL_X + rho, WHEEL_Y, z)       # (rho, z) about the wheel axis
WHEEL_AXIS = Axis((WHEEL_X, WHEEL_Y, 0), (0, 0, 1))


def zslab(face, half):
    """extrude an XY-plane face symmetrically to |z| <= half"""
    return extrude(face, amount=half, both=True)


def yprism(face_xz, y0, y1):
    return extrude(face_xz, amount=y1 - y0, dir=(0, 1, 0))


def ycyl(r, y0, y1, x=0.0, z=0.0):
    return Solid.make_cylinder(r, y1 - y0, Plane((x, y0, z), z_dir=(0, 1, 0)))


def zcyl(r, z0, z1, x, y):
    return Solid.make_cylinder(r, z1 - z0, Plane((x, y, z0), z_dir=(0, 0, 1)))


def solid_of(shape):
    sols = shape.solids()
    if len(sols) != 1:
        print(f"  WARNING: {len(sols)} solids, keeping the largest", file=sys.stderr)
    return max(sols, key=lambda s: s.volume)


def try_fillet(shape, edges, r, what):
    try:
        out = fillet(edges, r) if not isinstance(shape, Solid) else shape.fillet(r, edges)
        if out.is_valid and out.volume > 0:
            print(f"  fillet OK: {what} ({len(edges)} edges, R{r})")
            return out
        print(f"  fillet INVALID: {what}", file=sys.stderr)
    except Exception as ex:  # noqa: BLE001
        print(f"  fillet FAILED: {what}: {ex}", file=sys.stderr)
    return shape


def _tangent_seam(e, faces_of):
    """True for straight edges between two tangent faces (no fillet wanted)."""
    fs = faces_of(e)
    if len(fs) != 2:
        return False
    p = e.position_at(0.5)
    n0, n1 = fs[0].normal_at(p), fs[1].normal_at(p)
    return n0.dot(n1) > 0.999


# ----------------------------------------------------------------------------
# P01 Fork
# ----------------------------------------------------------------------------
def build_fork():
    # F1 outer side profile P_out
    p_out = profile((1.01841, -0.80829), [
        ("A", (1.515, -1.25), (WHEEL_X, WHEEL_Y), "ccw"),
        ("A", (2.0658, -0.6992), (1.515, -0.6992), "ccw"),
        ("L", (2.06496, 0.58138)),
        ("A", (2.72879, 1.25219), (2.74786, 0.56946), "cw"),
        ("L", (3.54269, 1.27493)),
        ("A", (LEG_END_X, 1.42487), (3.5385, 1.42487), "ccw"),
        ("L", (LEG_END_X, 1.61657)),
        ("A", (3.5987, 1.75396), (3.5385, 1.61657), "ccw"),
        ("A", (1.28005, 2.40286), TOP_ARC_C, "ccw"),
        ("L", (1.221, DECK_TOP_Y)),
        ("L", (-1.2, DECK_TOP_Y)),
        ("L", (-1.2, 1.3862)),
        ("A", (1.01841, -0.80829), FRONT_ARC_C, "cw"),
    ], XY)
    outer = zslab(p_out, FORK_HALF_W)
    trim = Box(BIG, BIG, BIG).moved(Location((BIG / 2, 0, 0))) + ycyl(FORK_HALF_W, -BIG / 2, BIG / 2)
    outer = solid_of(outer & trim)

    # F10 R0.06 rounds: every edge of OUTER except tangent seams (x = 0 lines)
    edges = [e for e in outer.edges() if not _tangent_seam(e, lambda ed: [f for f in outer.faces() if ed in f.edges()])]
    # the edges between the flat faces and the top/bevel: the bevel/top crossing
    # edge (parallel to Z) stays sharp per spec
    def keep(e):
        if e.geom_type == GeomType.LINE:
            d = e.tangent_at(0.5)
            if abs(d.Z) > 0.999:     # edges parallel to Z (top/bevel crossing) - sharp
                return False
        return True
    edges = [e for e in edges if keep(e)]
    outer = try_fillet(outer, edges, FORK_ROUND_R, "fork outer R0.06")

    # F2 ridge
    r_xy = profile((-1.2, 2.098), [
        ("L", (0.21544, 2.098)),
        ("A", (0.42225, 2.08144), (0.21544, 0.798), "cw"),
        ("A", (1.656, 0.314), (0.18362, 0.60055), "cw"),
        ("A", (1.286, 0.314), (1.471, 0.314), "cw"),
        ("A", (1.2176, 0.66736), (-0.40784, 0.16942), "ccw"),
        ("A", (-0.21661, 1.728), (-0.21661, 0.228), "ccw"),
        ("L", (-1.2, 1.728)),
    ], XY)
    ridge = zslab(r_xy, RIDGE_HALF_W)
    trim2 = Box(BIG, BIG, BIG).moved(Location((BIG / 2, 0, 0))) + ycyl(RIDGE_HALF_W, -BIG / 2, BIG / 2)
    ridge = solid_of(ridge & trim2)
    redges = [e for e in ridge.edges()
              if not _tangent_seam(e, lambda ed: [f for f in ridge.faces() if ed in f.edges()])]
    ridge = try_fillet(ridge, redges, RIDGE_ROUND_R, "ridge R0.04")

    fork = solid_of(outer + ridge)

    # F3 gap between the legs
    gap_xy = profile((0.0, -BIG / 2), [
        ("L", (0.0, DECK_CEIL_Y)),
        ("L", (1.10215, DECK_CEIL_Y)),
        ("L", (1.14698, 2.13758)),
        ("A", (GAP_END_X, 1.86879), TOP_ARC_C, "cw"),
        ("L", (GAP_END_X, BIG / 2)),
        ("L", (BIG / 2, BIG / 2)),
        ("L", (BIG / 2, -BIG / 2)),
    ], XY)
    gap = zslab(gap_xy, GAP_HALF_W) + ycyl(GAP_HALF_W, -BIG / 2, DECK_CEIL_Y)
    fork = fork - gap
    # F4 kingpin hole, F5 axle bore
    fork = fork - ycyl(KINGPIN_HOLE_R, DECK_CEIL_Y - 0.5, DECK_TOP_Y + 0.5)
    fork = fork - zcyl(AXLE_BORE_R, -BIG / 2, BIG / 2, WHEEL_X, WHEEL_Y)
    return solid_of(fork)


# ----------------------------------------------------------------------------
# P02 Top plate
# ----------------------------------------------------------------------------
def build_plate():
    y0, y1 = PLATE_TOP_Y - PLATE_T, PLATE_TOP_Y
    plate = Box(2 * PLATE_HALF_L, PLATE_T, 2 * PLATE_HALF_W).moved(Location((0, (y0 + y1) / 2, 0)))
    vert = [e for e in plate.edges() if e.geom_type == GeomType.LINE and abs(e.tangent_at(0.5).Y) > 0.999]
    plate = plate.fillet(PLATE_CORNER_R, vert)
    # T2 slots (obround along X)
    r = SLOT_W / 2
    for sx in (-1, 1):
        for sz in (-1, 1):
            xa, xb, z = sx * SLOT_X_IN, sx * SLOT_X_OUT, sz * SLOT_Z
            slot = ycyl(r, y0 - 0.1, y1 + 0.1, xa, z) + ycyl(r, y0 - 0.1, y1 + 0.1, xb, z) + \
                Box(abs(xb - xa), PLATE_T + 0.2, SLOT_W).moved(Location(((xa + xb) / 2, (y0 + y1) / 2, z)))
            plate = plate - slot
    # T3 pressed centre
    plate = plate - ycyl(PRESS_R, y0 - 0.1, y1 + 0.1)
    sec = profile((0.719, 2.75), [
        ("A", (0.57754, 2.70610), (0.719, 2.5), None),
        ("L", (0.37560, 2.56750)),
        ("A", (0.3595, 2.55860), (0.319, 2.65), None),
        ("L", (0.3595, 2.502)),
        ("L", (0.3605, 2.502)),
        ("A", (0.3755, 2.487), (0.3605, 2.487), None),
        ("L", (0.3755, 2.45330)),
        ("A", (0.40660, 2.46750), (0.35, 2.55), None),
        ("L", (0.60855, 2.60610)),
        ("A", (PRESS_R, 2.65), (0.75, 2.4), None),
        ("L", (PRESS_R, 2.75)),
    ], XY)
    centre = revolve(sec, Axis.Y, 360)
    plate = plate + centre
    return solid_of(plate.clean())


# ----------------------------------------------------------------------------
# P03 Kingpin
# ----------------------------------------------------------------------------
def build_kingpin():
    sec = profile((0.0, 2.136), [
        ("L", (0.236, 2.0728)),
        ("L", (0.236, 1.7767)),
        ("L", (0.2557, 1.757)),
        ("L", (0.2732, 1.757)),
        ("L", (0.29285, 1.7767)),
        ("L", (0.29285, 2.367)),
        ("A", (0.30785, 2.382), (0.30785, 2.367), None),
        ("L", (0.3605, 2.382)),
        ("A", (0.3755, 2.397), (0.3605, 2.397), None),
        ("L", (0.3755, 2.487)),
        ("A", (0.3605, 2.502), (0.3605, 2.487), None),
        ("L", (0.3115, 2.502)),
        ("A", (0.2965, 2.517), (0.3115, 2.517), None),
        ("L", (0.2965, 2.7303)),
        ("L", (0.2768, 2.75)),
        ("L", (0.0, 2.75)),
    ], XY)
    pin = revolve(sec, Axis.Y, 360)
    # K2 anti-rotation lug, plan outline in (x, z)
    y0 = 2.502
    lug = profile((-0.2832, 0.0878), [
        ("A", (-0.3115, 0.0612), (-0.3208, 0.0995), None),
        ("A", (-0.3115, -0.0612), (-0.2965, 0.0), None),
        ("A", (-0.2832, -0.0878), (-0.3208, -0.0995), None),
        ("A", (-0.2832, 0.0878), (0.0, 0.0), None),
    ], XZ(y0))
    lug = yprism(lug, y0, LUG_TOP_Y)
    return solid_of((pin + lug).clean())


# ----------------------------------------------------------------------------
# P04 washer, P05 hex ring
# ----------------------------------------------------------------------------
def build_washer():
    sec = profile((0.401, WASHER_Y0), [
        ("L", (WASHER_R_OUT, WASHER_Y0)),
        ("L", (WASHER_R_OUT, WASHER_Y1)),
        ("L", (0.5107, WASHER_Y1)),
        ("L", (0.4066, 2.4675)),
        ("A", (0.401, WASHER_Y0), (0.35, 2.55), None),
    ], XY)
    return solid_of(revolve(sec, Axis.Y, 360))


def build_hex():
    rc = HEX_AF / 2 / math.cos(math.radians(30))
    pts = [(rc * math.cos(math.radians(60 * i)), rc * math.sin(math.radians(60 * i))) for i in range(6)]
    hexf = profile(pts[0], [("L", p) for p in pts[1:]], XZ(HEX_Y0))
    ring = yprism(hexf, HEX_Y0, HEX_Y1)
    bore = profile((0.0, HEX_Y0), [
        ("L", (0.5107, HEX_Y0)),
        ("L", (0.60855, 2.6061)),
        ("A", (0.6208, HEX_Y1), (0.75, 2.4), None),
        ("L", (0.0, HEX_Y1)),
    ], XY)
    return solid_of(ring - revolve(bore, Axis.Y, 360))


# ----------------------------------------------------------------------------
# P06 Brake pedal
# ----------------------------------------------------------------------------
def build_pedal():
    stem = profile((GAP_END_X, 1.18953), [
        ("L", (GAP_END_X, 2.15992)),
        ("A", (3.5987, 1.75396), TOP_ARC_C, "cw"),
        ("A", (3.60992, 1.74847), (3.5385, 1.6166), "cw"),
        ("A", (FOOT_X0, 1.714), (0.03345, -6.51039), "cw"),
        ("L", (FOOT_X0, 1.42487)),
        ("A", (3.54269, 1.27493), (3.5385, 1.42487), "cw"),
        ("L", (2.72879, 1.25219)),
        ("A", (GAP_END_X, 1.18953), (2.74786, 0.56946), "ccw"),
    ], XY)
    stem = zslab(stem, STEM_HALF_W)

    side = profile((FOOT_X0, 1.38078), [
        ("L", (FOOT_X0, 1.65822)),
        ("A", (3.74187, 1.70811), (3.7385, 1.65822), "cw"),
        ("A", (4.08040, 1.77815), (3.7857, 2.3496), "ccw"),
        ("A", (FOOT_X1, 1.6445), (4.1485, 1.6445), "cw"),
        ("L", (FOOT_X1, 1.3945)),
        ("A", (4.0804, 1.26085), (4.1485, 1.3945), "cw"),
        ("A", (3.74187, 1.33089), (3.7857, 0.6894), "ccw"),
        ("A", (FOOT_X0, 1.38078), (3.7385, 1.38078), "cw"),
    ], XY)
    side = zslab(side, FOOT_HALF_W)
    yb = 1.0
    plan = profile((FOOT_X0, -1.01), [
        ("L", (FOOT_X0, 1.01)),
        ("A", (3.7285, 1.05), (3.7285, 1.01), None),
        ("L", (3.8139, 1.05)),
        ("A", (3.94710, 1.01157), (3.8139, 0.8), None),
        ("A", (4.25988, 0.69922), (3.4144, 0.1653), None),
        ("A", (FOOT_X1, 0.5657), (4.0485, 0.5657), None),
        ("L", (FOOT_X1, -0.5657)),
        ("A", (4.25988, -0.69922), (4.0485, -0.5657), None),
        ("A", (3.94710, -1.01157), (3.4144, -0.1653), None),
        ("A", (3.8139, -1.05), (3.8139, -0.8), None),
        ("L", (3.7285, -1.05)),
        ("A", (FOOT_X0, -1.01), (3.7285, -1.01), None),
    ], XZ(yb))
    plan = yprism(plan, yb, 2.0)
    foot = solid_of(side & plan)
    # B2 rounds R0.04 between plan side faces and profile top/bottom surfaces
    def is_round_edge(e):
        bb = e.bounding_box()
        if bb.max.X < FOOT_X0 + 1e-6 or bb.min.X > FOOT_X1 - 1e-6:   # in end planes
            return False
        if e.geom_type == GeomType.LINE:   # straight seams (along Y or along Z)
            return False
        return True
    # OCC fails on the lower edges directly, but the side profile is exactly
    # symmetric about y = FOOT_MID_Y: round the upper edges, keep the upper half
    # and mirror it to make the lower half.
    fedges = [e for e in foot.edges() if is_round_edge(e) and e.bounding_box().min.Y > FOOT_MID_Y]
    foot_r = try_fillet(foot, fedges, FOOT_ROUND_R, "foot plate R0.04 (upper edges)")
    if foot_r is not foot:
        upper = solid_of(foot_r & Box(BIG, BIG, BIG).moved(Location((0, FOOT_MID_Y + BIG / 2, 0))))
        lower = solid_of(mirror(upper, Plane((0, FOOT_MID_Y, 0), z_dir=(0, 1, 0))))
        foot = solid_of((upper + lower).clean())

    pedal = stem + foot
    # B3 grip ribs
    for (x, y) in STEM_RIBS:
        pedal = pedal + zcyl(RIB_R, -STEM_RIB_HALF_L, STEM_RIB_HALF_L, x, y)
    for (x, y) in FOOT_RIBS:
        pedal = pedal + zcyl(RIB_R, -FOOT_RIB_HALF_L, FOOT_RIB_HALF_L, x, y)
    return solid_of(pedal.clean())


# ----------------------------------------------------------------------------
# Wheel P07..P10, axle H1
# ----------------------------------------------------------------------------
def build_tread():
    rr = TREAD_ROUND_R
    zc = TREAD_HALF_W - rr
    sec = profile((TREAD_RI, -TREAD_HALF_W), [
        ("L", (TREAD_RO - rr, -TREAD_HALF_W)),
        ("A", (TREAD_RO, -zc), (TREAD_RO - rr, -zc), None),
        ("L", (TREAD_RO, zc)),
        ("A", (TREAD_RO - rr, TREAD_HALF_W), (TREAD_RO - rr, zc), None),
        ("L", (TREAD_RI, TREAD_HALF_W)),
    ], WH)
    return solid_of(revolve(sec, WHEEL_AXIS, 360))


def build_insert():
    return solid_of(zcyl(TREAD_RI, -TREAD_HALF_W, TREAD_HALF_W, WHEEL_X, WHEEL_Y)
                    - zcyl(INSERT_RI, -1, 1, WHEEL_X, WHEEL_Y))


def build_core():
    return solid_of(zcyl(CORE_R, -CORE_HALF_W, CORE_HALF_W, WHEEL_X, WHEEL_Y))


def build_flange_a():
    C = (FL_HUB_R, FL_DISH_CZ)                       # dish centre (rho, z)
    c_rim = (CORE_R - FL_ROUND_R, -FL_RIM_Z)
    c_hub = (FL_HUB_R + FL_ROUND_R, -FL_HUB_ROUND_Z)

    def tpt(c):  # internal tangency point of the R0.02 round with the dish arc
        dx, dy = c[0] - C[0], c[1] - C[1]
        L = math.hypot(dx, dy)
        return (C[0] + dx / L * FL_DISH_R, C[1] + dy / L * FL_DISH_R)

    t_rim, t_hub = tpt(c_rim), tpt(c_hub)
    sec = profile((FL_HUB_R, -CORE_HALF_W), [
        ("L", (CORE_R, -CORE_HALF_W)),
        ("L", (CORE_R, -FL_RIM_Z)),
        ("A", t_rim, c_rim, None),
        ("A", t_hub, C, None),
        ("A", (FL_HUB_R, -FL_HUB_ROUND_Z), c_hub, None),
    ], WH)
    return solid_of(revolve(sec, WHEEL_AXIS, 360))


def build_pin():
    return solid_of(zcyl(PIN_R, -PIN_HALF_L, PIN_HALF_L, WHEEL_X, WHEEL_Y))


# ----------------------------------------------------------------------------
def build_all():
    parts = {}
    for name, fn in [("P01_Fork", build_fork), ("P02_TopPlate", build_plate),
                     ("P03_Kingpin", build_kingpin), ("P04_BearingWasher", build_washer),
                     ("P05_HexBearingRing", build_hex), ("P06_BrakePedal", build_pedal),
                     ("P07_WheelTread", build_tread), ("P08_WheelInsertRing", build_insert),
                     ("P09_WheelCoreDisc", build_core), ("P10a_CoreFlange_negZ", build_flange_a),
                     ("H1_AxlePin", build_pin)]:
        print(f"building {name}")
        parts[name] = fn()
    fa = parts["P10a_CoreFlange_negZ"]
    parts["P10b_CoreFlange_posZ"] = solid_of(mirror(fa, Plane.XY))
    order = ["P01_Fork", "P02_TopPlate", "P03_Kingpin", "P04_BearingWasher", "P05_HexBearingRing",
             "P06_BrakePedal", "P07_WheelTread", "P08_WheelInsertRing", "P09_WheelCoreDisc",
             "P10a_CoreFlange_negZ", "P10b_CoreFlange_posZ", "H1_AxlePin"]
    out = []
    for n in order:
        s = parts[n]
        s.label = n
        out.append(s)
    return out


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    solids = build_all()
    asm = Compound(children=solids)
    asm.label = "swivel_plate_caster_4in"
    path = os.path.join(here, "final.step")
    # model coordinates are inches; write the STEP length unit as INCH too
    # (without this OCCT converts to its default output unit, mm)
    from OCP.Interface import Interface_Static
    from OCP.STEPControl import STEPControl_Controller
    STEPControl_Controller.Init_s()
    Interface_Static.SetCVal_s("write.step.schema", "AP214IS")
    Interface_Static.SetCVal_s("write.step.unit", "INCH")
    export_step(asm, path, unit=Unit.IN)
    print("wrote", path)
