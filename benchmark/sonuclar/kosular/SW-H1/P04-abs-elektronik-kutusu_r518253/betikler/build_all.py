"""Rebuild everything from scratch: P01 base, P02 lid, H1 screw, assembly, final.step, report.
usage:  python build_all.py            (SolidWorks 2024, pywin32)"""
import os, sys, json
import win32com.client
import swlib
from swlib import IN
import build_base, build_lid_screw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, ".."))

TARGET = {"P01": (0.50384, 16.4101, -0.2902), "P02": (0.47934, 15.9829, 0.3372), "H1": (0.00230, 0.1618, -0.2265)}


def interference(C):
    """pairwise intersection volumes via temporary body copies (IBody2.Operations2, SWBODYINTERSECT)"""
    from win32com.client import gencache
    out = {}
    try:
        m = gencache.EnsureModule('{83A33D31-27C5-11CE-BFD4-00400513BB57}', 0, 32, 0)
        bs = {b.Name.split(">")[0].strip("<"): m.IBody2(b._oleobj_) for b in C.bodies()}
        keys = sorted(bs)
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                a, b = bs[keys[i]].Copy(), bs[keys[j]].Copy()
                r = m.IBody2(a).Operations2(15901, m.IBody2(b), 0)
                res = r[0] if isinstance(r, tuple) else r
                vol = 0.0
                if res:
                    for x in res:
                        mp = m.IBody2(x).GetMassProperties(1.0)
                        vol += mp[3]
                out[keys[i] + "-" + keys[j]] = (vol / IN ** 3, vol * 1e9)
                print("interference %s-%s: %.6f in3 = %.3f mm3" % (keys[i], keys[j], vol / IN ** 3, vol * 1e9))
    except Exception as ex:
        print("interference check failed", ex)
    return out


def main():
    sw = win32com.client.Dispatch("SldWorks.Application")
    sw.Visible = True
    mine = []
    results, params = {}, []
    specs = [("P01", "P01_Base.SLDPRT", build_base.build),
             ("P02", "P02_Lid.SLDPRT", build_lid_screw.build_lid),
             ("H1", "H1_Screw.SLDPRT", build_lid_screw.build_screw)]
    paths = []
    for pid, fname, fn in specs:
        P = swlib.Part(sw)
        fn(P, verbose=False)
        P.m.ForceRebuild3(False)
        v, a, c = P.mass()
        results[pid] = dict(vol=v, area=a, com=c, bbox=P.bbox()[0], faces=P.nfaces(), bodies=len(P.bodies()))
        params += [(pid,) + t for t in P.params]
        path = os.path.join(OUT, fname)
        if os.path.exists(path):
            os.remove(path)
        P.save(path)
        paths.append(path)
        mine.append(P.m.GetTitle)
        print(pid, json.dumps(results[pid]))

    # ---- combined multibody part: the three parts inserted (linked) at identity placement ----
    # (IAssemblyDoc.AddComponent5 returned Nothing in this SolidWorks session, see build_log.md)
    C = swlib.Part(sw)
    for p in paths:
        C.m.InsertPart3(p, 1, "")          # swInsertPartImportSolids, no move/rotate
    C.m.ForceRebuild3(False)
    for bdy, nm in zip(sorted(C.bodies(), key=lambda b: b.Name), []):
        pass
    print("combined bodies", [b.Name for b in C.bodies()], C.bbox())
    v, a_, c_ = C.mass()
    results["ALL"] = dict(vol=v, area=a_, com=c_, bodies=len(C.bodies()))
    print("ALL", json.dumps(results["ALL"]))
    results["interference"] = interference(C)
    apath = os.path.join(OUT, "Kutu_Hepsi.SLDPRT")
    if os.path.exists(apath):
        os.remove(apath)
    C.save(apath)
    mine.append(C.m.GetTitle)
    A = C.m

    # ---- STEP AP214 ----
    # STEP AP214: swStepAP (75) is a system option -> set 214 for this export, then restore the user's value
    old_ap = sw.GetUserPreferenceIntegerValue(75)
    sw.SetUserPreferenceIntegerValue(75, 214)
    spath = os.path.join(OUT, "final.step")
    if os.path.exists(spath):
        os.remove(spath)
    ok = A.SaveAs3(spath, 0, 1)
    sw.SetUserPreferenceIntegerValue(75, old_ap)
    print("step export", ok, os.path.exists(spath), "AP option was", old_ap, "restored")
    results["params"] = params
    with open(os.path.join(HERE, "olcum.json"), "w") as f:
        json.dump(results, f, indent=1, default=str)
    with open(os.path.join(HERE, "acik_belgeler.txt"), "w") as f:
        f.write("\n".join(mine))
    for pid, (v, a, cz) in TARGET.items():
        r = results[pid]
        print("%s  V %.5f (target %.5f, %+.3f%%)  A %.4f (target %.4f)  CoMz %.4f (target %.4f)" % (
            pid, r["vol"], v, 100 * (r["vol"] - v) / v, r["area"], a, r["com"][2], cz))


if __name__ == "__main__":
    main()
