# -*- coding: utf-8 -*-
"""
P01 Spanner -- hook spanner wrench for side-slot round nuts (spec P17).
Builds the part from scratch in SolidWorks via COM (pywin32), saves
P01_Spanner.SLDPRT and final.step (AP214, inches) next to this script.

Usage:  python build_spanner.py            (SolidWorks is attached / started via COM)

Global frame (spec): plate between Y=-0.06 and Y=+0.06, outline in XZ, handle along +X,
handle top edge on Z=0, part in Z<=0.  Units: inch (SolidWorks API works in metres,
conversion IN=0.0254 is applied at the API boundary only).
"""
import math
import os
import sys

import pythoncom
import win32com.client
from win32com.client import VARIANT

HERE = os.path.dirname(os.path.abspath(__file__))
PART_PATH = os.path.join(HERE, "P01_Spanner.SLDPRT")
STEP_PATH = os.path.join(HERE, "final.step")

IN = 0.0254  # metres per inch

# ----------------------------------------------------------------------------------
# Named parameters (inch / degree) -- see parametreler.md
# ----------------------------------------------------------------------------------
P = dict(
    T=0.12,                    # plate thickness (F1, symmetric about Y=0)
    X_HEAD_TOP=-1.354007,      # left end of the handle top edge (F1 seg 1/11)
    X_END_C=1.970605,          # x of the handle-end semicircle centre (F1 seg 2)
    R_END=0.194895,            # handle end radius = handle width / 2 (F1 seg 2)
    W_HANDLE=0.389790,         # handle width (F1 seg 3)
    X_NECK=-0.703984,          # start of the neck blend (F1 seg 3/4)
    R_NECK=0.468750,           # concave neck blend radius 15/32 (F1 seg 4)
    NECK_END=(-1.024250, -0.516259),
    HEAD_C=(-1.507307, 0.0),   # head back arc centre (F1 seg 5)
    R_HEAD=0.707013,           # head back radius (F1 seg 5) = head height
    HOOK_P1=(-2.159435, -0.273121),
    HOOK_C=(-2.087375, -0.242941),
    R_HOOK=0.078125,           # hook tip radius 5/64 (F1 seg 6)
    HOOK_P2=(-2.104284, -0.166668),
    PIN_TOP=(-1.931443, -0.128350),   # F1 seg 7 end
    PIN_TIP=(-1.864243, -0.193720),   # F1 seg 8 end
    PIN_LOW=(-1.922674, -0.215905),   # F1 seg 9 end (pin underside 0.0625)
    JAW_C=(-1.696750, 0.0),    # jaw centre (F1 seg 10)
    R_JAW=0.312500,            # jaw radius 5/16 (0.625 nut)
    JAW_END=(-1.411824, -0.128350),
    SLOT_X1=1.918717,          # obround slot centre 1 (F2)
    SLOT_X2=1.944702,          # obround slot centre 2 (F2)
    SLOT_R=0.064965,           # obround slot radius (F2)
    R_EDGE=0.015625,           # handle edge round 1/64 (F3)
    X_ROUND_START=-0.441484,   # rounds start (F3) / run-out start (F4)
    X_RUNOUT_END=-0.478189,    # run-out end, edge sharp again (F4)
    RUNOUT_ANG=10.0,           # run-out cone half angle, deg (F4)
)
P["Z_MID"] = -P["W_HANDLE"] / 2.0
P["Y_FACE"] = P["T"] / 2.0

TARGET = dict(volume=0.208501, area=4.612036, com=(-0.088238, 0.0, -0.251719),
              bbox=(-2.165500, -0.06, -0.707013, 2.165500, 0.06, 0.0), faces=27)

# SolidWorks constants (from swconst.tlb)
swDefaultTemplatePart = 8
swUnitSystem = 263
swUnitSystem_IPS = 3
swStepAP = 75
swEndCondBlind = 0
swEndCondMidPlane = 6
swRefPlaneReferenceConstraint_Distance = 8
swRefPlaneReferenceConstraint_OptionFlip = 256


def log(*a):
    print(*a, flush=True)


# ----------------------------------------------------------------------------------
# SolidWorks helpers
# ----------------------------------------------------------------------------------
swApp = win32com.client.dynamic.Dispatch("SldWorks.Application")
swApp.Visible = True
math_util = swApp.GetMathUtility
math_util._FlagAsMethod("CreatePoint")


def close_if_open(path):
    doc = swApp.GetOpenDocumentByName(path)
    if doc is not None:
        swApp.CloseDoc(doc.GetTitle)


