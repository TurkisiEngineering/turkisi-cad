"""Small helper layer over the SolidWorks 2024 COM API (pywin32, early binding).

All geometry is given in INCHES in the global frame of spec.md; conversion to the
API's metres happens here (IN = 0.0254).
"""
import math
import os
import pythoncom
import win32com.client
from win32com.client import gencache, VARIANT

IN = 0.0254
SWMOD = gencache.GetModuleForTypelib('{83A33D31-27C5-11CE-BFD4-00400513BB57}', 0, 32, 0)
C = gencache.GetModuleForTypelib('{4687F359-55D0-4CD3-B6CF-2EB42C11F989}', 0, 32, 0).constants


def cast(obj, iface):
    """QueryInterface obj to the early-bound interface class `iface` (e.g. 'IModelDoc2')."""
    if obj is None:
        return None
    cls = getattr(SWMOD, iface)
    ole = obj._oleobj_ if hasattr(obj, '_oleobj_') else obj
    return cls(ole.QueryInterface(cls.CLSID, pythoncom.IID_IDispatch))


_SW = None


def sw():
    global _SW
    if _SW is None:
        raw = win32com.client.Dispatch("SldWorks.Application")
        _SW = cast(raw, 'ISldWorks')
        _SW.Visible = True
    return _SW


def setname(f, name):
    win32com.client.dynamic.Dispatch(f._oleobj_).Name = name


def nothing():
    return VARIANT(pythoncom.VT_DISPATCH, None)


# ----------------------------------------------------------------------------------------------
# 2D path helpers (profile coordinates u,v as in spec: first coord right, second up)
# ----------------------------------------------------------------------------------------------
def arc_mid(c, s, e, d='short', thru=None):
    """Mid point of an arc about c from s to e. d in 'ccw','cw','short'."""
    if thru is not None:
        return thru
    R = math.hypot(s[0] - c[0], s[1] - c[1])
    Re = math.hypot(e[0] - c[0], e[1] - c[1])
    if abs(R - Re) > 2e-3:
        print("  WARN arc radius mismatch", c, s, e, R, Re)
    a0 = math.atan2(s[1] - c[1], s[0] - c[0])
    a1 = math.atan2(e[1] - c[1], e[0] - c[0])
    ccw = (a1 - a0) % (2 * math.pi)
    if ccw == 0:
        ccw = 2 * math.pi
    cw = ccw - 2 * math.pi
    if d == 'ccw':
        sw_ = ccw
    elif d == 'cw':
        sw_ = cw
    else:
        sw_ = ccw if abs(ccw) <= abs(cw) else cw
    am = a0 + sw_ / 2
    return (c[0] + R * math.cos(am), c[1] + R * math.sin(am))


class Path:
    """Closed 2D path: start point, then ('L', p) and ('A', c, p, dir|thru) segments."""

    def __init__(self, start):
        self.start = tuple(start)
        self.cur = tuple(start)
        self.segs = []

    def L(self, p):
        self.segs.append(('L', self.cur, tuple(p)))
        self.cur = tuple(p)
        return self

    def A(self, c, p, d='short', thru=None):
        m = arc_mid(c, self.cur, p, d, thru)
        self.segs.append(('A', self.cur, m, tuple(p)))
        self.cur = tuple(p)
        return self

    def close(self):
        if math.hypot(self.cur[0] - self.start[0], self.cur[1] - self.start[1]) > 1e-9:
            self.L(self.start)
        return self


def mirror_v(path):
    """Return a Path mirrored about v=0 (u, v) -> (u, -v)."""
    p = Path((path.start[0], -path.start[1]))
    for s in path.segs:
        if s[0] == 'L':
            p.segs.append(('L', (s[1][0], -s[1][1]), (s[2][0], -s[2][1])))
        else:
            p.segs.append(('A', (s[1][0], -s[1][1]), (s[2][0], -s[2][1]), (s[3][0], -s[3][1])))
    return p


# mapping functions profile (u,v) -> model xyz (inches)
def XY(z=0.0):
    return lambda u, v: (u, v, z)


def XZ(y):
    return lambda u, v: (u, y, v)


def RY():   # (r, y) half section about the Y axis, drawn in the plane z = 0
    return lambda u, v: (u, v, 0.0)


def WHEEL():  # (rho, z) half section about the wheel axis, drawn in the plane y = -0.75
    return lambda u, v: (1.515 + u, -0.75, v)


