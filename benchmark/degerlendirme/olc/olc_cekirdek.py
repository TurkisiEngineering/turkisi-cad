"""olc.py core: STEP loading, per-body properties, fine mesh, exact two-way surface deviation, face census, boolean worker.

Önceki dahili puanlama betiklerinden türetildi.
Everything in mm. Deterministic: every random draw uses a seed derived from a stable string (crc32).

Deviation method (RUBRIK §1 notes):
  * sample points on every face of body X (barycentric on the fine triangulation), then projected exactly onto the face's
    own surface (removes X's chord error);
  * nearest triangle of body Y's fine mesh -> mesh distance dm and the candidate Y face;
  * exact distance de = projection onto that Y face's surface when the foot lies inside the face (BRepClass), otherwise
    BRepExtrema point-to-face;
  * d = min(de, dm + chord_Y).  Both terms are upper bounds of the true distance; de is the exact B-rep value whenever
    Extrema finds the global minimum (analytic faces), dm + chord only wins where Extrema misses (helical / spline faces).
    The number of points where the mesh bound won is reported per body.
"""
import json, math, os, subprocess, sys, tempfile, threading, time, zlib, queue
import numpy as np

from OCP.STEPControl import STEPControl_Reader
from OCP.IFSelect import IFSelect_RetDone
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
from OCP.Bnd import Bnd_Box
from OCP.BRepBndLib import BRepBndLib
from OCP.TopExp import TopExp_Explorer, TopExp
from OCP.TopAbs import TopAbs_SOLID, TopAbs_SHELL, TopAbs_FACE, TopAbs_EDGE, TopAbs_REVERSED, TopAbs_IN, TopAbs_ON
from OCP.TopoDS import TopoDS
from OCP.TopLoc import TopLoc_Location
from OCP.BRep import BRep_Tool
from OCP.BRepMesh import BRepMesh_IncrementalMesh
from OCP.BRepBuilderAPI import BRepBuilderAPI_Copy, BRepBuilderAPI_MakeVertex, BRepBuilderAPI_MakeSolid
from OCP.BRepExtrema import BRepExtrema_DistShapeShape
from OCP.Extrema import Extrema_ExtFlag_MIN
from OCP.GeomAPI import GeomAPI_ProjectPointOnSurf
from OCP.BRepClass import BRepClass_FaceClassifier
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.GeomAbs import (GeomAbs_Plane, GeomAbs_Cylinder, GeomAbs_Cone, GeomAbs_Torus, GeomAbs_Sphere,
                         GeomAbs_BSplineSurface, GeomAbs_SurfaceOfRevolution, GeomAbs_SurfaceOfExtrusion)
from OCP.gp import gp_Pnt, gp_Pnt2d
from OCP.TopTools import TopTools_IndexedDataMapOfShapeListOfShape, TopTools_IndexedMapOfShape
from OCP.BRepTools import BRepTools
from OCP.BRep import BRep_Builder
from OCP.TopoDS import TopoDS_Shape, TopoDS_Solid

# ---- mesh / sampling constants (one place) ----
MESH_DEFL_MM = 0.002        # chord tolerance of the fine mesh (as in the press grading)
MESH_ANG_RAD = 0.08
SAMPLE_DENS_PER_MM2 = 0.3   # random sample density per face
SAMPLE_MIN_PER_FACE = 40
SAMPLE_MAX_PER_FACE = 2500
HOT_CAND_DENS = 2.0         # candidate density for hot-point search (mesh distance only)
HOT_CAND_MAX = 6000
FBOX_PAD_MM = 1e-3          # face bbox enlargement (lower bounds must never exceed the true distance)
REFINE_FREEFORM_MM = 1e-4   # free-form nearest face and exact distance above this -> mesh bound too
ANALYTIC = ("plane", "cylinder", "cone", "torus", "sphere")
TREE_MAX_PTS = 200          # worst refined points per side that get the (slow) Tree re-solve
TREE_RESOLVE_MM = 1e-3      # refined points still above this get the Extrema Tree re-solve
SEARCH_MARGIN_MM = 0.05     # face search continues while the bbox lower bound < KD bound + this
PROJ_SUSPECT_MM = 0.01      # own-projection move above this = face mesh and surface disagree -> mesh bound too
OWN_PROJ_MAX_MM = 0.5       # a sample is moved onto its own exact surface if the foot is closer than this
HOT_PER_FACE = 8           # hottest candidates kept per face (weight 0 in P95, count for max)


def seed(*parts):
    return zlib.crc32("|".join(str(p) for p in parts).encode()) & 0x7FFFFFFF


# ------------------------------------------------------------------ loading
def _nshell(s):
    n = 0; ex = TopExp_Explorer(s, TopAbs_SHELL)
    while ex.More():
        n += 1; ex.Next()
    return n


EMPTY_VOL_MM3 = 1e-6         # solids / shells below this volume or area are empty (dropped, counted)
EMPTY_AREA_MM2 = 1e-6
LAST_LOAD = {}               # info of the last load_step call: dropped empty bodies


