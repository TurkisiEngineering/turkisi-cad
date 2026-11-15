"""Measurement recipes of PAKET_SEMASI.md, reusable by olc.py (task A) and the C-task scoring.

A recipe is a dict with `tip` and fields; points are mm in the global frame. Bodies are olc_cekirdek.Body objects,
addressed by spec name through the `govdeler` dict passed in (the caller maps spec names to the matched bodies).

Schema types: bbox_boyut, silindir_cap, eksen_mesafe, duzlem_mesafe, aci, sayi, bolgesel_sapma, koordinat
(`eksen`, `uc` min|max, `referans` mm -> |referans - body bbox extreme|). govde "MONTAJ" = all bodies together
(bbox_boyut / koordinat on the assembly bbox).
Optional extensions (all backward compatible, used by the calibration hidden set; tell the spec writers):
  * every two-point recipe: `govde2` = body of nokta2 (default: govde); `tur1` / `tur2` = "duzlem" | "eksen" to measure
    plane-to-axis distances (default: both "duzlem" for duzlem_mesafe, both "eksen" for eksen_mesafe / aci auto);
  * bbox_boyut: `bolge` [xmin,ymin,zmin,xmax,ymax,zmax] = only the part of the body inside this box (mesh vertices);
  * sayi with r_mm on cylinder / torus also counts B-spline faces whose curvature radius matches (kernel independence);
  * sayi: `yon` [3] = plane normal / axis direction filter (sign-free, 1e-3); `sayi` counts distinct surfaces: faces on
    the same analytic surface that share an edge count once (a hole written as two half-cylinders = 1);
  * bolgesel_sapma: `kutu` [6] (+ optional `haric` list of boxes) instead of nokta / r_mm; neither = whole body.
Returned value: dict(deger, birim in {"mm","deg","adet"}, detay...) or dict(deger=None, hata=...).
"""
import math
import numpy as np
from OCP.BRepExtrema import BRepExtrema_DistShapeShape
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeVertex
from OCP.gp import gp_Pnt
from OCP.Bnd import Bnd_Box
from OCP.BRepBndLib import BRepBndLib

import olc_cekirdek as K

LEN_TOL_MM = 0.05     # PAKET_SEMASI default length tolerance
ANG_TOL_DEG = 0.2     # default angle tolerance
R_TOL_MM = 0.05       # sayi: radius tolerance
DIR_TOL = 1e-3        # sayi: direction tolerance (1 - |cos|)
TYPE_MAP = {"plane": ("plane",), "cylinder": ("cylinder",), "cone": ("cone",), "torus": ("torus",), "sphere": ("sphere",),
            "bspline": ("bspline", "revolution", "extrusion", "other")}
BIRIM = {"bbox_kenar_fark": "mm", "montaj_bbox_boyut": "mm", "duzlem_mesafe_govdeler": "mm", "koordinat": "mm", "bbox_boyut": "mm", "silindir_cap": "mm", "eksen_mesafe": "mm", "duzlem_mesafe": "mm", "aci": "deg",
         "sayi": "adet", "bolgesel_sapma": "mm"}


def _face_boxes(body):
    return body.fbox()


def nearest_face(body, p, types):
    """Index of the face of one of `types` (census types) nearest to point p, and its distance (exact BRep)."""
    C = body.census(); FB = _face_boxes(body); p = np.asarray(p, float)
    cand = [i for i, r in enumerate(C) if r["t"] in types]
    if not cand:
        return None, None
    lo = np.array([np.linalg.norm(np.maximum(0, np.maximum(FB[i, :3] - p, p - FB[i, 3:]))) for i in cand])
    order = np.argsort(lo)
    best, bi = math.inf, None
    v = BRepBuilderAPI_MakeVertex(gp_Pnt(*p)).Vertex()
    for k in order:
        if lo[k] > best:
            break
        i = cand[k]
        e = BRepExtrema_DistShapeShape(v, body.faces[i])
        if e.IsDone() and e.NbSolution() > 0 and e.Value() < best:
            best, bi = e.Value(), i
    return bi, best