# ----------------------------------------------------------------------------------------------
class Part:
    def __init__(self, name):
        self.name = name
        app = sw()
        tmpl = app.GetUserPreferenceStringValue(C.swDefaultTemplatePart)
        doc = app.NewDocument(tmpl, 0, 0, 0)
        self.doc = cast(doc, 'IModelDoc2')
        self.ext = cast(self.doc.Extension, 'IModelDocExtension')
        self.fm = cast(self.doc.FeatureManager, 'IFeatureManager')
        self.sm = cast(self.doc.SketchManager, 'ISketchManager')
        self.part = cast(doc, 'IPartDoc')
        self.mu = cast(app.GetMathUtility(), 'IMathUtility')
        # units: inches, 5 decimals
        self.ext.SetUserPreferenceInteger(C.swUnitSystem, 0, C.swUnitSystem_IPS)
        self.ext.SetUserPreferenceInteger(C.swUnitsLinear, 0, C.swINCHES)
        self.ext.SetUserPreferenceInteger(C.swUnitsLinearDecimalPlaces, 0, 5)
        self.sm.AddToDB = True
        self.sm.DisplayWhenAdded = False
        planes = []
        f = cast(self.doc.FirstFeature(), 'IFeature')
        while f is not None:
            if f.GetTypeName2() == 'RefPlane':
                planes.append(f)
            f = cast(f.GetNextFeature(), 'IFeature')
        self.front, self.top, self.right = planes[:3]
        self.nfeat = 0
        self.LOG = []

    # --- reference planes ---------------------------------------------------------------------
    def plane_y(self, y, name=None):
        """Plane parallel to Top plane at height y (inches)."""
        self.doc.ClearSelection2(True)
        self.top.Select2(False, 0)
        cons = C.swRefPlaneReferenceConstraint_Distance
        if y < 0:
            cons |= C.swRefPlaneReferenceConstraint_OptionFlip
        ret = self.fm.InsertRefPlane(cons, abs(y) * IN, 0, 0, 0, 0)
        if ret is None:
            raise RuntimeError("ref plane failed")
        f = cast(self.doc.FeatureByPositionReverse(0), 'IFeature')
        if name:
            setname(f, name)
        # verify plane height
        rp = cast(ret, 'IRefPlane')
        t = cast(rp.Transform, 'IMathTransform').ArrayData
        if abs(t[10] / IN - y) > 1e-6:
            raise RuntimeError("ref plane at %s instead of %s" % (t[10] / IN, y))
        self.doc.ClearSelection2(True)
        return f

    # --- sketches -----------------------------------------------------------------------------
    def sketch(self, plane_feat, paths, mapping, circles=(), centerline=None, name=None):
        """Create a sketch on plane_feat with closed paths (list of Path, profile coords mapped by
        mapping(u,v)->xyz inches), circles [(centre_xyz, r)], optional centerline (xyz, xyz)."""
        self.doc.ClearSelection2(True)
        plane_feat.Select2(False, 0)
        self.sm.InsertSketch(True)
        sk = cast(self.sm.ActiveSketch, 'ISketch')
        xf = cast(sk.ModelToSketchTransform, 'IMathTransform')

        def P(xyz):
            mp = cast(self.mu.CreatePoint(VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [c * IN for c in xyz])), 'IMathPoint')
            mp = cast(mp.MultiplyTransform(xf), 'IMathPoint')
            return list(mp.ArrayData)

        for path in paths:
            for s in path.segs:
                if s[0] == 'L':
                    a, b = P(mapping(*s[1])), P(mapping(*s[2]))
                    r = self.sm.CreateLine(a[0], a[1], 0, b[0], b[1], 0)
                else:
                    a, m, b = P(mapping(*s[1])), P(mapping(*s[2])), P(mapping(*s[3]))
                    r = self.sm.Create3PointArc(a[0], a[1], 0, b[0], b[1], 0, m[0], m[1], 0)
                if r is None:
                    raise RuntimeError("sketch segment failed %s" % (s,))
        for (c, rad) in circles:
            cc = P(c)
            if self.sm.CreateCircleByRadius(cc[0], cc[1], 0, rad * IN) is None:
                raise RuntimeError("circle failed")
        if centerline is not None:
            a, b = P(centerline[0]), P(centerline[1])
            self.sm.CreateCenterLine(a[0], a[1], 0, b[0], b[1], 0)
        self.sm.InsertSketch(True)
        f = cast(self.doc.FeatureByPositionReverse(0), 'IFeature')
        if name:
            setname(f, name)
        self.doc.ClearSelection2(True)
        return f

    def _named(self, feat, name, what):
        if feat is None:
            raise RuntimeError("%s failed (%s)" % (what, name))
        f = cast(feat, 'IFeature')
        if name:
            setname(f, name)
        self.doc.ClearSelection2(True)
        return f

    # --- features -----------------------------------------------------------------------------
    def extrude(self, sketch, d1, d2=None, mid=False, flip=False, merge=True, name=None,
                t1=None, t2=None):
        """Boss extrude. mid=True: symmetric, total depth d1. Else direction 1 = plane normal,
        depth d1; if d2 given, second direction depth d2."""
        self.doc.ClearSelection2(True)
        sketch.Select2(False, 0)
        if mid:
            T1, T2, D1, D2, sd = C.swEndCondMidPlane, 0, d1 * IN, 0, True
        else:
            T1 = C.swEndCondBlind if t1 is None else t1
            T2 = (C.swEndCondBlind if t2 is None else t2) if d2 is not None else 0
            D1, D2 = d1 * IN, (d2 or 0) * IN
            sd = d2 is None
        f = self.fm.FeatureExtrusion3(sd, flip, False, T1, T2, D1, D2, False, False, False, False,
                                      0, 0, False, False, False, False, merge, True, True,
                                      0, 0, False)
        return self._named(f, name, 'extrude')

    def cut(self, sketch, d1=None, d2=None, mid=False, flip=False, name=None, through_both=False,
            t1=None, t2=None):
        self.doc.ClearSelection2(True)
        sketch.Select2(False, 0)
        if through_both:
            sd, T1, T2, D1, D2 = False, C.swEndCondThroughAll, C.swEndCondThroughAll, 0, 0
        elif mid:
            sd, T1, T2, D1, D2 = True, C.swEndCondMidPlane, 0, d1 * IN, 0
        else:
            T1 = C.swEndCondBlind if t1 is None else t1
            T2 = (C.swEndCondBlind if t2 is None else t2) if (d2 is not None or t2 is not None) else 0
            D1, D2 = (d1 or 0) * IN, (d2 or 0) * IN
            sd = not (d2 is not None or t2 is not None)
        f = self.fm.FeatureCut4(sd, flip, False, T1, T2, D1, D2, False, False, False, False, 0, 0,
                                False, False, False, False, False, True, True, True, True, False,
                                0, 0, False, False)
        return self._named(f, name, 'cut')

    def revolve(self, sketch, cut=False, merge=True, name=None):
        self.doc.ClearSelection2(True)
        sketch.Select2(False, 0)
        f = self.fm.FeatureRevolve2(True, True, False, cut, False, False, 0, 0, 2 * math.pi, 0,
                                    False, False, 0, 0, 0, 0, 0, merge, True, True)
        return self._named(f, name, 'revolve')

    def fillet(self, edges, r, name=None, propagate=False):
        self.doc.ClearSelection2(True)
        if not edges:
            raise RuntimeError("no edges for fillet " + str(name))
        arr = VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, [e._oleobj_ for e in edges])
        n = self.ext.MultiSelect2(arr, False, None)
        opts = C.swFeatureFilletUniformRadius | (C.swFeatureFilletPropagate if propagate else 0)
        E = VARIANT(pythoncom.VT_VARIANT, None)
        f = self.fm.FeatureFillet3(opts, r * IN, 0, 0, 0, 0, 0, E, E, E, E, E, E, E)
        return self._named(f, name, 'fillet(%d edges sel=%s)' % (len(edges), n))

    def fillet_at(self, pt, r, name=None):
        """Fillet the single edge found at model point pt (inches). Returns True on success."""
        self.doc.ClearSelection2(True)
        ok = self.ext.SelectByID2("", "EDGE", pt[0] * IN, pt[1] * IN, pt[2] * IN, False, 0, None, 0)
        if not ok:
            return False
        E = VARIANT(pythoncom.VT_VARIANT, None)
        f = self.fm.FeatureFillet3(C.swFeatureFilletUniformRadius, r * IN, 0, 0, 0, 0, 0, E, E, E, E, E, E, E)
        self.doc.ClearSelection2(True)
        if f is None:
            return False
        if name:
            setname(f, name)
        return True

    # --- topology queries ---------------------------------------------------------------------
    def bodies(self):
        bs = self.part.GetBodies2(C.swSolidBody, True)
        return [cast(b, 'IBody2') for b in (bs or [])]

    def body(self):
        bs = self.bodies()
        if len(bs) != 1:
            raise RuntimeError("expected 1 body, got %d" % len(bs))
        return bs[0]

    def edges(self):
        return [cast(e, 'IEdge') for e in self.body().GetEdges()]

    def faces(self):
        return [cast(f, 'IFace2') for f in self.body().GetFaces()]

    # --- equations / global variables --------------------------------------------------------
    def globals(self, params):
        em = cast(self.doc.GetEquationMgr(), 'IEquationMgr')
        for k, v in params.items():
            em.Add2(-1, '"%s" = %.6fin' % (k, v), True)

    def link(self, dimname, gvar):
        em = cast(self.doc.GetEquationMgr(), 'IEquationMgr')
        r = em.Add2(-1, '"%s" = "%s"' % (dimname, gvar), True)
        return r

    def rebuild(self):
        self.doc.ForceRebuild3(False)

    def save(self, path):
        self.doc.ForceRebuild3(False)
        if os.path.exists(path):
            os.remove(path)
        ok = self.doc.SaveAs3(path, 0, C.swSaveAsOptions_Silent)
        if ok != 0:
            raise RuntimeError("save failed %s %s" % (path, ok))

    def close(self):
        sw().CloseDoc(self.doc.GetTitle())


