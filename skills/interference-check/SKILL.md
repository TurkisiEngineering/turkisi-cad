---
name: interference-check
description: Detect clashes between solids in a build123d/OCP CAD assembly by computing pairwise boolean-intersection volumes, and verify clearance gaps between a chassis and inserted components. Use as the numeric gate in any multi-part CAD assembly or chassis-integration loop — returns which pairs interfere and by how much (mm³), so QA can block on interference instead of eyeballing renders.
---

# interference-check

The blocking gate for assemblies: **no two solids may overlap**, and the housing must keep a **minimum clearance** around each inserted component. Both are measured from geometry, never judged by eye.

## Pairwise interference (overlap volume)
```python
from itertools import combinations


def overlap_volume(a, b):
    """Volume (mm^3) of the intersection of two placed solids. 0.0 => no interference."""
    inter = a & b  # build123d boolean intersection
    try:
        return float(inter.volume)
    except Exception:
        return 0.0  # empty intersection has no volume


def interference_report(named_solids, tol=1e-3):
    """named_solids: dict name -> placed solid. Returns list of clashing pairs."""
    clashes = []
    for (na, a), (nb, b) in combinations(named_solids.items(), 2):
        v = overlap_volume(a, b)
        if v > tol:
            clashes.append((na, nb, round(v, 2)))
    return clashes  # empty list == PASS
```

## Clearance between chassis and a component
A component must not touch its pocket. Grow the component by the clearance and confirm it still fits inside the pocket void (or: shrink-check the wall between them).
```python
def min_clearance_ok(component, chassis_solid, gap=0.4):
    """True if the chassis does not intrude within `gap` mm of the component.
    Offset the component outward by `gap`; if that inflated shape clashes with the
    chassis material, the wall is too close."""
    inflated = component.offset(gap)  # 3D offset; check API/version
    return overlap_volume(inflated, chassis_solid) <= 1e-3
```
If `offset` is unavailable/unstable, approximate with a bbox-expanded box or sample the gap by distance queries.

## How to use in the loop
- Run `interference_report` over ALL placed components (Phase: layout) — any non-empty result is a hard REVISE.
- Run chassis↔component `min_clearance_ok` for every pocket (Phase: chassis) — any False is a hard REVISE.
- Report numbers, not prose: `clashes=[('brush','wheel_R',214.3)]` or `clashes=[] PASS`.

## Gotchas
- Boolean ops on noisy/scanned meshes-as-solids can fail; if `&` throws, treat as "cannot verify" (REVISE + flag), not as PASS.
- Coincident touching faces may yield a tiny sliver volume — that is why `tol` (~1e-3 mm³) exists; keep it small, don't inflate it to hide real overlaps.
- Always confirm all solids share ONE coordinate frame (same units, same origin) before checking — a frame mismatch reads as a giant false clash or a false clear.
