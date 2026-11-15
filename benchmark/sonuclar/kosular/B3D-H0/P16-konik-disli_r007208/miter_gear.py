"""P16 - Straight-tooth miter (bevel) gear with plain round bore.

build123d 0.11.1. Units: mm. Global frame per spec: gear axis = Y, back face y = 0,
teeth toward +Y; a tooth space is centred on +Z.

Run:  python miter_gear.py   -> writes final.step next to this script.
"""
from pathlib import Path

from build123d import (
    Axis, Edge, Solid, Wire, Face, export_step, revolve,
)
from OCP.Geom import Geom_BSplineCurve
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.gp import gp_Pnt
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge

# ---------------------------------------------------------------- parameters
N_TEETH = 20                     # number of teeth
PITCH_ANGLE_STEP = 360.0 / N_TEETH   # 18 deg pattern step
BORE_R = 4.0                     # bore radius (dia 8)
BORE_CHAMFER = 0.4               # 45 deg bore chamfer, both ends
HUB_R = 12.5                     # hub radius (dia 25)
HUB_LEN = 7.75                   # hub length (y of hub/back-cone corner)
HEEL_TIP_R = 16.385              # heel tip edge radius (OD 32.77)
HEEL_TIP_Y = 9.36                # heel tip edge height
TOE_TIP_R = 11.73752             # toe tip edge radius
TOE_TIP_Y = 19.33                # overall width (toe tip edge height)
FRONT_FACE_OUT_R = 8.5           # outer radius of front face annulus
FRONT_FACE_Y = 18.0              # front face height

# blank profile (r, y), closed polygon, revolved about Y
BLANK_PROFILE = [
    (BORE_R + BORE_CHAMFER, 0.0),
    (HUB_R, 0.0),
    (HUB_R, HUB_LEN),
    (HEEL_TIP_R, HEEL_TIP_Y),
    (TOE_TIP_R, TOE_TIP_Y),
    (FRONT_FACE_OUT_R, FRONT_FACE_Y),
    (BORE_R + BORE_CHAMFER, FRONT_FACE_Y),
    (BORE_R, FRONT_FACE_Y - BORE_CHAMFER),
    (BORE_R, BORE_CHAMFER),
]

# tooth-space cutter poles (right half, x >= 0), global frame
SA_FLANK = [(0.87084, 7.27758, 14.26998), (0.96531, 7.52986, 14.87873),
            (1.16091, 7.77651, 15.47392), (1.73652, 8.23609, 16.58289),
            (2.11640, 8.44891, 17.09644), (2.57105, 8.63507, 17.54565)]
SA_FILLET = [(0.87084, 7.27758, 14.26998), (0.84943, 7.22045, 14.13202),
             (0.77207, 7.16685, 14.00268), (0.54276, 7.09215, 13.82243),
             (0.39217, 7.07150, 13.77260), (0.24135, 7.07257, 13.77517)]
SA_ROOT = [(-0.24135, 7.07257, 13.77517), (-0.08047, 7.07371, 13.77791),
           (0.08047, 7.07371, 13.77791), (0.24135, 7.07257, 13.77517)]

SB_FLANK = [(0.55803, 20.67480, 8.76922), (0.65705, 20.93923, 9.40732),
            (0.86209, 21.19778, 10.03121), (1.46545, 21.67950, 11.19366),
            (1.86365, 21.90259, 11.73198), (2.34023, 22.09772, 12.20284)]
SB_FILLET = [(0.55803, 20.67480, 8.76922), (0.54746, 20.64621, 8.70124),
             (0.50926, 20.61973, 8.63737), (0.39602, 20.58283, 8.54836),
             (0.32165, 20.57262, 8.52376), (0.24717, 20.57315, 8.52502)]
SB_ROOT = [(-0.24717, 20.57315, 8.52502), (-0.08241, 20.57425, 8.52785),
           (0.08241, 20.57425, 8.52785), (0.24717, 20.57315, 8.52502)]