def new_part():
    tmpl = swApp.GetUserPreferenceStringValue(swDefaultTemplatePart)
    doc = swApp.NewDocument(tmpl, 0, 0, 0)
    doc.Extension.SetUserPreferenceInteger(swUnitSystem, 0, swUnitSystem_IPS)
    return doc


def ref_planes(doc):
    planes = []
    f = doc.FirstFeature
    while f is not None:
        if f.GetTypeName2 == "RefPlane":
            planes.append(f)
        f = f.GetNextFeature
    return planes  # Front(XY), Top(XZ), Right(YZ)


def last_feature(doc):
    return doc.FeatureByPositionReverse(0)


class Sketch:
    """Open a sketch on a plane feature; draw with MODEL coordinates in inches."""

    def __init__(self, doc, plane_feat):
        self.doc = doc
        doc.ClearSelection2(True)
        plane_feat.Select2(False, 0)
        sm = doc.SketchManager
        sm.InsertSketch(True)
        sm.AddToDB = True
        sm.DisplayWhenAdded = False
        self.sm = sm
        self.xf = sm.ActiveSketch.ModelToSketchTransform

    def to_sk(self, p):
        arr = VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [p[0] * IN, p[1] * IN, p[2] * IN])
        mp = math_util.CreatePoint(arr).MultiplyTransform(self.xf)
        return list(mp.ArrayData)

    def line(self, a, b, center=False):
        s, e = self.to_sk(a), self.to_sk(b)
        fn = self.sm.CreateCenterLine if center else self.sm.CreateLine
        seg = fn(s[0], s[1], 0.0, e[0], e[1], 0.0)
        assert seg is not None, ("line failed", a, b)
        return seg

    def arc3(self, a, b, m):
        s, e, mm = self.to_sk(a), self.to_sk(b), self.to_sk(m)
        seg = self.sm.Create3PointArc(s[0], s[1], 0.0, e[0], e[1], 0.0, mm[0], mm[1], 0.0)
        assert seg is not None, ("arc failed", a, b, m)
        return seg

    def close(self):
        self.sm.AddToDB = False
        self.sm.DisplayWhenAdded = True
        self.sm.InsertSketch(True)
        feat = last_feature(self.doc)
        return feat


def offset_plane(doc, base, dist_in, probe_model_in, name):
    """Offset plane from `base`; flips if the probe point does not lie on it."""
    for flip in (False, True):
        doc.ClearSelection2(True)
        base.Select2(False, 0)
        c = swRefPlaneReferenceConstraint_Distance | (swRefPlaneReferenceConstraint_OptionFlip if flip else 0)
        doc.FeatureManager.InsertRefPlane(c, abs(dist_in) * IN, 0, 0, 0, 0)
        pl = last_feature(doc)
        assert pl.GetTypeName2 == "RefPlane", pl.GetTypeName2
        t = list(pl.GetSpecificFeature2.Transform.ArrayData)
        nrm, org = t[6:9], t[9:12]
        d = sum((probe_model_in[i] * IN - org[i]) * nrm[i] for i in range(3))
        if abs(d) < 1e-9:
            pl.Name = name
            return pl
        doc.ClearSelection2(True)
        pl.Select2(False, 0)
        doc.EditDelete()
    raise RuntimeError("could not place plane " + name)


def mass(doc):
    ext = doc.Extension
    ext._FlagAsMethod("CreateMassProperty")
    mp = ext.CreateMassProperty()
    v = mp.Volume / IN ** 3
    a = mp.SurfaceArea / IN ** 2
    c = [x / IN for x in mp.CenterOfMass]
    return v, a, c


def volume(doc):
    doc.ForceRebuild3(False)
    return mass(doc)[0]


def cut_extrude_2dir(doc, sketch_feat, d1_in, d2_in, flip=False):
    doc.ClearSelection2(True)
    sketch_feat.Select2(False, 0)
    f = doc.FeatureManager.FeatureCut4(
        False, False, flip, swEndCondBlind, swEndCondBlind, d1_in * IN, d2_in * IN,
        False, False, False, False, 0.0, 0.0, False, False, False, False,
        False, True, True, True, True, False, 0, 0.0, False, False)
    assert f is not None, "FeatureCut4 failed"
    return f


def cut_through_all(doc, sketch_feat):
    doc.ClearSelection2(True)
    sketch_feat.Select2(False, 0)
    swEndCondThroughAllBoth = 9
    f = doc.FeatureManager.FeatureCut4(
        False, False, False, 1, 1, 0.01, 0.01,
        False, False, False, False, 0.0, 0.0, False, False, False, False,
        False, True, True, True, True, False, 0, 0.0, False, False)
    assert f is not None, "through-all cut failed"
    return f


