"""P10 ribbed comfort-grip knob -- build123d 0.11.1, units inch, spec frame.
Run:  python knob.py   -> writes final.step (AP214, inch) next to this file."""
import math
import os
import sys

from build123d import *

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from params import *  # noqa: E402,F403


# ---------------------------------------------------------------- helpers
def P(r, z):
    return Vector(r, 0, z)


def arc_c(c, p1, p2):
    """Arc in the (r,z) half plane with centre c from p1 to p2 (shorter way)."""
    a1 = math.atan2(p1[1] - c[1], p1[0] - c[0])
    a2 = math.atan2(p2[1] - c[1], p2[0] - c[0])
    d = (a2 - a1 + math.pi) % (2 * math.pi) - math.pi
    am = a1 + d / 2
    R = math.hypot(p1[0] - c[0], p1[1] - c[1])
    m = (c[0] + R * math.cos(am), c[1] + R * math.sin(am))
    return ThreePointArc(P(*p1), P(*m), P(*p2))


def revolve_rz(segs):
    """segs: list of ('L',(r,z)) or ('A',centre,(r,z)); closed polygon, first item = start point."""
    start = segs[0][1]
    edges, cur = [], start
    for s in segs[1:] + [("L", start)]:
        if s[0] == "L":
            if (abs(s[1][0] - cur[0]) + abs(s[1][1] - cur[1])) > 1e-9:
                edges.append(Line(P(*cur), P(*s[1])))
            cur = s[1]
        else:
            edges.append(arc_c(s[1], cur, s[2]))
            cur = s[2]
    face = Face(Wire(edges))
    return revolve(face, Axis.Z, 360)


def scallop_centres():
    return [
        (SCALLOP_PCR * math.cos(math.radians(SCALLOP_THETA0 + 45 * k)),
         SCALLOP_PCR * math.sin(math.radians(SCALLOP_THETA0 + 45 * k)))
        for k in range(N_LOBES)
    ]


def lobed_outline(R, rs, corner=0.0):
    """Plan face: circle R minus 8 discs rs on the scallop centres, corners optionally rounded."""
    f = Circle(R)
    for (x, y) in scallop_centres():
        f = f - Pos(x, y) * Circle(rs)
    f = f.faces()[0]
    if corner > 0:
        f = f.fillet_2d(corner, f.vertices())
    return f


def prism(face, z1, z2):
    return extrude(Pos(0, 0, z1) * face, z2 - z1)


# ---------------------------------------------------------------- P01 core
def hub_r(z):
    return HUB_R_END + TAN3 * (z - HUB_END_Z)


