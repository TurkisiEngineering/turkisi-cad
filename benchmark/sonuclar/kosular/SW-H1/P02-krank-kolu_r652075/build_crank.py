# -*- coding: utf-8 -*-
"""
P01 Crank handle -- SolidWorks COM (pywin32) rebuild script.

Usage:  python build_crank.py [output_dir]
  output_dir defaults to the folder of this script.
Produces: "P01 Crank handle.SLDPRT", final.step (AP214), measure.json

Global frame / units exactly as spec: mm, hub/bore axis = X, hub bottom face X=0,
arm toward -Y, grip axis Y=-100 Z=0, symmetric about Z=0.
All named parameters are in PARAM below (also written into the SLDPRT as
global variables in the Equation Manager).
"""
import json
import math
import os
import sys

import pythoncom
import win32com.client
from win32com.client import VARIANT

# --------------------------------------------------------------------------
# Named parameters (mm)
# --------------------------------------------------------------------------
PARAM = {
    # hub / bore
    "hub_d": 28.0,              # A1 step 1-2, hub cylinder diameter
    "hub_len": 28.0,            # A1 step 11, hub top face X
    "hub_cyl_end_x": 18.153,    # A1 step 2, end of hub cylinder
    "bore_d": 10.0,             # C, through bore diameter
    "csk_d": 13.4641,           # C, countersink diameter at X=0 (120 deg incl.)
    "csk_depth": 1.0,           # C, countersink depth
    # S-neck / arm (revolve A1)
    "neck_fillet_r": 2.5,       # A1 step 3
    "neck_in_r": 18.0,          # A1 step 4
    "neck_rev_r": 30.0,         # A1 step 5
    "arm_in_x": 48.0,           # A1 step 6, arm inner face X
    "arm_out_x": 52.68507,      # A1 step 7-8, arm outer face X
    "arm_radial_constr": 112.0, # A1 step 6-7, construction radius (trimmed by A2)
    "neck_out_r": 37.5,         # A1 step 9
    "neck_out_r2": 10.5,        # A1 step 10
    # plan outline (A2)
    "collar_r": 15.5,           # A2 hub collar radius
    "crank_r": 100.0,           # hub axis -> grip axis
    "boss_plan_r": 8.0,         # A2 grip boss circle radius
    "arm_half_w0": 8.25150,     # A2 strip half width at y=0
    "arm_taper": 0.0150150,     # A2 strip half width slope dz/dy
    "blend_hub_r": 22.5,        # A2 blend arc at hub
    "blend_grip_r": 13.5,       # A2 blend arc at grip boss
    # grip (revolve B)
    "grip_boss_d": 16.0,        # B step 1-2
    "grip_boss_end_x": 60.5,    # B step 2
    "grip_boss_edge_r": 0.5,    # B step 3
    "grip_neck_d": 13.0,        # B step 5
    "grip_neck_x0": 61.0,       # B step 4
    "grip_neck_x1": 67.0,       # B step 6
    "grip_collar_d": 18.0,      # B step 7
    "grip_concave_r": 17.1,     # B step 8
    "grip_barrel_r": 40.502,    # B step 9 (barrel max dia 20 at x=103.95)
    "grip_end_r": 4.1,          # B step 10 spherical end radius
    "grip_end_x": 128.0,        # B step 10 overall X length
}
P = PARAM

MM = 0.001  # SolidWorks API works in metres


def V(x):
    """pywin32 may expose no-arg COM methods as properties (late bound) or as
    methods (gen_py early bound) -- return the value either way."""
    import types
    return x() if isinstance(x, types.MethodType) else x


def vnone():
    return VARIANT(pythoncom.VT_DISPATCH, None)


def connect():
    sw = win32com.client.Dispatch("SldWorks.Application")
    sw.Visible = True
    return sw