BSPL_KNOTS = [0.0, 0.5, 1.0]     # distinct knots of the 6-pole cubic B-splines
BSPL_MULTS = [4, 2, 4]
BEZ_KNOTS = [0.0, 1.0]
BEZ_MULTS = [4, 4]
DEGREE = 3


# ---------------------------------------------------------------- helpers
def bspline_edge(poles, knots, mults, degree=DEGREE) -> Edge:
    p = TColgp_Array1OfPnt(1, len(poles))
    for i, (x, y, z) in enumerate(poles, 1):
        p.SetValue(i, gp_Pnt(x, y, z))
    k = TColStd_Array1OfReal(1, len(knots))
    for i, v in enumerate(knots, 1):
        k.SetValue(i, v)
    m = TColStd_Array1OfInteger(1, len(mults))
    for i, v in enumerate(mults, 1):
        m.SetValue(i, v)
    curve = Geom_BSplineCurve(p, k, m, degree)
    return Edge(BRepBuilderAPI_MakeEdge(curve).Edge())


def mirror_x(poles):
    return [(-x, y, z) for (x, y, z) in poles]


def section_wire(flank, fillet, root) -> Wire:
    """Closed 6-segment chain: L flank, L fillet, root, R fillet, R flank, closing line."""
    b = lambda pts: bspline_edge(pts, BSPL_KNOTS, BSPL_MULTS)
    e1 = b(list(reversed(mirror_x(flank))))     # left flank: pole 6 -> pole 1
    e2 = b(mirror_x(fillet))                    # left fillet: flank junction -> root
    e3 = bspline_edge(root, BEZ_KNOTS, BEZ_MULTS)  # root Bezier, -x -> +x
    e4 = b(list(reversed(fillet)))              # right fillet: root -> flank
    e5 = b(flank)                               # right flank: fillet -> outer end
    e6 = Edge.make_line(flank[-1], mirror_x([flank[-1]])[0])  # closing line
    return Wire([e1, e2, e3, e4, e5, e6])


# ---------------------------------------------------------------- build
def build_blank() -> Solid:
    # profile in the XY plane: x = r, y = y; revolve about global Y
    face = Face(Wire.make_polygon([(r, y, 0) for r, y in BLANK_PROFILE], close=True))
    return revolve(face, Axis.Y, 360)


def build_cutter() -> Solid:
    wa = section_wire(SA_FLANK, SA_FILLET, SA_ROOT)
    wb = section_wire(SB_FLANK, SB_FILLET, SB_ROOT)
    return Solid.make_loft([wa, wb], ruled=True)


def build_gear():
    blank = build_blank()
    cutter = build_cutter()
    cutters = [cutter.rotate(Axis.Y, k * PITCH_ANGLE_STEP) for k in range(N_TEETH)]
    gear = blank.cut(*cutters)
    if not isinstance(gear, Solid):
        solids = gear.solids()
        assert len(solids) == 1, f"expected 1 solid, got {len(solids)}"
        gear = solids[0]
    gear.label = "P01 Miter gear"
    return gear


if __name__ == "__main__":
    out = Path(__file__).with_name("final.step")
    gear = build_gear()
    export_step(gear, str(out))
    bb = gear.bounding_box()
    com = gear.center()
    print(f"valid={gear.is_valid} solids={len(gear.solids())} faces={len(gear.faces())}")
    print(f"volume={gear.volume:.2f} area={gear.area:.2f}")
    print(f"com=({com.X:.3f}, {com.Y:.3f}, {com.Z:.3f})")
    print(f"bbox x[{bb.min.X:.3f},{bb.max.X:.3f}] y[{bb.min.Y:.3f},{bb.max.Y:.3f}] "
          f"z[{bb.min.Z:.3f},{bb.max.Z:.3f}]")
    print(f"wrote {out}")
