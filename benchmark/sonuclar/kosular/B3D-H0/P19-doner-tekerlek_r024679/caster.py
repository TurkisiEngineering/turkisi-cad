"""
Swivel plate caster, 4 in wheel, foot-pedal total lock  --  build123d 0.11.1
Units: INCH (model values are inches, STEP is written with INCH units).
Global frame per spec: +Y up, swivel axis = Y axis, wheel axis x=1.515, y=-0.75 // Z.

Run:  python caster.py            -> writes final.step next to this script
"""
import math
import sys
from pathlib import Path

from build123d import (Axis, Box, Compound, Cylinder, Edge, Face, Location, Plane, mirror,
                       Part, Pos, RegularPolygon, Solid, Unit, Vector, Wire,
                       export_step, extrude, revolve)
from OCP.BRepFilletAPI import BRepFilletAPI_MakeFillet
from OCP.TopAbs import TopAbs_EDGE, TopAbs_FACE
from OCP.TopExp import TopExp
from OCP.TopTools import TopTools_IndexedDataMapOfShapeListOfShape

# ----------------------------------------------------------------------------
# Named parameters (inches)
# ----------------------------------------------------------------------------
# global layout
PLATE_TOP_Y = 2.75            # mounting face
WHEEL_AX_X = 1.515            # swivel offset (trail)
WHEEL_AX_Y = -0.75            # wheel axis height
# fork P01
FORK_HALF_W = 1.029           # outer faces z = +/-
FORK_CROWN_R = 1.029          # crown round behind x=0
RIDGE_HALF_W = 1.133          # ridge top faces z = +/-
RIDGE_CROWN_R = 1.133
GAP_HALF_W = 0.83             # inner faces z = +/-
GAP_CROWN_R = 0.83
FORK_TOP_Y = 2.464
CEILING_Y = 2.184
DECK_R_OUT = 8.622            # convex top of deck
DECK_R_IN = 8.342             # ceiling arc
DECK_C = (0.13847, -6.14324)
GAP_END_X = 2.4615
LEG_END_X = 3.6885
FRONT_R = 2.5
FRONT_C = (-1.46454, -1.09977)
KINGPIN_HOLE_R = 0.5
AXLE_BORE_R = 0.3
FORK_ROUND_R = 0.06           # F10 outer face rounds
LEG_END_ROUND_R = 0.125       # F10 leg end vertical edges
RIDGE_ROUND_R = 0.04          # F10 ridge top edges
# top plate P02
PLATE_L = 3.625
PLATE_W = 2.5
PLATE_T = 0.1
PLATE_CORNER_R = 0.25
SLOT_W = 0.3125
SLOT_ARC_X = (1.40625, 1.53125)
SLOT_Z = 0.875
PRESS_R = 0.75                # pressed centre replaces plate inside r=0.75
# kingpin P03
LUG_TOP_Y = 2.6
LUG_BOT_Y = 2.502
LUG_BOSS_R = 0.063
LUG_FILLET_R = 0.0394
# washer P04 / hex ring P05
WASHER_R = 0.872
WASHER_Y = (2.464, 2.539)
HEX_AF = 1.51
HEX_Y = (2.539, 2.614)
# pedal P06
STEM_HALF_W = 0.825
FOOT_HALF_W = 1.05
FOOT_X = (3.6885, 4.2985)
PEDAL_ROUND_R = 0.04
RIB_R = 0.025
STEM_RIBS = [(2.5865, 2.1107), (2.7115, 2.0682), (2.8365, 2.0334)]
STEM_RIB_HALF_L = 0.675
FOOT_RIBS = [(3.7885, 1.7045), (3.8885, 1.7140), (3.9885, 1.7376)]
FOOT_RIB_HALF_L = 0.875
# wheel
TREAD_RO = 2.0
TREAD_RI = 1.56375
TREAD_HALF_W = 0.625
TREAD_ROUND_R = 0.2
INSERT_RI = 1.51375
CORE_R = 1.51375
CORE_HALF_W = 0.3125
FLANGE_HUB_R = 0.305
FLANGE_RIM_Z = 0.6106
FLANGE_DISH_R = 3.75269
FLANGE_DISH_CZ = 2.9277       # dish centre circle (rho=0.305, z=+2.9277) for P10-a
FLANGE_ROUND_R = 0.02
FLANGE_HUB_ROUND_Z = 0.8049
# axle pin H1
AXLE_R = 0.3
AXLE_HALF_L = 1.034

