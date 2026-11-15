# -*- coding: utf-8 -*-
"""P01 Miter gear (P16) - SolidWorks COM build script.

Usage:  python build_gear.py [output_dir]
Builds the part from scratch in SolidWorks (starts it via COM if needed),
saves P01_Miter_gear.SLDPRT and final.step (AP214) into output_dir
(default: ../ relative to this script, i.e. the teslim folder) and prints
mass properties / bounding box / face count.
Units: mm (API works in metres -> MM()).  Global frame = spec frame:
gear axis = Y, back face y=0, teeth toward +Y.
"""
import os
import sys
import math
import pythoncom
import win32com.client as w32
from win32com.client import VARIANT

# ---------------------------------------------------------------- parameters
P = dict(
    BoreDia=8.0,          # bore diameter
    BoreChamfer=0.4,      # 45 deg bore chamfer, both ends
    HubDia=25.0,          # hub diameter
    HubLength=7.75,       # hub cylinder length (y 0..7.75)
    BackConeR=16.385,     # back cone / tip cone corner radius
    BackConeY=9.36,       # back cone / tip cone corner height (heel OD 32.77)
    ToeTipR=11.73752,     # tip cone / toe cone corner radius
    FaceWidthY=19.33,     # overall width (toe tip edge height)
    ToeR=8.5,             # toe cone inner radius at front face
    FrontFaceY=18.0,      # front face height
    NTeeth=20,            # number of teeth (pattern count)
    SpaceAngle0=90.0,     # angular position of the modelled tooth space (+Z)
)

# Tooth-space cutter poles (right half, x>=0), mm, global frame  -- spec 3.B
SA_FLANK = [(0.87084, 7.27758, 14.26998), (0.96531, 7.52986, 14.87873), (1.16091, 7.77651, 15.47392),
            (1.73652, 8.23609, 16.58289), (2.11640, 8.44891, 17.09644), (2.57105, 8.63507, 17.54565)]
SA_FILLET = [(0.87084, 7.27758, 14.26998), (0.84943, 7.22045, 14.13202), (0.77207, 7.16685, 14.00268),
             (0.54276, 7.09215, 13.82243), (0.39217, 7.07150, 13.77260), (0.24135, 7.07257, 13.77517)]
SA_ROOT = [(-0.24135, 7.07257, 13.77517), (-0.08047, 7.07371, 13.77791), (0.08047, 7.07371, 13.77791),
           (0.24135, 7.07257, 13.77517)]
SB_FLANK = [(0.55803, 20.67480, 8.76922), (0.65705, 20.93923, 9.40732), (0.86209, 21.19778, 10.03121),
            (1.46545, 21.67950, 11.19366), (1.86365, 21.90259, 11.73198), (2.34023, 22.09772, 12.20284)]
SB_FILLET = [(0.55803, 20.67480, 8.76922), (0.54746, 20.64621, 8.70124), (0.50926, 20.61973, 8.63737),
             (0.39602, 20.58283, 8.54836), (0.32165, 20.57262, 8.52376), (0.24717, 20.57315, 8.52502)]
SB_ROOT = [(-0.24717, 20.57315, 8.52502), (-0.08241, 20.57425, 8.52785), (0.08241, 20.57425, 8.52785),
           (0.24717, 20.57315, 8.52502)]
KNOTS6 = [0, 0, 0, 0, 0.5, 0.5, 1, 1, 1, 1]
KNOTS4 = [0, 0, 0, 0, 1, 1, 1, 1]


def G(obj, name):
    """Late-bound COM no-arg member: property or method, whichever it is."""
    a = getattr(obj, name)
    return a() if callable(a) and not hasattr(a, "_oleobj_") else a


def MM(v):
    return v / 1000.0


def mirror(poles):
    return [(-x, y, z) for (x, y, z) in poles]


def vd(lst):
    return VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [float(v) for v in lst])


NOTHING = VARIANT(pythoncom.VT_DISPATCH, None)
_SWMOD = None


def typed(obj, iface):
    """Wrap a late-bound object with the early-bound SolidWorks interface class."""
    global _SWMOD
    if _SWMOD is None:
        from win32com.client import gencache
        _SWMOD = gencache.EnsureModule("{83A33D31-27C5-11CE-BFD4-00400513BB57}", 0, 32, 0)
    return getattr(_SWMOD, iface)(obj._oleobj_)


def connect():
    try:
        sw = w32.GetActiveObject("SldWorks.Application")
    except Exception:
        sw = w32.Dispatch("SldWorks.Application")
    sw.Visible = True
    return sw


def new_part(sw):
    tpl = sw.GetUserPreferenceStringValue(8)  # swDefaultTemplatePart
    model = sw.NewDocument(tpl, 0, 0, 0)
    if model is None:
        raise RuntimeError("NewDocument failed, template=%r" % tpl)
    # mm, 5 decimals
    model.Extension.SetUserPreferenceInteger(263, 0, 5)  # swUnitSystem = swUnitSystem_MMGS
    model.Extension.SetUserPreferenceInteger(49, 0, 5)   # swUnitsLinearDecimalPlaces
    return model


