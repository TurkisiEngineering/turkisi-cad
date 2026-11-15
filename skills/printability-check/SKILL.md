---
name: printability-check
description: Check a build123d solid for FDM/SLA 3D-printability — minimum wall thickness, print-bed bounding-box fit, and large unsupported overhangs — and report pass/fail with the offending measurements. Use as a manufacturability gate for any 3D-printed part (chassis, bracket, adapter, enclosure) before it passes QA.
---

# printability-check

Manufacturability gate for printed parts. Returns measured numbers so QA can block on a thin wall or an oversized part instead of guessing.

## Bounding box vs print bed
```python
def fits_bed(solid, bed=(256, 256, 256)):
    """True if the part fits the printer volume (mm). Reports the bbox either way."""
    bb = solid.bounding_box().size
    size = (round(bb.X, 1), round(bb.Y, 1), round(bb.Z, 1))
    ok = bb.X <= bed[0] and bb.Y <= bed[1] and bb.Z <= bed[2]
    return ok, size
```

## Minimum wall thickness (practical estimate)
True min-wall needs a medial-axis/thickness analysis. Two workable approaches:
1. **Design-side (preferred):** enforce wall/boss/rib ≥ `min_wall` (2.0 mm FDM) as PARAMETERS in the model so thin walls are impossible by construction, and assert them in the build script.
2. **Check-side (verify):** sample thickness — ray-cast pairs of opposite faces, or erode the solid by `min_wall/2` and confirm no region vanishes:
```python
def wall_ok(solid, min_wall=2.0):
    """Heuristic: shrinking the solid by min_wall/2 should not delete material
    that a wall thinner than min_wall would lose. Compare volumes."""
    try:
        eroded = solid.offset(-min_wall / 2)
        return float(eroded.volume) > 0  # a wall < min_wall would collapse to ~0 locally
    except Exception:
        return None  # inconclusive -> flag, do not pass
```
Treat `None` as "cannot verify" → REVISE + flag, never a silent PASS.

## Overhang flag (orientation sanity)
For a given print orientation (default: build up +Z), faces whose normal points strongly downward (angle from -Z below the self-support threshold, ~45°) need support.
```python
import math


def overhang_faces(solid, max_angle_deg=45):
    """Count downward faces steeper than the self-support limit."""
    bad = 0
    for f in solid.faces():
        n = f.normal_at()  # unit normal
        ang = math.degrees(math.acos(max(-1, min(1, -n.Z))))  # angle from straight-down
        if -n.Z > 0 and ang < max_angle_deg:
            bad += 1
    return bad
```
A nonzero count is a heads-up, not always a fail — report it and let the designer decide orientation/chamfers.

## Report shape
`printable: bed_fit=True(230x210x88) wall>=2.0=True overhangs=3` — numbers first. Any hard fail (bed, wall) blocks; overhangs are advisory.

## Notes
- `offset` behavior varies by build123d/OCP version; if unstable, prefer the design-side guarantee (approach 1) and assert parameters.
- Heat-set inserts: bosses for M3 inserts want ≥ Ø4.0–4.2 mm holes and ≥ 2 mm surrounding wall — check the hole+wall, not just the wall.
