"""olc.py: measurement + automatic sub-scores of RUBRIK.md task A, sections 1-5 (section 4 = proposals for the grader).

Usage:
  python olc.py <original.step> <rebuild.step> --gizli <hedefler/P##> --out <dir> [--teslim <teslim dir>]

Reads hedef.json (required), ozellikler.json and resim_olculeri.json (optional; missing -> that section is reported as
not measured) from --gizli. Writes <out>\\olcum.json (raw numbers, sub-scores, sources), <out>\\olcum.md (tables) and
<out>\\sapma_ornekleri.npz (deviation samples per body, for the grader's heat maps). No manual edits of the outputs.
Exit code 0 = done; 2 = failure (reason printed and written to <out>\\olcum_hata.txt).
All lengths mm. Deterministic (seeded sampling). Rubric curves and thresholds: the constants block below, nowhere else.
"""
import argparse, ctypes, json, math, os, sys, time, traceback
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.spatial import cKDTree
import olc_cekirdek as K
import tarifler as T

# =====================================================================  RUBRIC CONSTANTS (RUBRIK.md, task A)
S1 = dict(A=12.0, B=4.0, C=10.0, D=6.0, E=8.0)                     # §1 geometry, 40
IOU_CURVE = [(1 - 0.9995, 1.0), (1 - 0.999, 0.9), (1 - 0.995, 0.6), (1 - 0.98, 0.3), (1 - 0.95, 0.0)]   # x = 1 - IoU
P95_CURVE = [(0.005, 1.0), (0.02, 0.9), (0.05, 0.7), (0.127, 0.4), (0.5, 0.0)]                          # mm
MAX_CURVE = [(0.01, 1.0), (0.05, 0.8), (0.127, 0.5), (0.5, 0.2), (2.5, 0.0)]                            # mm
TOL_DV_PCT, TOL_DV_HW_PCT = 0.5, 2.0          # E: volume (hardware 2 %)
TOL_DA_PCT, TOL_DA_HW_PCT = 0.5, 2.0          # E: area
TOL_DCOM_MM, TOL_DBBOX_MM = 0.5, 0.13         # E: CoM, bbox
S2 = dict(govde=6.0, cesit=2.0, teslim=2.0)   # §2 completeness, 10
PEN_EXTRA, PEN_CESIT, PEN_TESLIM = 0.5, 0.5, 0.5
TESLIM_KALEMLER = ["final.step", "native kaynak", "yeniden_kur.md", "parametreler.md", "build_log.md"]
NATIVE_EXT = {".prt", ".sldprt", ".sldasm", ".slddrw", ".py", ".fcstd", ".f3d", ".f3z", ".scad", ".ipt", ".iam", ".catpart",
              ".catproduct", ".par", ".asm", ".x_t", ".ts", ".js", ".json", ".txt", ".cmd", ".scs"}
S3 = dict(poz=4.0, montaj=3.0, girisim=3.0)   # §3 assembly, 10
POSE_COM_MM = (0.025, 0.5)                    # full .. zero, linear
POSE_ANG_DEG = (0.01, 0.5)
GLOB_V_PCT, GLOB_A_PCT, GLOB_COM_MM, GLOB_BBOX_MM, GLOB_EACH = 0.1, 0.1, 0.13, 0.13, 0.75
INTERF_MIN_MM3, PEN_INTERF, INTERF_VOL_PCT, PEN_INTERF_VOL = 8.0, 1.0, 5.0, 0.5
S4 = 20.0                                     # §4 features
REGION_TOL_MM = 0.05                          # 'tam' needs region deviation <= this (PAKET_SEMASI)
HAKEM_PROVISIONAL = 0.0                       # 'hakem' item (kernel-dependent count): provisional score until the grader decides
PRESENT_MM = 1.0                              # olc.py proposal: region deviation above this = feature not there (kayip)
S5 = 5.0                                      # §5 drawing
SINGLE_BODY_S1_SCALE = 50.0 / 40.0            # §3 10 points moved to §1 proportionally for single-body parts
# measurement method constants
MESH_VS_OCC_PCT = 0.5                         # GProp vs mesh volume disagreement -> mesh values
BOOL_FUZZY = (1e-4, 2e-3)
BOOL_SHELL_AGREE = 0.002                      # boolean IoU accepted only if within this of the thin-shell estimate
BOOL_TIMEOUT_S = 120                          # + memory cap K.BOOL_MAX_GB (child killed -> thin-shell estimate)
CONGRUENT_PCT = dict(v=0.2, a=0.2, eig=0.5)   # §2: two rebuild bodies are the same part
MIN_FREE_GB = 4.0
IN = 25.4


# =====================================================================  helpers
def interp(x, pts):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return 0.0
    if x <= pts[0][0]:
        return pts[0][1]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return pts[-1][1]


def lin(x, full, zero):
    return 1.0 if x <= full else (0.0 if x >= zero else 1 - (x - full) / (zero - full))


class _MS(ctypes.Structure):
    _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong), ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong), ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong), ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]


def free_gb():
    try:
        m = _MS(); m.dwLength = ctypes.sizeof(_MS); ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
        return m.ullAvailPhys / 2 ** 30
    except Exception:
        return None


def peak_gb():
    try:
        import psutil
        return psutil.Process().memory_info().peak_wset / 2 ** 30
    except Exception:
        return None


def wait_memory(log):
    t0 = time.time()
    while True:
        f = free_gb()
        if f is None or f >= MIN_FREE_GB:
            return f
        if time.time() - t0 > 1800:
            raise RuntimeError("30 dk bekledi, bos bellek %.1f GB < %.1f GB" % (f, MIN_FREE_GB))
        log("bos bellek %.1f GB < %.1f GB, bekleniyor" % (f, MIN_FREE_GB)); time.sleep(30)


def jdump(o, path):
    def d(x):
        if isinstance(x, (np.integer,)):
            return int(x)
        if isinstance(x, (np.floating,)):
            return float(x)
        if isinstance(x, np.ndarray):
            return x.tolist()
        if isinstance(x, (np.bool_,)):
            return bool(x)
        return str(x)
    with open(path, "w", encoding="utf8") as fh:
        json.dump(o, fh, indent=1, ensure_ascii=False, default=d)