EPS = 1e-6


# ----------------------------------------------------------------------------
# 2D profile helpers
# ----------------------------------------------------------------------------
def _arc_mid(p0, c, p1, direction=None):
    a0 = math.atan2(p0[1] - c[1], p0[0] - c[0])
    a1 = math.atan2(p1[1] - c[1], p1[0] - c[0])
    r = 0.5 * (math.dist(p0, c) + math.dist(p1, c))
    if direction is None:
        d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
    elif direction == "ccw":
        d = (a1 - a0) % (2 * math.pi)
    elif direction == "cw":
        d = -((a0 - a1) % (2 * math.pi))
    else:
        raise ValueError(direction)
    am = a0 + d / 2
    return (c[0] + r * math.cos(am), c[1] + r * math.sin(am))


def profile_face(start, segs, to3d):
    """start=(u,v); segs: ('L',(u,v)) or ('A',centre,(u,v),dir|None).
    to3d maps (u,v)->(x,y,z). Returns a planar Face."""
    edges = []
    cur = start
    for s in segs:
        if s[0] == "L":
            nxt = s[1]
            edges.append(Edge.make_line(Vector(*to3d(cur)), Vector(*to3d(nxt))))
        else:
            _, c, nxt = s[0], s[1], s[2]
            d = s[3] if len(s) > 3 else None
            m = _arc_mid(cur, c, nxt, d)
            edges.append(Edge.make_three_point_arc(
                Vector(*to3d(cur)), Vector(*to3d(m)), Vector(*to3d(nxt))))
        cur = nxt
    if math.dist(cur, start) > 1e-9:
        edges.append(Edge.make_line(Vector(*to3d(cur)), Vector(*to3d(start))))
    return Face(Wire(edges))


XY = lambda p: (p[0], p[1], 0.0)                       # side view (x, y)
RY = lambda p: (p[0], p[1], 0.0)                       # half-section (r, y) about Y
def XZ_at(y0):                                          # top view (x, z) at height y0
    return lambda p: (p[0], y0, p[1])
WHEEL_AXIS = Axis((WHEEL_AX_X, WHEEL_AX_Y, 0), (0, 0, 1))
RHOZ = lambda p: (WHEEL_AX_X + p[0], WHEEL_AX_Y, p[1])  # half-section (rho, z)


def sym_z(face, half):
    """Extrude a face lying in z=0 symmetrically to |z|<=half."""
    return extrude(face, amount=half, both=True)


def along_y(face, y0, y1):
    """Extrude an (x,z) face lying at y=y0 up to y=y1."""
    return extrude(face, amount=y1 - y0, dir=(0, 1, 0))


def revolve_y(face):
    return revolve(face, axis=Axis.Y, revolution_arc=360)


def revolve_wheel(face):
    return revolve(face, axis=WHEEL_AXIS, revolution_arc=360)


def single_solid(shape):
    sols = shape.solids()
    if len(sols) != 1:
        raise RuntimeError(f"expected 1 solid, got {len(sols)}")
    return sols[0]


# --- topology helpers for fillets --------------------------------------------
def edge_face_map(shape):
    m = TopTools_IndexedDataMapOfShapeListOfShape()
    TopExp.MapShapesAndAncestors_s(shape.wrapped, TopAbs_EDGE, TopAbs_FACE, m)
    return m


def faces_of_edge(m, edge):
    idx = m.FindIndex(edge.wrapped)
    out = []
    if idx == 0:
        return out
    for f in m.FindFromIndex(idx):
        out.append(Face(f))
    return out