NOKTA_MAX_MM = 1.0   # rebuild: face may lie at most this much farther from the recipe point than on the original
SNAP_MM = 0.1   # a free-form face this close to the point (and closer than any face of the asked type) is fitted


def _feature(body, p, tur, lim=None):
    """tur 'duzlem' -> plane face; 'eksen' -> cylinder/cone face (axis). Kernel independence: if the face at the point
    is free-form (a plane or cylinder written as B-spline by some kernels), a plane / cylinder is fitted to it."""
    types = ("plane",) if tur == "duzlem" else ("cylinder", "cone")
    i, d = nearest_face(body, p, types)
    j, dj = nearest_face(body, p, TYPE_MAP["bspline"])
    if j is not None and dj <= SNAP_MM and (i is None or dj < d - 1e-6):
        fr = K.fit_primitive(body, j, "plane" if tur == "duzlem" else "cylinder")
        if fr is not None:
            fr["_dist"] = dj
            return fr
    if i is None or (lim is not None and d > lim):
        return None   # no face of the asked type at the point (farther than on the original + NOKTA_MAX_MM)
    r = dict(body.census()[i]); r["_dist"] = d
    return r


def _line_dist(o1, a1, o2, a2):
    o1, a1, o2, a2 = map(lambda x: np.asarray(x, float), (o1, a1, o2, a2))
    w = o2 - o1; c = np.cross(a1, a2); nc = np.linalg.norm(c)
    if nc < 1e-9:
        return float(np.linalg.norm(w - a1 * (w @ a1)))
    return float(abs(w @ c) / nc)


def _dist(f1, f2):
    t1, t2 = f1["t"], f2["t"]
    if t1 == "plane" and t2 == "plane":
        n = np.array(f1["n"]); return float(abs(n @ np.array(f2["c"]) - f1["d"])), _ang(n, f2["n"])
    if t1 == "plane":
        n = np.array(f1["n"]); return float(abs(n @ np.array(f2["o"]) - f1["d"])), 90 - _ang(n, f2["ax"])
    if t2 == "plane":
        n = np.array(f2["n"]); return float(abs(n @ np.array(f1["o"]) - f2["d"])), 90 - _ang(n, f1["ax"])
    return _line_dist(f1["o"], f1["ax"], f2["o"], f2["ax"]), _ang(f1["ax"], f2["ax"])


def _ang(a, b):
    c = abs(float(np.dot(a, b)) / (np.linalg.norm(a) * np.linalg.norm(b)))
    return math.degrees(math.acos(min(1.0, c)))


def _dirv(r):
    return np.array(r["n"] if r["t"] == "plane" else r["ax"])


def _inbox(P, box):
    box = np.asarray(box, float)
    return np.all((P >= box[:3]) & (P <= box[3:]), axis=1)


def olc(recipe, govdeler, hepsi=None, ref=None):
    """Evaluate one single-model recipe. govdeler: spec name -> Body. bolgesel_sapma is not handled here (two models).
    `ekle_mm` (optional) is added to a length result; tip `duzlem_mesafe_govdeler` = duzlem_mesafe with govde2."""
    lim = None
    if ref is not None:   # rebuild: the face may be at most NOKTA_MAX_MM farther from the point than on the original
        u = ref.get("uzaklik")
        u = max(u) if isinstance(u, list) else u
        lim = (u or 0.0) + NOKTA_MAX_MM
    r = _olc(recipe, govdeler, hepsi, lim)
    if recipe.get("ekle_mm") and r.get("deger") is not None and r.get("birim") == "mm":
        r["ham"] = r["deger"]; r["deger"] = r["deger"] + float(recipe["ekle_mm"])
    return r


MONTAJ = "MONTAJ"   # govde name meaning "all bodies of the model together" (assembly bbox)


def _bbox_all(bodies):
    B = np.array([b.bbox for b in bodies])
    return list(B[:, :3].min(0)) + list(B[:, 3:].max(0))