def build_core():
    t = math.radians(3.0)
    # R0.02 round tangent to the end face and to the 3 deg hub cone
    zc = HUB_END_Z + HUB_END_ROUND
    hub_end_round_c = (hub_r(zc) - HUB_END_ROUND / math.cos(t), zc)
    p2 = (hub_end_round_c[0] + HUB_END_ROUND * math.cos(t),
          hub_end_round_c[1] - HUB_END_ROUND * math.sin(t))
    c1 = revolve_rz([
        ("L", (0, HUB_END_Z)),
        ("L", (hub_end_round_c[0], HUB_END_Z)),
        ("A", hub_end_round_c, p2),
        ("L", (hub_r(HEAD_UNDER_Z), HEAD_UNDER_Z)),
        ("L", (CORE_RIM_R, HEAD_UNDER_Z)),
        ("L", (CORE_RIM_R, RIM_TOP_Z)),
        ("L", (TOP_FLAT_R_IN, RIM_TOP_Z)),
        ("A", DOME_C, (DOME_END_R, CORE_TOP_Z)),
        ("L", (0, CORE_TOP_Z)),
    ])
    # C2 scallops
    scal = [Pos(x, y, HEAD_UNDER_Z - 0.05)
            * Cylinder(SCALLOP_R_CORE, 1.0, align=(Align.CENTER, Align.CENTER, Align.MIN))
            for (x, y) in scallop_centres()]
    core = c1 - scal
    # C3 underside cavity
    lci = lobed_outline(LCI_R, LCI_SCALLOP_R)
    k1 = prism(lci, HEAD_UNDER_Z, CAV_STEP_Z)
    k2 = revolve_rz([("L", (0, CAV_STEP_Z)), ("L", (CAV_CONE_R_LO, CAV_STEP_Z)),
                     ("L", (CAV_CONE_R_HI, CAV_CEIL_Z)), ("L", (0, CAV_CEIL_Z))])
    k2 = k2 & prism(lci, CAV_STEP_Z - 0.01, CAV_CEIL_Z + 0.01)
    zl, zh = HEAD_UNDER_Z - 0.1, CAV_CEIL_Z + 0.1
    hub = revolve_rz([("L", (0, zl)), ("L", (hub_r(zl), zl)), ("L", (hub_r(zh), zh)), ("L", (0, zh))])
    ribs = [Rot(0, 0, a) * Box(3.0, RIB_T, 1.0) for a in (0, 45, 90, 135)]
    cav = (k1 + k2) - hub - ribs
    core = core - cav
    # C4 bore
    bore = revolve_rz([
        ("L", (0, HUB_END_Z - 0.1)),
        ("L", (BORE_SEAT_R, HUB_END_Z - 0.1)),
        ("L", (BORE_SEAT_R, BORE_STEP_Z)),
        ("L", (BORE_R0, BORE_STEP_Z)),
        ("L", BORE_TAN_PT),
        ("A", BORE_ROUND_C, (BORE_ROUND_C[0], CORE_TOP_Z)),
        ("L", (BORE_ROUND_C[0], CORE_TOP_Z + 0.1)),
        ("L", (0, CORE_TOP_Z + 0.1)),
    ])
    core = core - bore
    # C5 hub end ridge
    ridge = revolve_rz([("L", (RIDGE_RI, HUB_END_Z - RIDGE_H)), ("L", (RIDGE_RO, HUB_END_Z - RIDGE_H)),
                        ("L", (RIDGE_RO, HUB_END_Z)), ("L", (RIDGE_RI, HUB_END_Z))])
    core = core + ridge
    return core


# ---------------------------------------------------------------- P02 coating
def build_coating(core):
    lo = lobed_outline(LO_R, LO_SCALLOP_R, PLAN_CORNER_R)
    li = lobed_outline(LI_R, LI_SCALLOP_R, PLAN_CORNER_R)
    b = prism(lo, COAT_BOT_Z, COAT_FLAT_TOP_Z) - prism(li, COAT_BOT_Z - 0.05, CAV_STEP_Z)
    b = b.solids()[0]
    # S2: R0.06 rounds on outer bottom, outer top, inner bottom loops (all horizontal edges at z=-0.18 / 0.5)
    eds = [e for e in b.edges()
           if (abs(e.center().Z - COAT_BOT_Z) < 1e-6 or abs(e.center().Z - COAT_FLAT_TOP_Z) < 1e-6)
           and abs(e.bounding_box().max.Z - e.bounding_box().min.Z) < 1e-6]
    b = b.fillet(COAT_EDGE_R, eds)
    # S3: dome cap
    cap = revolve_rz([("L", (0, COAT_FLAT_TOP_Z)), ("L", (TOP_FLAT_R_IN, COAT_FLAT_TOP_Z)),
                      ("A", DOME_C, (COAT_DOME_END_R, COAT_TOP_Z)), ("L", (0, COAT_TOP_Z))])
    c = b + cap
    # S4: cuts
    lci = lobed_outline(LCI_R, LCI_SCALLOP_R)
    c = c - prism(lci, CAV_STEP_Z, CAV_CEIL_Z)
    opening = revolve_rz([("L", (0, 0.3)), ("L", (TOP_OPEN_R, 0.3)), ("L", (TOP_OPEN_R, CORE_TOP_Z)),
                          ("L", (COAT_DOME_END_R, TOP_OPEN_CONE_Z)),
                          ("L", (COAT_DOME_END_R, COAT_TOP_Z + 0.1)), ("L", (0, COAT_TOP_Z + 0.1))])
    c = c - opening
    c = c - core
    return c


