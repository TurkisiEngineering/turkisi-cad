"""Ribbed comfort-grip knob with threaded insert (P10) - build123d 0.11.1.

All model values in INCHES, global frame of spec.md (knob axis = Z).
Run:  python knob.py   -> writes final.step (AP214, unit inch) next to this file.
"""
import math
import os
import sys

from build123d import (
    Axis, Box, BuildSketch, Circle, Compound, Edge, Face, Helix, Locations,
    Mode, Plane, Pos, Rot, Shell, Solid, Unit, Wire, export_step, extrude, fillet,
    revolve, Vector,
)

# ---------------------------------------------------------------- parameters
TAN3 = math.tan(math.radians(3.0))

# general / scallops
N_LOBES = 8
SCALLOP_PCD_R = 1.39          # radius of circle carrying the scallop centres
SCALLOP_ANG0 = 22.5           # first scallop centre angle [deg]

# P01 core
HUB_END_Z = -0.68             # hub end face
HUB_END_R = 0.625             # hub radius at end face (dia 1.25)
HUB_END_ROUND = 0.02          # hub end round
HUB_DRAFT_DEG = 3.0
HEAD_UNDER_Z = -0.12          # head underside level
CORE_RIM_R = 1.2              # head rim (dia 2.4)
CORE_RIM_TOP_Z = 0.44         # top of rim / top flat ring
DOME_START_R = 1.06           # dome start radius on flat ring
CORE_DOME_R = 2.175763        # core dome radius
DOME_CENTRE = (0.124593, -1.524424)  # (r, z) of dome arc centre (core & coating)
CORE_TOP_Z = 0.62             # core top annulus
CORE_DOME_END_R = 0.492553    # dome meets top annulus
SCALLOP_R_CORE = 0.33         # L0 scallop radius
CI_R = 1.11                   # Lci circle radius (rim inner)
SCALLOP_R_CI = 0.39           # Lci scallop radius
CAV_STEP_Z = 0.26             # cavity step plane
CAV_CEIL_Z = 0.35             # cavity ceiling
CAV_STEP_R = 1.01             # cone bottom radius
CAV_CEIL_R = 0.92             # cone top radius (45 deg)
RIB_T = 0.05                  # rib thickness
SEAT_R = 0.265625             # insert seat bore (dia 0.53125)
SEAT_TOP_Z = -0.18            # seat bottom (step)
BORE_R0 = 0.36                # tapered bore radius at z=-0.18
BORE_ROUND = 0.015            # bore top round
RIDGE_RI, RIDGE_RO = 0.385417, 0.505208
RIDGE_H = 0.015

# P02 coating
SKIN_T = 0.06
LO_R, LO_SC_R = 1.26, 0.27    # coating outer outline
LI_R, LI_SC_R = 1.05, 0.45    # coating liner inner outline
PLAN_ROUND = 0.1              # plan corner rounds of Lo / Li
COAT_BOT_Z = -0.18
COAT_FLAT_Z = 0.5
COAT_EDGE_ROUND = 0.06
COAT_DOME_R = 2.230085
COAT_TOP_Z = 0.68
COAT_DOME_END_R = 0.461925
OPEN_R = 0.421954             # top opening radius (z <= 0.62)
OPEN_CONE_TOP_Z = 0.674670

# P03 insert
INS_R = 0.265625
INS_Z0, INS_Z1 = -0.68, -0.18
PITCH = 0.0625                # 3/8"-16
MAJOR_R = 0.1875
MINOR_R = 0.146906
FLAT = PITCH / 8.0            # root & crest axial flats
ROOT_FLAT_Z0 = -0.379218      # root flat centre in half plane theta=0
CSK_R = 0.21875               # countersink radius at faces (90 deg incl.)
THREAD_EMBED = 0.005          # modelling overlap of tooth into tube wall (not geometry)


# ---------------------------------------------------------------- helpers
def P(r, z):
    """Point in the XZ half plane (r -> X, z -> Z)."""
    return Vector(r, 0, z)


