---
name: cad-section
description: Produce a clean 2D cross-section or silhouette PNG of a build123d solid for visual QA, using matplotlib with explicitly expanded axis limits so no dimension text, label, or edge is ever clipped at the frame. Use whenever a CAD loop needs section images (Y=const or X=const slices, top silhouettes) for a human or QA agent to inspect fit, wall, and layout.
---

# cad-section

Section images are the visual half of the QA gate. The #1 defect in headless matplotlib output is **clipping** — labels or geometry touching the frame edge. Always expand the limits with margin.

## Never-clip rule
Compute the data extent, then set limits to extent + a margin (≥ 8% of the span, or ≥ 5 mm). Set `equal` aspect so the part isn't distorted. Draw dimension text INSIDE the padded area.
```python
import matplotlib

matplotlib.use("Agg")  # headless
import matplotlib.pyplot as plt


def framed_axes(xs, ys, margin_frac=0.08, min_margin=5.0):
    fig, ax = plt.subplots(figsize=(8, 8))
    xmin, xmax, ymin, ymax = min(xs), max(xs), min(ys), max(ys)
    mx = max((xmax - xmin) * margin_frac, min_margin)
    my = max((ymax - ymin) * margin_frac, min_margin)
    ax.set_xlim(xmin - mx, xmax + mx)  # <-- explicit, expanded — prevents clipping
    ax.set_ylim(ymin - my, ymax + my)
    ax.set_aspect("equal", adjustable="box")
    return fig, ax
```

## Slicing a solid at a plane
Cut the solid with a plane and plot the resulting section edges. Use build123d's section/split; fall back to the OCP section algorithm if needed.
```python
from build123d import Plane


def section_edges_xz(solid, y=0.0):
    """Return list of (xs, ys) polylines from the section at plane Y=y (XZ view)."""
    plane = Plane.XZ.offset(y)  # section plane
    sect = solid & plane  # intersection -> face(s)/wire(s); verify API
    polylines = []
    for edge in sect.edges():
        pts = [edge.position_at(t) for t in [i / 24 for i in range(25)]]
        polylines.append(([p.X for p in pts], [p.Z for p in pts]))
    return polylines
```
If `solid & plane` doesn't yield a section in your version, use OCP `BRepAlgoAPI_Section(solid.wrapped, plane_face)` and read the resulting edges — same plotting afterward.

## Assemble the figure
```python
def plot_section(polylines, title, out_png):
    allx = [x for xs, ys in polylines for x in xs]
    ally = [y for xs, ys in polylines for y in ys]
    fig, ax = framed_axes(allx, ally)
    for xs, ys in polylines:
        ax.plot(xs, ys, "-", lw=1.4)
    ax.set_title(title)
    ax.set_xlabel("mm")
    ax.set_ylabel("mm")
    fig.savefig(out_png, dpi=150, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
```
`bbox_inches="tight"` + `pad_inches` is a second guard against clipping.

## Conventions
- Name sections by what they show and where: `section_Y0_layout.png`, `section_X0_wheel.png`.
- For assembly layouts, overlay each component's section in a distinct color + a legend placed inside the padded axes (`loc="upper right"`, `framealpha=0.9`).
- Add dimension callouts as annotations well inside the limits; never at x/ymax.