# ---------------------------------------------------------------- P03 insert
def build_insert():
    L = INS_Z1 - INS_Z0
    tube = Pos(0, 0, INS_Z0) * Cylinder(INS_R, L, align=(Align.CENTER, Align.CENTER, Align.MIN))
    major = Pos(0, 0, INS_Z0 - 0.1) * Cylinder(TH_MAJOR_R, L + 0.2,
                                               align=(Align.CENTER, Align.CENTER, Align.MIN))
    body = tube - major                 # sleeve with the root (major) cylinder
    # Thread ridge (material) bounded by exact helical ruled surfaces.
    # Profile in the axial half plane theta=0, centred on a crest flat (= root flat + P/2).
    tan30 = math.tan(math.radians(30.0))
    dr_out = 0.005                      # ridge base buried in the sleeve wall (clean boolean)
    r_out = TH_MAJOR_R + dr_out
    hw_out = TH_FLAT / 2 + (TH_MAJOR_R - TH_MINOR_R + dr_out) * tan30
    n_below = 7
    zc0 = TH_PHASE_Z + PITCH / 2 - n_below * PITCH   # start below the insert, same phase
    height = 13 * PITCH
    prof = [(r_out, -hw_out), (TH_MINOR_R, -TH_FLAT / 2), (TH_MINOR_R, TH_FLAT / 2), (r_out, hw_out)]
    hel = [Edge.make_helix(PITCH, height, r, center=(0, 0, zc0 + dz)).edges()[0]  # right-hand
           for r, dz in prof]
    faces = [Face.make_surface_from_curves(hel[i], hel[(i + 1) % 4]) for i in range(4)]
    for t in (0.0, 1.0):
        faces.append(Face(Polyline(*[h.position_at(t) for h in hel], close=True)))
    ridge = Solid(Shell(faces))
    ridge = ridge & tube
    ins = body + ridge
    # countersinks both ends, 90 deg included; the 45 deg cones continue through the thread
    e = 0.01
    csk_lo = revolve_rz([("L", (0, INS_Z0 - e)), ("L", (CSK_R + e, INS_Z0 - e)),
                         ("L", (0, INS_Z0 + CSK_R))])
    csk_hi = revolve_rz([("L", (0, INS_Z1 + e)), ("L", (CSK_R + e, INS_Z1 + e)),
                         ("L", (0, INS_Z1 - CSK_R))])
    ins = ins - csk_lo - csk_hi
    return ins


def solid_of(shape):
    s = shape.solids()
    assert len(s) == 1, f"expected 1 solid, got {len(s)}"
    return s[0]


def report(name, s):
    bb = s.bounding_box()
    c = s.center(CenterOf.MASS)
    print(f"{name}: valid={s.is_valid} V={s.volume:.5f} A={s.area:.4f} "
          f"CoM=({c.X:.5f},{c.Y:.5f},{c.Z:.5f}) "
          f"bb=({bb.min.X:.4f},{bb.min.Y:.4f},{bb.min.Z:.4f})..({bb.max.X:.4f},{bb.max.Y:.4f},{bb.max.Z:.4f}) "
          f"faces={len(s.faces())}", flush=True)


def build_all():
    core = solid_of(build_core())
    core.label = "P01_knob_core"
    coat = solid_of(build_coating(core))
    coat.label = "P02_grip_coating"
    ins = solid_of(build_insert())
    ins.label = "P03_threaded_insert"
    return core, coat, ins


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    core, coat, ins = build_all()
    report("P01 core", core)
    report("P02 coating", coat)
    report("P03 insert", ins)
    asm = Compound(label="P10_knob", children=[core, coat, ins])
    report("ASM", asm)
    # AP214, length unit INCH written with the model values unchanged (model is built in inch)
    from OCP.Interface import Interface_Static
    from OCP.STEPControl import STEPControl_Controller
    STEPControl_Controller.Init_s()
    Interface_Static.SetCVal_s("write.step.schema", "AP214IS")
    Interface_Static.SetCVal_s("xstep.cascade.unit", "INCH")
    Interface_Static.SetCVal_s("write.step.unit", "INCH")
    export_step(asm, os.path.join(here, "final.step"), unit=Unit.IN)
    print("written final.step")