# ----------------------------------------------------------------------------------------------
# geometry inspection helpers
# ----------------------------------------------------------------------------------------------
def face_info(face):
    s = cast(face.GetSurface(), 'ISurface')
    box = list(face.GetBox())
    box = [v / IN for v in box]
    info = {'box': box, 'type': 'other', 'face': face, 'surf': s}
    if s.IsPlane():
        p = list(s.PlaneParams)
        n = p[0:3]
        if not face.FaceInSurfaceSense():
            n = [-v for v in n]
        info.update(type='plane', n=n, p=[v / IN for v in p[3:6]])
    elif s.IsCylinder():
        p = list(s.CylinderParams)
        info.update(type='cyl', o=[v / IN for v in p[0:3]], a=p[3:6], r=p[6] / IN)
    elif s.IsTorus():
        info['type'] = 'torus'
    elif s.IsCone():
        info['type'] = 'cone'
    elif s.IsSphere():
        info['type'] = 'sphere'
    return info


def edge_mid(edge):
    cp = list(edge.GetCurveParams2())
    cur = cast(edge.GetCurve(), 'ICurve')
    t = 0.5 * (cp[6] + cp[7])
    ev = list(cur.Evaluate2(t, 0))
    return [v / IN for v in ev[0:3]]


def normal_at(finfo, pt):
    """Unit normal (sign not reliable) of a face at a point on it; None if unknown."""
    if finfo['type'] == 'plane':
        return finfo['n']
    if finfo['type'] == 'cyl':
        o, a = finfo['o'], finfo['a']
        v = [pt[i] - o[i] for i in range(3)]
        d = sum(v[i] * a[i] for i in range(3))
        w = [v[i] - d * a[i] for i in range(3)]
        L = math.sqrt(sum(c * c for c in w))
        return [c / L for c in w]
    r = finfo['surf'].EvaluateAtPoint(pt[0] * IN, pt[1] * IN, pt[2] * IN)
    if r is None:
        return None
    return list(r)[0:3]