def fillet_multi(solid, radius_edges):
    """radius_edges: list of (radius, Edge). One BRepFilletAPI_MakeFillet run."""
    mk = BRepFilletAPI_MakeFillet(solid.wrapped)
    for r, e in radius_edges:
        mk.Add(r, e.wrapped)
    mk.Build()
    if not mk.IsDone():
        raise RuntimeError("fillet failed")
    return single_solid(Compound(mk.Shape()))


def face_normal(f):
    return f.normal_at(f.center())


def is_plane(f):
    return f.geom_type.name == "PLANE"


# ----------------------------------------------------------------------------
# P01 Fork
# ----------------------------------------------------------------------------
def fork_raw():
    A = (1.01841, -0.80829)
    p_out = profile_face(A, [
        ("A", (WHEEL_AX_X, WHEEL_AX_Y), (1.515, -1.25), "ccw"),
        ("A", (1.515, -0.6992), (2.0658, -0.6992), "ccw"),
        ("L", (2.06496, 0.58138)),
        ("A", (2.74786, 0.56946), (2.72879, 1.25219), "cw"),
        ("L", (3.54269, 1.27493)),
        ("A", (3.5385, 1.42487), (LEG_END_X, 1.42487), "ccw"),
        ("L", (LEG_END_X, 1.61657)),
        ("A", (3.5385, 1.61657), (3.5987, 1.75396), "ccw"),
        ("A", DECK_C, (1.28005, 2.40286), "ccw"),
        ("L", (1.221, FORK_TOP_Y)),
        ("L", (-1.2, FORK_TOP_Y)),
        ("L", (-1.2, 1.3862)),
        ("A", FRONT_C, A, "cw"),
    ], XY)
    outer = sym_z(p_out, FORK_HALF_W)
    keep_o = (Pos(3, 0, 0) * Box(6, 10, 6)) + Cylinder(FORK_CROWN_R, 10, rotation=(90, 0, 0))
    outer = outer & keep_o

    r_xy = profile_face((-1.2, 2.098), [
        ("L", (0.21544, 2.098)),
        ("A", (0.21544, 0.798), (0.42225, 2.08144), "cw"),
        ("A", (0.18362, 0.60055), (1.656, 0.314), "cw"),
        ("A", (1.471, 0.314), (1.286, 0.314), "cw"),
        ("A", (-0.40784, 0.16942), (1.2176, 0.66736), "ccw"),
        ("A", (-0.21661, 0.228), (-0.21661, 1.728), "ccw"),
        ("L", (-1.2, 1.728)),
    ], XY)
    ridge = sym_z(r_xy, RIDGE_HALF_W)
    keep_r = (Pos(3, 0, 0) * Box(6, 10, 6)) + Cylinder(RIDGE_CROWN_R, 10, rotation=(90, 0, 0))
    ridge = ridge & keep_r

    body = outer + ridge

    gap_prof = profile_face((0, -3), [
        ("L", (0, CEILING_Y)),
        ("L", (1.10215, CEILING_Y)),
        ("L", (1.14698, 2.13758)),
        ("A", DECK_C, (GAP_END_X, 1.86879), "cw"),
        ("L", (GAP_END_X, 4)),
        ("L", (6, 4)),
        ("L", (6, -3)),
    ], XY)
    gap = sym_z(gap_prof, GAP_HALF_W)
    gap_cyl = Pos(0, (CEILING_Y - 3) / 2, 0) * Cylinder(GAP_CROWN_R, CEILING_Y + 3,
                                                       rotation=(90, 0, 0))
    body = body - gap - gap_cyl
    # kingpin hole and axle bore
    body = body - Cylinder(KINGPIN_HOLE_R, 10, rotation=(90, 0, 0))
    body = body - Pos(WHEEL_AX_X, WHEEL_AX_Y, 0) * Cylinder(AXLE_BORE_R, 5)
    return single_solid(body)


