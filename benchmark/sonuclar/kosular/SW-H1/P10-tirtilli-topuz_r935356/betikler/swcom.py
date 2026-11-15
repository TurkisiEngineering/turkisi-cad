"""Ortak SolidWorks COM yardimcilari (pywin32). Birim: inc (SW API metre -> IN ile cevrilir)."""
import os, math, pythoncom
import win32com.client as wc

SWDIR = r"C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS"


def _load(tlb):
    tl = pythoncom.LoadTypeLib(os.path.join(SWDIR, tlb))
    a = tl.GetLibAttr()
    return wc.gencache.EnsureModule(str(a[0]), a[1], a[3], a[4])


swmod = _load("sldworks.tlb")
cmod = _load("swconst.tlb")


class _C:
    def __getattr__(self, n):
        for m in (cmod, swmod):
            if hasattr(m.constants, n):
                return getattr(m.constants, n)
        raise AttributeError(n)


C = _C()
IN = 0.0254
DEG = math.pi / 180
OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def app():
    sw = wc.Dispatch("SldWorks.Application")
    sw = swmod.ISldWorks(sw._oleobj_)
    sw.Visible = True
    return sw


def cast(obj, iface):
    try:
        o = obj._oleobj_.QueryInterface(iface.CLSID, pythoncom.IID_IDispatch)
    except Exception:
        o = obj._oleobj_
    return iface(o)


def setname(f, name):
    try:
        wc.dynamic.Dispatch(f._oleobj_).Name = name
    except Exception:
        try:
            setname(f, name)
        except Exception as e:
            print("rename failed", name, e)


def close_title(sw, title):
    sw.CloseDoc(title)


def VARR_D(objs):
    return wc.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, objs)


def pol(r, t):
    return (r * math.cos(t * DEG), r * math.sin(t * DEG))


# ---------------- plan outline (all circular arcs) ----------------
def outline(R, s, rr, d=1.39, n=8, th0=22.5):
    """Circle R about Z minus n discs radius s centred on radius d at th0+k*360/n;
    corners rounded rr (0 = sharp). Returns closed chain of arcs (p_start, p_mid, p_end) in XY."""
    segs = []
    step = 360.0 / n
    if rr == 0:
        phi = math.degrees(math.acos((R * R + d * d - s * s) / (2 * R * d)))
        for k in range(n):
            tl = k * step
            ts = th0 + k * step
            segs.append((pol(R, ts - step + phi), pol(R, tl), pol(R, ts - phi)))
            segs.append((pol(R, ts - phi), pol(d - s, ts), pol(R, ts + phi)))
        return segs
    Rc = R - rr
    Dc = s + rr
    phi = math.degrees(math.acos((Rc * Rc + d * d - Dc * Dc) / (2 * Rc * d)))

    def tang_sc(cc, scc):
        vx, vy = cc[0] - scc[0], cc[1] - scc[1]
        L = math.hypot(vx, vy)
        return (scc[0] + vx * s / L, scc[1] + vy * s / L)

    def mid_round(cc, pa, pb):
        mx, my = (pa[0] + pb[0]) / 2 - cc[0], (pa[1] + pb[1]) / 2 - cc[1]
        L = math.hypot(mx, my)
        return (cc[0] + mx * rr / L, cc[1] + my * rr / L)

    for k in range(n):
        tl = k * step
        ts = th0 + k * step
        A = pol(R, ts - step + phi)
        Bp = pol(R, ts - phi)
        segs.append((A, pol(R, tl), Bp))
        c2 = pol(Rc, ts - phi)
        sc = pol(d, ts)
        T2 = tang_sc(c2, sc)
        segs.append((Bp, mid_round(c2, Bp, T2), T2))
        cn = pol(Rc, ts + phi)
        T3 = tang_sc(cn, sc)
        segs.append((T2, pol(d - s, ts), T3))
        An = pol(R, ts + phi)
        segs.append((T3, mid_round(cn, T3, An), An))
    return segs


