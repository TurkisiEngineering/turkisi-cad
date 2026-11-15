"""P16 - Duz disli konik (miter) disli, duz delikli. build123d 0.11.1.
Calistirma:  python miter_gear.py   -> ayni klasore final.step yazar.
Cerceve: disli ekseni = Y, arka yuz y=0, disler +Y yonunde; birim mm.
"""
import math
from pathlib import Path
from build123d import *
from OCP.Geom import Geom_BSplineCurve
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.gp import gp_Pnt
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge

# ---------------- Parametreler ----------------
N_TEETH = 20                 # dis sayisi
PITCH_ANGLE = 360.0 / N_TEETH  # 18 deg dis bolumu
BORE_R = 4.0                 # delik capi 8
BORE_CHAMFER = 0.4           # delik pahi 0.4 x 45
HUB_R = 12.5                 # gobek capi 25
HUB_LEN = 7.75               # gobek boyu
HEEL_TIP = (16.385, 9.36)    # topuk dis cap kosesi (dis cap 32.77)
TOE_TIP = (11.73752, 19.33)  # burun dis ucu, toplam genislik 19.33
FRONT_Y = 18.0               # on yuz yuksekligi
FRONT_R = 8.5                # on yuz dis yaricapi

# Blank profili (r, y) - spec 3.A
BLANK_PROFILE = [
    (BORE_R + BORE_CHAMFER, 0.0),
    (HUB_R, 0.0),
    (HUB_R, HUB_LEN),
    HEEL_TIP,
    TOE_TIP,
    (FRONT_R, FRONT_Y),
    (BORE_R + BORE_CHAMFER, FRONT_Y),
    (BORE_R, FRONT_Y - BORE_CHAMFER),
    (BORE_R, BORE_CHAMFER),
]

# Kesici kesit kutuplari (sag yari, x>=0) - spec 3.B
SA_FLANK = [(0.87084, 7.27758, 14.26998), (0.96531, 7.52986, 14.87873), (1.16091, 7.77651, 15.47392),
            (1.73652, 8.23609, 16.58289), (2.11640, 8.44891, 17.09644), (2.57105, 8.63507, 17.54565)]
SA_FILLET = [(0.87084, 7.27758, 14.26998), (0.84943, 7.22045, 14.13202), (0.77207, 7.16685, 14.00268),
             (0.54276, 7.09215, 13.82243), (0.39217, 7.07150, 13.77260), (0.24135, 7.07257, 13.77517)]
SA_ROOT = [(-0.24135, 7.07257, 13.77517), (-0.08047, 7.07371, 13.77791),
           (0.08047, 7.07371, 13.77791), (0.24135, 7.07257, 13.77517)]
SB_FLANK = [(0.55803, 20.67480, 8.76922), (0.65705, 20.93923, 9.40732), (0.86209, 21.19778, 10.03121),
            (1.46545, 21.67950, 11.19366), (1.86365, 21.90259, 11.73198), (2.34023, 22.09772, 12.20284)]
SB_FILLET = [(0.55803, 20.67480, 8.76922), (0.54746, 20.64621, 8.70124), (0.50926, 20.61973, 8.63737),
             (0.39602, 20.58283, 8.54836), (0.32165, 20.57262, 8.52376), (0.24717, 20.57315, 8.52502)]
SB_ROOT = [(-0.24717, 20.57315, 8.52502), (-0.08241, 20.57425, 8.52785),
           (0.08241, 20.57425, 8.52785), (0.24717, 20.57315, 8.52502)]

KNOTS_6 = ([0.0, 0.5, 1.0], [4, 2, 4])   # 6 kutuplu kubik B-spline
KNOTS_BEZ = ([0.0, 1.0], [4, 4])         # kubik Bezier


def bspline_edge(poles, knots_mults):
    knots, mults = knots_mults
    P = TColgp_Array1OfPnt(1, len(poles))
    for i, p in enumerate(poles, 1):
        P.SetValue(i, gp_Pnt(*p))
    K = TColStd_Array1OfReal(1, len(knots))
    M = TColStd_Array1OfInteger(1, len(mults))
    for i, (k, m) in enumerate(zip(knots, mults), 1):
        K.SetValue(i, k)
        M.SetValue(i, m)
    curve = Geom_BSplineCurve(P, K, M, 3)
    return Edge(BRepBuilderAPI_MakeEdge(curve).Edge())


def mirror_x(poles):
    return [(-x, y, z) for (x, y, z) in poles]


def section_wire(flank, fillet, root):
    """6 segmentli kapali kesit: sol yanak, sol radyus, taban, sag radyus, sag yanak, kapatma cizgisi."""
    edges = [
        bspline_edge(list(reversed(mirror_x(flank))), KNOTS_6),   # 1 sol yanak: kutup 6 -> 1
        bspline_edge(mirror_x(fillet), KNOTS_6),                  # 2 sol radyus: kutup 1 -> 6
        bspline_edge(root, KNOTS_BEZ),                            # 3 taban
        bspline_edge(list(reversed(fillet)), KNOTS_6),            # 4 sag radyus: kutup 6 -> 1
        bspline_edge(flank, KNOTS_6),                             # 5 sag yanak: kutup 1 -> 6
        Edge.make_line(Vector(*flank[-1]), Vector(*mirror_x(flank)[-1])),  # 6 kapatma
    ]
    return Wire(edges)


def build():
    # A. Blank
    prof = [(r, y) for r, y in BLANK_PROFILE]
    with BuildPart() as bp:
        with BuildSketch(Plane.XY):
            Polygon(*prof, align=None)
        revolve(axis=Axis.Y)
    blank = bp.part.solid()

    # B. Dis bosluk kesicisi (ruled loft)
    wa = section_wire(SA_FLANK, SA_FILLET, SA_ROOT)
    wb = section_wire(SB_FLANK, SB_FILLET, SB_ROOT)
    cutter = Solid.make_loft([wa, wb], ruled=True)

    cutters = [cutter.rotate(Axis.Y, k * PITCH_ANGLE) for k in range(N_TEETH)]
    gear = blank - Compound(cutters)
    gear = gear.solid() if hasattr(gear, "solid") else gear
    gear.label = "P01 Miter gear"
    return gear, blank, cutter


if __name__ == "__main__":
    gear, blank, cutter = build()
    out = Path(__file__).with_name("final.step")
    export_step(gear, str(out))
    bb = gear.bounding_box()
    c = gear.center(CenterOf.MASS)
    print(f"valid={gear.is_valid} solids={len(gear.solids())} faces={len(gear.faces())}")
    print(f"vol={gear.volume:.2f} area={gear.area:.2f} com=({c.X:.3f},{c.Y:.3f},{c.Z:.3f})")
    print(f"bb min=({bb.min.X:.3f},{bb.min.Y:.3f},{bb.min.Z:.3f}) max=({bb.max.X:.3f},{bb.max.Y:.3f},{bb.max.Z:.3f})")
    print("wrote", out)
