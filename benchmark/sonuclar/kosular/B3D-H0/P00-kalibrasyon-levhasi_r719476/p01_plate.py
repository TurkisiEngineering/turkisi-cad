"""P01 Plate - calibration plate (build123d 0.11.1). Produces final.step in this folder."""
from pathlib import Path
from build123d import *

# ---- Parameters (mm) ----
PLATE_L = 100.0        # F1 length along X
PLATE_W = 60.0         # F1 width along Y
PLATE_T = 10.0         # F1 thickness along Z (Z=0..10)
CORNER_R = 3.0         # F2 vertical corner round radius
HOLE_D = 6.0           # F3 through-hole diameter
HOLE_EDGE = 8.0        # F3 hole centre distance from adjacent outer edge
HOLE_PITCH_X = PLATE_L - 2 * HOLE_EDGE   # 84
HOLE_PITCH_Y = PLATE_W - 2 * HOLE_EDGE   # 44
POCKET_D = 20.0        # F4 central pocket diameter
POCKET_DEPTH = 4.0     # F4 pocket depth from top (floor at Z=6)

OUT = Path(__file__).resolve().parent / "final.step"


def build_plate() -> Part:
    with BuildPart() as p:
        # F1 plate block, bottom on Z=0
        Box(PLATE_L, PLATE_W, PLATE_T, align=(Align.CENTER, Align.CENTER, Align.MIN))
        # F2 vertical corner rounds
        fillet(p.edges().filter_by(Axis.Z), radius=CORNER_R)
        # F3 four corner through-holes
        with Locations(Plane.XY):
            with GridLocations(HOLE_PITCH_X, HOLE_PITCH_Y, 2, 2):
                Cylinder(HOLE_D / 2, PLATE_T, align=(Align.CENTER, Align.CENTER, Align.MIN),
                         mode=Mode.SUBTRACT)
        # F4 central blind pocket from top face
        with Locations((0, 0, PLATE_T - POCKET_DEPTH)):
            Cylinder(POCKET_D / 2, POCKET_DEPTH, align=(Align.CENTER, Align.CENTER, Align.MIN),
                     mode=Mode.SUBTRACT)
    part = p.part
    part.label = "P01 Plate"
    return part


if __name__ == "__main__":
    plate = build_plate()
    export_step(plate, str(OUT))
    bb = plate.bounding_box()
    com = plate.center()
    print(f"solids={len(plate.solids())} faces={len(plate.faces())}")
    print(f"volume={plate.volume:.3f} area={plate.area:.3f}")
    print(f"com=({com.X:.4f},{com.Y:.4f},{com.Z:.4f})")
    print(f"bbox=({bb.min.X:.3f},{bb.min.Y:.3f},{bb.min.Z:.3f})..({bb.max.X:.3f},{bb.max.Y:.3f},{bb.max.Z:.3f})")
    print(f"wrote {OUT}")