def _olc(recipe, govdeler, hepsi=None, lim=None):
    t = recipe["tip"]
    if t == "duzlem_mesafe_govdeler":
        t = "duzlem_mesafe"
    if t == "montaj_bbox_boyut":   # alias: bbox_boyut with govde MONTAJ
        recipe = dict(recipe, tip="bbox_boyut", govde=MONTAJ); t = "bbox_boyut"
    try:
        if t == "bbox_kenar_fark":
            # |bbox(govde2)[kenar2] - bbox(govde)[kenar]|, kenar = xmin|ymin|zmin|xmax|ymax|zmax (exact bboxes)
            K6 = ["xmin", "ymin", "zmin", "xmax", "ymax", "zmax"]
            g1 = govdeler.get(recipe.get("govde")); g2 = govdeler.get(recipe.get("govde2", recipe.get("govde")))
            if g1 is None or g2 is None:
                return dict(deger=None, hata="govde yok")
            v1 = g1.bbox[K6.index(recipe["kenar"])]; v2 = g2.bbox[K6.index(recipe["kenar2"])]
            return dict(deger=float(abs(v2 - v1)), birim="mm", kenarlar=[float(v1), float(v2)])
        if recipe.get("govde") == MONTAJ:
            allb = list(hepsi) if hepsi is not None else list(govdeler.values())
            if t == "bbox_boyut":
                k = "xyz".index(recipe["eksen"].lower()); bb = _bbox_all(allb)
                return dict(deger=float(bb[k + 3] - bb[k]), birim="mm", kaynak="kesin bbox, butun govdeler")
            if t == "koordinat":
                k = "xyz".index(recipe["eksen"].lower()); bb = _bbox_all(allb)
                v = bb[k] if recipe.get("uc", "min") == "min" else bb[k + 3]
                return dict(deger=float(abs(float(recipe.get("referans", 0.0)) - v)), birim="mm", uc_deger=float(v))
            return dict(deger=None, hata="MONTAJ yalniz bbox_boyut / koordinat ile")
        g = govdeler.get(recipe.get("govde"))
        if g is None:
            return dict(deger=None, hata="govde yok: %s" % recipe.get("govde"))
        if t == "bbox_boyut":
            k = "xyz".index(recipe["eksen"].lower())
            if recipe.get("bolge"):
                m = _inbox(g.V, recipe["bolge"])
                if not m.any():
                    return dict(deger=None, hata="bolgede nokta yok")
                v = g.V[m, k]; return dict(deger=float(v.max() - v.min()), birim="mm", kaynak="mesh dugumleri (bolge)")
            return dict(deger=float(g.bbox[k + 3] - g.bbox[k]), birim="mm", kaynak="kesin bbox")
        if t == "koordinat":
            # |referans - extreme coordinate of the body| along eksen; uc = "min" | "max" (exact bbox)
            k = "xyz".index(recipe["eksen"].lower())
            v = g.bbox[k] if recipe.get("uc", "min") == "min" else g.bbox[k + 3]
            return dict(deger=float(abs(float(recipe.get("referans", 0.0)) - v)), birim="mm", uc_deger=float(v))
        if t == "silindir_cap":
            f = _feature(g, recipe["nokta"], "eksen", lim)
            if f is None or f["t"] != "cylinder":
                return dict(deger=None, hata="silindir yok")
            return dict(deger=2 * f["r"], birim="mm", yuz=f["i"], uzaklik=f["_dist"])
        if t in ("eksen_mesafe", "duzlem_mesafe", "aci"):
            g2 = govdeler.get(recipe.get("govde2", recipe.get("govde")))
            if g2 is None:
                return dict(deger=None, hata="govde2 yok")
            dflt = "eksen" if t == "eksen_mesafe" else "duzlem"
            if t == "aci":
                f1 = _auto(g, recipe["nokta1"], recipe.get("tur1"), lim); f2 = _auto(g2, recipe["nokta2"], recipe.get("tur2"), lim)
            else:
                f1 = _feature(g, recipe["nokta1"], recipe.get("tur1", dflt), lim); f2 = _feature(g2, recipe["nokta2"], recipe.get("tur2", dflt), lim)
            if f1 is None or f2 is None:
                return dict(deger=None, hata="yuz bulunamadi")
            if t == "aci":
                return dict(deger=_ang(_dirv(f1), _dirv(f2)), birim="deg", yuz=[f1["i"], f2["i"]], uzaklik=[f1["_dist"], f2["_dist"]])
            d, a = _dist(f1, f2)
            return dict(deger=d, birim="mm", yuz=[f1["i"], f2["i"]], paralellik_deg=a, uzaklik=[f1["_dist"], f2["_dist"]])
        if t == "sayi":
            # faces filtered by type, radius, direction and region (face bbox centre), then grouped:
            # default = distinct analytic surfaces (faces on one surface count once; same rule as the spec writers' tool);
            # `ayri_yuzler: true` = faces on one surface count once only when they share an edge (coplanar lands apart).
            types = TYPE_MAP[recipe["yuzey"]]
            C = g.census(); FB = _face_boxes(g); sel = []
            for r0 in C:
                if r0["t"] not in types:
                    continue
                if recipe.get("r_mm") is not None and ("r" not in r0 or abs(r0["r"] - recipe["r_mm"]) > R_TOL_MM):
                    continue
                if recipe.get("yon") is not None and r0["t"] in ("plane", "cylinder", "cone", "torus"):
                    if abs(abs(float(np.dot(_dirv(r0), recipe["yon"]) / np.linalg.norm(recipe["yon"]))) - 1) > DIR_TOL:
                        continue
                if recipe.get("bolge"):
                    c = (FB[r0["i"], :3] + FB[r0["i"], 3:]) / 2
                    if not _inbox(c[None], recipe["bolge"])[0]:
                        continue
                sel.append(r0["i"])
            if recipe.get("ayri_yuzler"):
                ss = set(sel); groups = []
                for comp in K.face_components(g):
                    m = [i for i in comp if i in ss]
                    if m:
                        groups.append(m)
            else:
                groups = []
                for i in sel:
                    for gr in groups:
                        if K.same_surface(C[gr[0]], C[i]):
                            gr.append(i); break
                    else:
                        groups.append([i])
            # kernel independence: with r_mm on cylinder / torus, free-form faces (a rolling-ball fillet or a cylinder
            # written as B-spline) whose curvature radius matches also count; adjacent such patches count once
            spl_ok, spl_all = [], 0
            if recipe["yuzey"] in ("cylinder", "torus"):
                for r0 in C:
                    if r0["t"] not in TYPE_MAP["bspline"]:
                        continue
                    if recipe.get("bolge"):
                        c = (FB[r0["i"], :3] + FB[r0["i"], 3:]) / 2
                        if not _inbox(c[None], recipe["bolge"])[0]:
                            continue
                    spl_all += 1
                    if recipe.get("r_mm") is not None:
                        rr = K.spline_radius(g, r0["i"])
                        if rr is not None and abs(rr - recipe["r_mm"]) <= R_TOL_MM:
                            spl_ok.append(r0["i"])
            if spl_ok:
                ss = set(spl_ok)
                for comp in K.face_components(g, joinable=lambda a, b: a in ss and b in ss):
                    m = [i for i in comp if i in ss]
                    if m:
                        groups.append(m)
            return dict(deger=len(groups), birim="adet", yuzler=groups, bspline_kabul=len(spl_ok), bspline_bolgede=spl_all)
        return dict(deger=None, hata="bilinmeyen tip %s" % t)
    except Exception as e:
        return dict(deger=None, hata="%s: %s" % (type(e).__name__, e))


