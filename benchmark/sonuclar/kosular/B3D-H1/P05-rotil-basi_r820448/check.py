"""Verification: measure built bodies + re-imported STEP against spec targets."""
import sys, math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from build123d import *
import rod_end

T = {"P01": (0.69442, 9.8350, (0, 0.1926, 0), (-0.75, -1.625, -0.25, 0.75, 1.75, 0.25)),
     "P02": (0.59227, 6.2209, (0, 1.0, 0), (-0.5625, 0.4375, -0.625, 0.5625, 1.5625, 0.625))}

def report(name, s):
    v, a = s.volume, s.area
    c = s.center(CenterOf.MASS); bb = s.bounding_box()
    tv, ta, tc, tb = T[name]
    print(f"{name}: valid={s.is_valid} faces={len(s.faces())} vol={v:.5f} ({(v/tv-1)*100:+.3f}%) "
          f"area={a:.4f} ({(a/ta-1)*100:+.3f}%) CoM=({c.X:.4f},{c.Y:.4f},{c.Z:.4f}) dCoM={(c-Vector(*tc)).length:.4f}")
    got = (bb.min.X, bb.min.Y, bb.min.Z, bb.max.X, bb.max.Y, bb.max.Z)
    print("   bbox", tuple(round(g, 4) for g in got), "max dev", round(max(abs(g-t) for g, t in zip(got, tb)), 5))
    return v

h, b = rod_end.build()
report("P01", h); report("P02", b)
print("interference vol:", (h & b).volume if (h & b) else 0.0)
imp = import_step(str(Path(__file__).with_name("final.step")))
sols = imp.solids()
print("STEP solids:", len(sols))
for s in sols:
    print("  imported vol", round(s.volume, 5), "bbox", s.bounding_box())
hdr = Path(__file__).with_name("final.step").read_text(errors="ignore")
print("schema:", [l for l in hdr.splitlines() if "FILE_SCHEMA" in l][:1])
print("units:", [l[:120] for l in hdr.splitlines() if "CONVERSION_BASED_UNIT" in l or "LENGTH_UNIT" in l][:3])
