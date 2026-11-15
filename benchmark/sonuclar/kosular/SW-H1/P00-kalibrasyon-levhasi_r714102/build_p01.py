# -*- coding: utf-8 -*-
"""
P01 Plate (calibration plate P0) - SolidWorks COM build script.
Usage:  python build_p01.py [output_dir]
Builds the part from scratch in a new SolidWorks part document, writes
P01_Plate.SLDPRT and final.step (AP214) into output_dir (default: this script's folder),
prints the measured properties and closes only the document it created.

Global frame (spec): mm, plate bottom on XY plane (Z=0), +Z up, centred on origin.
SolidWorks "Front Plane" == model XY plane with normal +Z, so every sketch is made on
Front Plane (or a plane offset from it along +Z): sketch x,y == model X,Y.
"""
import os
import sys
import math
import pythoncom
import win32com.client
from win32com.client import VARIANT

# ---------------------------------------------------------------- parameters (mm)
P = {
    "L": 100.0,          # plate length along X
    "W": 60.0,           # plate width along Y
    "T": 10.0,           # plate thickness along Z
    "R_corner": 3.0,     # vertical corner round radius
    "D_hole": 6.0,       # corner through-hole diameter
    "E_hole": 8.0,       # hole centre distance from adjacent outer edges
    "D_pocket": 20.0,    # central pocket diameter
    "H_pocket": 4.0,     # central pocket depth from top face
}
MM = 0.001  # SolidWorks API works in metres

# ---------------------------------------------------------------- SW constants (from swconst.tlb)
swDefaultTemplatePart = 8
swInputDimValOnCreate = 10
swSketchInference = 249
swUnitSystem = 263
swUnitSystem_MMGS = 5
swStepAP = 75
swEndCondBlind = 0
swEndCondThroughAll = 1
swEndCondThroughAllBoth = 9
swFmFillet = 1
swConstRadiusFillet = 0

OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
NULL_DISP = VARIANT(pythoncom.VT_DISPATCH, None)


def log(*a):
    print(*a, flush=True)


def get_sw():
    try:
        sw = win32com.client.GetActiveObject("SldWorks.Application")
    except Exception:
        sw = win32com.client.Dispatch("SldWorks.Application")
    sw.Visible = True
    return sw


def measure(doc, label):
    mp = g(doc.Extension, "CreateMassProperty")
    mp.UseSystemUnits = True
    vol = mp.Volume / MM ** 3
    area = mp.SurfaceArea / MM ** 2
    com = [c / MM for c in mp.CenterOfMass]
    bodies = doc.GetBodies2(0, False)
    box = [b / MM for b in g(bodies[0], "GetBodyBox")]
    nf = g(bodies[0], "GetFaceCount")
    log(f"[{label}] bodies={len(bodies)} V={vol:.3f} A={area:.3f} "
        f"CoM=({com[0]:.4f},{com[1]:.4f},{com[2]:.4f}) "
        f"box=({box[0]:.3f},{box[1]:.3f},{box[2]:.3f})-({box[3]:.3f},{box[4]:.3f},{box[5]:.3f}) faces={nf}")
    return dict(V=vol, A=area, com=com, box=box, faces=nf, nbodies=len(bodies))


def g(obj, name):
    """late-bound no-arg method / property access (pywin32 dynamic dispatch exposes
    argument-less SolidWorks methods as properties)"""
    v = getattr(obj, name)
    return v() if callable(v) and not hasattr(v, "_oleobj_") else v


def dim_name(dd):
    """'D1@Sketch1@Part1.SLDPRT' -> 'D1@Sketch1'  (dd: DisplayDimension or dimension name)"""
    if isinstance(dd, str):
        return dd
    full = dd.GetDimension2(0).FullName
    return "@".join(full.split("@")[:2])


def main():
    sw = get_sw()
    sw.SetUserPreferenceToggle(swInputDimValOnCreate, False)
    tmpl = sw.GetUserPreferenceStringValue(swDefaultTemplatePart)
    doc = sw.NewDocument(tmpl, 0, 0, 0)
    if doc is None:
        raise RuntimeError("NewDocument failed (template: %s)" % tmpl)
    try:
        return build(sw, doc)
    except Exception:
        sw.CloseDoc(g(doc, "GetTitle"))   # close only our own document
        raise