def load_step(path):
    """All solids of the STEP (assembly instances located). Empty solids / shells (zero volume or zero area, e.g. the
    16 / 18 empty shells in the P2 / P3 originals) are dropped and counted in LAST_LOAD["bos_atilan"]."""
    r = STEPControl_Reader()
    if r.ReadFile(str(path)) != IFSelect_RetDone:
        raise RuntimeError("STEP okunamadi: %s" % path)
    r.TransferRoots()
    shape = r.OneShape()
    cand = []
    ex = TopExp_Explorer(shape, TopAbs_SOLID)
    while ex.More():
        cand.append(TopoDS.Solid_s(ex.Current())); ex.Next()
    n_free_shell = 0
    if not cand:  # some writers emit closed shells only
        ex = TopExp_Explorer(shape, TopAbs_SHELL)
        while ex.More():
            mk = BRepBuilderAPI_MakeSolid(TopoDS.Shell_s(ex.Current())); ex.Next()
            if mk.IsDone():
                cand.append(mk.Solid())
    else:  # shells that are not inside any solid (free shells) are ignored; count them
        ex = TopExp_Explorer(shape, TopAbs_SHELL, TopAbs_SOLID)
        while ex.More():
            n_free_shell += 1; ex.Next()
    out, dropped, dropped_sh = [], 0, 0
    cand2 = []
    for s in cand:   # empty (zero-area) shells inside a solid, e.g. 18 x 6 degenerate faces in the P3 original
        shells = []; ex = TopExp_Explorer(s, TopAbs_SHELL)
        while ex.More():
            sh = ex.Current(); ex.Next()
            a = GProp_GProps(); BRepGProp.SurfaceProperties_s(sh, a, True)
            if a.Mass() < EMPTY_AREA_MM2:
                dropped_sh += 1
            else:
                shells.append(TopoDS.Shell_s(sh))
        if len(shells) and dropped_sh and len(shells) < _nshell(s):
            bld = BRep_Builder(); ns = TopoDS_Solid(); bld.MakeSolid(ns)
            for sh in shells:
                bld.Add(ns, sh)
            cand2.append(ns)
        else:
            cand2.append(s)
    cand = cand2
    for s in cand:
        g = GProp_GProps(); BRepGProp.VolumeProperties_s(s, g, True)
        a = GProp_GProps(); BRepGProp.SurfaceProperties_s(s, a, True)
        if abs(g.Mass()) < EMPTY_VOL_MM3 or a.Mass() < EMPTY_AREA_MM2:
            dropped += 1; continue
        out.append(s)
    LAST_LOAD.clear(); LAST_LOAD.update(dosya=str(path), bos_atilan=dropped, bos_kabuk_atilan=dropped_sh, serbest_kabuk_yok_sayilan=n_free_shell, govde=len(out))
    if not out:
        raise RuntimeError("STEP icinde dolu govde yok: %s" % path)
    return out


def faces_of(s):
    out = []; ex = TopExp_Explorer(s, TopAbs_FACE)
    while ex.More():
        out.append(TopoDS.Face_s(ex.Current())); ex.Next()
    return out


def bbox_exact(s):
    b = Bnd_Box(); b.SetGap(0.0); BRepBndLib.AddOptimal_s(s, b, False, False)
    return list(b.Get())


def occ_props(s):
    g = GProp_GProps(); BRepGProp.VolumeProperties_s(s, g, True)
    c = g.CentreOfMass(); M = g.MatrixOfInertia()
    a = GProp_GProps(); BRepGProp.SurfaceProperties_s(s, a, True)
    return dict(vol=g.Mass(), area=a.Mass(), com=[c.X(), c.Y(), c.Z()],
                inertia=[[M.Value(i, j) for j in (1, 2, 3)] for i in (1, 2, 3)])


def face_area(f):
    g = GProp_GProps(); BRepGProp.SurfaceProperties_s(f, g, True)
    return g.Mass()


# ------------------------------------------------------------------ mesh
def mesh_body(s, defl=MESH_DEFL_MM, ang=MESH_ANG_RAD):
    """Mesh a private copy. Returns (copy, faces, V, F, fid) with outward winding; fid = face index per triangle."""
    s2 = BRepBuilderAPI_Copy(s, True, False).Shape()
    BRepMesh_IncrementalMesh(s2, defl, False, ang, False)
    fl = faces_of(s2)
    Vs, Fs, Is, off = [], [], [], 0
    for i, f in enumerate(fl):
        loc = TopLoc_Location()
        tri = BRep_Tool.Triangulation_s(f, loc)
        if tri is None:
            continue
        T = loc.Transformation()
        n = tri.NbNodes()
        P = np.empty((n, 3))
        for k in range(1, n + 1):
            p = tri.Node(k).Transformed(T)
            P[k - 1] = (p.X(), p.Y(), p.Z())
        m = tri.NbTriangles()
        idx = np.empty((m, 3), dtype=np.int64)
        for k in range(1, m + 1):
            a, b, c = tri.Triangle(k).Get()
            idx[k - 1] = (a - 1, b - 1, c - 1)
        if f.Orientation() == TopAbs_REVERSED:
            idx = idx[:, ::-1]
        Vs.append(P); Fs.append(idx + off); Is.append(np.full(m, i)); off += n
    if not Vs:
        raise RuntimeError("govde uclenemedi")
    return s2, fl, np.vstack(Vs), np.vstack(Fs), np.concatenate(Is)


def mesh_props(V, F):
    v0, v1, v2 = V[F[:, 0]], V[F[:, 1]], V[F[:, 2]]
    sv = np.einsum("ij,ij->i", v0, np.cross(v1, v2)) / 6.0
    vol = float(sv.sum())
    com = ((v0 + v1 + v2) / 4.0 * sv[:, None]).sum(0) / vol
    area = float(0.5 * np.linalg.norm(np.cross(v1 - v0, v2 - v0), axis=1).sum())
    # inertia about the centre of mass (tetra with apex at com)
    a0, a1, a2 = v0 - com, v1 - com, v2 - com
    sv2 = np.einsum("ij,ij->i", a0, np.cross(a1, a2)) / 6.0
    pts = np.stack([a0, a1, a2, np.zeros_like(a0)], axis=1)
    cov = np.zeros((3, 3))
    for i in range(4):
        for j in range(4):
            k = 0.1 if i == j else 0.05
            cov += k * (pts[:, i].T * sv2) @ pts[:, j]
    I = np.trace(cov) * np.eye(3) - cov
    return dict(vol=vol, area=area, com=com.tolist(), inertia=I.tolist())