def cut_revolve(doc, sketch_feat, angle_deg, midplane=False, reverse=False):
    doc.ClearSelection2(True)
    sketch_feat.Select2(False, 0)
    t = swEndCondMidPlane if midplane else swEndCondBlind
    f = doc.FeatureManager.FeatureRevolve2(
        True, True, False, True, reverse, False, t, 0,
        math.radians(angle_deg), 0.0, False, False, 0.0, 0.0, 0, 0.0, 0.0, True, True, True)
    assert f is not None, "FeatureRevolve2 failed"
    return f


def delete_feature(doc, f, sketch=None):
    doc.ClearSelection2(True)
    f.Select2(False, 0)
    doc.Extension.DeleteSelection2(1)  # absorbed sketch
    if sketch is not None:
        doc.ClearSelection2(True)
        try:
            if sketch.Select2(False, 0):
                doc.EditDelete()
        except Exception:
            pass


def unsuppress_sketch_reuse(doc, sk):
    return sk


# ----------------------------------------------------------------------------------
# Geometry helpers (model coordinates, inch)
# ----------------------------------------------------------------------------------
def xz(p):          # outline point (x, z) -> model (x, 0, z)
    return (p[0], 0.0, p[1])


def minor_mid(c, r, a, b):
    mx, mz = (a[0] + b[0]) / 2 - c[0], (a[1] + b[1]) / 2 - c[1]
    L = math.hypot(mx, mz)
    return (c[0] + r * mx / L, c[1] + r * mz / L)


def corner_profile(map_ab, r, e=0.01):
    """Corner-minus-quarter-disk region in local (a, b): a = outward from the Y face,
    b = outward from the edge face; corner at (0, 0), round centre at (-r, -r)."""
    _m = map_ab
    map_ab = lambda p: _m(p[0], p[1])
    A, B = (0.0, -r), (-r, 0.0)
    C, D, E = (-r, e), (e, e), (e, -r)
    m = (-r + r / math.sqrt(2), -r + r / math.sqrt(2))
    return [("arc", map_ab(A), map_ab(B), map_ab(m)),
            ("line", map_ab(B), map_ab(C)), ("line", map_ab(C), map_ab(D)),
            ("line", map_ab(D), map_ab(E)), ("line", map_ab(E), map_ab(A))]


def draw(sk, items):
    for it in items:
        if it[0] == "arc":
            sk.arc3(it[1], it[2], it[3])
        else:
            sk.line(it[1], it[2])