def eff_props(b):
    """OCC GProp unless it disagrees with the fine-mesh integral by > MESH_VS_OCC_PCT (then mesh)."""
    dv = abs(b.occ["vol"] - b.mesh["vol"]) / abs(b.mesh["vol"]) * 100
    return dv > MESH_VS_OCC_PCT, dv


def props(b, use_mesh):
    p = b.mesh if use_mesh else b.occ
    return dict(vol=p["vol"], area=p["area"], com=list(p["com"]), inertia=p["inertia"], src="mesh" if use_mesh else "OCC")


def cost_matrix(PA, PB):
    C = np.zeros((len(PA), len(PB)))
    for i, a in enumerate(PA):
        for j, b in enumerate(PB):
            C[i, j] = np.linalg.norm(np.subtract(a["com"], b["com"])) + np.abs(np.subtract(a["bbox"], b["bbox"])).sum() + abs(a["vol"] - b["vol"]) ** (1 / 3)
    return C


def bbox_overlap(a, b, slack=0.0):
    return all(a[k] <= b[k + 3] + slack and b[k] <= a[k + 3] + slack for k in range(3))


def principal(I):
    e, v = np.linalg.eigh(np.array(I))
    distinct = [bool(min(abs(e[i] - e[j]) for j in range(3) if j != i) / abs(e).mean() > 0.01) for i in range(3)]
    return e, v, distinct


def icp_angle(src, dst, iters=40):
    """Point-to-point ICP src -> dst from identity; rotation angle (deg) and translation (mm)."""
    tree = cKDTree(dst); R = np.eye(3); t = np.zeros(3); S = src.copy()
    for _ in range(iters):
        _, j = tree.query(S); D = dst[j]
        ms, md = S.mean(0), D.mean(0)
        H = (S - ms).T @ (D - md); U, _, Vt = np.linalg.svd(H)
        Ri = Vt.T @ U.T
        if np.linalg.det(Ri) < 0:
            Vt[-1] *= -1; Ri = Vt.T @ U.T
        ti = md - Ri @ ms; S = (Ri @ S.T).T + ti; R = Ri @ R; t = Ri @ t + ti
    ang = math.degrees(math.acos(max(-1, min(1, (np.trace(R) - 1) / 2))))
    return ang, float(np.linalg.norm(t))