def tri_areas(V, F):
    return 0.5 * np.linalg.norm(np.cross(V[F[:, 1]] - V[F[:, 0]], V[F[:, 2]] - V[F[:, 0]]), axis=1)


class Body:
    """One solid with its fine mesh, exact face list, proximity structure and face census (lazy)."""

    def __init__(self, solid, name):
        self.solid = solid; self.name = name
        self.copy, self.faces, self.V, self.F, self.fid = mesh_body(solid)
        self.occ = occ_props(solid)
        self.mesh = mesh_props(self.V, self.F)
        self.bbox = bbox_exact(solid)
        self.nfaces = len(self.faces)
        self._tm = None; self._census = None; self._farea = None
        self._surf = {}

    @property
    def farea(self):
        if self._farea is None:
            self._farea = np.array([face_area(f) for f in self.faces])
        return self._farea

    def kd(self):
        """KD-tree on mesh nodes + dense area-uniform points on the triangles (all within one chord of the surface):
        distance to the nearest cloud point + chord is an upper bound of the distance to the body."""
        if getattr(self, "_kd", None) is None:
            from scipy.spatial import cKDTree
            rng = np.random.default_rng(seed(self.name, "kd"))
            A = tri_areas(self.V, self.F); At = A.sum()
            n = int(min(3_000_000, max(20 * self.nfaces, At * 1.0)))
            idx = rng.choice(len(self.F), n, p=A / At)
            r1, r2 = rng.random(n), rng.random(n); s = np.sqrt(r1)
            Q = (1 - s)[:, None] * self.V[self.F[idx, 0]] + (s * (1 - r2))[:, None] * self.V[self.F[idx, 1]] + (s * r2)[:, None] * self.V[self.F[idx, 2]]
            self._kd = cKDTree(np.vstack([self.V, Q]))
        return self._kd, None

    def fbox(self):
        if getattr(self, "_fb", None) is None:
            bb = []
            for f in self.faces:
                b = Bnd_Box(); BRepBndLib.AddOptimal_s(f, b, False, False); bb.append(b.Get())
            self._fb = np.array(bb) + np.array([-1, -1, -1, 1, 1, 1]) * FBOX_PAD_MM   # Add() was not conservative on tori
        return self._fb

    def tm(self):
        if self._tm is None:
            import trimesh
            self._tm = trimesh.Trimesh(self.V, self.F, process=False, validate=False)
        return self._tm

    def surface(self, i):
        if i not in self._surf:
            self._surf[i] = BRep_Tool.Surface_s(self.faces[i])
        return self._surf[i]

    def release(self):
        self._tm = None; self._kd = None; self._tkd = None

    def census(self):
        if self._census is None:
            self._census = face_census(self)
        return self._census


# ------------------------------------------------------------------ sampling + deviation
def sample_faces(body, tag):
    """Random area-uniform samples per face, projected on the exact surface.
    Returns pts (n,3), face index (n,), weight (n,) [area share; 0 for hot candidates], hot flag."""
    rng = np.random.default_rng(seed(body.name, tag))
    A = tri_areas(body.V, body.F)
    pts, fids, ws = [], [], []
    for i in range(body.nfaces):
        m = body.fid == i
        if not m.any():
            continue
        Fi = body.F[m]; ai = A[m]; At = ai.sum()
        if At <= 0:
            continue
        n = int(min(SAMPLE_MAX_PER_FACE, max(SAMPLE_MIN_PER_FACE, math.ceil(At * SAMPLE_DENS_PER_MM2))))
        idx = rng.choice(len(Fi), n, p=ai / At)
        r1, r2 = rng.random(n), rng.random(n); s = np.sqrt(r1)
        P = (1 - s)[:, None] * body.V[Fi[idx, 0]] + (s * (1 - r2))[:, None] * body.V[Fi[idx, 1]] + (s * r2)[:, None] * body.V[Fi[idx, 2]]
        pts.append(P); fids.append(np.full(n, i)); ws.append(np.full(n, body.farea[i] / n))
    return np.vstack(pts), np.concatenate(fids), np.concatenate(ws)


def hot_candidates(body, other, tag):
    """Dense mesh-distance scan per face; returns the HOT_PER_FACE farthest points of each face (weight 0)."""
    rng = np.random.default_rng(seed(body.name, tag, "hot"))
    A = tri_areas(body.V, body.F)
    P_all, f_all = [], []
    for i in range(body.nfaces):
        m = body.fid == i
        if not m.any():
            continue
        Fi = body.F[m]; ai = A[m]; At = ai.sum()
        if At <= 0:
            continue
        n = int(min(HOT_CAND_MAX, max(64, math.ceil(At * HOT_CAND_DENS))))
        idx = rng.choice(len(Fi), n, p=ai / At)
        r1, r2 = rng.random(n), rng.random(n); s = np.sqrt(r1)
        P = (1 - s)[:, None] * body.V[Fi[idx, 0]] + (s * (1 - r2))[:, None] * body.V[Fi[idx, 1]] + (s * r2)[:, None] * body.V[Fi[idx, 2]]
        P_all.append(P); f_all.append(np.full(n, i))
    P = np.vstack(P_all); fi = np.concatenate(f_all)
    dm = other.kd()[0].query(P)[0]   # screening only (upper bound by node spacing)
    keep = []
    for i in np.unique(fi):
        w = np.where(fi == i)[0]
        keep.extend(w[np.argsort(-dm[w])[:HOT_PER_FACE]].tolist())
    keep = np.array(sorted(keep))
    return P[keep], fi[keep]


