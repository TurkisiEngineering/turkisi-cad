"""Compare built bodies (or final.step) with spec section 6 targets.

python measure.py            -> measures final.step (re-imported)
"""
import sys
from pathlib import Path

# name: (vol in3, area in2, com x, y, z, xmin, xmax, ymin, ymax, zmin, zmax)
TARGETS = {
    "P01_Base": (4.5937, 35.896, 0.0, -0.1019, 2.0, -1.25, 1.25, -0.3946, 0.3554, 0.0, 4.0),
    "P02_Carriage": (0.8300, 10.704, 0.0, 0.2243, 2.75, -0.8721, 0.8721, -0.0196, 0.4104, 1.5, 4.0),
    "P03_Drive_nut": (0.4059, 3.187, 0.0, 0.1494, 2.75, -0.4975, 0.4975, -0.1116, 0.4104, 2.2525, 3.2475),
    "P04_End_block": (1.1376, 9.266, 0.0, 0.0099, 4.3108, -1.25, 1.25, -0.3846, 0.4054, 4.0, 4.625),
    "P05_End_plate": (0.1114, 4.066, 0.0, -0.0144, -0.0310, -1.25, 1.25, -0.3846, 0.3554, -0.062, 0.0),
    "P06_Lead_screw": (0.1685, 4.926, 0.0, 0.0424, 2.7523, -0.125, 0.125, -0.0826, 0.1674, 0.5, 5.0),
    "P07_Handwheel": (1.0320, 7.532, 0.0, 0.0424, 5.2015, -0.875, 0.875, -0.8326, 0.9174, 4.687, 5.437),
    "P08_Crank_handle": (0.0447, 0.861, 0.0, -0.5886, 5.9992, -0.125, 0.125, -0.7136, -0.4636, 5.437, 6.5622),
    "H1_a": (0.0225, 0.628, 1.031, -0.0196, 4.4179, 0.844, 1.218, -0.2066, 0.1674, 3.9379, 4.725),
    "H1_b": (0.0225, 0.628, -1.031, -0.0196, 4.4179, -1.218, -0.844, -0.2066, 0.1674, 3.9379, 4.725),
    "H1_c": (0.0225, 0.628, 1.031, -0.0196, 0.1451, 0.844, 1.218, -0.2066, 0.1674, -0.162, 0.6251),
    "H1_d": (0.0225, 0.628, -1.031, -0.0196, 0.1451, -1.218, -0.844, -0.2066, 0.1674, -0.162, 0.6251),
}


def measure(shape):
    bb = shape.bounding_box(optimal=True)
    c = shape.center()
    return (shape.volume, shape.area, c.X, c.Y, c.Z, bb.min.X, bb.max.X, bb.min.Y, bb.max.Y,
            bb.min.Z, bb.max.Z)


def report(parts, scale=1.0):
    rows = []
    tv = ta = 0.0
    ok_all = True
    print(f"{'body':18s} {'vol':>8s} {'tgt':>8s} {'dV%':>7s} {'area':>8s} {'tgt':>8s} {'dA%':>7s} "
          f"{'dCoM':>8s} {'dBB':>8s} {'valid':>5s} ok")
    for name, shp in parts.items():
        m = measure(shp)
        if scale != 1.0:
            m = (m[0] / scale**3, m[1] / scale**2) + tuple(v / scale for v in m[2:])
        t = TARGETS[name]
        dv = 100 * (m[0] - t[0]) / t[0]
        da = 100 * (m[1] - t[1]) / t[1]
        dcom = max(abs(m[i] - t[i]) for i in (2, 3, 4))
        dbb = max(abs(m[i] - t[i]) for i in range(5, 11))
        vtol = 2.0 if name.startswith("H1") else 0.5
        # targets are rounded to 4 decimals -> allow 0.00005 rounding on top of 0.005
        ok = abs(dv) <= vtol and dcom <= 0.02 and dbb <= 0.00505
        ok_all &= ok
        tv += m[0]
        ta += m[1]
        print(f"{name:18s} {m[0]:8.4f} {t[0]:8.4f} {dv:7.3f} {m[1]:8.3f} {t[1]:8.3f} {da:7.3f} "
              f"{dcom:8.5f} {dbb:8.5f} {str(shp.is_valid):>5s} {'OK' if ok else 'FAIL'}")
        rows.append((name, m))
    print(f"total volume {tv:.4f} in3 (target 8.4138), total area {ta:.3f} in2 (target 78.949)")
    vs = sum(m[0] for _, m in rows)
    com = [sum(m[0] * m[2 + i] for _, m in rows) / vs for i in range(3)]
    print("assembly CoM (%.4f, %.4f, %.4f) target (0.0000, -0.0224, 2.8277)" % tuple(com))
    print("assembly bbox X [%.5f, %.5f] Y [%.5f, %.5f] Z [%.5f, %.5f]" % (
        min(m[5] for _, m in rows), max(m[6] for _, m in rows), min(m[7] for _, m in rows),
        max(m[8] for _, m in rows), min(m[9] for _, m in rows), max(m[10] for _, m in rows)))
    print("target bbox    X [-1.25, 1.25] Y [-0.83256, 0.91744] Z [-0.162, 6.5622]")
    print("ALL OK" if ok_all else "SOME FAIL")
    return ok_all


if __name__ == "__main__":
    from build123d import import_step
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("final.step")
    asm = import_step(str(path))       # build123d imports in mm
    parts = {}

    def walk(node):  # labelled leaf bodies of the imported assembly
        if node.children:
            for ch in node.children:
                walk(ch)
        else:
            parts[node.label] = node
    walk(asm)
    print(f"{len(parts)} bodies, {len(asm.solids())} solids in {path.name}")
    report(parts, scale=25.4)