def edge_faces(edge):
    fs = edge.GetTwoAdjacentFaces2()
    return [cast(f, 'IFace2') for f in fs]


def is_tangent(edge, fi1, fi2, tol=1e-3):
    m = edge_mid(edge)
    n1, n2 = normal_at(fi1, m), normal_at(fi2, m)
    if n1 is None or n2 is None:
        return False
    d = abs(sum(a * b for a, b in zip(n1, n2)))
    return d > 1 - tol


def measure(part):
    """Volume, area, CoM, exact bbox for the single body of a part (inches)."""
    b = part.body()
    mp = cast(part.ext.CreateMassProperty(), 'IMassProperty')
    vol = mp.Volume / IN ** 3
    area = mp.SurfaceArea / IN ** 2
    com = [v / IN for v in mp.CenterOfMass]
    bb = []
    for d in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        r = b.GetExtremePoint(d[0], d[1], d[2])
        pt = r[1:4] if isinstance(r, tuple) and len(r) >= 4 else r
        bb.append(pt)
    box = [bb[0][0] / IN, bb[1][0] / IN, bb[2][1] / IN, bb[3][1] / IN, bb[4][2] / IN, bb[5][2] / IN]
    nf = b.GetFaceCount()
    return dict(vol=vol, area=area, com=com, box=box, faces=nf)