def mesh_dist(body, P, chunk=20000):
    """Distance from points to the body's fine mesh, plus nearest triangle's face index."""
    tm = body.tm()
    d = np.empty(len(P)); f = np.empty(len(P), dtype=np.int64)
    for i in range(0, len(P), chunk):
        _, dd, tri = tm.nearest.on_surface(P[i:i + chunk])
        d[i:i + chunk] = dd; f[i:i + chunk] = body.fid[tri]
    return d, f


def project_own(body, P, fids, return_ok=False):
    """Exact projection of each sample on its own face surface (removes chord error)."""
    out = P.copy(); ok = np.zeros(len(P), bool)
    for k in range(len(P)):
        pr = GeomAPI_ProjectPointOnSurf(gp_Pnt(*P[k]), body.surface(int(fids[k])))
        if pr.NbPoints() > 0:
            q = pr.NearestPoint()
            mv = q.Distance(gp_Pnt(*P[k]))
            if mv < OWN_PROJ_MAX_MM:   # BRepMesh sag can exceed the asked chord on some faces
                out[k] = (q.X(), q.Y(), q.Z()); ok[k] = mv < PROJ_SUSPECT_MM
    if return_ok:
        return out, ok
    return out


def _uv_info(other, fi):
    if not hasattr(other, "_uv"):
        other._uv = {}
    if fi not in other._uv:
        S = other.surface(fi)
        u0, u1, v0, v1 = BRepTools.UVBounds_s(other.faces[fi])
        other._uv[fi] = (u0, u1, v0, v1, S.UPeriod() if S.IsUPeriodic() else 0.0, S.VPeriod() if S.IsVPeriodic() else 0.0)
    return other._uv[fi]


def _wrap(x, lo, hi, per):
    """Move a periodic parameter into the face's [lo, hi] range when a shift by the period lands it there."""
    if per <= 0 or lo - 1e-9 <= x <= hi + 1e-9:
        return x
    k = math.floor((x - lo) / per)
    for kk in (k, k + 1, k - 1):
        y = x - kk * per
        if lo - 1e-9 <= y <= hi + 1e-9:
            return y
    return x - k * per


_VIA = [False]   # set by exact_to_face: True when the value came from a classified projection


def exact_to_face(other, p, fi, ext):
    face = other.faces[fi]
    try:
        pr = GeomAPI_ProjectPointOnSurf(p, other.surface(fi))
        if pr.NbPoints() > 0:
            u, v = pr.LowerDistanceParameters()
            u0, u1, v0, v1, pu, pv = _uv_info(other, fi)
            u = _wrap(u, u0, u1, pu); v = _wrap(v, v0, v1, pv)
            cl = BRepClass_FaceClassifier(face, gp_Pnt2d(u, v), 1e-7)
            if cl.State() in (TopAbs_IN, TopAbs_ON):
                _VIA[0] = True
                return pr.LowerDistance()
        _VIA[0] = False
        ext.LoadS2(face)
        ext.LoadS1(BRepBuilderAPI_MakeVertex(p).Vertex()); ext.Perform()
        if ext.IsDone() and ext.NbSolution() > 0:
            return ext.Value()
    except Exception:
        pass
    return np.inf


def exact_dist(other, P, cand):
    """Exact distance of each point to `other`: min over its candidate faces (projection inside face, else Extrema)."""
    d = np.full(len(P), np.inf)
    ext = BRepExtrema_DistShapeShape(); ext.SetFlag(Extrema_ExtFlag_MIN)
    for k in range(len(P)):
        p = gp_Pnt(*P[k])
        for fi in cand[k]:
            v = exact_to_face(other, p, int(fi), ext)
            if v < d[k]:
                d[k] = v
            if d[k] < 1e-7:
                break
    return d


def exact_dist_bb(other, P, ub, chunk=4000):
    """Exact distance to the whole body: faces visited in order of their bounding-box lower bound, stopping when the
    lower bound exceeds the best value (or the upper bound ub). Rigorous up to Extrema's own convergence."""
    FB = other.fbox(); d = np.full(len(P), np.inf); bf = np.full(len(P), -1); vp = np.zeros(len(P), bool)
    ext = BRepExtrema_DistShapeShape(); ext.SetFlag(Extrema_ExtFlag_MIN)
    for c0 in range(0, len(P), chunk):
        Pc = P[c0:c0 + chunk]
        lb = np.linalg.norm(np.maximum(0, np.maximum(FB[None, :, :3] - Pc[:, None, :], Pc[:, None, :] - FB[None, :, 3:])), axis=2)
        order = np.argsort(lb, axis=1)
        for k in range(len(Pc)):
            p = gp_Pnt(*Pc[k]); best = np.inf; lim = ub[c0 + k]
            for fi in order[k]:
                l = lb[k, fi]
                if l > best or l > lim:
                    break
                v = exact_to_face(other, p, int(fi), ext)
                if v < best:
                    best = v; bf[c0 + k] = fi; vp[c0 + k] = _VIA[0]
                if best < 1e-9:
                    break
            d[c0 + k] = best
    return d, bf, vp


def tree_dist(Y, P, ub):
    """Exact distance with Extrema_ExtAlgo_Tree to the faces whose bbox lies within ub of each point."""
    from OCP.Extrema import Extrema_ExtAlgo_Tree
    FB = Y.fbox(); out = np.full(len(P), np.inf)
    for k in range(len(P)):
        p = P[k]
        lb = np.linalg.norm(np.maximum(0, np.maximum(FB[:, :3] - p, p - FB[:, 3:])), axis=1)
        v = BRepBuilderAPI_MakeVertex(gp_Pnt(*p)).Vertex()
        for fi in np.where(lb <= ub[k])[0]:
            e = BRepExtrema_DistShapeShape(); e.SetAlgo(Extrema_ExtAlgo_Tree); e.SetFlag(Extrema_ExtFlag_MIN)
            e.LoadS1(v); e.LoadS2(Y.faces[int(fi)]); e.Perform()
            if e.IsDone() and e.NbSolution() > 0 and e.Value() < out[k]:
                out[k] = e.Value()
    return out


