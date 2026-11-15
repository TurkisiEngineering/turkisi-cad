"""Paket denetimi: hedef.json'u referans STEP'e karşı bağımsız ölçer (gövde sayısı, hacim, montaj bbox) ve gizli listelerin
kalem sayılarını yazar. Değerlendirici, kendi referans STEP'inin bu hedef listesine ait olduğunu bununla doğrular.

Kullanım:
  python -I paket_denetle.py --hedefler <hedefler klasörü> --referans P00=<P00 referans.step> [P02=<...> ...]
  -> her paket için stdout'a bir JSON satırı

Not: F23'teki asıl sürüm orijinal katalog STEP'ini ve yapımcı dosyalarının SHA-256'sını okuyordu. Orijinal STEP'ler
yayımlanmadığı için yol artık argümandır; ölçüm mantığı aynıdır.
"""
import argparse, json
from pathlib import Path
from OCP.STEPControl import STEPControl_Reader
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SOLID
from OCP.TopoDS import TopoDS
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
from OCP.Bnd import Bnd_Box
from OCP.BRepBndLib import BRepBndLib


def oku(p):
    r = STEPControl_Reader(); assert r.ReadFile(str(p)) == 1; r.TransferRoots(); s = r.OneShape()
    out = []; ex = TopExp_Explorer(s, TopAbs_SOLID)
    while ex.More():
        so = TopoDS.Solid_s(ex.Current()); ex.Next()
        g = GProp_GProps(); BRepGProp.VolumeProperties_s(so, g, True)
        if abs(g.Mass()) > 1e-6:
            out.append((so, g.Mass()))
    b = Bnd_Box(); b.SetGap(0)
    for so, _ in out:
        BRepBndLib.AddOptimal_s(so, b, True, False)
    return out, list(b.Get())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hedefler", required=True, help="hedefler/ klasörü (içinde P00, P01 ...)")
    ap.add_argument("--referans", nargs="+", required=True, metavar="P##=STEP", help="paket = referans STEP yolu")
    a = ap.parse_args()
    kok = Path(a.hedefler)
    for ikili in a.referans:
        p, step = ikili.split("=", 1)
        g = kok / p
        h = json.loads((g / "hedef.json").read_text(encoding="utf-8"))
        sol, bb = oku(step)
        hv = sum(x["hacim_mm3"] for x in h["govdeler"])
        ov = sum(v for _, v in sol)
        hb = h.get("montaj", {}).get("bbox_mm") or bb
        dbb = max(abs(x - y) for x, y in zip(hb, bb))
        print(json.dumps({"parca": p, "govde_hedef": len(h["govdeler"]), "govde_step": len(sol),
                          "hacim_fark_yuzde_occ": round(100 * (hv - ov) / ov, 4), "montaj_bbox_fark_mm": round(dbb, 4),
                          "ozellik": len(json.loads((g / "ozellikler.json").read_text(encoding="utf-8"))["items"]),
                          "resim": len(json.loads((g / "resim_olculeri.json").read_text(encoding="utf-8"))["rows"]),
                          "param": len(json.loads((g / "parametreler.json").read_text(encoding="utf-8"))["anahtar"]),
                          "dogrulama": (g / "spec_dogrulama.md").exists()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
