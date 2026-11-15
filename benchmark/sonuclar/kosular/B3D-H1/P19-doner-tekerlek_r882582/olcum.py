"""Measure every body of caster.py (or of final.step) against the spec section 6 table.
python olcum.py            -> builds via caster.py and compares
python olcum.py final.step -> re-imports the STEP and compares
"""
import os
import sys

from build123d import import_step

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# ID: vol, area, com(x,y,z), bbox(xmin,xmax,ymin,ymax,zmin,zmax)
TARGET = {
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


def measure(solids, scale=1.0):
    rows = []
    tv = ta = 0
    for s in solids:
        key = s.label.split("_")[0]
        v, a = s.volume * scale ** 3, s.area * scale ** 2
        c = s.center() * scale
        bb = s.bounding_box()
        b = [bb.min.X, bb.max.X, bb.min.Y, bb.max.Y, bb.min.Z, bb.max.Z]
        b = [x * scale for x in b]
        tvol, tarea, tc, tb = TARGET[key]
        dv = (v - tvol) / tvol * 100
        da = (a - tarea) / tarea * 100
        dc = max(abs(c.X - tc[0]), abs(c.Y - tc[1]), abs(c.Z - tc[2]))
        db = max(abs(p - q) for p, q in zip(b, tb))
        nf = len(s.faces())
        tv += v
        ta += a
        rows.append((key, v, tvol, dv, a, da, dc, db, nf, s.is_valid))
    print(f"{'ID':5} {'vol':>9} {'target':>9} {'dV%':>7} {'area':>9} {'dA%':>6} {'dCoM':>7} {'dBBox':>7} {'faces':>5} valid")
    for r in rows:
        print(f"{r[0]:5} {r[1]:9.5f} {r[2]:9.5f} {r[3]:7.3f} {r[4]:9.4f} {r[5]:6.2f} {r[6]:7.4f} {r[7]:7.4f} {r[8]:5d} {r[9]}")
    print(f"total volume {tv:.5f} (target 25.68092), total area {ta:.4f} (target 211.8978)")
    return rows


if __name__ == "__main__":
    if len(sys.argv) > 1:
        shp = import_step(sys.argv[1])
        sols = list(shp.solids())
        # import_step returns mm (OCC base unit); convert back to inch
        bb = shp.bounding_box()
        scale = 1 / 25.4 if bb.max.Y > 10 else 1.0
        print(f"imported {len(sols)} solids, scale {scale}")
        # labels may be lost on solids; map by order
        names = ["P01", "P02", "P03", "P04", "P05", "P06", "P07", "P08", "P09", "P10a", "P10b", "H1"]
        for s, n in zip(sols, names):
            s.label = n
        measure(sols, scale)
    else:
        import caster
        sols = caster.build_all()
        measure(sols)
        # interference check P09-H1
        p = {s.label.split("_")[0]: s for s in sols}
        print("P09&H1 overlap", (p["P09"] & p["H1"]).volume, "target 0.17671")