def fork_fillet_edges(f):
    """Return (list_06_and_125, list_04) of (radius, Edge)."""
    m = edge_face_map(f)
    faces = f.faces()
    zpl = FORK_HALF_W
    outer_faces = [fc for fc in faces if is_plane(fc)
                   and abs(abs(face_normal(fc).Z) - 1) < 1e-6
                   and abs(abs(fc.center().Z) - zpl) < 1e-6]
    crown_faces = [fc for fc in faces if fc.geom_type.name == "CYLINDER"
                   and fc.bounding_box().max.X < 1e-4
                   and abs(fc.radius - FORK_CROWN_R) < 1e-6]
    top_faces = [fc for fc in faces if is_plane(fc)
                 and abs(fc.center().Y - FORK_TOP_Y) < 1e-6
                 and abs(face_normal(fc).Y - 1) < 1e-6]
    ridge_top = [fc for fc in faces if is_plane(fc)
                 and abs(abs(face_normal(fc).Z) - 1) < 1e-6
                 and abs(abs(fc.center().Z) - RIDGE_HALF_W) < 1e-6]
    ridge_ring = [fc for fc in faces if fc.geom_type.name == "CYLINDER"
                  and abs(fc.radius - RIDGE_CROWN_R) < 1e-6]

    def is_ridge_wall(fc):
        # ridge band walls reach out beyond the outer faces (|z| up to 1.133)
        bb = fc.bounding_box()
        return max(abs(bb.min.Z), abs(bb.max.Z)) > zpl + 1e-3 and \
            not any(fc.wrapped.IsSame(t.wrapped) for t in ridge_top)

    def is_x0_vertical(e):
        bb = e.bounding_box()
        return abs(bb.min.X) < 1e-4 and abs(bb.max.X) < 1e-4 and bb.max.Y - bb.min.Y > 1e-3 \
            and abs(bb.max.Z - bb.min.Z) < 1e-6

    sel06, sel125, sel04 = [], [], []
    seen = []

    def add(lst, e):
        for s in seen:
            if s.wrapped.IsSame(e.wrapped):
                return
        seen.append(e)
        lst.append(e)

    for fc in outer_faces:
        for e in fc.edges():
            nb = [g for g in faces_of_edge(m, e) if not g.wrapped.IsSame(fc.wrapped)]
            if not nb:
                continue
            g = nb[0]
            if g.geom_type.name == "CYLINDER" and abs(g.radius - AXLE_BORE_R) < 1e-6:
                continue                       # axle bore: no round
            if is_ridge_wall(g):
                continue                       # ridge foot: no round
            if any(g.wrapped.IsSame(c.wrapped) for c in crown_faces):
                continue                       # tangent seam at x=0
            bb = e.bounding_box()
            if abs(bb.min.X - LEG_END_X) < 1e-6 and abs(bb.max.X - LEG_END_X) < 1e-6:
                add(sel125, e)
            else:
                add(sel06, e)
    for fc in crown_faces:
        for e in fc.edges():
            if is_x0_vertical(e):
                continue
            nb = [g for g in faces_of_edge(m, e) if not g.wrapped.IsSame(fc.wrapped)]
            if not nb:
                continue
            g = nb[0]
            if is_ridge_wall(g) or any(g.wrapped.IsSame(r.wrapped) for r in ridge_ring):
                continue
            # ridge ring foot planes (y=1.728 / 2.098) and R1.5 wall: skip
            gbb = g.bounding_box()
            if gbb.min.Y > 1.70 and gbb.max.Y < 2.10 + 1e-6 and \
                    not any(g.wrapped.IsSame(t.wrapped) for t in top_faces):
                continue
            add(sel06, e)
    for fc in ridge_top + ridge_ring:
        for e in fc.edges():
            if is_x0_vertical(e):
                continue
            nb = [g for g in faces_of_edge(m, e) if not g.wrapped.IsSame(fc.wrapped)]
            if not nb:
                continue
            g = nb[0]
            if any(g.wrapped.IsSame(r.wrapped) for r in ridge_top + ridge_ring):
                continue
            add(sel04, e)
    return sel06, sel125, sel04


