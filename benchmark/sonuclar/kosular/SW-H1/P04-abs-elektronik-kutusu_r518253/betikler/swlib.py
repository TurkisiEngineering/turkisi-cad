"""Small helper layer over the SolidWorks COM API (pywin32).
All public functions take INCH values in the global frame of the spec (Z = opening direction)."""
import math
import pythoncom
import win32com.client
from win32com.client import VARIANT

IN = 0.0254  # SolidWorks API works in metres
NOTHING = VARIANT(pythoncom.VT_DISPATCH, None)
EMPTY = VARIANT(pythoncom.VT_EMPTY, None)
R2 = math.sqrt(0.5)


def darr(vals):
    return VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [float(v) for v in vals])


class Part:
    CUTFLIP = True
    def __init__(self, sw):
        self.sw = sw
        tmpl = sw.GetUserPreferenceStringValue(8)
        sw.NewDocument(tmpl, 0, 0, 0)
        self.m = sw.ActiveDoc
        ext = self.m.Extension
        ext.SetUserPreferenceInteger(263, 0, 3)          # swUnitSystem -> swUnitSystem_IPS (inch)
        ext.SetUserPreferenceInteger(49, 0, 5)           # swUnitsLinearDecimalPlaces
        self.fm = self.m.FeatureManager
        self.sm = self.m.SketchManager
        self.mu = sw.GetMathUtility
        self.planes = [f for f in self._features() if f.GetTypeName2 == "RefPlane"][:3]
        self.front = self.planes[0]   # XY plane, normal +Z
        self.top = self.planes[1]     # XZ plane
        self.right = self.planes[2]   # YZ plane
        self.params = []              # (name, value, feature, note)
        self.lastsketch = None

    def _features(self):
        f = self.m.FirstFeature
        out = []
        while f is not None:
            out.append(f)
            f = f.GetNextFeature
        return out

    def param(self, name, value, feature, note=""):
        self.params.append((name, value, feature, note))
        return value

    # ---------- reference planes ----------
    def zplane(self, z, name):
        if abs(z) < 1e-12:
            return self.front
        self.m.ClearSelection2(True)
        self.front.Select2(False, 0)
        cons = 8 if z > 0 else 8 | 256
        p = self.fm.InsertRefPlane(cons, abs(z) * IN, 0, 0, 0, 0)
        if p is None:
            raise RuntimeError("plane failed " + name)
        p.Name = name
        return p

    # ---------- sketch ----------
    def begin(self, plane, name=None):
        self.m.ClearSelection2(True)
        plane.Select2(False, 0)
        self.sm.InsertSketch(True)
        self.sk = self.m.GetActiveSketch2
        self.x_ms = self.sk.ModelToSketchTransform
        self.xa = list(self.x_ms.ArrayData)
        self.sm.AddToDB = True
        self.skname = name
        o = self._s3((0, 0, 0))
        n = self._s3((0, 0, 1 / IN))
        # sketch-space z of model +Z: >0 means the sketch normal points along +Z
        self.normal = [0, 0, n[2] - o[2]]

    def _s3(self, p):
        a = self.xa
        x, y, z = p[0] * IN, p[1] * IN, p[2] * IN
        return (x * a[0] + y * a[3] + z * a[6] + a[9],
                x * a[1] + y * a[4] + z * a[7] + a[10],
                x * a[2] + y * a[5] + z * a[8] + a[11])

    def _s(self, p):
        q = self._s3(p)
        return q[0], q[1]

    def line(self, a, b):
        (x1, y1), (x2, y2) = self._s(a), self._s(b)
        return self.sm.CreateLine(x1, y1, 0, x2, y2, 0)

    def cline(self, a, b):
        (x1, y1), (x2, y2) = self._s(a), self._s(b)
        return self.sm.CreateCenterLine(x1, y1, 0, x2, y2, 0)

    def _arc1(self, c, a, b):
        (xc, yc), (x1, y1), (x2, y2) = self._s(c), self._s(a), self._s(b)
        cr = (x1 - xc) * (y2 - yc) - (y1 - yc) * (x2 - xc)
        d = 1 if cr > 0 else -1
        return self.sm.CreateArc(xc, yc, 0, x1, y1, 0, x2, y2, 0, d)

    def arc(self, c, a, b, mid):
        """arc with centre c from a to b passing through mid (model 3D points); drawn as 2 sub-arcs"""
        self._arc1(c, a, mid)
        self._arc1(c, mid, b)

    def circle(self, c, r):
        xc, yc = self._s(c)
        return self.sm.CreateCircleByRadius(xc, yc, 0, r * IN)

    def poly(self, pts, z):
        n = len(pts)
        for i in range(n):
            a, b = pts[i], pts[(i + 1) % n]
            self.line((a[0], a[1], z), (b[0], b[1], z))

    def rect(self, x0, y0, x1, y1, z):
        self.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], z)

    def rrect(self, hx, hy, r, z, cx=0.0, cy=0.0):
        """rounded rectangle: half sizes hx, hy, corner radius r, centred (cx, cy), in plane z"""
        ax, ay = hx - r, hy - r
        P = lambda x, y: (cx + x, cy + y, z)
        k = r * R2
        self.line(P(-ax, -hy), P(ax, -hy))
        self.arc(P(ax, -ay), P(ax, -hy), P(hx, -ay), P(ax + k, -ay - k))
        self.line(P(hx, -ay), P(hx, ay))
        self.arc(P(ax, ay), P(hx, ay), P(ax, hy), P(ax + k, ay + k))
        self.line(P(ax, hy), P(-ax, hy))
        self.arc(P(-ax, ay), P(-ax, hy), P(-hx, ay), P(-ax - k, ay + k))
        self.line(P(-hx, ay), P(-hx, -ay))
        self.arc(P(-ax, -ay), P(-hx, -ay), P(-ax, -hy), P(-ax - k, -ay - k))

    def slot_y(self, xc, y0, y1, r, z):
        """stadium along Y: centre line x = xc, semicircle centres at y0 < y1, radius r"""
        self.line((xc + r, y0, z), (xc + r, y1, z))
        self.arc((xc, y1, z), (xc + r, y1, z), (xc - r, y1, z), (xc, y1 + r, z))
        self.line((xc - r, y1, z), (xc - r, y0, z))
        self.arc((xc, y0, z), (xc - r, y0, z), (xc + r, y0, z), (xc, y0 - r, z))

    def slot_x(self, yc, x0, x1, r, z):
        self.line((x0, yc - r, z), (x1, yc - r, z))
        self.arc((x1, yc, z), (x1, yc - r, z), (x1, yc + r, z), (x1 + r, yc, z))
        self.line((x1, yc + r, z), (x0, yc + r, z))
        self.arc((x0, yc, z), (x0, yc + r, z), (x0, yc - r, z), (x0 - r, yc, z))

    def end(self):
        self.sm.InsertSketch(True)
        f = self.m.FeatureByPositionReverse(0)
        if self.skname:
            f.Name = self.skname
        self.lastsketch = f
        self.lastnormal = self.normal
        return f

    # ---------- features ----------
    def extrude(self, depth, up, draft=0.0, outward=False, cut=False, name=None, sketch=None):
        """blind extrude/cut of the last sketch along +Z (up=True) or -Z; draft in degrees;
        outward=True -> profile grows along the extrusion"""
        sketch = sketch or self.lastsketch
        self.m.ClearSelection2(True)
        sketch.Select2(False, 0)
        flip = ((self.lastnormal[2] > 0) != up) != bool(cut and self.CUTFLIP)
        dch = draft > 0
        da = math.radians(draft)
        if cut:
            f = self.fm.FeatureCut4(True, False, flip, 0, 0, depth * IN, 0, dch, False, outward, False, da, 0,
                                    False, False, False, False, False, True, True, True, True, False,
                                    0, 0, False, False)
        else:
            f = self.fm.FeatureExtrusion3(True, False, flip, 0, 0, depth * IN, 0, dch, False, outward, False,
                                          da, 0, False, False, False, False, True, True, True, 0, 0, False)
        if f is None:
            raise RuntimeError("extrude failed: %s" % name)
        if name:
            f.Name = name
        return f

    def revolve(self, cut=False, name=None, sketch=None):
        sketch = sketch or self.lastsketch
        self.m.ClearSelection2(True)
        sketch.Select2(False, 0)
        f = self.fm.FeatureRevolve2(True, True, False, cut, False, False, 0, 0, 2 * math.pi, 0,
                                    False, False, 0, 0, 0, 0, 0, True, True, True)
        if f is None:
            raise RuntimeError("revolve failed: %s" % name)
        if name:
            f.Name = name
        return f

    def find_edge(self, p, tol=2e-4):
        """edge closest to the model point p (inch); returns (edge, distance_inch)"""
        best, bd = None, 1e9
        x, y, z = p[0] * IN, p[1] * IN, p[2] * IN
        for b in self.bodies():
            for e in b.GetEdges():
                q = e.GetClosestPointOn(x, y, z)
                d = ((q[0] - x) ** 2 + (q[1] - y) ** 2 + (q[2] - z) ** 2) ** 0.5 / IN
                if d < bd:
                    best, bd = e, d
        return best, bd

    def select_edges(self, pts, tol=2e-4):
        self.m.ClearSelection2(True)
        n = 0
        for p in pts:
            e, d = self.find_edge(p)
            if e is not None and d < tol:
                n += bool(e.Select4(True, NOTHING))
            else:
                print("  no edge near", p, "closest d=", d)
        return n

    def fillet(self, pts, r, name=None, propagate=True):
        n = self.select_edges(pts)
        if n != len(pts):
            print("WARN edge selection %d/%d for %s" % (n, len(pts), name))
        opts = 2 | (1 if propagate else 0)
        f = self.fm.FeatureFillet3(opts, r * IN, 0, 0, 0, 0, 0, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY)
        if f is None:
            raise RuntimeError("fillet failed: %s" % name)
        if name:
            f.Name = name
        return f

    def mass(self):
        self.m.ForceRebuild3(False)
        mp = self.m.Extension.CreateMassProperty
        v = mp.Volume / IN ** 3
        a = mp.SurfaceArea / IN ** 2
        c = [x / IN for x in mp.CenterOfMass]
        return v, a, c

    def bodies(self):
        b = self.m.GetBodies2(0, True)
        return list(b) if b else []

    def bbox(self):
        out = []
        for b in self.bodies():
            bb = b.GetBodyBox()
            out.append([round(x / IN, 5) for x in bb])
        return out

    def nfaces(self):
        return sum(b.GetFaceCount() for b in self.bodies())

    def report(self, tag=""):
        v, a, c = self.mass()
        print("%-18s bodies=%d faces=%d V=%.5f A=%.4f C=(%.4f,%.4f,%.4f) bbox=%s" % (
            tag, len(self.bodies()), self.nfaces(), v, a, c[0], c[1], c[2], self.bbox()))

    def loft(self, sk1, p1, sk2, p2, name=None):
        """ruled loft between two sketches; p1/p2 = corresponding pick points (inch, model)"""
        self.m.ClearSelection2(True)
        e = self.m.Extension
        e.SelectByID2(sk1.Name, "SKETCH", p1[0] * IN, p1[1] * IN, p1[2] * IN, True, 1, NOTHING, 0)
        e.SelectByID2(sk2.Name, "SKETCH", p2[0] * IN, p2[1] * IN, p2[2] * IN, True, 1, NOTHING, 0)
        f = None
        try:
            f = self.fm.InsertProtrusionBlend2(False, True, False, 1.0, 0, 0, 1.0, 1.0, True, True,
                                               False, 0, 0, 0, True, True, True, 0, 0)
        except Exception as ex:
            print("Blend2 exc", ex)
        if f is None:
            try:
                f = self.fm.InsertProtrusionBlend(False, True, False, 1.0, 0, 0, 1.0, 1.0, True, True,
                                                  False, 0, 0, 0, True, True, True)
            except Exception as ex:
                print("Blend exc", ex)
        if f is None:
            raise RuntimeError("loft failed: %s" % name)
        if name:
            f.Name = name
        return f

    def sel_count(self):
        return self.m.SelectionManager.GetSelectedObjectCount2(-1)

    def save(self, path):
        errs = self.m.SaveAs3(path, 0, 2)
        return errs

    def title(self):
        return self.m.GetTitle

    def pz(self, z, name=None):
        """cached reference plane parallel to XY at height z (inch)"""
        if not hasattr(self, "_pz"):
            self._pz = {}
        if abs(z) < 1e-12:
            return self.front
        k = round(z, 6)
        if k not in self._pz:
            self._pz[k] = self.zplane(z, name or ("Z_%+.4f" % z).replace(".", "_"))
        return self._pz[k]