def one_way(X, Y, tag):
    """Samples of X -> distance to Y. Returns dict(pts, d, w, face, hot, n_mesh_bound, n_refined).
    ub = KD-cloud distance + chord (upper bound). Exact distance over the faces whose bbox lower bound is below the
    running best and ub. Where the exact value exceeds ub (Extrema missed the minimum, e.g. on helical spline faces)
    the true mesh distance (trimesh) is computed and d = min(exact, mesh + chord)."""
    P, fi, w = sample_faces(X, tag)
    H, hfi = hot_candidates(X, Y, tag)
    P = np.vstack([P, H]); fi = np.concatenate([fi, hfi]); w = np.concatenate([w, np.zeros(len(H))])
    hot = np.concatenate([np.zeros(len(P) - len(H), bool), np.ones(len(H), bool)])
    P, pok = project_own(X, P, fi, return_ok=True)   # pok False: face mesh far from its own surface (defective face)
    kd, _ = Y.kd()
    dk = kd.query(P)[0]
    de, bf, vp = exact_dist_bb(Y, P, dk + SEARCH_MARGIN_MM)   # margin > chord: BRepMesh sag may exceed the asked chord
    # Extrema is reliable on analytic faces; on free-form faces (helical threads, splines) it can miss the global
    # minimum, so every point whose best face is free-form (and not ~0) also gets the mesh bound
    freeform = np.array([r["t"] not in ANALYTIC for r in Y.census()])
    ff = np.zeros(len(P), bool); ok = bf >= 0; ff[ok] = freeform[bf[ok]]
    if freeform.any():   # a free-form face lies closer (by bbox) than the value found: Extrema may have missed it there
        FBf = Y.fbox()[freeform]
        for c0 in range(0, len(P), 20000):
            Pc = P[c0:c0 + 20000]
            lbf = np.linalg.norm(np.maximum(0, np.maximum(FBf[None, :, :3] - Pc[:, None, :], Pc[:, None, :] - FBf[None, :, 3:])), axis=2).min(1)
            ff[c0:c0 + 20000] |= lbf < de[c0:c0 + 20000]
    # ... and every point whose best value came from the Extrema fallback (foot classified outside the face: trimmed
    # faces with helical / spline edges can be misclassified and Extrema then misses)
    dt = tri_dist(Y, P)   # fast mesh bound for every point: catches faces whose trimming disagrees with their mesh
    bad = np.where((de > dk + MESH_DEFL_MM + 1e-6) | (de > dt + MESH_DEFL_MM + 1e-6) | ((ff | ~vp | ~pok) & (de > REFINE_FREEFORM_MM)))[0]
    n_mb = 0
    if len(bad):
        dm = dt[bad]   # mesh bound (vectorised point-triangle; trimesh no longer needed here)
        ub = dm + MESH_DEFL_MM
        best = de[bad].copy()
        # Extrema Tree algorithm on the faces near the point (as s09b): finds the global minimum on helical splines
        # where the default (Grad) algorithm and a coarse BRepMesh both fail
        hard = np.where((best > TREE_RESOLVE_MM) & (best > dm + MESH_DEFL_MM + TREE_RESOLVE_MM))[0]   # exact and mesh disagree
        hard = hard[np.argsort(-best[hard])][:TREE_MAX_PTS]
        if len(hard):
            best[hard] = np.minimum(best[hard], tree_dist(Y, P[bad][hard], dm[hard] + SEARCH_MARGIN_MM))
        n_mb = int((ub < best - 1e-6).sum())
        de[bad] = np.minimum(best, ub)
    return dict(pts=P, d=de, w=w, face=fi, hot=hot, n_mesh_bound=n_mb, n_refined=int(len(bad)), n=len(P), n_izdusumsuz=int((~pok).sum()))


def wstats(d, w):
    m = w > 0
    dd, ww = d[m], w[m]
    i = np.argsort(dd); dd, ww = dd[i], ww[i]
    c = np.cumsum(ww) / ww.sum()
    return float((dd * ww).sum() / ww.sum()), float(np.interp(0.95, c, dd))


def deviation(A, B, tag):
    """Two-way deviation between bodies A (original) and B (rebuild)."""
    ab = one_way(A, B, tag + "/A")
    ba = one_way(B, A, tag + "/B")
    d = np.concatenate([ab["d"], ba["d"]]); w = np.concatenate([ab["w"], ba["w"]])
    mean, p95 = wstats(d, w)
    mA = float((ab["d"] * ab["w"]).sum() / ab["w"].sum()); mB = float((ba["d"] * ba["w"]).sum() / ba["w"].sum())
    wh = np.argmax(d); P = np.vstack([ab["pts"], ba["pts"]])
    return dict(mean=mean, p95=p95, max=float(d.max()), where_max=P[wh].tolist(), mean_A=mA, mean_B=mB,
                n=[ab["n"], ba["n"]], n_mesh_bound=[ab["n_mesh_bound"], ba["n_mesh_bound"]],
                _ab=ab, _ba=ba)


# ------------------------------------------------------------------ face census (analytic surfaces)
def _v(d):
    return np.array([d.X(), d.Y(), d.Z()])


