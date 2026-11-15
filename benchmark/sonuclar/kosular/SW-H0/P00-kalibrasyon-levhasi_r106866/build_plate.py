"""P01 Plate - SolidWorks COM (pywin32) build script.
Usage:  python build_plate.py [output_dir]
Builds P01_Plate.SLDPRT and final.step (AP214) in output_dir (default: this script's folder).
Global frame: SolidWorks Front Plane == spec XY plane (normal +Z). Units: mm (API takes metres)."""
import os, sys, time, json, types
import pythoncom
import win32com.client as wc
from win32com.client import VARIANT

ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
OUT = os.path.abspath(ARGS[0] if ARGS else os.path.dirname(os.path.abspath(__file__)))
os.makedirs(OUT, exist_ok=True)
PRT = os.path.join(OUT, "P01_Plate.SLDPRT")
STEP = os.path.join(OUT, "final.step")

# ---------------- named parameters (mm) ----------------
P = dict(
    Plate_L=100.0,      # length along X
    Plate_W=60.0,       # width along Y
    Plate_T=10.0,       # thickness along Z
    Corner_R=3.0,       # vertical corner round radius
    Hole_D=6.0,         # corner through-hole diameter
    Hole_PX=84.0,       # hole centre spacing along X
    Hole_PY=44.0,       # hole centre spacing along Y
    Pocket_D=20.0,      # central pocket diameter
    Pocket_Depth=4.0,   # pocket depth from top face
)
mm = 0.001


def g(o, n):
    """Zero-arg COM member: pywin32 late binding sometimes yields the value, sometimes a bound method."""
    v = getattr(o, n)
    return v() if isinstance(v, types.MethodType) else v

NOTHING = VARIANT(pythoncom.VT_DISPATCH, None)

# swconst values (read from swconst.tlb)
swInputDimValOnCreate = 10
swUnitSystem, swUnitSystem_MMGS = 263, 5
swDefaultTemplatePart = 8
swStepAP = 75
swEndCondBlind, swEndCondThroughAll = 0, 1


def log(*a):
    print(*a, flush=True)


def connect():
    try:
        app = wc.GetActiveObject("SldWorks.Application")
    except Exception:
        app = wc.Dispatch("SldWorks.Application")
    app.Visible = True
    for _ in range(120):
        try:
            if g(app, "GetProcessID"):
                break
        except Exception:
            pass
        time.sleep(1)
    return app


app = connect()
log("SolidWorks", app.RevisionNumber)
app.SetUserPreferenceToggle(swInputDimValOnCreate, False)
tmpl = app.GetUserPreferenceStringValue(swDefaultTemplatePart)
doc = app.NewDocument(tmpl, 0, 0, 0)
assert doc is not None, "NewDocument failed (template: %s)" % tmpl
ext = doc.Extension
ext.SetUserPreferenceInteger(swUnitSystem, 0, swUnitSystem_MMGS)
sm = doc.SketchManager
fm = doc.FeatureManager
sm.AddToDB = True          # no inference snapping while creating geometry
sm.DisplayWhenAdded = False

# ---------------- global variables ----------------
eq = g(doc, "GetEquationMgr")
for k, v in P.items():
    eq.Add2(-1, '"%s" = %g' % (k, v), True)


def sel(name, typ, x=0, y=0, z=0, append=False, mark=0):
    ok = ext.SelectByID2(name, typ, x, y, z, append, mark, NOTHING, 0)
    if not ok:
        raise RuntimeError("select failed: %s %s (%g,%g,%g)" % (name, typ, x, y, z))


def selmm(name, typ, x=0, y=0, z=0, append=False, mark=0):
    sel(name, typ, x * mm, y * mm, z * mm, append, mark)


selmgr = doc.SelectionManager


def sel_obj(obj, append=False, mark=0):
    data = g(selmgr, "CreateSelectData")
    data.Mark = mark
    if not obj.Select4(append, data):
        raise RuntimeError("Select4 failed")


def sketch_of(name):
    return g(doc.FeatureByName(name), "GetSpecificFeature2")


def sk_lines(name):
    out = []
    for sg in g(sketch_of(name), "GetSketchSegments"):
        if g(sg, "GetType") == 0 and not sg.ConstructionGeometry:
            a, b = g(sg, "GetStartPoint2"), g(sg, "GetEndPoint2")
            out.append((sg, (a.X / mm, a.Y / mm), (b.X / mm, b.Y / mm)))
    return out


def sk_circles(name):
    out = []
    for sg in g(sketch_of(name), "GetSketchSegments"):
        if g(sg, "GetType") == 1:
            c = g(sg, "GetCenterPoint2")
            out.append((sg, c, (round(c.X / mm, 6), round(c.Y / mm, 6))))
    return out