def ref_planes(model):
    planes = []
    f = G(model, "FirstFeature")
    while f is not None:
        if G(f, "GetTypeName2") == "RefPlane":
            planes.append(f)
        f = G(f, "GetNextFeature")
    return planes  # [Front(XY), Top(XZ), Right(YZ)]


def origin_axis_y(model):
    """Reference axis along global Y (for revolve/pattern)."""
    planes = ref_planes(model)
    model.ClearSelection2(True)
    planes[0].Select2(False, 0)   # Front (XY)
    planes[2].Select2(True, 0)    # Right (YZ) -> intersection = Y axis
    model.InsertAxis2(True)
    ax = None
    f = G(model, "FirstFeature")
    while f is not None:
        if G(f, "GetTypeName2") == "RefAxis":
            ax = f
        f = G(f, "GetNextFeature")
    ax.Name = "Axis_Y"
    model.ClearSelection2(True)
    return ax


def add_globals(model):
    eq = G(model, "GetEquationMgr")
    for k, v in P.items():
        unit = "" if k in ("NTeeth",) else ("deg" if "Angle" in k else "mm")
        s = '"%s" = %s%s' % (k, repr(v), unit)
        eq.Add2(-1, s, True)
    return eq


def build_blank(model):
    planes = ref_planes(model)
    model.ClearSelection2(True)
    planes[0].Select2(False, 0)
    sm = model.SketchManager
    sm.InsertSketch(True)
    sm.AddToDB = True
    pts = [(P["BoreDia"] / 2 + P["BoreChamfer"], 0.0),
           (P["HubDia"] / 2, 0.0),
           (P["HubDia"] / 2, P["HubLength"]),
           (P["BackConeR"], P["BackConeY"]),
           (P["ToeTipR"], P["FaceWidthY"]),
           (P["ToeR"], P["FrontFaceY"]),
           (P["BoreDia"] / 2 + P["BoreChamfer"], P["FrontFaceY"]),
           (P["BoreDia"] / 2, P["FrontFaceY"] - P["BoreChamfer"]),
           (P["BoreDia"] / 2, P["BoreChamfer"])]
    segs = []
    for i in range(len(pts)):
        a, b = pts[i], pts[(i + 1) % len(pts)]
        segs.append(sm.CreateLine(MM(a[0]), MM(a[1]), 0, MM(b[0]), MM(b[1]), 0))
    sm.CreateCenterLine(0, 0, 0, 0, MM(25), 0)
    sm.AddToDB = False
    sk = model.SketchManager.ActiveSketch
    skfeat = sk  # sketch object
    sm.InsertSketch(True)
    # name the sketch feature
    f = model.FeatureByPositionReverse(0)
    f.Name = "Sk_BlankProfile"
    model.ClearSelection2(True)
    f.Select2(False, 0)
    feat = model.FeatureManager.FeatureRevolve2(True, True, False, False, False, False,
                                                0, 0, 2 * math.pi, 0, False, False, 0, 0,
                                                0, 0, 0, True, True, True)
    if feat is None:
        raise RuntimeError("Revolve failed")
    feat.Name = "Blank_Revolve"
    return feat


def spline3d(sm, poles, knots):
    pd = typed(G(sm, "CreateSplineParamData"), "ISplineParamData")
    pd.Dimension = 3
    pd.Order = 4
    pd.ControlPointsCount = len(poles)
    pd.Periodic = 0
    ok1 = pd.SetKnotPoints(vd(knots))
    flat = []
    for p in poles:
        flat += [MM(c) for c in p]
    ok2 = pd.SetControlPoints(vd(flat))
    res = typed(sm, "ISketchManager").CreateSplinesByEqnParams2(pd)
    if not res:
        raise RuntimeError("spline creation failed (%s,%s)" % (ok1, ok2))
    return res[0]


def section_sketch(model, flank, fillet, root, name):
    sm = model.SketchManager
    model.ClearSelection2(True)
    sm.Insert3DSketch(True)
    sm.AddToDB = True
    # chain: 1 left flank (6->1), 2 left fillet (1->6), 3 root, 4 right fillet (6->1), 5 right flank, 6 line
    spline3d(sm, list(reversed(mirror(flank))), KNOTS6)
    spline3d(sm, mirror(fillet), KNOTS6)
    spline3d(sm, root, KNOTS4)
    spline3d(sm, list(reversed(fillet)), KNOTS6)
    spline3d(sm, flank, KNOTS6)
    a, b = flank[-1], mirror(flank)[-1]
    sm.CreateLine(MM(a[0]), MM(a[1]), MM(a[2]), MM(b[0]), MM(b[1]), MM(b[2]))
    sm.AddToDB = False
    sm.Insert3DSketch(True)
    f = model.FeatureByPositionReverse(0)
    f.Name = name
    return f