def canon(d):
    d = np.array(d, float)
    for x in d:
        if abs(x) > 1e-6:
            return d * (1 if x > 0 else -1)
    return d


def face_census(body):
    """Per face: type (plane/cylinder/cone/torus/sphere/bspline/other), parameters, centroid, area.
    NX writes revolve faces as cones: ~0 deg cone -> cylinder, ~90 deg cone -> plane (as in s04_census)."""
    rows = []
    for i, f in enumerate(body.faces):
        S = BRepAdaptor_Surface(f); t = S.GetType()
        g = GProp_GProps(); BRepGProp.SurfaceProperties_s(f, g, True)
        a = g.Mass(); c = _v(g.CentreOfMass())
        r = dict(i=i, a=a, c=c.tolist())
        if t == GeomAbs_Plane:
            pl = S.Plane(); n = canon(_v(pl.Axis().Direction()))
            r.update(t="plane", n=n.tolist(), d=float(n @ _v(pl.Location())))
        elif t == GeomAbs_Cylinder:
            cy = S.Cylinder(); ax = canon(_v(cy.Axis().Direction())); o = _v(cy.Location())
            r.update(t="cylinder", ax=ax.tolist(), o=o.tolist(), r=cy.Radius())
        elif t == GeomAbs_Cone:
            co = S.Cone(); ax = canon(_v(co.Axis().Direction())); ap = _v(co.Apex()); ang = abs(math.degrees(co.SemiAngle()))
            if ang < 0.02:
                r0 = float(np.linalg.norm((c - ap) - ax * float(ax @ (c - ap))))
                r.update(t="cylinder", ax=ax.tolist(), o=ap.tolist(), r=r0, src="degenerate cone")
            elif ang > 89.98:
                r.update(t="plane", n=ax.tolist(), d=float(ax @ c), src="degenerate cone")
            else:
                r.update(t="cone", ax=ax.tolist(), o=ap.tolist(), ang=ang, r=co.RefRadius())
        elif t == GeomAbs_Torus:
            to = S.Torus(); ax = canon(_v(to.Axis().Direction()))
            r.update(t="torus", ax=ax.tolist(), o=_v(to.Location()).tolist(), R=to.MajorRadius(), r=to.MinorRadius())
        elif t == GeomAbs_Sphere:
            sp = S.Sphere(); r.update(t="sphere", o=_v(sp.Location()).tolist(), r=sp.Radius())
        else:
            r.update(t={GeomAbs_BSplineSurface: "bspline", GeomAbs_SurfaceOfRevolution: "revolution",
                        GeomAbs_SurfaceOfExtrusion: "extrusion"}.get(t, "other"))
        rows.append(r)
    return rows


def same_surface(a, b, tol=1e-3, atol=1e-4):
    if a["t"] != b["t"]:
        return False
    t = a["t"]
    if t == "plane":
        return abs(abs(np.dot(a["n"], b["n"])) - 1) < atol and abs(a["d"] - b["d"] * np.sign(np.dot(a["n"], b["n"]))) < tol
    if t in ("cylinder", "cone", "torus"):
        if abs(abs(np.dot(a["ax"], b["ax"])) - 1) > atol:
            return False
        dv = np.subtract(b["o"], a["o"]); ax = np.array(a["ax"])
        if t == "cone":
            if np.linalg.norm(dv) > tol or abs(a["ang"] - b["ang"]) > 0.01:
                return False
            return True
        if t == "torus":
            return np.linalg.norm(dv) < tol and abs(a["R"] - b["R"]) < tol and abs(a["r"] - b["r"]) < tol
        perp = dv - ax * (dv @ ax)
        return np.linalg.norm(perp) < tol and abs(a["r"] - b["r"]) < tol
    if t == "sphere":
        return np.linalg.norm(np.subtract(a["o"], b["o"])) < tol and abs(a["r"] - b["r"]) < tol
    return False


def face_adjacency(body):
    """dict face index -> set of face indices sharing an edge (cached)."""
    if getattr(body, "_adj", None) is None:
        fmap = TopTools_IndexedMapOfShape()
        for f in body.faces:
            fmap.Add(f)
        emap = TopTools_IndexedDataMapOfShapeListOfShape()
        TopExp.MapShapesAndAncestors_s(body.copy, TopAbs_EDGE, TopAbs_FACE, emap)
        adj = {}
        for k in range(1, emap.Extent() + 1):
            ids = sorted({fmap.FindIndex(sh) - 1 for sh in emap.FindFromIndex(k)} - {-1})
            for x in ids:
                adj.setdefault(x, set()).update(i for i in ids if i != x)
        body._adj = adj
    return body._adj


def face_components(body, joinable=None):
    """Union of faces that lie on the same analytic surface AND share an edge (a cylinder written as two halves = one).
    joinable(a, b) overrides the 'same surface' test (used for B-spline fillet patches)."""
    C = body.census()
    n = len(C); parent = list(range(n))
    test = joinable or (lambda a, b: same_surface(C[a], C[b]))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for a, nb in face_adjacency(body).items():
        for b in nb:
            if a < b and test(a, b):
                parent[find(a)] = find(b)
    comps = {}
    for i in range(n):
        comps.setdefault(find(i), []).append(i)
    return list(comps.values())