def dim(name, x, y, z=0, kind="auto"):
    """Add a dimension on the current selection and rename it."""
    if kind == "h":
        dd = doc.AddHorizontalDimension2(x * mm, y * mm, z * mm)
    elif kind == "v":
        dd = doc.AddVerticalDimension2(x * mm, y * mm, z * mm)
    else:
        dd = doc.AddDimension2(x * mm, y * mm, z * mm)
    if dd is None:
        raise RuntimeError("dimension failed: " + name)
    d = dd.GetDimension2(0)
    d.Name = name
    doc.ClearSelection2(True)
    return d


def last_feature_name():
    return doc.FeatureByPositionReverse(0).Name


EQ_FAIL = []


def link(owner, dimname, expr):
    s = '"%s@%s" = %s' % (dimname, owner, expr)
    r = eq.Add2(-1, s, True)
    if r < 0:
        EQ_FAIL.append(s)
    log("eq", s, "->", r)


def edit_sketch(name):
    doc.ClearSelection2(True)
    sel(name, "SKETCH")
    g(doc, "EditSketch")
    doc.ClearSelection2(True)


L, W, T = P["Plate_L"], P["Plate_W"], P["Plate_T"]

# ---------------- F1: plate block (Front plane = XY, extrude +Z) ----------------
sel("Front Plane", "PLANE")
sm.InsertSketch(True)
sm.CreateCenterRectangle(0, 0, 0, L / 2 * mm, W / 2 * mm, 0)
sm.InsertSketch(True)
sk1 = last_feature_name()
edit_sketch(sk1)
try:
    for sg, a, b in sk_lines(sk1):
        if abs(a[1] - W / 2) < 1e-6 and abs(b[1] - W / 2) < 1e-6:      # top edge -> length
            sel_obj(sg); dim("L", 0, W / 2 + 10)
        elif abs(a[0] - L / 2) < 1e-6 and abs(b[0] - L / 2) < 1e-6:    # right edge -> width
            sel_obj(sg); dim("W", L / 2 + 10, 0)
except Exception as e:
    log("F1 dims warning:", e)
sm.InsertSketch(True)
doc.ClearSelection2(True)
link(sk1, "L", '"Plate_L"'); link(sk1, "W", '"Plate_W"')
sel(sk1, "SKETCH")
f = fm.FeatureExtrusion3(True, False, False, swEndCondBlind, 0, T * mm, 0,
                         False, False, False, False, 0, 0, False, False, False, False,
                         True, True, True, 0, 0, False)
assert f is not None, "F1 extrude failed"
f.Name = "F1_PlateBlock"
link("F1_PlateBlock", "D1", '"Plate_T"')
doc.ClearSelection2(True)
log("F1 ok")

# ---------------- F2: corner rounds R3 on 4 vertical edges ----------------
R = P["Corner_R"]
n = 0
for e in g(doc.GetBodies2(0, True)[0], "GetEdges"):
    p, q = g(g(e, "GetStartVertex"), "GetPoint"), g(g(e, "GetEndVertex"), "GetPoint")
    if (abs(p[0] - q[0]) < 1e-9 and abs(p[1] - q[1]) < 1e-9 and
            abs(abs(p[0]) - L / 2 * mm) < 1e-9 and abs(abs(p[1]) - W / 2 * mm) < 1e-9):
        sel_obj(e, append=n > 0, mark=1)
        n += 1
assert n == 4, "expected 4 vertical corner edges, got %d" % n
f = None
try:
    empty = VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [])
    f = fm.FeatureFillet3(195, R * mm, 0, 0, 0, 0, 0, empty, empty, empty, empty, empty, empty, empty)
except Exception as e:
    log("FeatureFillet3 error:", e)
if f is None:
    raise RuntimeError("F2 fillet failed")
f.Name = "F2_CornerRounds"
link("F2_CornerRounds", "D1", '"Corner_R"')
doc.ClearSelection2(True)
log("F2 ok")

# ---------------- F3: four corner through-holes ----------------
hx, hy = P["Hole_PX"] / 2, P["Hole_PY"] / 2
sel("Front Plane", "PLANE")
sm.InsertSketch(True)
for sx in (-1, 1):
    for sy in (-1, 1):
        sm.CreateCircleByRadius(sx * hx * mm, sy * hy * mm, 0, P["Hole_D"] / 2 * mm)