def _auto(body, p, tur, lim=None):
    if tur:
        return _feature(body, p, tur, lim)
    a = _feature(body, p, "duzlem", lim); b = _feature(body, p, "eksen", lim)
    if a is None:
        return b
    if b is None:
        return a
    return a if a["_dist"] <= b["_dist"] else b


def bolge_maske(P, recipe):
    if recipe.get("nokta") is not None and recipe.get("r_mm") is not None:
        return np.linalg.norm(P - np.asarray(recipe["nokta"], float), axis=1) <= recipe["r_mm"]
    if recipe.get("kutu") is not None:
        m = _inbox(P, recipe["kutu"])
        for h in recipe.get("haric", []) or []:
            m &= ~_inbox(P, h)
        return m
    return np.ones(len(P), bool)


def bolgesel_sapma(recipe, ornek_A, ornek_B):
    """Two-way max deviation inside the region. ornek_X = dict(pts, d) of the samples on the original (A) and rebuild (B)
    faces, each with its distance to the other model (olc_cekirdek.deviation()['_ab'/'_ba'])."""
    out = dict(birim="mm")
    best, where, n = -1.0, None, [0, 0]
    for k, o in enumerate((ornek_A, ornek_B)):
        m = bolge_maske(o["pts"], recipe); n[k] = int(m.sum())
        if m.any():
            j = np.argmax(np.where(m, o["d"], -1));
            if o["d"][j] > best:
                best, where = float(o["d"][j]), o["pts"][j].tolist()
    if n[0] == 0 and n[1] == 0:
        out.update(deger=None, bos=True, hata="bolge bos: orijinalde de yuzey yok (gizli liste noktasi)", n=n)
        return out
    if n[1] == 0:
        out.update(deger=None, hata="yeniden yapimda bolgede yuzey yok", n=n)
        return out
    out.update(deger=best, nerede=where, n=n)
    return out