def spline_radius(body, i, n=4):
    """Radius of a B-spline / other free-form face read from its largest principal curvature (median over an n x n
    interior UV grid): a rolling-ball fillet or a cylinder written as B-spline gives its radius. None if undefined."""
    from OCP.GeomLProp import GeomLProp_SLProps
    if not hasattr(body, "_srad"):
        body._srad = {}
    if i in body._srad:
        return body._srad[i]
    S = body.surface(i); u0, u1, v0, v1 = BRepTools.UVBounds_s(body.faces[i]); rr = []
    for a in range(n):
        for b in range(n):
            u = u0 + (u1 - u0) * (a + 0.5) / n; v = v0 + (v1 - v0) * (b + 0.5) / n
            pr = GeomLProp_SLProps(S, u, v, 2, 1e-7)
            if pr.IsCurvatureDefined():
                k = max(abs(pr.MaxCurvature()), abs(pr.MinCurvature()))
                if k > 1e-9:
                    rr.append(1.0 / k)
    r = float(np.median(rr)) if rr else None
    body._srad[i] = r
    return r


# ------------------------------------------------------------------ boolean worker (separate process, timeout)
WORKER_SRC = r'''
import sys, json
from OCP.BRepTools import BRepTools
from OCP.BRep import BRep_Builder
from OCP.TopoDS import TopoDS_Shape
from OCP.BRepAlgoAPI import BRepAlgoAPI_Common, BRepAlgoAPI_Cut
from OCP.TopTools import TopTools_ListOfShape
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
from OCP.BRepCheck import BRepCheck_Analyzer
def rd(p):
    s = TopoDS_Shape(); BRepTools.Read_s(s, p, BRep_Builder()); return s
def vol(s):
    g = GProp_GProps(); BRepGProp.VolumeProperties_s(s, g); return g.Mass()
def op(cls, a, b, fz):
    L1 = TopTools_ListOfShape(); L1.Append(a); L2 = TopTools_ListOfShape(); L2.Append(b)
    c = cls(); c.SetArguments(L1); c.SetTools(L2); c.SetFuzzyValue(fz); c.SetRunParallel(False); c.Build()
    if not c.IsDone() or (hasattr(c, 'HasErrors') and c.HasErrors()):
        return None, False
    s = c.Shape()
    return vol(s), bool(BRepCheck_Analyzer(s).IsValid())
for line in sys.stdin:
    j = json.loads(line)
    try:
        a, b = rd(j["a"]), rd(j["b"])
        res = {}
        cv, cok = op(BRepAlgoAPI_Common, a, b, j["fuzzy"])
        res["common"] = cv; res["common_valid"] = cok
        if j.get("cut"):
            xv, xok = op(BRepAlgoAPI_Cut, a, b, j["fuzzy"])
            res["cut"] = xv; res["cut_valid"] = xok
        print(json.dumps(res), flush=True)
    except Exception as e:
        print(json.dumps({"error": str(e)}), flush=True)
'''


BOOL_MAX_GB = 3.0            # boolean child process is killed above this working set
BOOL_MIN_SYS_FREE_GB = 1.0   # ... or when the machine's free memory drops below this


class BoolWorker:
    """Runs OCC booleans in a child process so a hanging boolean can be killed (timeout)."""

    def __init__(self, timeout=120):
        self.timeout = timeout; self.p = None
        self.tmp = tempfile.TemporaryDirectory(prefix="olc_bool_")
        self.wpath = os.path.join(self.tmp.name, "worker.py")
        open(self.wpath, "w").write(WORKER_SRC)
        self.cache = {}; self.n = 0; self.timeouts = 0; self.killed = []; self.peak = 0.0

    def _start(self):
        self.p = subprocess.Popen([sys.executable, "-I", self.wpath], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  stderr=subprocess.DEVNULL, text=True, bufsize=1)
        self.q = queue.Queue()
        p = self.p

        def rd():
            for line in p.stdout:
                self.q.put(line)
        threading.Thread(target=rd, daemon=True).start()

    def path(self, key, shape):
        if key not in self.cache:
            fp = os.path.join(self.tmp.name, "s%05d.brep" % len(self.cache))
            BRepTools.Write_s(shape, fp)
            self.cache[key] = fp
        return self.cache[key]

    def run(self, ka, a, kb, b, fuzzy, cut=False):
        if self.p is None or self.p.poll() is not None:
            self._start()
        job = dict(a=self.path(ka, a), b=self.path(kb, b), fuzzy=fuzzy, cut=cut)
        self.p.stdin.write(json.dumps(job) + "\n"); self.p.stdin.flush(); self.n += 1
        t0 = time.time(); peak = 0.0
        try:
            import psutil
            proc = psutil.Process(self.p.pid)
        except Exception:
            psutil = None; proc = None
        while True:
            try:
                line = self.q.get(timeout=0.25)
                r = json.loads(line); r["bellek_gb"] = round(peak, 3); r["sure_s"] = round(time.time() - t0, 2)
                self.peak = max(self.peak, peak)
                return r
            except queue.Empty:
                pass
            why = None
            if proc is not None:
                try:
                    rss = proc.memory_info().rss / 2 ** 30; peak = max(peak, rss)
                    if rss > BOOL_MAX_GB:
                        why = "bellek %.1f GB > %.1f GB" % (rss, BOOL_MAX_GB)
                    elif psutil.virtual_memory().available / 2 ** 30 < BOOL_MIN_SYS_FREE_GB:
                        why = "sistem bos bellegi < %.1f GB" % BOOL_MIN_SYS_FREE_GB
                except Exception:
                    pass
            if why is None and time.time() - t0 > self.timeout:
                why = "zaman asimi %ds" % self.timeout
            if why is None and self.p.poll() is not None:
                why = "isci coktu"
            if why:
                self.timeouts += 1; self.killed.append(why); self.peak = max(self.peak, peak)
                try:
                    self.p.kill()
                except Exception:
                    pass
                self.p = None
                return {"error": why, "bellek_gb": round(peak, 3)}

    def close(self):
        if self.p is not None and self.p.poll() is None:
            self.p.stdin.close(); self.p.wait(10)
        self.tmp.cleanup()