def make_fork(rounds=True):
    f = fork_raw()
    if not rounds:
        return f, "no rounds"
    s06, s125, s04 = fork_fillet_edges(f)
    note = []
    try:
        f1 = fillet_multi(f, [(LEG_END_ROUND_R, e) for e in s125] +
                          [(FORK_ROUND_R, e) for e in s06])
        note.append(f"R0.06 x{len(s06)} + R0.125 x{len(s125)} ok")
    except Exception as ex:  # fallback: R0.06 only
        try:
            f1 = fillet_multi(f, [(FORK_ROUND_R, e) for e in s06 + s125])
            note.append(f"combined failed ({ex}); R0.06 on all incl. leg end")
        except Exception as ex2:
            f1 = f
            note.append(f"outer rounds failed ({ex2})")
    # ridge top rounds on the new solid: re-select
    if f1 is not f:
        _, _, s04 = fork_fillet_edges(f1)
    try:
        f2 = fillet_multi(f1, [(RIDGE_ROUND_R, e) for e in s04])
        note.append(f"R0.04 x{len(s04)} ok")
    except Exception as ex:
        f2 = f1
        note.append(f"ridge rounds failed ({ex})")
    return f2, "; ".join(note)


# ----------------------------------------------------------------------------
# P02 Top plate
# ----------------------------------------------------------------------------
def make_plate():
    y0, y1 = PLATE_TOP_Y - PLATE_T, PLATE_TOP_Y
    hx, hz, rc = PLATE_L / 2, PLATE_W / 2, PLATE_CORNER_R
    cx, cz = hx - rc, hz - rc
    outline = profile_face((hx, -cz), [
        ("L", (hx, cz)), ("A", (cx, cz), (cx, hz)),
        ("L", (-cx, hz)), ("A", (-cx, cz), (-hx, cz)),
        ("L", (-hx, -cz)), ("A", (-cx, -cz), (-cx, -hz)),
        ("L", (cx, -hz)), ("A", (cx, -cz), (hx, -cz)),
    ], XZ_at(y0))
    plate = along_y(outline, y0, y1)
    rs = SLOT_W / 2
    for sx in (-1, 1):
        for sz in (-1, 1):
            a, b = sorted((sx * SLOT_ARC_X[0], sx * SLOT_ARC_X[1]))
            z0 = sz * SLOT_Z
            slot = profile_face((a, z0 - rs), [
                ("L", (b, z0 - rs)), ("A", (b, z0), (b, z0 + rs), "ccw"),
                ("L", (a, z0 + rs)), ("A", (a, z0), (a, z0 - rs), "ccw"),
            ], XZ_at(y0 - 0.1))
            plate = plate - along_y(slot, y0 - 0.1, y1 + 0.1)
    plate = plate - Pos(0, (y0 + y1) / 2, 0) * Cylinder(PRESS_R, 1, rotation=(90, 0, 0))
    sec = profile_face((PRESS_R, y1), [
        ("L", (0.719, y1)),
        ("A", (0.719, 2.5), (0.57754, 2.70610)),
        ("L", (0.37560, 2.56750)),
        ("A", (0.319, 2.65), (0.3595, 2.55860)),
        ("L", (0.3595, 2.502)),
        ("L", (0.3605, 2.502)),
        ("A", (0.3605, 2.487), (0.3755, 2.487)),
        ("L", (0.3755, 2.45330)),
        ("A", (0.35, 2.55), (0.40660, 2.46750)),
        ("L", (0.60855, 2.60610)),
        ("A", (0.75, 2.4), (PRESS_R, y0)),
    ], RY)
    plate = plate + revolve_y(sec)
    return single_solid(plate.clean() if hasattr(plate, "clean") else plate)


