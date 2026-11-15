"""Compare built bodies (or final.step) with the spec section-6 acceptance table.
Usage:  python olcum.py            -> builds via caster.py and measures
        python olcum.py final.step -> measures the bodies inside a STEP file
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

TARGET = {  # ID: vol in3, area in2, com(x,y,z), bbox(xmin,xmax,ymin,ymax,zmin,zmax)
    "P01": (5.06749, 50.1952, (0.9987, 1.5153, 0), (-1.1330, 3.6885, -1.2500, 2.4640, -1.1330, 1.1330)),
    "P02": (0.83205, 18.5321, (0, 2.6876, 0), (-1.8125, 1.8125, 2.4533, 2.7500, -1.2500, 1.2500)),
    "P03": (0.23072, 3.1492, (-0.0009, 2.3584, 0), (-0.3755, 0.3755, 1.7570, 2.7500, -0.3755, 0.3755)),
    "P04": (0.12992, 4.2445, (0, 2.5004, 0), (-0.8720, 0.8720, 2.4640, 2.5390, -0.8720, 0.8720)),
    "P05": (0.07254, 2.7849, (0, 2.5740, 0), (-0.8718, 0.8718, 2.5390, 2.6140, -0.7550, 0.7550)),
    "P06": (1.90479, 11.7309, (3.2588, 1.5941, 0), (2.4615, 4.2985, 1.1895, 2.1599, -1.0500, 1.0500)),
    "P07": (5.89220, 35.5529, (1.515, -0.75, 0), (-0.4850, 3.5150, -2.7500, 1.2500, -0.6250, 0.6250)),
    "P08": (0.60427, 25.1375, (1.515, -0.75, 0), (-0.0487, 3.0787, -2.3138, 0.8137, -0.6250, 0.6250)),
    "P09": (4.49923, 20.3420, (1.515, -0.75, 0), (0.0013, 3.0288, -2.2638, 0.7638, -0.3125, 0.3125)),
    "P10a": (2.93150, 17.8824, (1.515, -0.75, -0.5290), (0.0013, 3.0288, -2.2638, 0.7638, -0.8249, -0.3125)),
    "P10b": (2.93150, 17.8824, (1.515, -0.75, 0.5290), (0.0013, 3.0288, -2.2638, 0.7638, 0.3125, 0.8249)),
    "H1": (0.58471, 4.4636, (1.515, -0.75, 0), (1.2150, 1.8150, -1.0500, -0.4500, -1.0340, 1.0340)),
}
ORDER = list(TARGET)


def measure(bodies, k_len=1.0):
    rows = []
    tv = ta = 0.0
    for key, (name, b) in zip(ORDER, bodies):
        v, a = b.volume * k_len ** 3, b.area * k_len ** 2
        c = b.center() * k_len
        bb = b.bounding_box()
        box = tuple(q * k_len for q in (bb.min.X, bb.max.X, bb.min.Y, bb.max.Y, bb.min.Z, bb.max.Z))
        T = TARGET[key]
        dv = (v - T[0]) / T[0] * 100
        dc = max(abs(c.X - T[2][0]), abs(c.Y - T[2][1]), abs(c.Z - T[2][2]))
        db = max(abs(p - q) for p, q in zip(box, T[3]))
        tol = 2.0 if key == "H1" else 0.5
        ok = abs(dv) <= tol and dc <= 0.02 and db <= 0.005
        tv += v
        ta += a
        rows.append(f"| {key} | {v:.5f} | {T[0]:.5f} | {dv:+.3f}% | {a:.4f} | {T[1]:.4f} | "
                    f"({c.X:.4f}, {c.Y:.4f}, {c.Z:.4f}) | {dc:.4f} | {db:.4f} | "
                    f"{len(b.faces())} | {'OK' if ok else 'FAIL'} |")
    hdr = ("| ID | Vol | Vol hedef | dVol | Alan | Alan hedef | CoM | dCoM max | dBBox max | faces | durum |\n"
           "|---|---|---|---|---|---|---|---|---|---|---|")
    out = hdr + "\n" + "\n".join(rows)
    out += f"\n\nToplam hacim {tv:.5f} in3 (hedef 25.68092), toplam alan {ta:.4f} in2 (hedef 211.8978)"
    return out


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower().endswith((".step", ".stp")):
        from build123d import import_step
        asm = import_step(sys.argv[1])
        sols = asm.solids()
        print("solids in STEP:", len(sols))
        # build123d import_step returns millimetres -> scale back to inches.
        # Labels are not carried onto the solids, the file order (P01..H1) is kept.
        named = [(getattr(s, "label", ""), s) for s in sols]
        # order by label prefix
        def k(t):
            lab = t[0] or ""
            for i, key in enumerate(ORDER):
                if lab.replace("_", "").upper().startswith(key.upper()):
                    return i
            return 99
        if all(n for n, _ in named):
            named.sort(key=k)
        print(measure(named, k_len=1 / 25.4))
    else:
        import caster
        bodies, notes = caster.build_all(rounds="--no-rounds" not in sys.argv)
        print(notes)
        print(measure(bodies))