def bolgesel_sapma_govde(recipe, govde_A, govde_B, etiket="C"):
    """Same, computing the two-way samples for the pair first (C-task use)."""
    D = K.deviation(govde_A, govde_B, etiket)
    return bolgesel_sapma(recipe, D["_ab"], D["_ba"])


MIN_REGION_PTS = 30   # fewer global samples than this inside a region -> dense local sampling


def bolgesel_sapma_yogun(recipe, govde_A, govde_B, n=400):
    """Dense local version: samples only the triangles inside the region (both bodies), exact distances."""
    import zlib
    rng = np.random.default_rng(zlib.crc32(repr(sorted(recipe.items())).encode()) & 0x7FFFFFFF)
    out = []
    for X, Y in ((govde_A, govde_B), (govde_B, govde_A)):
        if recipe.get("nokta") is not None and recipe.get("r_mm") is not None:
            c = np.asarray(recipe["nokta"], float); rb = np.concatenate([c - recipe["r_mm"], c + recipe["r_mm"]])
        elif recipe.get("kutu") is not None:
            rb = np.asarray(recipe["kutu"], float)
        else:
            rb = np.array(X.bbox)
        T3 = X.V[X.F]; lo, hi = T3.min(axis=1), T3.max(axis=1)
        m = np.where(np.all((lo <= rb[3:]) & (hi >= rb[:3]), axis=1))[0]   # triangles touching the region box
        if not len(m):
            out.append(dict(pts=np.zeros((0, 3)), d=np.zeros(0))); continue
        A = K.tri_areas(X.V, X.F[m]); n = max(n, 4 * len(m)); n = min(n, 20000)
        idx = m[rng.choice(len(m), n, p=A / A.sum())]
        r1, r2 = rng.random(n), rng.random(n); sq = np.sqrt(r1); F = X.F[idx]
        P = (1 - sq)[:, None] * X.V[F[:, 0]] + (sq * (1 - r2))[:, None] * X.V[F[:, 1]] + (sq * r2)[:, None] * X.V[F[:, 2]]
        keep = bolge_maske(P, recipe); P, idx = P[keep], idx[keep]
        if not len(P):
            out.append(dict(pts=np.zeros((0, 3)), d=np.zeros(0))); continue
        P = K.project_own(X, P, X.fid[idx])
        dk = Y.kd()[0].query(P)[0]
        d = K.exact_dist_bb(Y, P, dk + K.SEARCH_MARGIN_MM)[0]
        d = np.minimum(d, dk + K.MESH_DEFL_MM)
        out.append(dict(pts=P, d=d))
    r = bolgesel_sapma(recipe, out[0], out[1]); r["yogun"] = True
    return r