# ----------------------------------------------------------------------------
# P03 Kingpin
# ----------------------------------------------------------------------------
def make_kingpin():
    sec = profile_face((0, 2.136), [
        ("L", (0.236, 2.0728)),
        ("L", (0.236, 1.7767)),
        ("L", (0.2557, 1.757)),
        ("L", (0.2732, 1.757)),
        ("L", (0.29285, 1.7767)),
        ("L", (0.29285, 2.367)),
        ("A", (0.30785, 2.367), (0.30785, 2.382)),
        ("L", (0.3605, 2.382)),
        ("A", (0.3605, 2.397), (0.3755, 2.397)),
        ("L", (0.3755, 2.487)),
        ("A", (0.3605, 2.487), (0.3605, 2.502)),
        ("L", (0.3115, 2.502)),
        ("A", (0.3115, 2.517), (0.2965, 2.517)),
        ("L", (0.2965, 2.7303)),
        ("L", (0.2768, PLATE_TOP_Y)),
        ("L", (0, PLATE_TOP_Y)),
    ], RY)
    pin = revolve_y(sec)
    lug = profile_face((-0.2832, 0.0878), [
        ("A", (-0.3208, 0.0995), (-0.3115, 0.0612)),
        ("A", (-0.2965, 0.0), (-0.3115, -0.0612), "ccw"),
        ("A", (-0.3208, -0.0995), (-0.2832, -0.0878)),
        ("A", (0.0, 0.0), (-0.2832, 0.0878)),
    ], XZ_at(LUG_BOT_Y))
    pin = pin + along_y(lug, LUG_BOT_Y, LUG_TOP_Y)
    return single_solid(pin)


# ----------------------------------------------------------------------------
# P04 Bearing washer, P05 hex bearing ring
# ----------------------------------------------------------------------------
def make_washer():
    sec = profile_face((0.401, WASHER_Y[0]), [
        ("L", (WASHER_R, WASHER_Y[0])),
        ("L", (WASHER_R, WASHER_Y[1])),
        ("L", (0.5107, WASHER_Y[1])),
        ("L", (0.4066, 2.4675)),
        ("A", (0.35, 2.55), (0.401, WASHER_Y[0])),
    ], RY)
    return single_solid(revolve_y(sec))


def make_hex_ring():
    rc = HEX_AF / 2 / math.cos(math.radians(30))
    pts = [(rc * math.cos(math.radians(60 * i)), rc * math.sin(math.radians(60 * i)))
           for i in range(6)]
    hexf = profile_face(pts[0], [("L", p) for p in pts[1:]], XZ_at(HEX_Y[0]))
    ring = along_y(hexf, HEX_Y[0], HEX_Y[1])
    bore = profile_face((0, HEX_Y[0]), [
        ("L", (0.5107, HEX_Y[0])),
        ("L", (0.60855, 2.6061)),
        ("A", (0.75, 2.4), (0.6208, HEX_Y[1])),
        ("L", (0, HEX_Y[1])),
    ], RY)
    return single_solid(ring - revolve_y(bore))


