"""Ball joint rod end, male shank, 1/2-20 UNF-RH  --  build123d 0.11.1
Units: INCH (model numbers are inches; STEP written with unit=IN).
Global frame per spec: shank axis = Y (shank to -Y), ball centre (0,1,0), bore || Z.
Run:  python rod_end.py   -> writes final.step next to this script.
"""
import math
import sys
from pathlib import Path
from build123d import *

# ---------------------------------------------------------------- parameters
# Housing (P01)
EYE_R          = 0.75       # F1 eye sphere radius
BALL_CY        = 1.0        # ball / eye centre y
NECK_ARC_R     = 0.5        # F2 neck concave arc radius
NECK_ARC_CR    = 0.75       # F2 arc centre r  (centre at (r,y)=(0.75,0))
NECK_TOP_Y     = 0.4        # F2 neck top (tangent to sphere)
FLAT_Z         = 0.22656    # F3 side flat half-thickness
SLOPE_Y        = 0.09062    # F3 end of neck slope
SLOPE_Z0       = 0.25       # F3 slope half-width at y=0
SOCKET_R       = 0.5625     # F4 socket sphere radius (= ball radius)
# Shank / thread (F5)
SHANK_LEN      = 1.625      # shank end face at y=-SHANK_LEN
MAJOR_R        = 0.25       # crest radius (1/2")
PITCH          = 0.05       # 20 TPI
MINOR_R        = 0.21752    # root radius
THREAD_DEPTH   = MAJOR_R - MINOR_R          # 0.03248
FLAT_W         = PITCH / 8                   # root & crest flat width 0.00625
FLANK_HALF     = math.radians(30)            # 60 deg included
ROOT_PHASE_Y   = PITCH / 16                  # root flat centre at +X side: 0.003125 - 0.05k
END_FLAT_R     = 0.205      # end face disc radius (45 deg chamfer to MAJOR_R)
RUNOUT_TOP_R   = MAJOR_R    # run-out cone r = 0.25 + y (45 deg)
SHANK_EXTRA    = 0.3        # tool-only: temporary blank extension below the end face
GROOVE_OVERRUN = 0.003      # tool-only: flank continued past crest radius
GROOVE_CLEAR   = 0.02       # tool-only: groove cutter outer radius = MAJOR_R + this
K_START        = 37         # groove helix starts at root-centre y = ROOT_PHASE_Y - 37*PITCH (-1.8469)
TURNS_PER_SEG  = 19         # helix split into segments (one 38-turn sweep makes a failing boolean)
N_SEGS         = 2          # 2 x 19 turns: y -1.847 .. +0.053 (top end removed by run-out cone)
# Ball (P02)
BALL_R         = 0.5625
COLLAR_R       = 0.35
COLLAR_HALF    = 0.625
BORE_R         = 0.25
BORE_CHAMFER   = 0.025



def one(shape):
    """Coerce a boolean result to a single Solid."""
    if isinstance(shape, ShapeList):
        shape = Compound(list(shape))
    sols = shape.solids()
    assert len(sols) == 1, f"expected 1 solid, got {len(sols)}"
    return sols[0]


def revolve_ry(pts):
    """Revolve a closed (r, y) polyline about the global Y axis, 360 deg."""
    face = Face(Wire.make_polygon([Vector(r, y, 0) for r, y in pts], close=True))
    return Solid.revolve(face, 360, Axis.Y)


