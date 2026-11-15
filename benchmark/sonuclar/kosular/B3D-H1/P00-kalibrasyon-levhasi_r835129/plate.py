"""P01 Plate - calibration plate (spec.md). Units: mm. Run: python plate.py -> final.step"""
from pathlib import Path
from build123d import *

# --- Parameters ---
PLATE_L = 100.0        # X length (F1)
PLATE_W = 60.0         # Y width (F1)
PLATE_T = 10.0         # Z thickness (F1)
CORNER_R = 3.0         # vertical corner round radius (F2)
HOLE_D = 6.0           # corner through-hole diameter (F3)
HOLE_PITCH_X = 84.0    # hole centre spacing along X (F3)
HOLE_PITCH_Y = 44.0    # hole centre spacing along Y (F3)
POCKET_D = 20.0        # central pocket diameter (F4)
POCKET_DEPTH = 4.0     # pocket depth from top face (F4) -> floor at Z=6

def build():
    with BuildPart() as bp:
        # F1 + F2: rounded rectangle extruded Z=0..T (equivalent to block + vertical edge fillets)
        with BuildSketch(Plane.XY):
            RectangleRounded(PLATE_L, PLATE_W, CORNER_R)
        extrude(amount=PLATE_T)
        # F3: corner through-holes
        with BuildSketch(Plane.XY):
            with GridLocations(HOLE_PITCH_X, HOLE_PITCH_Y, 2, 2):
                Circle(HOLE_D / 2)
        extrude(amount=PLATE_T, mode=Mode.SUBTRACT)
        # F4: central blind pocket from top face
        with BuildSketch(Plane.XY.offset(PLATE_T)):
            Circle(POCKET_D / 2)
        extrude(amount=-POCKET_DEPTH, mode=Mode.SUBTRACT)
    part = bp.part
    part.label = "P01 Plate"
    return part

if __name__ == "__main__":
    p = build()
    out = Path(__file__).with_name("final.step")
    export_step(p, str(out))
    bb = p.bounding_box()
    c = p.center()
    print(f"valid={p.is_valid} solids={len(p.solids())} faces={len(p.faces())}")
    print(f"volume={p.volume:.3f} area={p.area:.3f}")
    print(f"com=({c.X:.4f},{c.Y:.4f},{c.Z:.4f})")
    print(f"bbox=({bb.min.X:.3f},{bb.min.Y:.3f},{bb.min.Z:.3f})-({bb.max.X:.3f},{bb.max.Y:.3f},{bb.max.Z:.3f})")
    print(f"wrote {out}")