# ----------------------------------------------------------------------------------
# Build
# ----------------------------------------------------------------------------------
def build():
    close_if_open(PART_PATH)
    doc = new_part()
    global CUR_DOC
    CUR_DOC = doc
    front, top, right = ref_planes(doc)[:3]

    # Named global variables (equation manager); T drives the F1 depth.
    eq = doc.GetEquationMgr
    for k in ("T", "R_END", "W_HANDLE", "R_NECK", "R_HEAD", "R_HOOK", "R_JAW",
              "SLOT_R", "R_EDGE", "X_ROUND_START", "X_RUNOUT_END", "RUNOUT_ANG"):
        unit = "" if k == "RUNOUT_ANG" else "in"
        eq.Add2(-1, '"%s" = %r%s' % (k, P[k], unit), False)

    # ---------------- F1: outline on Top plane (XZ), midplane extrude T ----------------
    sk = Sketch(doc, top)
    p0 = (P["X_HEAD_TOP"], 0.0)
    p1 = (P["X_END_C"], 0.0)
    p2 = (P["X_END_C"], -P["W_HANDLE"])
    p2m = (P["X_END_C"] + P["R_END"], P["Z_MID"])
    p3 = (P["X_NECK"], -P["W_HANDLE"])
    p4 = P["NECK_END"]
    neck_c = (P["X_NECK"], -P["W_HANDLE"] - P["R_NECK"])
    p5 = P["HOOK_P1"]
    p6 = P["HOOK_P2"]
    p7, p8, p9, p10 = P["PIN_TOP"], P["PIN_TIP"], P["PIN_LOW"], P["JAW_END"]
    sk.line(xz(p0), xz(p1))                                                     # 1
    sk.arc3(xz(p1), xz(p2), xz(p2m))                                            # 2
    sk.line(xz(p2), xz(p3))                                                     # 3
    sk.arc3(xz(p3), xz(p4), xz(minor_mid(neck_c, P["R_NECK"], p3, p4)))         # 4
    sk.arc3(xz(p4), xz(p5), xz(minor_mid(P["HEAD_C"], P["R_HEAD"], p4, p5)))    # 5
    sk.arc3(xz(p5), xz(p6), xz(minor_mid(P["HOOK_C"], P["R_HOOK"], p5, p6)))    # 6
    sk.line(xz(p6), xz(p7))                                                     # 7
    sk.line(xz(p7), xz(p8))                                                     # 8
    sk.line(xz(p8), xz(p9))                                                     # 9
    sk.arc3(xz(p9), xz(p10), xz(minor_mid(P["JAW_C"], P["R_JAW"], p9, p10)))    # 10
    sk.line(xz(p10), xz(p0))                                                    # 11
    s1 = sk.close()
    s1.Name = "SK_F1_Outline"
    doc.ClearSelection2(True)
    s1.Select2(False, 0)
    f1 = doc.FeatureManager.FeatureExtrusion3(
        True, False, False, swEndCondMidPlane, 0, P["T"] * IN, 0.0,
        False, False, False, False, 0.0, 0.0, False, False, False, False,
        True, True, True, 0, 0.0, False)
    assert f1 is not None, "F1 extrude failed"
    f1.Name = "F1_Outline"
    try:
        eq.Add2(-1, '"D1@F1_Outline" = "T"', True)
    except Exception as ex:
        log("equation link failed:", ex)
    v_f1 = volume(doc)
    log("F1 volume", v_f1)

    # ---------------- F2: obround slot, through all ----------------
    sk = Sketch(doc, top)
    zc, r = P["Z_MID"], P["SLOT_R"]
    a1, a2 = P["SLOT_X1"], P["SLOT_X2"]
    sk.line(xz((a1, zc + r)), xz((a2, zc + r)))
    sk.arc3(xz((a2, zc + r)), xz((a2, zc - r)), xz((a2 + r, zc)))
    sk.line(xz((a2, zc - r)), xz((a1, zc - r)))
    sk.arc3(xz((a1, zc - r)), xz((a1, zc + r)), xz((a1 - r, zc)))
    s2 = sk.close()
    s2.Name = "SK_F2_Slot"
    f2 = cut_through_all(doc, s2)
    f2.Name = "F2_Slot"
    v_f2 = volume(doc)
    log("F2 volume", v_f2)

    # ---------------- F3a: straight handle rounds (4 edges), cut from x=X_ROUND_START to X_END_C ----
    re_ = P["R_EDGE"]
    yf = P["Y_FACE"]
    def straight_sketch():
        sk = Sketch(doc, right)  # YZ plane at X=0
        for sy in (1, -1):
            for edge_z, n in ((0.0, 1), (-P["W_HANDLE"], -1)):
                mp = (lambda a, b, sy=sy, edge_z=edge_z, n=n: (0.0, sy * (yf + a), edge_z + n * b))
                draw(sk, corner_profile(mp, re_))
        s = sk.close()
        s.Name = "SK_F3_StraightRounds"
        return s
    L_pos, L_neg = P["X_END_C"], -P["X_ROUND_START"]
    expect = 4 * (1 - math.pi / 4) * re_ ** 2 * (L_pos - P["X_ROUND_START"])
    for flip in (False, True):
        d1, d2 = (L_pos, L_neg) if not flip else (L_neg, L_pos)
        s3 = straight_sketch()
        f3 = cut_extrude_2dir(doc, s3, d1, d2)
        dv = v_f2 - volume(doc)
        log("F3a flip", flip, "removed", dv, "expected", expect)
        if abs(dv - expect) < 0.01 * expect:
            break
        delete_feature(doc, f3, s3)
    else:
        raise RuntimeError("F3a direction")
    f3.Name = "F3a_HandleRounds"
    v_f3 = volume(doc)

    # ---------------- F3b: toroidal round around the semicircular end ----------------
    pl_end = offset_plane(doc, front, abs(P["Z_MID"]), (P["X_END_C"], 0.0, P["Z_MID"]), "PL_EndAxis")
    sk = Sketch(doc, pl_end)
    xc, zc = P["X_END_C"], P["Z_MID"]
    sk.line((xc, -0.1, zc), (xc, 0.1, zc), center=True)
    for sy in (1, -1):
        mp = (lambda a, b, sy=sy: (xc + P["R_END"] + b, sy * (yf + a), zc))
        draw(sk, corner_profile(mp, re_))
    s4 = sk.close()
    s4.Name = "SK_F3_EndRound"
    f4 = cut_revolve(doc, s4, 180.0, midplane=True)
    f4.Name = "F3b_EndRound"
    v_f4 = volume(doc)
    log("F3b removed", v_f3 - v_f4)

    # ---------------- F4: conical run-outs (4 places), 90 deg cut-revolves ----------------
    x1, x2 = P["X_ROUND_START"], P["X_RUNOUT_END"]
    r1 = re_
    r2 = re_ + math.tan(math.radians(P["RUNOUT_ANG"])) * (x1 - x2)
    big = 0.03
    yc = yf - re_
    planes = {}
    for sy in (1, -1):
        planes[sy] = offset_plane(doc, top, yc, (0.0, sy * yc, -0.1),
                                  "PL_Runout_%s" % ("Pos" if sy > 0 else "Neg"))
    v_prev = v_f4
    k = 0
    for sy in (1, -1):
        for edge_z, n, tag in ((0.0, 1, "Top"), (-P["W_HANDLE"], -1, "Bot")):
            zcl = edge_z - n * re_
            q = [(x1, zcl + n * r1), (x2, zcl + n * r2), (x2, zcl + n * big), (x1, zcl + n * big)]

            def runout(rev):
                sk = Sketch(doc, planes[sy])
                sk.line((x1 + 0.05, sy * yc, zcl), (x2 - 0.05, sy * yc, zcl), center=True)
                for i in range(4):
                    a, b = q[i], q[(i + 1) % 4]
                    sk.line((a[0], sy * yc, a[1]), (b[0], sy * yc, b[1]))
                s = sk.close()
                f = cut_revolve(doc, s, 90.0, reverse=rev)
                return s, f, v_prev - volume(doc)
            s, f, dv0 = runout(False)
            delete_feature(doc, f, s)
            s, f, dv1 = runout(True)
            log("F4", tag, sy, "removed fwd/rev", dv0, dv1)
            if dv0 < dv1:
                delete_feature(doc, f, s)
                s, f, dv = runout(False)
            k += 1
            s.Name = "SK_F4_Runout%d" % k
            f.Name = "F4_Runout_%s_%s" % (tag, "Pos" if sy > 0 else "Neg")
            v_prev = volume(doc)
            log("F4", f.Name, "kept, removed", min(dv0, dv1))

    # ---------------- checks ----------------
    doc.ForceRebuild3(False)
    bodies = doc.GetBodies2(0, True)
    log("bodies", len(bodies))
    body = bodies[0]
    try:
        body.Name = "P01 Spanner"
    except Exception as ex:
        log("body rename failed", ex)
    v, a, c = mass(doc)
    bb = []  # tight box from extreme points: Xmin Ymin Zmin Xmax Ymax Zmax
    for d in [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        r = body.GetExtremePoint(d[0], d[1], d[2], 0.0, 0.0, 0.0)
        bb.append(round(sum(r[1 + i] * abs(d[i]) for i in range(3)) / IN, 6))
    nf = body.GetFaceCount
    nf = nf() if callable(nf) else nf
    res = dict(volume=v, area=a, com=c, bbox=bb, faces=nf)
    log("RESULT", res)
    log("TARGET", TARGET)
    log("dV %.4f%%  dA %.4f%%" % (100 * (v / TARGET["volume"] - 1), 100 * (a / TARGET["area"] - 1)))

    # ---------------- save ----------------
    err = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    wrn = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    ok = doc.Extension.SaveAs(PART_PATH, 0, 1, VARIANT(pythoncom.VT_DISPATCH, None), err, wrn)
    log("save sldprt", ok, err.value, wrn.value)
    swApp.SetUserPreferenceIntegerValue(swStepAP, 214)
    split_old = swApp.GetUserPreferenceToggle(396)       # swStepExportSplitPeriodic
    swApp.SetUserPreferenceToggle(396, False)            # keep 27 faces in the STEP
    err2 = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    wrn2 = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    ok = doc.Extension.SaveAs(STEP_PATH, 0, 1, VARIANT(pythoncom.VT_DISPATCH, None), err2, wrn2)
    log("save step", ok, err2.value, wrn2.value)
    swApp.SetUserPreferenceToggle(396, split_old)        # restore user setting
    return doc, res


CUR_DOC = None
if __name__ == "__main__":
    try:
        doc, res = build()
    except Exception:
        if CUR_DOC is not None and "--keep-open" not in sys.argv:
            swApp.CloseDoc(CUR_DOC.GetTitle)
        raise
    if "--keep-open" not in sys.argv:
        swApp.CloseDoc(doc.GetTitle)