def build(sw, doc):
    ext = doc.Extension
    ext.SetUserPreferenceInteger(swUnitSystem, 0, swUnitSystem_MMGS)
    skm = doc.SketchManager
    fm = doc.FeatureManager
    eqm = g(doc, "GetEquationMgr")

    # ---- global variables (named parameters)
    for k, v in P.items():
        eqm.Add2(-1, f'"{k}" = {v:g}', True)
    links = []  # (dimension name, expression)

    L, W, T = P["L"] * MM, P["W"] * MM, P["T"] * MM

    # ================================================= F1 Plate block
    ext.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, NULL_DISP, 0)
    skm.InsertSketch(True)
    skm.AddToDB = True
    segs = skm.CreateCenterRectangle(0, 0, 0, L / 2, W / 2, 0)
    skm.AddToDB = False
    # segs: 4 lines (+ construction diagonals). find a horizontal & a vertical edge line
    hline = vline = None
    for s in segs:
        try:
            sp, ep = g(s, "GetStartPoint2"), g(s, "GetEndPoint2")
        except Exception:
            continue
        if s.ConstructionGeometry:
            continue
        if abs(sp.Y - ep.Y) < 1e-9 and hline is None:
            hline = s
        elif abs(sp.X - ep.X) < 1e-9 and vline is None:
            vline = s
    doc.ClearSelection2(True)
    hline.Select4(False, NULL_DISP)
    d = doc.AddDimension2(0, W / 2 + 0.01, 0)
    links.append((d, '"L"'))
    doc.ClearSelection2(True)
    vline.Select4(False, NULL_DISP)
    d = doc.AddDimension2(L / 2 + 0.01, 0, 0)
    links.append((d, '"W"'))
    doc.ClearSelection2(True)
    skm.InsertSketch(True)
    sk1 = doc.FeatureByPositionReverse(0)
    sk1.Name = "SK_PlateOutline"

    sk1.Select2(False, 0)
    f1 = fm.FeatureExtrusion3(True, False, False, swEndCondBlind, 0, T, 0,
                              False, False, False, False, 0, 0,
                              False, False, False, False, True, True, True, 0, 0, False)
    if f1 is None:
        raise RuntimeError("F1 extrusion failed")
    f1.Name = "F1_PlateBlock"
    links.append(("D1@F1_PlateBlock", '"T"'))
    m = measure(doc, "F1")
    if m["box"][2] < -1e-6:  # extruded towards -Z -> flip
        raise RuntimeError("F1 extruded in -Z")

    # ================================================= F2 Corner rounds (fillet feature on 4 vertical edges)
    doc.ClearSelection2(True)
    body = doc.GetBodies2(0, False)[0]
    nsel = 0
    for e in g(body, "GetEdges"):
        p0 = g(g(e, "GetStartVertex"), "GetPoint")
        p1 = g(g(e, "GetEndVertex"), "GetPoint")
        # vertical edge (parallel to Z) at |X| = L/2, |Y| = W/2
        if (abs(p0[0] - p1[0]) < 1e-9 and abs(p0[1] - p1[1]) < 1e-9
                and abs(abs(p0[0]) - L / 2) < 1e-9 and abs(abs(p0[1]) - W / 2) < 1e-9):
            if e.Select4(True, NULL_DISP):
                nsel += 1
    if nsel != 4:
        raise RuntimeError("corner edge selection: %d edges" % nsel)
    empty = VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [])
    f2 = fm.FeatureFillet3(195, P["R_corner"] * MM, 0, 0, 0, 0, 0,
                           empty, empty, empty, empty, empty, empty, empty)
    if f2 is None:
        raise RuntimeError("F2 fillet failed")
    f2.Name = "F2_CornerRounds"
    links.append(("D1@F2_CornerRounds", '"R_corner"'))
    measure(doc, "F2")

    # ================================================= F3 Corner holes (through all)
    doc.ClearSelection2(True)
    ext.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, NULL_DISP, 0)
    skm.InsertSketch(True)
    skm.AddToDB = True
    hx = (P["L"] / 2 - P["E_hole"]) * MM
    hy = (P["W"] / 2 - P["E_hole"]) * MM
    rh = P["D_hole"] / 2 * MM
    circles = []
    for sx, sy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        circles.append(skm.CreateCircleByRadius(sx * hx, sy * hy, 0, rh))
    skm.AddToDB = False
    doc.ClearSelection2(True)
    circles[3].Select4(False, NULL_DISP)
    d = doc.AddDimension2(hx + 0.008, hy + 0.008, 0)
    links.append((d, '"D_hole"'))
    doc.ClearSelection2(True)
    skm.InsertSketch(True)
    sk3 = doc.FeatureByPositionReverse(0)
    sk3.Name = "SK_CornerHoles"
    sk3.Select2(False, 0)
    f3 = fm.FeatureCut4(False, False, False, swEndCondThroughAllBoth, swEndCondBlind, 0.01, 0.01,
                        False, False, False, False, 0, 0, False, False, False, False,
                        False, True, True, True, True, False, 0, 0, False, False)
    if f3 is None:
        raise RuntimeError("F3 cut failed")
    f3.Name = "F3_CornerHoles"
    measure(doc, "F3")

    # ================================================= F4 Central pocket (blind, from top face)
    doc.ClearSelection2(True)
    ext.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, NULL_DISP, 0)
    pl = fm.InsertRefPlane(8, T, 0, 0, 0, 0)   # 8 = swRefPlaneReferenceConstraint_Distance
    if pl is None:
        raise RuntimeError("top plane failed")
    pl.Name = "PL_TopZ10"
    links.append(("D1@PL_TopZ10", '"T"'))
    doc.ClearSelection2(True)
    pl.Select2(False, 0)
    skm.InsertSketch(True)
    skm.AddToDB = True
    c = skm.CreateCircleByRadius(0, 0, 0, P["D_pocket"] / 2 * MM)
    skm.AddToDB = False
    doc.ClearSelection2(True)
    c.Select4(False, NULL_DISP)
    d = doc.AddDimension2(0.015, 0.015, 0)
    links.append((d, '"D_pocket"'))
    doc.ClearSelection2(True)
    skm.InsertSketch(True)
    sk4 = doc.FeatureByPositionReverse(0)
    sk4.Name = "SK_Pocket"
    before = measure(doc, "pre-F4")["V"]
    f4 = None
    for rev in (False, True):   # reverse-direction flag; never flip side-to-cut
        sk4.Select2(False, 0)
        f4 = fm.FeatureCut4(True, False, rev, swEndCondBlind, swEndCondBlind, P["H_pocket"] * MM, 0,
                            False, False, False, False, 0, 0, False, False, False, False,
                            False, True, True, True, True, False, 0, 0, False, False)
        if f4 is not None and before - measure(doc, f"F4 rev={rev}")["V"] > 1.0:
            break
        if f4 is not None:  # cut went into empty space -> undo and try the other direction
            doc.EditUndo2(1)
        f4 = None
    if f4 is None:
        raise RuntimeError("F4 pocket failed")
    f4.Name = "F4_CentralPocket"
    links.append(("D1@F4_CentralPocket", '"H_pocket"'))

    # ---- body name
    body = doc.GetBodies2(0, False)[0]
    body.Name = "P01 Plate"

    # ---- link dimensions to global variables
    for dd, expr in links:
        dn = dim_name(dd)
        idx = eqm.Add2(-1, f'"{dn}" = {expr}', True)
        log("equation", idx, dn, "=", expr)
    # hole position dimensions are expressed as relations in a derived equation-free way;
    doc.ForceRebuild3(False)
    res = measure(doc, "FINAL")
    log("equations:", [eqm.Equation(i) for i in range(g(eqm, "GetCount"))])

    # ---- save native + STEP AP214
    os.makedirs(OUT, exist_ok=True)
    sldprt = os.path.join(OUT, "P01_Plate.SLDPRT")
    step = os.path.join(OUT, "final.step")
    for p in (sldprt, step):
        if os.path.exists(p):
            os.remove(p)
    sw.SetUserPreferenceIntegerValue(swStepAP, 214)
    r1 = doc.SaveAs3(sldprt, 0, 1)
    r2 = doc.SaveAs3(step, 0, 1)
    log("save sldprt", r1, os.path.exists(sldprt), "| save step", r2, os.path.exists(step))
    title = g(doc, "GetTitle")
    sw.CloseDoc(title)
    return res


if __name__ == "__main__":
    main()