def arc(p0, c, p1):
    """Minor circular arc p0 -> p1 about centre c, all (r, z) tuples."""
    a0 = math.atan2(p0[1] - c[1], p0[0] - c[0])
    a1 = math.atan2(p1[1] - c[1], p1[0] - c[0])
    d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
    am = a0 + d / 2
    R = math.hypot(p0[0] - c[0], p0[1] - c[1])
    pm = (c[0] + R * math.cos(am), c[1] + R * math.sin(am))
    return Edge.make_three_point_arc(P(*p0), P(*pm), P(*p1))


def profile_solid(segs):
    """segs: list of ('L', p) or ('A', centre, p); starts at segs[0][1]."""
    edges = []
    cur = segs[0][1]
    for s in segs[1:] + [('L', segs[0][1])]:
        if s[0] == 'L':
            nxt = s[1]
            if math.dist(cur, nxt) > 1e-9:
                edges.append(Edge.make_line(P(*cur), P(*nxt)))
        else:
            nxt = s[2]
            edges.append(arc(cur, s[1], nxt))
        cur = nxt
    face = Face(Wire(edges))
    return revolve(face, Axis.Z, 360)


def scallop_centres():
    out = []
    for k in range(N_LOBES):
        a = math.radians(SCALLOP_ANG0 + 45.0 * k)
        out.append((SCALLOP_PCD_R * math.cos(a), SCALLOP_PCD_R * math.sin(a)))
    return out


def lobed_prism(R, rs, z0, z1, corner=None):
    """Prism of (circle R minus 8 discs rs at scallop centres) from z0 to z1,
    optionally with every plan corner rounded `corner`."""
    with BuildSketch(Plane.XY.offset(z0)) as sk:
        # rotate so the circle's seam lies at a scallop centre (cut away)
        with Locations(Rot(0, 0, SCALLOP_ANG0)):
            Circle(R)
        with Locations(*scallop_centres()):
            Circle(rs, mode=Mode.SUBTRACT)
        if corner:
            fillet(sk.vertices(), corner)
    return extrude(sk.sketch, z1 - z0)


def cone_solid(r_at, z0, z1):
    """Solid of revolution r <= r_at(z) between z0 and z1 (linear r_at)."""
    return profile_solid([('L', (0, z0)), ('L', (r_at(z0), z0)),
                          ('L', (r_at(z1), z1)), ('L', (0, z1))])


# ---------------------------------------------------------------- P01 core
def hub_r(z):
    return HUB_END_R + TAN3 * (z - HUB_END_Z)


def build_core():
    # C1 main revolve
    # tangent points of hub end round (from spec)
    rc = (0.606021, HUB_END_Z + HUB_END_ROUND)
    t1 = (0.606021, HUB_END_Z)
    t2 = (0.625994, -0.661047)
    main = profile_solid([
        ('L', (0, HUB_END_Z)),
        ('L', t1),
        ('A', rc, t2),
        ('L', (hub_r(HEAD_UNDER_Z), HEAD_UNDER_Z)),
        ('L', (CORE_RIM_R, HEAD_UNDER_Z)),
        ('L', (CORE_RIM_R, CORE_RIM_TOP_Z)),
        ('L', (DOME_START_R, CORE_RIM_TOP_Z)),
        ('A', DOME_CENTRE, (CORE_DOME_END_R, CORE_TOP_Z)),
        ('L', (0, CORE_TOP_Z)),
    ])
    core = main
    # C2 scallops
    h0, h1 = HEAD_UNDER_Z - 0.05, CORE_TOP_Z + 0.1
    for (x, y) in scallop_centres():
        core = core - Pos(x, y, h0) * Solid.make_cylinder(SCALLOP_R_CORE, h1 - h0)
    # C3 underside cavity
    k1 = lobed_prism(CI_R, SCALLOP_R_CI, HEAD_UNDER_Z - 0.05, CAV_STEP_Z)
    k2rev = profile_solid([('L', (0, CAV_STEP_Z - 0.001)),
                           ('L', (CAV_STEP_R + 0.001, CAV_STEP_Z - 0.001)),
                           ('L', (CAV_STEP_R, CAV_STEP_Z)),
                           ('L', (CAV_CEIL_R, CAV_CEIL_Z)),
                           ('L', (0, CAV_CEIL_Z))])
    k2 = k2rev & lobed_prism(CI_R, SCALLOP_R_CI, CAV_STEP_Z - 0.01, CAV_CEIL_Z + 0.01)
    cavity = k1 + k2
    cavity = cavity - cone_solid(hub_r, HUB_END_Z - 0.1, CAV_CEIL_Z + 0.1)
    for a in (0, 45, 90, 135):
        cavity = cavity - Rot(0, 0, a) * Box(3.0, RIB_T, 2.0)
    core = core - cavity
    # C4 bore
    b_top = (0.401182, 0.605785)
    bore = profile_solid([
        ('L', (0, HUB_END_Z - 0.1)),
        ('L', (SEAT_R, HUB_END_Z - 0.1)),
        ('L', (SEAT_R, SEAT_TOP_Z)),
        ('L', (BORE_R0, SEAT_TOP_Z)),
        ('L', b_top),
        ('A', (0.416161, CORE_TOP_Z - BORE_ROUND), (0.416161, CORE_TOP_Z)),
        ('L', (0.416161, CORE_TOP_Z + 0.1)),
        ('L', (0, CORE_TOP_Z + 0.1)),
    ])
    core = core - bore
    # C5 hub end ridge
    ridge = (Pos(0, 0, HUB_END_Z - RIDGE_H)
             * (Solid.make_cylinder(RIDGE_RO, RIDGE_H) - Solid.make_cylinder(RIDGE_RI, RIDGE_H)))
    core = core + ridge
    return single(core, "core")