FIT_RMS_MM = 0.01            # free-form face accepted as plane / cylinder when the fit residual RMS is below this


def face_grid(body, i, n=12):
    """Points and unit normals on an n x n UV grid of face i, only where the UV point is inside the face."""
    from OCP.GeomLProp import GeomLProp_SLProps
    S = body.surface(i); face = body.faces[i]
    u0, u1, v0, v1 = BRepTools.UVBounds_s(face); P, N = [], []
    for a in range(n):
        for b in range(n):
            u = u0 + (u1 - u0) * (a + 0.5) / n; v = v0 + (v1 - v0) * (b + 0.5) / n
            if BRepClass_FaceClassifier(face, gp_Pnt2d(u, v), 1e-7).State() not in (TopAbs_IN, TopAbs_ON):
                continue
            pr = GeomLProp_SLProps(S, u, v, 1, 1e-7)
            if not pr.IsNormalDefined():
                continue
            q = pr.Value(); nn = pr.Normal()
            P.append((q.X(), q.Y(), q.Z())); N.append((nn.X(), nn.Y(), nn.Z()))
    return np.array(P), np.array(N)


def fit_primitive(body, i, kind):
    """Fit a plane ('plane') or cylinder ('cylinder') to free-form face i. Returns a census-like dict or None."""
    P, N = face_grid(body, i)
    if len(P) < 8:
        return None
    c = P.mean(0)
    if kind == "plane":
        w, V = np.linalg.eigh((P - c).T @ (P - c)); n = canon(V[:, 0])
        rms = float(np.sqrt(np.mean(((P - c) @ n) ** 2)))
        if rms > FIT_RMS_MM:
            return None
        return dict(i=i, t="plane", n=n.tolist(), d=float(n @ c), c=c.tolist(), fit_rms=rms, fit="free-form face fitted as plane")
    w, V = np.linalg.eigh(N.T @ N); ax = canon(V[:, 0])          # normals are perpendicular to the axis
    e1 = np.cross(ax, [1, 0, 0] if abs(ax[0]) < 0.9 else [0, 1, 0]); e1 /= np.linalg.norm(e1); e2 = np.cross(ax, e1)
    x, y = (P - c) @ e1, (P - c) @ e2
    A = np.column_stack([x, y, np.ones_like(x)]); bb = x ** 2 + y ** 2
    sol, *_ = np.linalg.lstsq(A, bb, rcond=None)
    cx, cy = sol[0] / 2, sol[1] / 2; r = float(np.sqrt(sol[2] + cx ** 2 + cy ** 2))
    rms = float(np.sqrt(np.mean((np.hypot(x - cx, y - cy) - r) ** 2)))
    if rms > FIT_RMS_MM or not np.isfinite(r):
        return None
    o = c + cx * e1 + cy * e2
    return dict(i=i, t="cylinder", ax=ax.tolist(), o=o.tolist(), r=r, c=c.tolist(), fit_rms=rms, fit="free-form face fitted as cylinder")


def _closest_on_tri(P, A, B, C):
    """Vectorised closest point on triangles (Ericson, Real-Time Collision Detection 5.1.5). Shapes (...,3)."""
    ab, ac, ap = B - A, C - A, P - A
    d1 = (ab * ap).sum(-1); d2 = (ac * ap).sum(-1)
    bp = P - B; d3 = (ab * bp).sum(-1); d4 = (ac * bp).sum(-1)
    cp = P - C; d5 = (ab * cp).sum(-1); d6 = (ac * cp).sum(-1)
    va = d3 * d6 - d5 * d4; vb = d5 * d2 - d1 * d6; vc = d1 * d4 - d3 * d2
    den = va + vb + vc; den = np.where(np.abs(den) < 1e-30, 1e-30, den)
    v = vb / den; w = vc / den
    Q = A + ab * v[..., None] + ac * w[..., None]                      # inside
    with np.errstate(divide="ignore", invalid="ignore"):
        e_ab = A + ab * np.clip(d1 / np.where(d1 - d3 == 0, 1e-30, d1 - d3), 0, 1)[..., None]
        e_ac = A + ac * np.clip(d2 / np.where(d2 - d6 == 0, 1e-30, d2 - d6), 0, 1)[..., None]
        bc = C - B; t = np.clip((d4 - d3) / np.where((d4 - d3) + (d5 - d6) == 0, 1e-30, (d4 - d3) + (d5 - d6)), 0, 1)
        e_bc = B + bc * t[..., None]
    cand = np.stack([Q, e_ab, e_ac, e_bc, A, B, C], axis=-2)
    inside = (va >= 0) & (vb >= 0) & (vc >= 0)
    dist = np.linalg.norm(cand - P[..., None, :], axis=-1)
    dist[..., 0] = np.where(inside, dist[..., 0], np.inf)
    return dist.min(-1)


TRI_K = 32


def tri_dist(body, P, chunk=20000):
    """Upper bound of the distance from points to the body's mesh: exact point-triangle distance over the TRI_K
    triangles with the nearest centroids (exact whenever the nearest triangle is among them)."""
    if getattr(body, "_tkd", None) is None:
        from scipy.spatial import cKDTree
        body._tkd = cKDTree(body.V[body.F].mean(axis=1))
    out = np.empty(len(P))
    k = min(TRI_K, len(body.F))
    for c0 in range(0, len(P), chunk):
        Pc = P[c0:c0 + chunk]
        _, j = body._tkd.query(Pc, k=k)
        j = j.reshape(len(Pc), -1); T3 = body.V[body.F[j]]
        out[c0:c0 + chunk] = _closest_on_tri(Pc[:, None, :], T3[..., 0, :], T3[..., 1, :], T3[..., 2, :]).min(-1)
    return out
