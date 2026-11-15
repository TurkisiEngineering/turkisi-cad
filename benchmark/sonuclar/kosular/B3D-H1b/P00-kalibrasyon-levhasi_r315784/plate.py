"""P01 Plate - calibration plate (build123d 0.11.1). Run: python plate.py -> final.step"""
from pathlib import Path
from build123d import *

# --- Parameters (mm) ---
PLATE_L = 100.0        # F1 length along X
PLATE_W = 60.0         # F1 width along Y
PLATE_T = 10.0         # F1 thickness along Z
CORNER_R = 3.0         # F2 vertical corner round radius
HOLE_D = 6.0           # F3 through-hole diameter
HOLE_PITCH_X = 84.0    # F3 hole-centre spacing along X
HOLE_PITCH_Y = 44.0    # F3 hole-centre spacing along Y
POCKET_D = 20.0        # F4 pocket diameter
POCKET_DEPTH = 4.0     # F4 pocket depth (floor at Z = PLATE_T - POCKET_DEPTH)

def build_plate() -> Part:
    # F1: plate block, bottom on Z=0, centred in XY
    plate = Box(PLATE_L, PLATE_W, PLATE_T, align=(Align.CENTER, Align.CENTER, Align.MIN))
    # F2: round the four vertical edges
    plate = fillet(plate.edges().filter_by(Axis.Z), radius=CORNER_R)
    # F3: four through-holes
    for x in (-HOLE_PITCH_X / 2, HOLE_PITCH_X / 2):
        for y in (-HOLE_PITCH_Y / 2, HOLE_PITCH_Y / 2):
            plate -= Pos(x, y, 0) * Cylinder(HOLE_D / 2, PLATE_T,
                                             align=(Align.CENTER, Align.CENTER, Align.MIN))
    # F4: central blind pocket from top face
    plate -= Pos(0, 0, PLATE_T) * Cylinder(POCKET_D / 2, POCKET_DEPTH,
                                           align=(Align.CENTER, Align.CENTER, Align.MAX))
    plate.label = "P01 Plate"
    return plate

if __name__ == "__main__":
    part = build_plate()
    out = Path(__file__).resolve().parent / "final.step"
    export_step(part, str(out))
    bb = part.bounding_box()
    com = part.center()
    print(f"solids={len(part.solids())} faces={len(part.faces())}")
    print(f"volume={part.volume:.3f} area={part.area:.3f}")
    print(f"com=({com.X:.4f},{com.Y:.4f},{com.Z:.4f})")
    print(f"bbox=({bb.min.X:.3f},{bb.min.Y:.3f},{bb.min.Z:.3f})-({bb.max.X:.3f},{bb.max.Y:.3f},{bb.max.Z:.3f})")
    print("wrote", out)