# ---------------------------------------------------------------- P02 coating
def build_coating(core):
    lo = lobed_prism(LO_R, LO_SC_R, COAT_BOT_Z, COAT_FLAT_Z, PLAN_ROUND)
    li = lobed_prism(LI_R, LI_SC_R, COAT_BOT_Z - 0.05, CAV_STEP_Z, PLAN_ROUND)
    b = single(lo - li, "B")
    # S2 edge rounds: outer bottom, outer top, inner bottom loops
    eps = 1e-6
    sel = []
    for e in b.edges():
        bb = e.bounding_box()
        if bb.max.Z - bb.min.Z > eps:
            continue
        z = bb.min.Z
        if abs(z - COAT_BOT_Z) < eps or abs(z - COAT_FLAT_Z) < eps:
            # outer loops have r >= 1.12, inner (Li) loop r <= 1.05
            sel.append(e)
    b = b.fillet(COAT_EDGE_ROUND, sel)
    # S3 dome cap
    cap = profile_solid([
        ('L', (0, COAT_FLAT_Z - 0.01)),
        ('L', (DOME_START_R, COAT_FLAT_Z - 0.01)),
        ('L', (DOME_START_R, COAT_FLAT_Z)),
        ('A', DOME_CENTRE, (COAT_DOME_END_R, COAT_TOP_Z)),
        ('L', (0, COAT_TOP_Z)),
    ])
    c = b + cap
    # S4 cuts
    c = c - lobed_prism(CI_R, SCALLOP_R_CI, CAV_STEP_Z, CAV_CEIL_Z)
    opening = profile_solid([
        ('L', (0, -1.0)),
        ('L', (OPEN_R, -1.0)),
        ('L', (OPEN_R, CORE_TOP_Z)),
        ('L', (COAT_DOME_END_R, OPEN_CONE_TOP_Z)),
        ('L', (COAT_DOME_END_R, COAT_TOP_Z + 0.1)),
        ('L', (0, COAT_TOP_Z + 0.1)),
    ])
    c = c - opening
    c = c - core
    return single(c, "coating")