# ----------------------------------------------------------------------------
# P06 Brake pedal
# ----------------------------------------------------------------------------
def make_pedal(rounds=True):
    stem = profile_face((GAP_END_X, 1.18953), [
        ("L", (GAP_END_X, 2.15992)),
        ("A", DECK_C, (3.5987, 1.75396), "cw"),
        ("A", (3.5385, 1.6166), (3.60992, 1.74847), "cw"),
        ("A", (0.03345, -6.51039), (LEG_END_X, 1.714), "cw"),
        ("L", (LEG_END_X, 1.42487)),
        ("A", (3.5385, 1.42487), (3.54269, 1.27493), "cw"),
        ("L", (2.72879, 1.25219)),
        ("A", (2.74786, 0.56946), (GAP_END_X, 1.18953), "ccw"),
    ], XY)
    stem = sym_z(stem, STEM_HALF_W)

    side = profile_face((FOOT_X[0], 1.38078), [
        ("L", (FOOT_X[0], 1.65822)),
        ("A", (3.7385, 1.65822), (3.74187, 1.70811), "cw"),
        ("A", (3.7857, 2.3496), (4.08040, 1.77815), "ccw"),
        ("A", (4.1485, 1.6445), (FOOT_X[1], 1.6445), "cw"),
        ("L", (FOOT_X[1], 1.3945)),
        ("A", (4.1485, 1.3945), (4.0804, 1.26085), "cw"),
        ("A", (3.7857, 0.6894), (3.74187, 1.33089), "ccw"),
        ("A", (3.7385, 1.38078), (FOOT_X[0], 1.38078), "cw"),
    ], XY)
    side = sym_z(side, FOOT_HALF_W)
    plan = profile_face((FOOT_X[0], -1.01), [
        ("L", (FOOT_X[0], 1.01)),
        ("A", (3.7285, 1.01), (3.7285, 1.05)),
        ("L", (3.8139, 1.05)),
        ("A", (3.8139, 0.8), (3.94710, 1.01157)),
        ("A", (3.4144, 0.1653), (4.25988, 0.69922)),
        ("A", (4.0485, 0.5657), (FOOT_X[1], 0.5657)),
        ("L", (FOOT_X[1], -0.5657)),
        ("A", (4.0485, -0.5657), (4.25988, -0.69922)),
        ("A", (3.4144, -0.1653), (3.94710, -1.01157)),
        ("A", (3.8139, -0.8), (3.8139, -1.05)),
        ("L", (3.7285, -1.05)),
        ("A", (3.7285, -1.01), (FOOT_X[0], -1.01)),
    ], XZ_at(1.0))
    plan = along_y(plan, 1.0, 2.0)
    foot = single_solid(side & plan)
    note = "no rounds"
    if rounds:
        # OCC fails on the +z chain (numerical sliver edge at the tangent back
        # corner), so: round the -z half, cut at z=0, mirror, fuse.
        sel = [e for e in foot_round_edges(foot) if e.center().Z < 0]
        try:
            half = fillet_multi(foot, [(PEDAL_ROUND_R, e) for e in sel])
            half = half & (Pos(4, 1.5, -1.5) * Box(2, 2, 3))
            foot = single_solid((half + mirror(half, about=Plane.XY)).clean())
            note = f"foot plate R0.04 x{len(sel)} (-z half, mirrored) ok"
        except Exception as ex:
            note = f"foot plate rounds failed ({ex})"
    ped = stem + foot
    for (x, y) in STEM_RIBS:
        ped = ped + Pos(x, y, 0) * Cylinder(RIB_R, 2 * STEM_RIB_HALF_L)
    for (x, y) in FOOT_RIBS:
        ped = ped + Pos(x, y, 0) * Cylinder(RIB_R, 2 * FOOT_RIB_HALF_L)
    return single_solid(ped), note


def foot_round_edges(foot):
    """B2 rounds: edges between plan-outline side faces and side-profile faces."""
    m = edge_face_map(foot)
    sel = []
    for e in foot.edges():
        fs = faces_of_edge(m, e)
        if len(fs) != 2:
            continue
        kinds = []
        for fc in fs:
            n = face_normal(fc)
            if is_plane(fc) and abs(abs(n.X) - 1) < 1e-6:
                kinds.append("x")          # back / front faces: no round
            elif _parallel_to(fc, (0, 1, 0)):
                kinds.append("plan")       # side faces of the plan outline
            elif _parallel_to(fc, (0, 0, 1)):
                kinds.append("prof")       # top / bottom of the side profile
            else:
                kinds.append("?")
        if sorted(kinds) == ["plan", "prof"]:
            sel.append(e)
    return sel


def _parallel_to(fc, d):
    """True if the face is a ruled extrusion along direction d (normal _|_ d at
    several sample points)."""
    d = Vector(*d)
    for u in (0.1, 0.5, 0.9):
        for v in (0.1, 0.5, 0.9):
            try:
                n = fc.normal_at(u, v)
            except Exception:
                n = fc.normal_at(fc.center())
            if abs(n.dot(d)) > 1e-5:
                return False
    return True


# ----------------------------------------------------------------------------
# Wheel P07..P10, axle H1
# ----------------------------------------------------------------------------
def make_tread():
    rr, hw, ri, ro = TREAD_ROUND_R, TREAD_HALF_W, TREAD_RI, TREAD_RO
    sec = profile_face((ri, -hw), [
        ("L", (ro - rr, -hw)),
        ("A", (ro - rr, -hw + rr), (ro, -hw + rr)),
        ("L", (ro, hw - rr)),
        ("A", (ro - rr, hw - rr), (ro - rr, hw)),
        ("L", (ri, hw)),
    ], RHOZ)
    return single_solid(revolve_wheel(sec))