class Sk:
    """Thin helper around SketchManager working in mm."""

    def __init__(self, model):
        self.sm = model.SketchManager

    def line(self, a, b):
        s = self.sm.CreateLine(a[0] * MM, a[1] * MM, 0, b[0] * MM, b[1] * MM, 0)
        assert s is not None, ("line", a, b)
        return s

    def cline(self, a, b):
        s = self.sm.CreateCenterLine(a[0] * MM, a[1] * MM, 0, b[0] * MM, b[1] * MM, 0)
        assert s is not None, ("cline", a, b)
        return s

    def arc(self, c, a, b):
        """Minor arc with centre c from a to b, drawn as a 3-point arc through
        the angular midpoint (more robust than CreateArc + direction flag)."""
        r = math.hypot(a[0] - c[0], a[1] - c[1])
        t1 = math.atan2(a[1] - c[1], a[0] - c[0])
        t2 = math.atan2(b[1] - c[1], b[0] - c[0])
        dt = (t2 - t1 + math.pi) % (2 * math.pi) - math.pi  # minor sweep
        tm = t1 + dt / 2
        mid = (c[0] + r * math.cos(tm), c[1] + r * math.sin(tm))
        return self.arc3(a, b, mid)

    def arc3(self, a, b, m):
        """3-point arc start a, end b, through m."""
        s = self.sm.Create3PointArc(a[0] * MM, a[1] * MM, 0, b[0] * MM, b[1] * MM, 0,
                                    m[0] * MM, m[1] * MM, 0)
        assert s is not None, ("arc3", a, b, m)
        return s


def select_plane(model, name):
    ok = model.Extension.SelectByID2(name, "PLANE", 0, 0, 0, False, 0, vnone(), 0)
    assert ok, "cannot select " + name


def open_sketch(model, plane, name):
    model.ClearSelection2(True)
    select_plane(model, plane)
    model.SketchManager.InsertSketch(True)
    sk = model.SketchManager.ActiveSketch
    sk_feat = sk  # ISketch -> IFeature via cast is not needed; rename after closing
    return Sk(model)


def close_sketch(model, name):
    model.SketchManager.InsertSketch(True)
    feat = model.FeatureByPositionReverse(0)
    feat.Name = name
    return feat


def revolve(model, sketch_name, feat_name, cut=False):
    model.ClearSelection2(True)
    model.Extension.SelectByID2(sketch_name, "SKETCH", 0, 0, 0, False, 0, vnone(), 0)
    fm = model.FeatureManager
    f = fm.FeatureRevolve2(True, True, False, cut, False, False,
                           0, 0, 2 * math.pi, 0, False, False, 0, 0,
                           0, 0, 0, True, True, True)
    assert f is not None, "revolve failed: " + feat_name
    f.Name = feat_name
    return f


def build(outdir):
    sw = connect()
    model = None
    try:
        return _build(sw, outdir)
    except Exception:
        doc = sw.ActiveDoc
        if doc is not None and V(doc.GetPathName) == "" and not os.environ.get("KEEP"):
            sw.CloseDoc(V(doc.GetTitle))  # close only our own unsaved document
        raise