def delete_extra_bodies(model, name):
    """The cut-loft leaves the removed tooth-space volume as a separate body
    (SolidWorks splits instead of removing, see build_log.md); keep only the
    largest body = the gear."""
    bodies = [typed(x, "IBody2") for x in model.GetBodies2(0, True)]
    if len(bodies) < 2:
        return None
    bodies.sort(key=lambda x: x.GetMassProperties(1)[3])
    ext = typed(model.Extension, "IModelDocExtension")
    model.ClearSelection2(True)
    for i, bd in enumerate(bodies[:-1]):
        ext.SelectByID2(bd.Name, "SOLIDBODY", 0, 0, 0, i > 0, 0, None, 0)
    f = typed(model.FeatureManager, "IFeatureManager").InsertDeleteBody2(False)
    if f is None:
        raise RuntimeError("Delete body failed")
    f.Name = name
    return f


def build_cut(model, skA, skB):
    model.ClearSelection2(True)
    skA.Select2(False, 1)
    skB.Select2(True, 1)
    fm = typed(model.FeatureManager, "IFeatureManager")
    # KeepTangency=False: keep flank / fillet / root as separate faces
    feat = fm.InsertCutBlend(False, False, False, 1.0, 0, 0, False, 0, 0, 0, True, True)
    if feat is None:
        raise RuntimeError("Cut loft failed")
    feat.Name = "ToothSpace_Cut"
    delete_extra_bodies(model, "Remove_SpaceSlug")
    return feat


def build_pattern(model, cut, axis):
    model.ClearSelection2(True)
    cut.Select2(False, 4)    # features to pattern: mark 4
    axis.Select2(True, 1)    # axis: mark 1
    fm = typed(model.FeatureManager, "IFeatureManager")
    feat = None
    for geom in (True, False):   # geometry pattern first (works reliably via API here)
        model.ClearSelection2(True)
        cut.Select2(False, 4)
        axis.Select2(True, 1)
        feat = fm.FeatureCircularPattern5(P["NTeeth"], 2 * math.pi, False, "", geom, True,
                                          False, False, False, False, 1, 0, "", False)
        if feat is not None:
            print("pattern ok, GeometryPattern =", geom)
            break
    if feat is None:
        raise RuntimeError("Circular pattern failed")
    feat.Name = "ToothSpace_Pattern"
    delete_extra_bodies(model, "Remove_PatternSlugs")
    return feat


def link_pattern_count(model):
    try:
        eq = typed(G(model, "GetEquationMgr"), "IEquationMgr")
        n = eq.Add2(-1, '"D1@ToothSpace_Pattern" = "NTeeth"', True)
        print("pattern-count link index", n)
    except Exception as e:
        print("pattern-count link failed:", e)


def report(model):
    ext = model.Extension
    mp = typed(ext, "IModelDocExtension").CreateMassProperty()
    mp = typed(mp, "IMassProperty")
    mp.UseSystemUnits = True
    vol = mp.Volume * 1e9
    area = mp.SurfaceArea * 1e6
    com = [c * 1000 for c in mp.CenterOfMass]
    bodies = model.GetBodies2(0, True)
    nf = 0
    for b in bodies:
        nf += G(b, "GetFaceCount")
    box = G(bodies[0], "GetBodyBox")
    box = [v * 1000 for v in box]
    # exact extents via ExtremePoint
    ex = {}
    b = bodies[0]
    for nm, d in (("Xmin", (-1, 0, 0)), ("Xmax", (1, 0, 0)), ("Ymin", (0, -1, 0)),
                  ("Ymax", (0, 1, 0)), ("Zmin", (0, 0, -1)), ("Zmax", (0, 0, 1))):
        try:
            r = b.GetExtremePoint(d[0], d[1], d[2])
            if isinstance(r, tuple) and len(r) >= 4:
                ex[nm] = [v * 1000 for v in r[1:4]]
        except Exception:
            pass
    out = dict(volume=vol, area=area, com=com, faces=nf, nbodies=len(bodies), box=box, extreme=ex)
    return out


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(here, ".."))
    os.makedirs(outdir, exist_ok=True)
    sw = connect()
    model = new_part(sw)
    add_globals(model)
    axis = origin_axis_y(model)
    build_blank(model)
    skA = section_sketch(model, SA_FLANK, SA_FILLET, SA_ROOT, "Sk3D_SectionA_heel")
    skB = section_sketch(model, SB_FLANK, SB_FILLET, SB_ROOT, "Sk3D_SectionB_toe")
    cut = build_cut(model, skA, skB)
    build_pattern(model, cut, axis)
    link_pattern_count(model)
    model.ForceRebuild3(False)
    r = report(model)
    print("REPORT", r)
    sldprt = os.path.join(outdir, "P01_Miter_gear.SLDPRT")
    errs = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    warns = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    ok = model.Extension.SaveAs3(sldprt, 0, 1, NOTHING, NOTHING, errs, warns)
    print("save sldprt", ok, errs.value, warns.value)
    sw.SetUserPreferenceIntegerValue(75, 214)  # swStepAP -> AP214
    step = os.path.join(outdir, "final.step")
    ok = model.Extension.SaveAs3(step, 0, 1 | 2, NOTHING, NOTHING, errs, warns)
    print("save step", ok, errs.value, warns.value)
    return model, r


if __name__ == "__main__":
    main()