# ---------------------------------------------------------------- P03 insert
def build_insert():
    tube = Pos(0, 0, INS_Z0) * Solid.make_cylinder(INS_R, INS_Z1 - INS_Z0)
    tube = tube - Pos(0, 0, INS_Z0 - 0.1) * Solid.make_cylinder(MAJOR_R, 1.0)
    # thread tooth (material between the root grooves)
    half_root = (PITCH - FLAT) / 2.0          # tooth half width at major radius
    half_crest = FLAT / 2.0                   # tooth half width at minor radius
    tooth_c0 = ROOT_FLAT_Z0 + PITCH / 2.0     # tooth centre at theta=0
    n_below = math.ceil((tooth_c0 - (INS_Z0 - 2 * PITCH)) / PITCH)
    z0 = tooth_c0 - n_below * PITCH
    turns = math.ceil((INS_Z1 + 2 * PITCH - z0) / PITCH)
    # tooth profile (r, dz) relative to tooth centre; the flanks are carried
    # THREAD_EMBED beyond the major radius into the tube wall so that they cut
    # the bore cylinder transversally (the root flat = P/8 results exactly).
    slope = (half_root - half_crest) / (MAJOR_R - MINOR_R)   # tan 30 deg
    r_emb = MAJOR_R + THREAD_EMBED
    he = half_root + THREAD_EMBED * slope
    prof = [(MINOR_R, -half_crest), (r_emb, -he), (r_emb, he), (MINOR_R, half_crest)]
    height = turns * PITCH
    # exact helices through the profile corners (right hand), ruled faces between
    hel = []
    for r, dz in prof:
        h = Helix(PITCH, height, r, center=(0, 0, z0 + dz))
        hel.append(h.edges()[0])
    faces = [Face.make_surface_from_curves(hel[i], hel[(i + 1) % 4]) for i in range(4)]
    for zc, ang in ((z0, 0.0), (z0 + height, 2 * math.pi * turns)):
        faces.append(Face(Wire.make_polygon(
            [Vector(r * math.cos(ang), r * math.sin(ang), zc + dz) for r, dz in prof],
            close=True)))
    tooth = Solid(Shell(faces))
    if tooth.volume < 0:
        tooth = Solid(tooth.wrapped.Reversed())
    tooth = tooth & (Pos(0, 0, INS_Z0) * Solid.make_cylinder(INS_R, INS_Z1 - INS_Z0))
    ins = tube + tooth
    # countersinks, 90 deg included, cone continues inward (cuts thread)
    csk_lo = cone_solid(lambda z: CSK_R - (z - INS_Z0), INS_Z0 - 0.05, INS_Z0 + CSK_R - 0.01)
    csk_hi = cone_solid(lambda z: CSK_R - (INS_Z1 - z), INS_Z1 - CSK_R + 0.01, INS_Z1 + 0.05)
    ins = ins - csk_lo - csk_hi
    return single(ins, "insert")


def single(shape, name):
    sols = shape.solids()
    if len(sols) != 1:
        print(f"WARNING {name}: {len(sols)} solids, volumes "
              f"{[round(s.volume, 6) for s in sols]}", file=sys.stderr)
        sols = sorted(sols, key=lambda s: -s.volume)
    return sols[0]


def build_all():
    core = build_core()
    coating = build_coating(core)
    insert = build_insert()
    core.label, coating.label, insert.label = "P01_knob_core", "P02_grip_coating", "P03_threaded_insert"
    return core, coating, insert


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    parts = build_all()
    asm = Compound(children=list(parts), label="P10_knob")
    # write the STEP file in inches (spec unit), AP214
    from OCP.Interface import Interface_Static
    from OCP.STEPControl import STEPControl_Controller
    from OCP.STEPCAFControl import STEPCAFControl_Controller
    STEPCAFControl_Controller.Init_s()
    STEPControl_Controller.Init_s()
    Interface_Static.SetCVal_s("write.step.schema", "AP214IS")
    Interface_Static.SetCVal_s("write.step.unit", "INCH")
    export_step(asm, os.path.join(here, "final.step"), unit=Unit.IN)
    for p in parts:
        c = p.center()
        bb = p.bounding_box()
        print(f"{p.label}: V={p.volume:.5f} A={p.area:.4f} CoM=({c.X:.5f},{c.Y:.5f},{c.Z:.5f}) "
              f"bbox=({bb.min.X:.4f},{bb.min.Y:.4f},{bb.min.Z:.4f})..({bb.max.X:.4f},{bb.max.Y:.4f},{bb.max.Z:.4f}) "
              f"faces={len(p.faces())} valid={p.is_valid}")