class Part:
    def __init__(self, sw, name):
        self.sw = sw
        self.name = name
        tpl = sw.GetUserPreferenceStringValue(C.swDefaultTemplatePart)
        doc = sw.NewDocument(tpl, 0, 0, 0)
        self.m = swmod.IModelDoc2(doc._oleobj_)
        self.pd = cast(doc, swmod.IPartDoc)
        self.ext = self.m.Extension
        self.fm = self.m.FeatureManager
        self.sm = self.m.SketchManager
        self.mu = sw.GetMathUtility()
        self.ext.SetUserPreferenceInteger(C.swUnitSystem, 0, C.swUnitSystem_IPS)
        sw.SetUserPreferenceToggle(C.swSketchInference, False)
        self.planes = {}

    def plane_z(self, z):
        """reference plane parallel to Front plane at model z (in)."""
        if abs(z) < 1e-12:
            return "Front Plane"
        key = round(z, 6)
        if key in self.planes:
            return self.planes[key]
        self.m.ClearSelection2(True)
        self.ext.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, None, 0)
        cons = C.swRefPlaneReferenceConstraint_Distance
        if z < 0:
            cons |= C.swRefPlaneReferenceConstraint_OptionFlip
        f = self.fm.InsertRefPlane(cons, abs(z) * IN, 0, 0, 0, 0)
        assert f is not None, "plane fail %s" % z
        nm = "Z=%+.5f" % z
        setname(f, nm)
        self.planes[key] = nm
        return nm

    def sketch(self, plane):
        self.m.ClearSelection2(True)
        ok = self.ext.SelectByID2(plane, "PLANE", 0, 0, 0, False, 0, None, 0)
        assert ok, plane
        self.sm.InsertSketch(True)
        self.sm.AddToDB = True
        sk = self.sm.ActiveSketch
        xf = swmod.IMathTransform(sk.ModelToSketchTransform._oleobj_)
        self.xf = list(xf.ArrayData)
        return sk

    def P(self, x, y, z):
        a = self.xf  # SW MathTransform: p' = p*R + t (row vector), scale a[12]
        p = (x * IN, y * IN, z * IN)
        q = [sum(p[i] * a[3 * i + j] for i in range(3)) * a[12] + a[9 + j] for j in range(3)]
        assert abs(q[2]) < 1e-9, ("point off sketch plane", x, y, z, q)
        return q[0], q[1]

    def line(self, a, b):
        p, q = self.P(*a), self.P(*b)
        return self.sm.CreateLine(p[0], p[1], 0, q[0], q[1], 0)

    def cline(self, a, b):
        p, q = self.P(*a), self.P(*b)
        return self.sm.CreateCenterLine(p[0], p[1], 0, q[0], q[1], 0)

    def arc3(self, a, mid, b):
        p, q, r = self.P(*a), self.P(*b), self.P(*mid)
        return self.sm.Create3PointArc(p[0], p[1], 0, q[0], q[1], 0, r[0], r[1], 0)

    def circle(self, c, r):
        p = self.P(*c)
        return self.sm.CreateCircleByRadius(p[0], p[1], 0, r * IN)

    def rz_profile(self, segs, axis=True):
        """(r,z) profile in the XZ half plane (+X). segs[0]=start (r,z); then ('L',(r,z)) or ('A',(rm,zm),(r,z))."""
        cur = segs[0]
        for s in segs[1:]:
            if s[0] == 'L':
                self.line((cur[0], 0, cur[1]), (s[1][0], 0, s[1][1]))
                cur = s[1]
            else:
                self.arc3((cur[0], 0, cur[1]), (s[1][0], 0, s[1][1]), (s[2][0], 0, s[2][1]))
                cur = s[2]
        if axis:
            self.cline((0, 0, -2), (0, 0, 2))

    def plan(self, segs, z):
        for a, mid, b in segs:
            self.arc3((a[0], a[1], z), (mid[0], mid[1], z), (b[0], b[1], z))

    def end_sketch(self, name=None):
        self.sm.AddToDB = False
        self.sm.InsertSketch(True)
        f = self.m.FeatureByPositionReverse(0)
        if name:
            setname(f, name)
        self.m.ClearSelection2(True)
        f.Select2(False, 0)
        return f

    def revolve(self, name, cut=False):
        f = self.fm.FeatureRevolve2(True, True, False, cut, False, False, 0, 0, 2 * math.pi, 0,
                                    False, False, 0, 0, 0, 0, 0, True, False, True)
        assert f is not None, "revolve fail " + name
        setname(f, name)
        return f

    def extrude(self, name, d, up=True, cut=False, both=False):
        """blind extrude d (in) from a plane parallel to Front; up=True -> +Z."""
        t = 1 if both else 0
        if not cut:
            f = self.fm.FeatureExtrusion3(not both, False, not up, t, t, d * IN, d * IN,
                                          False, False, False, False, 0, 0, False, False, False, False,
                                          True, False, True, 0, 0, False)
        else:
            f = self.fm.FeatureCut4(not both, False, up, t, t, d * IN, d * IN,
                                    False, False, False, False, 0, 0, False, False, False, False,
                                    False, False, True, False, False, False, 0, 0, False, False)
        assert f is not None, "extrude fail " + name
        setname(f, name)
        return f

    def bodies(self):
        b = self.pd.GetBodies2(C.swSolidBody, True)
        return list(b) if b else []

    def report(self, tag=""):
        out = []
        for b in self.bodies():
            bx = b.GetBodyBox()
            mp = b.GetMassProperties(1.0)  # cx,cy,cz,vol,area,mass,...
            out.append(dict(faces=b.GetFaceCount(), vol=round(mp[3] / IN ** 3, 5), area=round(mp[4] / IN ** 2, 4),
                            com=tuple(round(v / IN, 5) for v in mp[0:3]),
                            box=tuple(round(v / IN, 4) for v in bx)))
        print(tag, out, flush=True)
        return out

    def equations(self, params):
        em = self.m.GetEquationMgr()
        for k, v in params.items():
            if k.endswith("_deg") or k.startswith("N_"):
                em.Add2(-1, '"%s" = %.6f' % (k, v), True)
            else:
                em.Add2(-1, '"%s" = %.6fin' % (k, v), True)

    def save(self, fn):
        p = os.path.join(OUT, fn)
        self.m.ForceRebuild3(False)
        e = self.ext.SaveAs3(p, 0, 1, None, None, 0, 0)
        print("saved", p, e, flush=True)
        return p