def _build(sw, outdir):
    tmpl = sw.GetUserPreferenceStringValue(8)  # swDefaultTemplatePart
    model = sw.NewDocument(tmpl, 0, 0, 0)
    assert model is not None, "NewDocument failed"
    sm = model.SketchManager
    sm.AddToDB = True
    sm.DisplayWhenAdded = False

    # ---------------------------------------------------------------
    # A1  hub + S-neck + arm disc : revolve about X, sketch on Front (XY)
    #     sketch x = model X, sketch y = model Y (= r)
    # ---------------------------------------------------------------
    hub_r = P["hub_d"] / 2
    x_in, x_out, R = P["arm_in_x"], P["arm_out_x"], P["arm_radial_constr"]
    s = open_sketch(model, "Front Plane", "SK_A1")
    s.cline((-5, 0), (60, 0))
    s.line((0, 0), (0, hub_r))
    s.line((0, hub_r), (P["hub_cyl_end_x"], hub_r))
    s.arc((P["hub_cyl_end_x"], hub_r + P["neck_fillet_r"]), (P["hub_cyl_end_x"], hub_r), (20.63435, 16.19512))
    s.arc((38.5, 14.0), (20.63435, 16.19512), (30.8125, 30.27582))
    s.arc((x_in - P["neck_rev_r"], 57.40224), (30.8125, 30.27582), (x_in, 57.40224))
    s.line((x_in, 57.40224), (x_in, R))
    s.line((x_in, R), (x_out, R))
    s.line((x_out, R), (x_out, 54.40268))
    s.arc((15.21507, 55.90244), (x_out, 54.40268), (32.53906, 22.64391))
    s.arc((38.5, 14.0), (32.53906, 22.64391), (P["hub_len"], 14.0))
    s.line((P["hub_len"], 14.0), (P["hub_len"], 0))
    s.line((P["hub_len"], 0), (0, 0))
    close_sketch(model, "SK_A1")
    revolve(model, "SK_A1", "A1_HubArmRevolve")

    # ---------------------------------------------------------------
    # A2  plan outline, keep inside (extrude-cut, flip side) ; sketch on
    #     Right Plane (YZ). sketch y = model Y; sketch x = +/-Z (symmetric)
    #     Points below are written as (z, y).
    # ---------------------------------------------------------------
    cr = P["collar_r"]
    yg = -P["crank_r"]
    s = open_sketch(model, "Right Plane", "SK_A2")
    hub_t = (12.40487, -9.29351)     # tangent blend R22.5 / R15.5 (z, y)
    strip_h = (7.91447, -22.44628)   # tangent blend R22.5 / strip
    strip_g = (6.85697, -92.87592)   # tangent blend R13.5 / strip
    boss_t = (7.57412, -97.42460)    # tangent blend R13.5 / R8
    c_h = (30.41193, -22.78408)
    c_g = (20.35545, -93.07860)

    def m(p):  # mirror z
        return (-p[0], p[1])

    # hub circle, major arc through (0, +15.5)
    s.arc3(hub_t, m(hub_t), (0, cr))
    # -z side
    s.arc(m(c_h), m(hub_t), m(strip_h))
    s.line(m(strip_h), m(strip_g))
    s.arc(m(c_g), m(strip_g), m(boss_t))
    # grip boss circle, major arc through (0, -108)
    s.arc3(m(boss_t), boss_t, (0, yg - P["boss_plan_r"]))
    # +z side
    s.arc(c_g, boss_t, strip_g)
    s.line(strip_g, strip_h)
    s.arc(c_h, strip_h, hub_t)
    close_sketch(model, "SK_A2")

    model.ClearSelection2(True)
    model.Extension.SelectByID2("SK_A2", "SKETCH", 0, 0, 0, False, 0, vnone(), 0)
    fm = model.FeatureManager
    f = fm.FeatureCut4(False, True, False, 1, 0, 0.2, 0.2, False, False, False, False,
                       0, 0, False, False, False, False, False, True, True, True, True,
                       False, 0, 0, False, False)
    assert f is not None, "A2 cut failed"
    f.Name = "A2_PlanTrim"

    # ---------------------------------------------------------------
    # B  grip revolve about Y=-100 (Front plane), r measured toward +Y
    # ---------------------------------------------------------------
    def g(x, r):
        return (x, yg + r)

    s = open_sketch(model, "Front Plane", "SK_B")
    s.cline(g(40, 0), g(135, 0))
    bR = P["grip_boss_d"] / 2
    s.line(g(x_in, 0), g(x_in, bR))
    s.line(g(x_in, bR), g(P["grip_boss_end_x"], bR))
    s.arc(g(P["grip_boss_end_x"], bR - P["grip_boss_edge_r"]), g(P["grip_boss_end_x"], bR),
          g(P["grip_neck_x0"], bR - P["grip_boss_edge_r"]))
    s.line(g(P["grip_neck_x0"], 7.5), g(P["grip_neck_x0"], P["grip_neck_d"] / 2))
    s.line(g(P["grip_neck_x0"], P["grip_neck_d"] / 2), g(P["grip_neck_x1"], P["grip_neck_d"] / 2))
    s.line(g(P["grip_neck_x1"], P["grip_neck_d"] / 2), g(P["grip_neck_x1"], P["grip_collar_d"] / 2))
    s.line(g(P["grip_neck_x1"], P["grip_collar_d"] / 2), g(72.96886, P["grip_collar_d"] / 2))
    s.arc(g(82.729, 23.041), g(72.96886, 9.0), g(89.40919, 7.29981))
    s.arc(g(103.95, -30.502), g(89.40919, 7.29981), g(125.58325, 3.73854))
    s.arc(g(P["grip_end_x"] - P["grip_end_r"], 0), g(125.58325, 3.73854), g(P["grip_end_x"], 0))
    s.line(g(P["grip_end_x"], 0), g(x_in, 0))
    close_sketch(model, "SK_B")
    revolve(model, "SK_B", "B_GripRevolve")

    # ---------------------------------------------------------------
    # C  bore + 120deg countersink : revolve cut about X (Front plane)
    #    profile extended to x = hub_len + 1 to avoid a coplanar cap
    # ---------------------------------------------------------------
    s = open_sketch(model, "Front Plane", "SK_C")
    rb = P["bore_d"] / 2
    s.cline((-5, 0), (40, 0))
    s.line((-0.0, 0), (0, P["csk_d"] / 2))
    s.line((0, P["csk_d"] / 2), (P["csk_depth"], rb))
    s.line((P["csk_depth"], rb), (P["hub_len"] + 1, rb))
    s.line((P["hub_len"] + 1, rb), (P["hub_len"] + 1, 0))
    s.line((P["hub_len"] + 1, 0), (0, 0))
    close_sketch(model, "SK_C")
    revolve(model, "SK_C", "C_Bore", cut=True)

    sm.AddToDB = False
    sm.DisplayWhenAdded = True

    # global variables (documentation of the parameter set inside the part)
    eq = V(model.GetEquationMgr)
    for k, v in PARAM.items():
        eq.Add2(-1, '"%s" = %s' % (k, repr(v)), True)

    model.ForceRebuild3(False)

    # body name / part name
    bodies = model.GetBodies2(0, True)
    assert bodies is not None and len(bodies) == 1, "expected 1 solid body, got %r" % (bodies,)
    body = bodies[0]
    body.Name = "P01 Crank handle"

    # measurement
    mp = V(model.Extension.CreateMassProperty)
    com = V(mp.CenterOfMass)
    box = V(body.GetBodyBox)
    meas = {
        "bodies": len(bodies),
        "volume_mm3": V(mp.Volume) * 1e9,
        "area_mm2": V(mp.SurfaceArea) * 1e6,
        "com_mm": [c * 1000 for c in com],
        "bbox_mm": [b * 1000 for b in box],
        "faces": V(body.GetFaceCount),
    }
    print(json.dumps(meas, indent=1))

    # save
    os.makedirs(outdir, exist_ok=True)
    prt = os.path.join(outdir, "P01 Crank handle.SLDPRT")
    stp = os.path.join(outdir, "final.step")
    err = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    wrn = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    ok = model.Extension.SaveAs(prt, 0, 1, vnone(), err, wrn)
    print("save sldprt", ok, err.value, wrn.value)
    sw.SetUserPreferenceIntegerValue(75, 214)  # swStepAP = AP214
    ok = model.Extension.SaveAs(stp, 0, 1, vnone(), err, wrn)
    print("save step", ok, err.value, wrn.value)
    # STEP product name = file name ("final"); rename it to the part name
    with open(stp, "r", encoding="latin-1") as fh:
        txt = fh.read()
    txt = txt.replace("PRODUCT ( 'final', 'final',", "PRODUCT ( 'P01 Crank handle', 'P01 Crank handle',")
    with open(stp, "w", encoding="latin-1", newline="") as fh:
        fh.write(txt)
    with open(os.path.join(outdir, "measure.json"), "w") as fh:
        json.dump(meas, fh, indent=1)
    return sw, model, meas


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    sw, model, meas = build(out)
    if not os.environ.get("KEEP"):
        sw.CloseDoc(V(model.GetTitle))  # close only the document we created