# ---------------------------------------------------------------- P01 housing
def build_housing():
    # F1 eye sphere
    eye = Solid.make_sphere(EYE_R).moved(Location((0, BALL_CY, 0)))

    # F2 neck: region r <= 0.75 - sqrt(0.25 - y^2), y in [0, 0.4]
    r0 = NECK_ARC_CR - NECK_ARC_R                                   # 0.25 at y=0
    r1 = NECK_ARC_CR - math.sqrt(NECK_ARC_R**2 - NECK_TOP_Y**2)     # 0.45 at y=0.4
    arc_mid_y = NECK_TOP_Y / 2
    arc_mid_r = NECK_ARC_CR - math.sqrt(NECK_ARC_R**2 - arc_mid_y**2)
    neck_prof = Wire([
        Edge.make_line((0, 0, 0), (r0, 0, 0)),
        Edge.make_three_point_arc((r0, 0, 0), (arc_mid_r, arc_mid_y, 0), (r1, NECK_TOP_Y, 0)),
        Edge.make_line((r1, NECK_TOP_Y, 0), (0, NECK_TOP_Y, 0)),
        Edge.make_line((0, NECK_TOP_Y, 0), (0, 0, 0)),
    ])
    neck = Solid.revolve(Face(neck_prof), 360, Axis.Y)
    body = one(eye.fuse(neck).clean())

    # F3 side flats + neck slopes: keep |z| <= min(FLAT_Z, SLOPE_Z0 - k*y)
    keep_yz = [(-0.5, SLOPE_Z0), (0, SLOPE_Z0), (SLOPE_Y, FLAT_Z), (2.5, FLAT_Z),
               (2.5, -FLAT_Z), (SLOPE_Y, -FLAT_Z), (0, -SLOPE_Z0), (-0.5, -SLOPE_Z0)]
    keep_face = Face(Wire.make_polygon([Vector(-1, y, z) for y, z in keep_yz], close=True))
    keep = Solid.extrude(keep_face, Vector(2, 0, 0))
    body = one(body.intersect(keep))

    # F4 ball socket
    socket = Solid.make_sphere(SOCKET_R).moved(Location((0, BALL_CY, 0)))
    body = one(body.cut(socket))

    # F5 shank blank: plain cylinder r=MAJOR_R, extended SHANK_EXTRA below the end face so the
    # helical cut never crosses the end face (that boolean fails); end face + chamfer trimmed after.
    y_end = -SHANK_LEN
    shank = revolve_ry([(0, y_end - SHANK_EXTRA), (MAJOR_R, y_end - SHANK_EXTRA),
                        (MAJOR_R, 0.0), (0, 0.0)])

    # helical groove: profile in the +X half plane (z=0), swept along an RH helix about +Y.
    # Root flat at MINOR_R, 30 deg flanks; flanks continued a little past the crest radius
    # (avoids a helix edge lying exactly on the crest cylinder), then radial-parallel walls.
    half_root = FLAT_W / 2
    half_open = half_root + THREAD_DEPTH * math.tan(FLANK_HALF)    # 0.021875 at crest radius
    r_f = MAJOR_R + GROOVE_OVERRUN
    half_f = half_open + GROOVE_OVERRUN * math.tan(FLANK_HALF)
    r_out = MAJOR_R + GROOVE_CLEAR
    prof_pts = [(MINOR_R, -half_root), (r_f, -half_f), (r_out, -half_f),
                (r_out, half_f), (r_f, half_f), (MINOR_R, half_root)][::-1]
    # built about +Z (helix starts on +X, CCW about +Z = right hand), profile in XZ plane
    groove_profile = Face(Wire.make_polygon([Vector(r, 0, h) for r, h in prof_pts], close=True))
    seg_height = PITCH * TURNS_PER_SEG
    seg = Solid.sweep(groove_profile, Wire(Helix(PITCH, seg_height, MINOR_R).edges()), is_frenet=True)
    if seg.volume < 0:
        seg = Solid(seg.wrapped.Reversed())
    # map local frame to global: X->X, Z->+Y, Y->-Z (rotation -90 deg about X).
    # => turning from +X toward -Z advances +Y : right-hand thread about +Y.
    z2y = Location((0, 0, 0), (1, 0, 0), -90)
    y_start = ROOT_PHASE_Y - PITCH * K_START       # root centre on +X at the helix start (below the end face)
    segs = [seg.moved(Location((0, y_start + i * seg_height, 0)) * z2y) for i in range(N_SEGS)]
    # thread run-out: material inside the 45 deg cone r <= 0.25 + y is not cut
    runout = revolve_ry([(0, -RUNOUT_TOP_R), (0.6, 0.6 - RUNOUT_TOP_R), (0.6, 0.3), (0, 0.3)])
    segs[-1] = one(segs[-1].cut(runout))
    for sg in segs:
        v_before = shank.volume
        shank = one(shank.cut(sg))
        assert v_before - shank.volume > 0.01, "helical groove cut failed"

    # lower end: flat disc r=END_FLAT_R at y=-SHANK_LEN, 45 deg chamfer to MAJOR_R
    endcut = revolve_ry([(0, y_end - 1), (0.4, y_end - 1), (0.4, y_end + 0.4 - END_FLAT_R),
                         (END_FLAT_R, y_end), (0, y_end)])
    shank = one(shank.cut(endcut))

    housing = one(body.fuse(shank).clean())
    housing.label = "P01_Housing_threaded_shank"
    return housing


# ---------------------------------------------------------------- P02 ball
def build_ball():
    c = Location((0, BALL_CY, 0))
    sph = Solid.make_sphere(BALL_R)
    collar = Solid.make_cylinder(COLLAR_R, 2 * COLLAR_HALF).moved(Location((0, 0, -COLLAR_HALF)))
    ball = one(sph.fuse(collar))
    # bore with 45 deg chamfers, profile in (r, z), revolved about Z
    zc = COLLAR_HALF - BORE_CHAMFER
    rc = BORE_R + BORE_CHAMFER
    bore_pts = [(0, -COLLAR_HALF - 0.1), (rc + 0.1, -COLLAR_HALF - 0.1), (BORE_R, -zc),
                (BORE_R, zc), (rc + 0.1, COLLAR_HALF + 0.1), (0, COLLAR_HALF + 0.1)]
    bore_face = Face(Wire.make_polygon([Vector(r, 0, z) for r, z in bore_pts], close=True))
    bore = Solid.revolve(bore_face, 360, Axis.Z)
    ball = one(ball.cut(bore).clean())
    ball = ball.moved(c)    # centre the ball (built about origin) at (0,1,0)
    ball.label = "P02_Ball_with_collars"
    return ball


def build():
    housing = build_housing()
    ball = build_ball()
    return housing, ball


if __name__ == "__main__":
    from OCP.Interface import Interface_Static
    from OCP.STEPControl import STEPControl_Controller
    STEPControl_Controller.Init_s()
    Interface_Static.SetCVal_s("write.step.schema", "AP214IS")
    Interface_Static.SetCVal_s("write.step.unit", "INCH")   # write lengths in inches
    housing, ball = build()
    out = Path(__file__).with_name("final.step")
    asm = Compound(children=[housing, ball], label="rod_end_1-2-20")
    export_step(asm, str(out), unit=Unit.IN)
    print("wrote", out)