def make_insert():
    sec = profile_face((INSERT_RI, -TREAD_HALF_W), [
        ("L", (TREAD_RI, -TREAD_HALF_W)), ("L", (TREAD_RI, TREAD_HALF_W)),
        ("L", (INSERT_RI, TREAD_HALF_W))], RHOZ)
    return single_solid(revolve_wheel(sec))


def make_core():
    return single_solid(Pos(WHEEL_AX_X, WHEEL_AX_Y, 0) * Cylinder(CORE_R, 2 * CORE_HALF_W))


def make_flange(sign):
    """sign=-1 -> P10-a (z<0), +1 -> P10-b."""
    s = -1  # build P10-a in (rho, z) then mirror z if needed
    dc = (FLANGE_HUB_R, FLANGE_DISH_CZ)
    rim_c = (CORE_R - FLANGE_ROUND_R, -FLANGE_RIM_Z)
    hub_c = (FLANGE_HUB_R + FLANGE_ROUND_R, -FLANGE_HUB_ROUND_Z)

    def tangent(c):
        v = (c[0] - dc[0], c[1] - dc[1])
        L = math.hypot(*v)
        k = FLANGE_DISH_R / L
        return (dc[0] + v[0] * k, dc[1] + v[1] * k)
    t1, t2 = tangent(rim_c), tangent(hub_c)
    pts = [
        (FLANGE_HUB_R, -CORE_HALF_W),
        ("L", (CORE_R, -CORE_HALF_W)),
        ("L", (CORE_R, -FLANGE_RIM_Z)),
        ("A", rim_c, t1),
        ("A", dc, t2),
        ("A", hub_c, (FLANGE_HUB_R, -FLANGE_HUB_ROUND_Z)),
    ]
    mapz = (lambda p: RHOZ((p[0], p[1]))) if sign < 0 else (lambda p: RHOZ((p[0], -p[1])))
    sec = profile_face(pts[0], pts[1:], mapz)
    return single_solid(revolve_wheel(sec))


def make_axle():
    return single_solid(Pos(WHEEL_AX_X, WHEEL_AX_Y, 0) * Cylinder(AXLE_R, 2 * AXLE_HALF_L))


# ----------------------------------------------------------------------------
def build_all(rounds=True):
    notes = {}
    fork, notes["P01"] = make_fork(rounds)
    pedal, notes["P06"] = make_pedal(rounds)
    bodies = [
        ("P01_Fork", fork),
        ("P02_Top_plate", make_plate()),
        ("P03_Kingpin", make_kingpin()),
        ("P04_Bearing_washer", make_washer()),
        ("P05_Hex_bearing_ring", make_hex_ring()),
        ("P06_Brake_pedal", pedal),
        ("P07_Wheel_tread", make_tread()),
        ("P08_Wheel_insert_ring", make_insert()),
        ("P09_Wheel_core_centre_disc", make_core()),
        ("P10a_Core_side_flange_negZ", make_flange(-1)),
        ("P10b_Core_side_flange_posZ", make_flange(+1)),
        ("H1_Axle_pin", make_axle()),
    ]
    for name, b in bodies:
        b.label = name
    return bodies, notes


def main(out=None):
    out = Path(out) if out else Path(__file__).with_name("final.step")
    bodies, notes = build_all(rounds="--no-rounds" not in sys.argv)
    for k, v in notes.items():
        print(f"{k}: {v}")
    asm = Compound(children=[b for _, b in bodies], label="swivel_caster_4in")
    # STEP length unit = INCH (spec unit). The XDE doc unit is inch (unit=Unit.IN),
    # and the writer's output unit is forced to INCH so coordinates stay 1:1.
    from OCP.Interface import Interface_Static
    from OCP.STEPCAFControl import STEPCAFControl_Controller
    STEPCAFControl_Controller.Init_s()
    Interface_Static.SetCVal_s("write.step.schema", "AP214IS")
    Interface_Static.SetCVal_s("write.step.unit", "INCH")
    export_step(asm, str(out), unit=Unit.IN)
    print("written", out)
    return bodies


if __name__ == "__main__":
    main()