# =====================================================================  main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("orijinal"); ap.add_argument("yeniden")
    ap.add_argument("--gizli", required=True); ap.add_argument("--out", required=True); ap.add_argument("--teslim")
    ap.add_argument("--_ic", action="store_true", help=argparse.SUPPRESS); ap.add_argument("--_atla", default="", help=argparse.SUPPRESS)
    a = ap.parse_args()
    ATLA = set(x for x in a._atla.split("|") if x)
    ILER = os.path.join(a.out, "_ilerleme.json")

    def adim(key):
        """Progress marker: the supervisor reads it when the child dies inside OCC and skips this step next time."""
        with open(ILER, "w", encoding="utf8") as fh:
            json.dump(dict(adim=key, zaman=time.time()), fh)
        if os.environ.get("OLC_TEST_COKME") == key:   # test hook: simulate a hard OCC crash in this step
            os._exit(9)
    os.makedirs(a.out, exist_ok=True)
    t_start = time.time()
    LOG = []

    def log(*m):
        s = " ".join(str(x) for x in m); LOG.append("%7.1f s  %s" % (time.time() - t_start, s)); print(LOG[-1], flush=True)

    for p in (a.orijinal, a.yeniden, os.path.join(a.gizli, "hedef.json")):
        if not os.path.isfile(p):
            raise RuntimeError("dosya yok: %s" % p)
    H = json.load(open(os.path.join(a.gizli, "hedef.json"), encoding="utf8"))
    OZ = json.load(open(os.path.join(a.gizli, "ozellikler.json"), encoding="utf8")) if os.path.isfile(os.path.join(a.gizli, "ozellikler.json")) else None
    RS = json.load(open(os.path.join(a.gizli, "resim_olculeri.json"), encoding="utf8")) if os.path.isfile(os.path.join(a.gizli, "resim_olculeri.json")) else None
    notes = []

    log("bos bellek GB", wait_memory(log))
    SA = K.load_step(a.orijinal); yukA = dict(K.LAST_LOAD)
    SB = K.load_step(a.yeniden); yukB = dict(K.LAST_LOAD)
    for side, y in (("orijinal", yukA), ("yeniden yapim", yukB)):
        if y["bos_atilan"] or y["serbest_kabuk_yok_sayilan"] or y.get("bos_kabuk_atilan"):
            notes.append("%s: %d bos (sifir hacim / alan) govde ve govde icinde %d bos kabuk atildi, %d serbest kabuk yok sayildi" % (
                side, y["bos_atilan"], y.get("bos_kabuk_atilan", 0), y["serbest_kabuk_yok_sayilan"]))
    log("govde: orijinal", len(SA), "yeniden", len(SB))
    if len(SA) != len(H["govdeler"]):
        raise RuntimeError("orijinalde %d govde, hedef.json %d govde: gizli liste bu STEP'e ait degil" % (len(SA), len(H["govdeler"])))
    BA = [K.Body(s, "A%02d" % i) for i, s in enumerate(SA)]
    BB = [K.Body(s, "B%02d" % i) for i, s in enumerate(SB)]
    log("ince mesh tamam; bos bellek GB %.1f" % (free_gb() or -1))

    # ---- names of original bodies from hedef.json (Hungarian on CoM + bbox + volume)
    HP = [dict(com=g["com_mm"], bbox=g["bbox_mm"], vol=g["hacim_mm3"]) for g in H["govdeler"]]
    flagsA = [eff_props(b) for b in BA]; flagsB = [eff_props(b) for b in BB]
    PA0 = [dict(com=(b.mesh if f[0] else b.occ)["com"], bbox=b.bbox, vol=(b.mesh if f[0] else b.occ)["vol"]) for b, f in zip(BA, flagsA)]
    PB0 = [dict(com=(b.mesh if f[0] else b.occ)["com"], bbox=b.bbox, vol=(b.mesh if f[0] else b.occ)["vol"]) for b, f in zip(BB, flagsB)]
    C = cost_matrix(HP, PA0); hi, ai = linear_sum_assignment(C)
    nameA = {}
    for h, i in zip(hi, ai):
        nameA[int(i)] = H["govdeler"][h]["ad"]; BA[i].name = H["govdeler"][h]["ad"]
    hed = {g["ad"]: g for g in H["govdeler"]}
    worst_name_cost = float(max(C[h, i] for h, i in zip(hi, ai)))
    if worst_name_cost > 5.0:
        notes.append("hedef.json -> orijinal adlandirmada en kotu maliyet %.3f mm (beklenen ~0)" % worst_name_cost)

    # ---- match original <-> rebuild
    C2 = cost_matrix(PA0, PB0); ri, rj = linear_sum_assignment(C2)
    match = {}
    for i, j in zip(ri, rj):
        va, vb = PA0[i]["vol"], PB0[j]["vol"]
        if bbox_overlap(PA0[i]["bbox"], PB0[j]["bbox"], 1.0) and 0.5 <= vb / va <= 2.0:
            match[int(i)] = int(j)
    nameB = {j: nameA[i] for i, j in match.items()}
    extra = [j for j in range(len(BB)) if j not in nameB]
    for k, j in enumerate(extra):
        nameB[j] = "FAZLA-%d" % (k + 1)
    for j, n in nameB.items():
        BB[j].name = n
    log("eslesen", len(match), "/", len(BA), "fazla", len(extra))

    for side, Bs, fl in (("orijinal", BA, flagsA), ("yeniden yapim", BB, flagsB)):
        for b, f in zip(Bs, fl):
            if f[0]:
                notes.append("%s %s: OCC GProp hacmi ince mesh integralinden %%%.3f farkli -> bu ciftte hacim / alan / CoM / atalet mesh'ten" % (side, b.name, f[1]))
    # ---- per pair measures
    W = K.BoolWorker(BOOL_TIMEOUT_S)
    rows = []; samples = {}
    for i in range(len(BA)):
        n = nameA[i]; A = BA[i]; g = hed[n]; hw = g.get("tur") == "donanim"
        r = dict(ad=n, tur=g.get("tur", "parca"), eslesti=i in match)
        if i not in match:
            r.update(sebep="eslesen yeniden yapim govdesi yok"); rows.append(r); continue
        key = "govde:" + n
        if key in ATLA:
            r.update(olcum_coktu=True, sebep="OCC cokmesi: bu govdenin olcumu atlandi (supervizor)"); rows.append(r); notes.append("%s: olcum cokmesi, govde puansiz; puanlayici tekrar kossun" % n); continue
        adim(key)
        try:
            B = BB[match[i]]
            um = flagsA[i][0] or flagsB[match[i]][0]
            pa, pb = props(A, um), props(B, um)
            t0 = time.time()
            wait_memory(log)
            D = K.deviation(A, B, n)
            A.release(); B.release()
            samples[n] = D
            # IoU
            shell = 0.5 * (D["mean_A"] * pa["area"] + D["mean_B"] * pb["area"])
            shell_iou = max(0.0, 1 - shell / (0.5 * (pa["vol"] + pb["vol"]) + shell / 2))
            iou, src, btry = None, None, []
            if not um:
                for fz in BOOL_FUZZY:
                    res = W.run(("A", i), A.solid, ("B", match[i]), B.solid, fz, cut=True)
                    btry.append(dict(fuzzy=fz, **res))
                    cv, xv = res.get("common"), res.get("cut")
                    if cv is None or xv is None or not res.get("common_valid"):
                        continue
                    Va, Vb = A.occ["vol"], B.occ["vol"]
                    if not (0 <= cv <= min(Va, Vb) * (1 + 1e-5)) or abs(Va - cv - xv) > 1e-4 * Va + 1e-3:
                        continue
                    bi = min(1.0, cv / (Va + Vb - cv))
                    if abs(bi - shell_iou) > BOOL_SHELL_AGREE:
                        btry[-1]["red"] = "kabuk tahmininden %.4f farkli" % (bi - shell_iou); continue
                    iou, src = bi, "OCC boolean (fuzzy %g)" % fz; break
            if iou is None:
                iou, src = shell_iou, "ince kabuk tahmini (kesin B-rep sapmasi)" + (" [mesh hacim]" if um else "")
            dV = 100 * (pb["vol"] / pa["vol"] - 1); dA = 100 * (pb["area"] / pa["area"] - 1)
            dC = float(np.linalg.norm(np.subtract(pb["com"], pa["com"])))
            dB = float(np.abs(np.subtract(B.bbox, A.bbox)).max())
            checks = dict(dV=abs(dV) <= (TOL_DV_HW_PCT if hw else TOL_DV_PCT), dA=abs(dA) <= (TOL_DA_HW_PCT if hw else TOL_DA_PCT),
                          dCoM=dC <= TOL_DCOM_MM, dBbox=dB <= TOL_DBBOX_MM)
            ea, va, da = principal(pa["inertia"]); eb, vb, _ = principal(pb["inertia"])
            angs = [math.degrees(math.acos(min(1, abs(float(va[:, k] @ vb[:, k]))))) for k in range(3) if da[k]]
            if angs:
                ang, asrc = max(angs), "asal eksenler"
            else:
                ang, _ = icp_angle(D["_ba"]["pts"][::max(1, len(D["_ba"]["pts"]) // 20000)], D["_ab"]["pts"]); asrc = "ICP"
            r.update(yeniden_index=match[i], yuz=[A.nfaces, B.nfaces], hacim_kaynak=pa["src"],
                     occ_mesh_fark_pct=[flagsA[i][1], flagsB[match[i]][1]],
                     V_orj=pa["vol"], V_yen=pb["vol"], dV_pct=dV, A_orj=pa["area"], A_yen=pb["area"], dA_pct=dA,
                     com_orj=pa["com"], com_yen=pb["com"], dCoM_mm=dC, bbox_orj=A.bbox, bbox_yen=B.bbox, dBbox_mm=dB,
                     kontroller=checks, iou=iou, iou_kaynak=src, kabuk_iou=shell_iou, boolean_denemeleri=btry,
                     sapma=dict((k, v) for k, v in D.items() if not k.startswith("_")), yonelim_deg=ang, yonelim_kaynak=asrc,
                     s_iou=interp(1 - iou, IOU_CURVE), s_p95=interp(D["p95"], P95_CURVE), s_max=interp(D["max"], MAX_CURVE),
                     s_tol=sum(checks.values()) / 4.0, s_poz=min(lin(dC, *POSE_COM_MM), lin(ang, *POSE_ANG_DEG)), sure_s=time.time() - t0)
            rows.append(r)
            log("%-6s IoU %.6f [%s] p95 %.5f max %.4f dV %+.3f%% dC %.4f ang %.4f (%.0f s)" % (n, iou, src[:10], D["p95"], D["max"], dV, dC, ang, time.time() - t0))
        except Exception as e:
            r.update(olcum_coktu=True, sebep="%s: %s" % (type(e).__name__, e)); rows.append(r)
            notes.append("%s: olcum hatasi (%s), govde puansiz" % (n, e)); log("HATA govde", n, e)

    # ---- §1
    single = len(BA) == 1
    scale = SINGLE_BODY_S1_SCALE if single else 1.0
    N = len(rows)
    gs = lambda k: [r.get(k, 0.0) if r["eslesti"] else 0.0 for r in rows]
    vol_w = np.array([hed[r["ad"]]["hacim_mm3"] for r in rows])
    s1 = dict(A=S1["A"] * np.mean(gs("s_iou")), B=S1["B"] * float((np.array(gs("s_iou")) * vol_w).sum() / vol_w.sum()),
              C=S1["C"] * np.mean(gs("s_p95")), D=S1["D"] * np.mean(gs("s_max")), E=S1["E"] * np.mean(gs("s_tol")))
    s1 = {k: v * scale for k, v in s1.items()}; s1["toplam"] = sum(s1.values()); s1["azami"] = 40 * scale

    # ---- §2
    m_ok = len(match)
    s2_govde = max(0.0, S2["govde"] * m_ok / len(BA) - PEN_EXTRA * len(extra))
    groups = {}
    for g in H["govdeler"]:
        groups.setdefault(g.get("esdeger_grubu", g["ad"]), []).append(g["ad"])
    # rebuild congruence clusters
    PBe = [props(b, flagsB[j][0]) for j, b in enumerate(BB)]
    eigB = [np.sort(np.linalg.eigvalsh(np.array(p["inertia"]))) for p in PBe]
    par = list(range(len(BB)))

    def fnd(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for x in range(len(BB)):
        for y in range(x + 1, len(BB)):
            px, py = PBe[x], PBe[y]
            if abs(px["vol"] / py["vol"] - 1) * 100 <= CONGRUENT_PCT["v"] and abs(px["area"] / py["area"] - 1) * 100 <= CONGRUENT_PCT["a"] \
                    and np.all(np.abs(eigB[x] / eigB[y] - 1) * 100 <= CONGRUENT_PCT["eig"]):
                par[fnd(x)] = fnd(y)
    cl = {}
    for j in range(len(BB)):
        cl.setdefault(fnd(j), set()).add(j)
    inv = {v: k for k, v in nameB.items()}
    cesit = []
    for gname, members in sorted(groups.items()):
        js = [inv[m] for m in members if m in inv]
        ok = len(js) == len(members) and len({fnd(j) for j in js}) == 1 and cl[fnd(js[0])] == set(js)
        cesit.append(dict(grup=gname, adet=len(members), eslesen=len(js), dogru=bool(ok),
                          kume=sorted(nameB[x] for x in cl[fnd(js[0])]) if js else []))
    n_wrong = sum(1 for c in cesit if not c["dogru"])
    s2_cesit = max(0.0, S2["cesit"] - PEN_CESIT * n_wrong)
    teslim = None
    if a.teslim:
        tl = {}
        files = []
        for root, _, fs in os.walk(a.teslim):
            files += [os.path.join(root, f) for f in fs]
        low = [os.path.basename(f).lower() for f in files]
        tl["final.step"] = "final.step" in low or "final.stp" in low
        tl["native kaynak"] = any(os.path.splitext(f)[1] in NATIVE_EXT for f in low)
        for k in ("yeniden_kur.md", "parametreler.md", "build_log.md"):
            tl[k] = k in low
        teslim = tl
        s2_teslim = max(0.0, S2["teslim"] - PEN_TESLIM * sum(1 for v in tl.values() if not v))
    else:
        s2_teslim = S2["teslim"]
        notes.append("--teslim verilmedi: teslimat kalemi 2/2 varsayildi, puanlayici dogrular")
    s2 = dict(govde=s2_govde, cesit=s2_cesit, teslim=s2_teslim, toplam=s2_govde + s2_cesit + s2_teslim,
              eslesen=m_ok, orijinal=len(BA), fazla=len(extra), cesit_tablo=cesit, teslim_tablo=teslim,
              teslim_kontrol="yapildi" if a.teslim else "yapilmadi (varsayilan tam)")

    # ---- §3
    pose = S3["poz"] * np.mean(gs("s_poz"))
    PAe = [props(b, flagsA[i][0]) for i, b in enumerate(BA)]

    def glob(P, Bs):
        v = sum(p["vol"] for p in P); ar = sum(p["area"] for p in P)
        c = sum(np.array(p["com"]) * p["vol"] for p in P) / v
        bb = [min(b.bbox[k] for b in Bs) for k in range(3)] + [max(b.bbox[k] for b in Bs) for k in range(3, 6)]
        return dict(hacim=v, alan=ar, com=c.tolist(), bbox=bb)
    GA, GB = glob(PAe, BA), glob(PBe, BB)
    gv = abs(GB["hacim"] / GA["hacim"] - 1) * 100; ga = abs(GB["alan"] / GA["alan"] - 1) * 100
    gc = float(np.linalg.norm(np.subtract(GB["com"], GA["com"]))); gb = float(np.abs(np.subtract(GB["bbox"], GA["bbox"])).max())
    gchk = dict(hacim=gv <= GLOB_V_PCT, alan=ga <= GLOB_A_PCT, com=gc <= GLOB_COM_MM, bbox=gb <= GLOB_BBOX_MM)
    s3_glob = GLOB_EACH * sum(gchk.values())
    hm = H.get("montaj") or {}
    if hm:
        notes.append("hedef.json montaj capraz kontrol: orijinal olculen hacim farki %.4f%%, CoM %.4f mm" % (
            abs(GA["hacim"] / hm["hacim_mm3"] - 1) * 100, float(np.linalg.norm(np.subtract(GA["com"], hm["com_mm"])))))

    def interferences(Bs, names, side):
        out = {}; unk = []
        for x in range(len(Bs)):
            for y in range(x + 1, len(Bs)):
                if not bbox_overlap(Bs[x].bbox, Bs[y].bbox, -1e-6):
                    continue
                cv = None
                for fz in BOOL_FUZZY:
                    res = W.run((side, x), Bs[x].solid, (side, y), Bs[y].solid, fz)
                    c = res.get("common")
                    if c is not None and -1e-6 <= c <= min(Bs[x].occ["vol"], Bs[y].occ["vol"]) * (1 + 1e-6):
                        cv = c; break
                key = tuple(sorted((names[x], names[y])))
                if cv is None:
                    unk.append(list(key))
                elif cv > INTERF_MIN_MM3:
                    out[key] = cv
        return out, unk
    if not single:
        wait_memory(log)
        IA = IB = None
        if "girisim" not in ATLA:
            adim("girisim")
            try:
                IA, uA = interferences(BA, nameA, "A"); IB, uB = interferences(BB, nameB, "B")
            except Exception as e:
                notes.append("girisim olcumu hatasi: %s" % e)
        if IA is None:
            IA, IB, uA, uB = {}, {}, ["olculemedi"], ["olculemedi"]
            notes.append("girisim olculemedi (cokme / hata): girisim puani 0, puanlayici tekrar kossun")
        log("girisim: orijinal", len(IA), "yeniden", len(IB), "bilinmeyen", len(uA), len(uB))
        only = sorted(set(IA) ^ set(IB)); both = sorted(set(IA) & set(IB))
        voldiff = [k for k in both if abs(IB[k] / IA[k] - 1) * 100 > INTERF_VOL_PCT]
        s3_int = 0.0 if uA == ["olculemedi"] else max(0.0, S3["girisim"] - PEN_INTERF * len(only) - PEN_INTERF_VOL * len(voldiff))
        hg = {tuple(sorted((g["a"], g["b"]))) for g in H.get("girisimler", [])}
        if hg != set(IA):
            notes.append("hedef.json girisimleri (%s) olculen orijinal girisimlerinden (%s) farkli" % (sorted(hg), sorted(IA)))
        s3 = dict(poz=pose, montaj=s3_glob, girisim=s3_int, toplam=pose + s3_glob + s3_int, azami=10.0,
                  montaj_olcum=dict(orijinal=GA, yeniden=GB, dV_pct=gv, dA_pct=ga, dCoM_mm=gc, dBbox_mm=gb, kontroller=gchk),
                  girisim_orijinal=[dict(a=k[0], b=k[1], hacim_mm3=v) for k, v in sorted(IA.items())],
                  girisim_yeniden=[dict(a=k[0], b=k[1], hacim_mm3=v) for k, v in sorted(IB.items())],
                  yalniz_birinde=[list(k) for k in only], hacim_farki_buyuk=[list(k) for k in voldiff], olculemeyen=dict(orijinal=uA, yeniden=uB))
    else:
        s3 = dict(poz=0.0, montaj=0.0, girisim=0.0, toplam=0.0, azami=0.0, not_="tek govde: §3 puani §1'e dagitildi",
                  bilgi=dict(poz=pose, montaj=s3_glob, montaj_olcum=dict(dV_pct=gv, dA_pct=ga, dCoM_mm=gc, dBbox_mm=gb, kontroller=gchk)))

    # ---- §4
    govA = {nameA[i]: BA[i] for i in range(len(BA))}
    govB = {nameB[j]: BB[j] for j in range(len(BB)) if not nameB[j].startswith("FAZLA")}
    s4 = None
    if OZ:
        items = []; tot = 0.0
        for it in OZ["items"]:
            key = "ozellik:%s" % it.get("id")
            if key in ATLA:
                items.append(dict(id=it.get("id"), govde=it.get("govde"), etiket=it.get("etiket"), tur=it.get("tur"), oneri="olculemedi", puan=0.0,
                                  hata="OCC cokmesi (supervizor atladi)")); continue
            adim(key)
            try:
                rec = ozellik_kalemi(it, govA, govB, BA, BB, samples)
            except Exception as e:
                rec = dict(id=it.get("id"), govde=it.get("govde"), etiket=it.get("etiket"), tur=it.get("tur"), oneri="olculemedi", puan=0.0, hata=str(e))
            items.append(rec); tot += rec["puan"]
        s4 = dict(kalemler=items, toplanan=tot, toplam=len(items), puan=S4 * tot / max(1, len(items)),
                  not_="oneri; uydurma ozellik (-0.5) ve son karar puanlayicida")

    # ---- §5
    s5 = None
    if RS:
        out = []; n_c = 0; n_p = 0
        for ri_, row in enumerate(RS["rows"]):
            o = row.get("olcum"); rec = dict(dim=row["dim"], nom=row["nom"], birim=row.get("birim", "mm"), tol=row["tol"], modelde_var=row.get("modelde_var", True))
            key = "resim:%d" % ri_
            if o and key in ATLA:
                rec.update(sayildi=True, gecti=False, olcum_hata="OCC cokmesi (supervizor atladi)"); n_c += 1; out.append(rec); continue
            if o:
                adim(key)
                try:
                    ma = T.olc(o, govA, BA); mb = T.olc(o, govB, BB, ref=ma)
                except Exception as e:
                    mb = ma = dict(deger=None, hata=str(e))
                f = (1 / IN) if (rec["birim"] == "in" and mb.get("birim", T.BIRIM.get(o["tip"])) == "mm") else 1.0
                vb = None if mb.get("deger") is None else mb["deger"] * f
                va = None if ma.get("deger") is None else ma["deger"] * f
                ok = vb is not None and abs(vb - row["nom"]) <= row["tol"] + 1e-9
                rec.update(yeniden=vb, orijinal=va, hata=vb - row["nom"] if vb is not None else None, gecti=bool(ok), olcum_hata=mb.get("hata"),
                           sayildi=True)
                n_c += 1; n_p += ok
            else:
                rec.update(sayildi=False, gecti=None, not_="modelde karsiligi yok / olculemez; sayilmadi")
            out.append(rec)
        s5 = dict(satirlar=out, sayilan=n_c, gecen=n_p, puan=S5 * n_p / n_c if n_c else None)
        if not n_c:
            notes.append("resim_olculeri.json'da olculebilir tarif yok: §5 olculmedi (puanlayici elle)")
        bos = [r["dim"] for r in out if r["modelde_var"] and not r["sayildi"]]
        if bos:
            notes.append("modelde_var=true ama olcum tarifi yok: %s (gizli liste eksigi)" % bos)
    W.close()

    total = s1["toplam"] + s2["toplam"] + s3["toplam"] + (s4["puan"] if s4 else 0) + ((s5 or {}).get("puan") or 0)
    res = dict(surum="olc.py 1.0", girdi=dict(orijinal=a.orijinal, yeniden=a.yeniden, gizli=a.gizli, teslim=a.teslim),
               tek_govde=single, yukleme=dict(orijinal=yukA, yeniden=yukB), alt_puanlar=dict(geometri=s1, tamlik=s2, montaj=s3, ozellik=s4["puan"] if s4 else None,
                                                   resim=(s5 or {}).get("puan"), toplam_1_5=total, azami_1_5=85.0),
               govdeler=rows, tamlik=s2, montaj=s3, ozellik=s4, resim=s5, notlar=notes,
               yontem=dict(mesh_defl_mm=K.MESH_DEFL_MM, mesh_ang_rad=K.MESH_ANG_RAD, ornek_yogunluk_mm2=K.SAMPLE_DENS_PER_MM2,
                           sapma="ornek kendi yuzeyine kesin izdusum; karsi govde: kesin B-rep (yuz izdusumu / BRepExtrema), d=min(kesin, mesh+kiris)",
                           iou="OCC boolean (Common+Cut tutarli, kabuk tahminine %g icinde) yoksa ince kabuk" % BOOL_SHELL_AGREE,
                           hacim="OCC GProp; mesh integrali ile fark > %%%g ise mesh (cift icin iki taraf)" % MESH_VS_OCC_PCT),
               sure_s=time.time() - t_start, tepe_bellek_gb=peak_gb(), boolean_is=W.n, boolean_zaman_asimi=W.timeouts, boolean_oldurulen=W.killed, boolean_tepe_bellek_gb=W.peak, log=LOG)
    jdump(res, os.path.join(a.out, "olcum.json"))
    np.savez_compressed(os.path.join(a.out, "sapma_ornekleri.npz"), **{
        "%s__%s" % (n, s): np.column_stack([D["_ab" if s == "orj" else "_ba"]["pts"], D["_ab" if s == "orj" else "_ba"]["d"]])
        for n, D in samples.items() for s in ("orj", "yen")})
    write_md(res, os.path.join(a.out, "olcum.md"))
    log("TOPLAM §1-§5 %.2f / 85  (geometri %.2f, tamlik %.2f, montaj %.2f, ozellik %s, resim %s)" % (
        total, s1["toplam"], s2["toplam"], s3["toplam"], "%.2f" % s4["puan"] if s4 else "-", "%.2f" % s5["puan"] if (s5 and s5["puan"] is not None) else "-"))


def ozellik_kalemi(it, govA, govB, BA, BB, samples):
    """One ozellikler.json item -> record with measured value, region deviation and the proposal."""
    mb = ma = {}
    o = it.get("olcum"); rec = dict(id=it.get("id"), govde=it.get("govde"), etiket=it.get("etiket"), tur=it.get("tur"))
    vb = va = None; numok = True; cnt = False
    if o and o["tip"] == "bolgesel_sapma":   # region deviation used as the measurement itself (nom = 0)
        gn = o.get("govde", it.get("govde"))
        if gn in samples:
            ma = T.bolgesel_sapma(o, samples[gn]["_ab"], samples[gn]["_ba"])
            if sum(ma.get("n") or [0, 0]) < T.MIN_REGION_PTS and gn in govA and gn in govB:
                ma = T.bolgesel_sapma_yogun(o, govA[gn], govB[gn])
        else:
            ma = dict(deger=None, hata="govde eslesmedi")
        mb = ma; vb = ma.get("deger"); va = 0.0
        tol = max(it.get("tol") or 0.0, REGION_TOL_MM)
        numok = vb is not None and vb <= it.get("nom", 0.0) + tol
        rec.update(olcum_tip=o["tip"], nom=it.get("nom", 0.0), tol=tol, yeniden=vb, orijinal=va, hata=ma.get("hata"), bspline=None)
        if not it.get("bolge"):
            rec.update(bolge_sapma_mm=vb, bolge_n=ma.get("n"), bolge_nerede=ma.get("nerede"))
    elif o:
        ma = T.olc(o, govA, BA); mb = T.olc(o, govB, BB, ref=ma); vb, va = mb.get("deger"), ma.get("deger")
        cnt = o["tip"] == "sayi"
        tol = it.get("tol") or (0 if cnt else (T.ANG_TOL_DEG if o["tip"] == "aci" else T.LEN_TOL_MM))
        numok = vb is not None and abs(vb - it["nom"]) <= tol + 1e-9
        rec.update(olcum_tip=o["tip"], nom=it["nom"], tol=tol, yeniden=vb, orijinal=va, hata=mb.get("hata"),
                   bspline=[mb.get("bspline_kabul"), mb.get("bspline_bolgede")] if cnt else None)
    bo = it.get("bolge"); reg = None
    if bo:
        gn = bo.get("govde", it.get("govde"))
        if gn in samples:
            reg = T.bolgesel_sapma(bo, samples[gn]["_ab"], samples[gn]["_ba"])
            if sum(reg.get("n") or [0, 0]) < T.MIN_REGION_PTS and gn in govA and gn in govB:
                reg = T.bolgesel_sapma_yogun(bo, govA[gn], govB[gn])   # region too small for the global samples
        else:
            reg = dict(deger=None, hata="govde eslesmedi")
        rec.update(bolge_sapma_mm=reg.get("deger"), bolge_n=reg.get("n"), bolge_nerede=reg.get("nerede"), bolge_hata=reg.get("hata"))
        if reg.get("bos"):
            reg = None   # empty region on both models: shape check not possible, item judged by its number only
    rd = None if reg is None else reg.get("deger")
    if (it.get("govde") not in govB and it.get("govde") != T.MONTAJ) or (o and vb is None) or (reg is not None and rd is None):
        st = "kayip"
    elif cnt and not numok:
        # count wrong but free-form faces sit in the region: kernel-dependent count -> grader decides
        st = "hakem" if (mb.get("bspline_bolgede", 0) > 0 or ma.get("bspline_bolgede", 0) > 0) else "kayip"
    elif numok and (rd is None or rd <= REGION_TOL_MM):
        st = "tam"
    elif not cnt and rd is not None and rd > PRESENT_MM:
        st = "kayip"
    else:
        st = "yakin"
    sc = {"tam": 1.0, "yakin": 0.5, "kayip": 0.0, "hakem": HAKEM_PROVISIONAL}[st]
    rec.update(oneri=st, puan=sc)
    return rec


def f(x, p=4):
    if x is None:
        return "-"
    if isinstance(x, bool):
        return "evet" if x else "HAYIR"
    if isinstance(x, (int, np.integer)):
        return str(x)
    return ("%." + str(p) + "f") % x


def write_md(R, path):
    P = R["alt_puanlar"]; s1 = P["geometri"]; L = []
    L += ["# olc.py ölçümü", "", "- Orijinal: `%s`" % R["girdi"]["orijinal"], "- Yeniden yapım: `%s`" % R["girdi"]["yeniden"],
          "- Gizli liste: `%s`" % R["girdi"]["gizli"], "- Süre %.0f s, tepe bellek %s GB, boolean iş %d (zaman aşımı %d)" % (
              R["sure_s"], f(R["tepe_bellek_gb"], 2), R["boolean_is"], R["boolean_zaman_asimi"]), ""]
    L += ["## Alt puanlar (§1-§5)", "", "| Kategori | Puan | Azami | Ayrıntı |", "|---|---|---|---|",
          "| 1 Geometri | %.2f | %.0f | IoU %.2f + %.2f, P95 %.2f, maks %.2f, tolerans %.2f |" % (s1["toplam"], s1["azami"], s1["A"], s1["B"], s1["C"], s1["D"], s1["E"]),
          "| 2 Tamlık | %.2f | 10 | gövde %.2f, çeşit %.2f, teslimat %.2f (%s) |" % (P["tamlik"]["toplam"], P["tamlik"]["govde"], P["tamlik"]["cesit"], P["tamlik"]["teslim"], P["tamlik"]["teslim_kontrol"]),
          "| 3 Montaj | %.2f | %.0f | poz %.2f, montaj %.2f, girişim %.2f |" % (P["montaj"]["toplam"], P["montaj"]["azami"], P["montaj"]["poz"], P["montaj"]["montaj"], P["montaj"]["girisim"]),
          "| 4 Özellik (öneri) | %s | 20 | %s |" % (f(P["ozellik"], 2), "%.1f / %d kalem" % (R["ozellik"]["toplanan"], R["ozellik"]["toplam"]) if R["ozellik"] else "liste yok"),
          "| 5 Resim | %s | 5 | %s |" % (f(P["resim"], 2), "%d / %d ölçü" % (R["resim"]["gecen"], R["resim"]["sayilan"]) if R["resim"] else "liste yok"),
          "| **§1-§5** | **%.2f** | **85** | §6 CAD kalitesi puanlayıcıda |" % P["toplam_1_5"], ""]
    L += ["## Gövdeler (hizalamasız)", "", "| Gövde | ΔV % | ΔA % | ΔCoM mm | Δbbox mm | IoU | IoU kaynağı | P95 mm | maks mm | yön ° | tol. | hacim |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in R["govdeler"]:
        if not r["eslesti"] or "sapma" not in r:
            L.append("| %s | %s |  |  |  |  |  |  |  |  |  |  |" % (r["ad"], "eşleşmedi" if not r["eslesti"] else "ÖLÇÜLEMEDİ: " + r.get("sebep", ""))); continue
        s = r["sapma"]
        L.append("| %s | %+.4f | %+.4f | %.5f | %.5f | %.6f | %s | %.5f | %.4f | %.4f | %d/4 | %s |" % (
            r["ad"], r["dV_pct"], r["dA_pct"], r["dCoM_mm"], r["dBbox_mm"], r["iou"], r["iou_kaynak"].split(" (")[0], s["p95"], s["max"],
            r["yonelim_deg"], sum(r["kontroller"].values()), r["hacim_kaynak"]))
    L += ["", "Mesh sınırının kazandığı örnek sayısı (helis / spline): " + ", ".join(
        "%s %d" % (r["ad"], sum(r["sapma"]["n_mesh_bound"])) for r in R["govdeler"] if "sapma" in r and sum(r["sapma"]["n_mesh_bound"]) > 0) or "yok", ""]
    T2 = R["tamlik"]
    L += ["## Tamlık", "", "Eşleşen %d / %d, fazla %d." % (T2["eslesen"], T2["orijinal"], T2["fazla"]), "",
          "| Grup | Adet | Eşleşen | Doğru | Yeniden yapımdaki küme |", "|---|---|---|---|---|"]
    for c in T2["cesit_tablo"]:
        L.append("| %s | %d | %d | %s | %s |" % (c["grup"], c["adet"], c["eslesen"], f(c["dogru"]), ", ".join(c["kume"])))
    if T2["teslim_tablo"]:
        L += ["", "Teslimat: " + ", ".join("%s %s" % (k, "var" if v else "YOK") for k, v in T2["teslim_tablo"].items())]
    M = R["montaj"]; L += ["", "## Montaj"]
    mo = M.get("montaj_olcum") or M.get("bilgi", {}).get("montaj_olcum")
    if mo:
        L += ["", "ΔV %.4f %%, ΔA %.4f %%, ΔCoM %.4f mm, Δbbox %.4f mm; kontroller: %s" % (mo["dV_pct"], mo["dA_pct"], mo["dCoM_mm"], mo["dBbox_mm"],
                                                                                         ", ".join("%s %s" % (k, f(v)) for k, v in mo["kontroller"].items()))]
    if "girisim_orijinal" in M:
        L += ["", "Girişimler (> %g mm³): orijinal %s; yeniden %s; yalnız birinde %s; hacim farkı > %%%g: %s" % (
            INTERF_MIN_MM3, ", ".join("%s-%s %.2f" % (g["a"], g["b"], g["hacim_mm3"]) for g in M["girisim_orijinal"]) or "yok",
            ", ".join("%s-%s %.2f" % (g["a"], g["b"], g["hacim_mm3"]) for g in M["girisim_yeniden"]) or "yok",
            M["yalniz_birinde"] or "yok", INTERF_VOL_PCT, M["hacim_farki_buyuk"] or "yok")]
    if R["ozellik"]:
        L += ["", "## Özellikler (olc.py önerisi; puanlayıcı onaylar)", "",
              "`sayi`: r_mm verilen silindir / tor sayımında eğrilik yarıçapı tutan B-spline yüzler de sayılır (çekirdek bağımsızlığı). "
              "Sayı yine tutmuyor ama bölgede serbest-form yüz varsa öneri `hakem` olur (geçici puan %g; karar puanlayıcının)." % HAKEM_PROVISIONAL, "", "| id | gövde | kalem | ölçüm | nom | yeniden | orijinal | bölge sapması mm | öneri |", "|---|---|---|---|---|---|---|---|---|"]
        for it in R["ozellik"]["kalemler"]:
            L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (it["id"], it["govde"], it["etiket"], it.get("olcum_tip", "-"), f(it.get("nom")),
                                                                     f(it.get("yeniden")), f(it.get("orijinal")), f(it.get("bolge_sapma_mm")), it["oneri"]))
    if R["resim"]:
        L += ["", "## Teknik resim ölçüleri", "", "| ölçü | nom | birim | tol | yeniden | orijinal | hata | sonuç |", "|---|---|---|---|---|---|---|---|"]
        for r in R["resim"]["satirlar"]:
            L.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (r["dim"], r["nom"], r["birim"], r["tol"], f(r.get("yeniden"), 5), f(r.get("orijinal"), 5),
                                                             f(r.get("hata"), 5), ("geçti" if r["gecti"] else "KALDI") if r["sayildi"] else "sayılmadı"))
    if R["notlar"]:
        L += ["", "## Notlar", ""] + ["- " + n for n in R["notlar"]]
    open(path, "w", encoding="utf8").write("\n".join(L) + "\n")


SUPERVISOR_RETRIES = 6        # child crashes tolerated; each crash skips the step it died in


def supervisor(argv):
    """Runs the measurement in a child process. If OCC kills the child (access violation, no Python traceback), the
    step it was in (body pair, interference, feature item, drawing row) is skipped on the next try and marked in
    olcum.json, so a crash never leaves nothing. A Python error (exit 2) is final."""
    import subprocess
    out = argv[argv.index("--out") + 1]
    os.makedirs(out, exist_ok=True)
    iler = os.path.join(out, "_ilerleme.json"); atla = []
    for k in range(SUPERVISOR_RETRIES + 1):
        if os.path.exists(iler):
            os.replace(iler, iler + ".onceki")
        rc = subprocess.call([sys.executable, os.path.abspath(__file__)] + argv + ["--_ic", "--_atla", "|".join(atla)])
        if rc in (0, 2):
            return rc
        step = None
        try:
            step = json.load(open(iler, encoding="utf8"))["adim"]
        except Exception:
            pass
        print("UYARI: olcum sureci cokti (kod %s) adim=%s" % (rc, step), flush=True)
        if not step or step in atla:
            break
        atla.append(step)
    msg = "olcum sureci tekrar tekrar cokti; son adim %s, atlanan %s" % (step, atla)
    jdump(dict(surum="olc.py 1.0", durum="basarisiz", hata=msg, atlanan=atla), os.path.join(out, "olcum.json"))
    open(os.path.join(out, "olcum_hata.txt"), "w", encoding="utf8").write(msg + chr(10))
    print("HATA: " + msg, file=sys.stderr)
    return 3


if __name__ == "__main__":
    if "--_ic" not in sys.argv:
        sys.exit(supervisor(sys.argv[1:]))
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        msg = "HATA: %s: %s" % (type(e).__name__, e)
        print(msg, file=sys.stderr); traceback.print_exc()
        try:
            out = sys.argv[sys.argv.index("--out") + 1]
            os.makedirs(out, exist_ok=True)
            open(os.path.join(out, "olcum_hata.txt"), "w", encoding="utf8").write(msg + "\n" + traceback.format_exc())
        except Exception:
            pass
        sys.exit(2)