sm.InsertSketch(True)
sk3 = last_feature_name()
edit_sketch(sk3)
for i, (sg, cp, (cx, cy)) in enumerate(sorted(sk_circles(sk3), key=lambda t: t[2]), 1):
    sx, sy = (1 if cx > 0 else -1), (1 if cy > 0 else -1)
    try:
        sel_obj(sg); dim("HoleD%d" % i, cx + 6, cy + 6)
        sel_obj(cp); sel("Point1@Origin", "EXTSKETCHPOINT", append=True)
        dim("HoleX%d" % i, cx / 2, cy + sy * 6, kind="h")
        sel_obj(cp); sel("Point1@Origin", "EXTSKETCHPOINT", append=True)
        dim("HoleY%d" % i, cx + sx * 6, cy / 2, kind="v")
    except Exception as e:
        log("F3 dims warning:", i, e)
sm.InsertSketch(True)
doc.ClearSelection2(True)
for i in range(1, 5):
    link(sk3, "HoleD%d" % i, '"Hole_D"')
    link(sk3, "HoleX%d" % i, '"Hole_PX" / 2')
    link(sk3, "HoleY%d" % i, '"Hole_PY" / 2')
sel(sk3, "SKETCH")
# sketch on Z=0, cut through all (into material = +Z)
f = None
for direction in (False, True):          # try both directions; the one that removes material succeeds
    doc.ClearSelection2(True); sel(sk3, "SKETCH")
    f = fm.FeatureCut4(True, False, direction, swEndCondThroughAll, 0, 0, 0,
                       False, False, False, False, 0, 0, False, False, False, False,
                       False, True, True, True, True, False, 0, 0, False, False)
    if f is not None:
        log("F3 cut direction flag:", direction)
        break
assert f is not None, "F3 cut failed"
f.Name = "F3_CornerHoles"
doc.ClearSelection2(True)
log("F3 ok")

# ---------------- F4: central blind pocket from top face ----------------
top = [fc for fc in g(doc.GetBodies2(0, True)[0], "GetFaces")
       if g(fc, "Normal")[2] > 0.999 and abs(g(fc, "GetBox")[2] - T * mm) < 1e-9][0]
sel_obj(top)
sm.InsertSketch(True)
sm.CreateCircleByRadius(0, 0, 0, P["Pocket_D"] / 2 * mm)   # sketch coords; centre on model origin projection
sm.InsertSketch(True)
sk4 = last_feature_name()
edit_sketch(sk4)
try:
    sel_obj(sk_circles(sk4)[0][0])
    dim("PocketD", 15, 15, T)
except Exception as e:
    log("F4 dims warning:", e)
sm.InsertSketch(True)
doc.ClearSelection2(True)
link(sk4, "PocketD", '"Pocket_D"')
sel(sk4, "SKETCH")
f = fm.FeatureCut4(True, False, False, swEndCondBlind, 0, P["Pocket_Depth"] * mm, 0,
                   False, False, False, False, 0, 0, False, False, False, False,
                   False, True, True, True, True, False, 0, 0, False, False)
assert f is not None, "F4 cut failed"
f.Name = "F4_CentralPocket"
link("F4_CentralPocket", "D1", '"Pocket_Depth"')
doc.ClearSelection2(True)
log("F4 ok")

g(eq, "EvaluateAll")
doc.ForceRebuild3(False)

# ---------------- body name ----------------
bodies = doc.GetBodies2(0, True)
assert len(bodies) == 1, "expected one solid body, got %d" % len(bodies)
body = bodies[0]
body.Name = "P01 Plate"

# ---------------- measure ----------------
mp = g(ext, "CreateMassProperty")
mp.UseSystemUnits = True
com = mp.CenterOfMass
box = g(body, "GetBodyBox")
feats = []
ft = g(doc, "FirstFeature")
while ft is not None:
    feats.append(ft.Name)
    ft = g(ft, "GetNextFeature")
eqs = [eq.Equation(k) for k in range(g(eq, "GetCount"))]
res = dict(volume_mm3=mp.Volume * 1e9, area_mm2=mp.SurfaceArea * 1e6,
           com=[c * 1e3 for c in com], bbox=[b * 1e3 for b in box],
           faces=g(body, "GetFaceCount"), body=body.Name, features=feats,
           equations=eqs, failed_equations=EQ_FAIL)
log(json.dumps(res, indent=1))
with open(os.path.join(OUT, "olcum.json"), "w") as fh:
    json.dump(res, fh, indent=1)

# ---------------- save ----------------
for p in (PRT, STEP):
    if os.path.exists(p):
        os.remove(p)
r = doc.SaveAs3(PRT, 0, 1)
log("save sldprt:", r, os.path.exists(PRT))
app.SetUserPreferenceIntegerValue(swStepAP, 214)
r = doc.SaveAs3(STEP, 0, 1)
log("save step:", r, os.path.exists(STEP))
if "--keep-open" not in sys.argv:
    app.CloseDoc(os.path.basename(PRT))
