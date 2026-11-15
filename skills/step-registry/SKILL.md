---
name: step-registry
description: Import STEP/STP components into build123d, measure their bounding box/volume/mount references, place them in a shared assembly coordinate frame, and hot-swap one placeholder CAD file for another without touching downstream code. Use whenever a CAD task consumes external component STEP files (LiDAR, motors, wheels, PCBs, brushes) and must position or later replace them — the core of any assembly-integration or placeholder-driven design run.
---

# step-registry

A component **registry** is a single dict mapping each functional component to `{step, pos, rot}`. Everything downstream reads geometry by *measuring the imported solid*, never by hard-coded numbers — that is what makes a placeholder swap a one-line change.

## The rule that makes swaps work
Never hard-code a component's size or mount location. Always derive it from the imported solid's bounding box and its real faces/holes. When a scanned STEP replaces a placeholder, only the `step` path changes; pockets and mounts regenerate from the new bbox.

## Registry pattern (`registry.py`)
```python
# registry.py — single source of truth for component placement. Positions in mm,
# rotations in degrees (X,Y,Z), in the CHASSIS frame (origin = footprint center, Z up).
REGISTRY = {
    "lidar": {"step": "00_Placeholders/lidar.step", "pos": (0, 40, 70), "rot": (0, 0, 0)},
    "compute": {"step": "00_Placeholders/compute_module.step", "pos": (0, 60, 20), "rot": (0, 0, 0)},
    "wheel_L": {"step": "00_Placeholders/wheel_left.stp", "pos": (-70, 0, 15), "rot": (0, 0, 0)},
    "wheel_R": {"step": "00_Placeholders/wheel_right.stp", "pos": (70, 0, 15), "rot": (0, 0, 0)},
    # add: caster, brush, brush_motor, fan, battery ...
}
```

## Load + measure helper
```python
from build123d import import_step, Pos, Rot


def load_component(entry):
    """Import a STEP, apply placement, return (solid, info dict). Measures bbox — never assume size."""
    solid = import_step(entry["step"])
    rx, ry, rz = entry["rot"]
    placed = Pos(*entry["pos"]) * Rot(rx, ry, rz) * solid
    bb = placed.bounding_box()
    info = {
        "bbox_size": tuple(round(v, 2) for v in (bb.size.X, bb.size.Y, bb.size.Z)),
        "bbox_min": tuple(round(v, 2) for v in (bb.min.X, bb.min.Y, bb.min.Z)),
        "bbox_max": tuple(round(v, 2) for v in (bb.max.X, bb.max.Y, bb.max.Z)),
        "volume_mm3": round(placed.volume, 1),
    }
    return placed, info


def load_all(registry):
    return {name: load_component(e) for name, e in registry.items()}
```

## Identifying unknown parts (coded filenames)
When filenames are opaque (e.g. `XYZ-M01L-01.stp`), classify by geometry, then have a human confirm:
- Import each, print `bbox_size` and `volume_mm3`.
- Heuristics: **wheel** → one bbox dim ≈ another (disc), moderate thickness; **roller/brush** → one long axis, round cross-section; **battery** → box, large volume; **motor/gearbox** → stubby cylinder + box. Report guesses; do not assume.
- Run identification as parallel workers (one file each) and converge to a proposed mapping for sign-off.

## Swap protocol
1. Drop the new STEP in `00_Placeholders/`. 2. Change that one `step` line in `registry.py`.
3. Re-run only the affected component's load + fit. If anything else needs editing, the design leaked a hard-coded size — fix that instead.

## Notes
- Units: STEP is mm; keep the whole assembly in mm. Verify with a known part's bbox.
- If `import_step` returns a Compound with sub-solids, keep it as one placed object for placement; use `.solids()` when you need individual bodies.
- Mount points: prefer selecting real holes/faces (`.faces()`, `.edges()` filtered by radius/position) over inventing boss locations.
