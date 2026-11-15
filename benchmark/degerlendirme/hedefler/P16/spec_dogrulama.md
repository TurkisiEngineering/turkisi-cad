# P16 spec verification

Master: 1 solid, 134 faces (100 B-spline tooth faces = 20 spaces x 5: 2 flanks, 2 root fillets, 1 root), no empty
shells. GProp vs mesh volume 0.012 %, GProp kept.

## Tooth-form analysis (`is/s02_teeth.py`, `is/s03_poles.py`)

Every tooth face is a non-rational B-spline of degree 1 x 3: a ruled surface between two cubic curves (flank / fillet:
6 poles, knots (0,0,0,0,0.5,0.5,1,1,1,1) after normalisation; root: 4-pole Bezier). The rulings are exactly straight
(deviation 0.00000 mm). Flank rulings do not meet at one apex (closest approach 0.38 mm from the axis at y 46.2);
root rulings meet the axis at y 42.50. Hence the spec gives the master's own poles instead of a textbook involute.
The spec re-expresses the two pole rows at ruling parameters u = -0.05 (heel side, outside the blank) and u = 0.6
(beyond the toe), which is the same surface with margin for the boolean, rounded to 5 decimals. The flank / fillet
junction poles of adjacent faces differ by up to 0.0006 mm in the master at the far row; the spec makes them equal.

## Independent rebuild of the spec text (`is/s04_rebuild.py`, build123d + OCC ThruSections ruled)

Revolved blank (9 points) minus 20 ruled cutters made from the printed poles.

| Body | spec V mm3 | master V (B-rep / mesh) | rebuild V | ΔV % | rebuild A / master A | dev mean / P95 / max mm |
|---|---|---|---|---|---|---|
| P01 | 8494.85 | 8494.85 / 8493.86 | 8494.78 | -0.0008 | 3858.284 / 3858.295 | 0.0000 / 0.0000 / 0.00026 |

Deviation measured with `olc_cekirdek.deviation` (two-way, `is/s05_sapma.py`). ΔCoM, Δbbox 0.000 mm.

## Self-check with olc.py (original vs itself)

`is/olc_kendi/olcum.md`: **85.00 / 85** (single body: geometry 50, completeness 10, features 18 / 18, drawing 3 / 3 measurable rows). `paket_denetle.py P16`: 1 body = STEP, ΔV 0.0 %, bbox Δ 0.0 mm. Features 18, all reproduce on the master
(`is/s09_tarif.py`, 0 failures).

## Notes

- Drawing (7 dimensions): 8 bore and 25 hub dia and 19.33 overall width have recipes. 32.77 (heel OD), 11 (face width
  along the pitch cone) and 7.75 (hub length) have no single-recipe counterpart (teeth are not on the bbox axes; no
  plane at y 7.75), listed with `olcum: null`, `modelde_var: true`; 30 (pitch dia) is a reference value,
  `modelde_var: false`. Features F6 and F8 cover 7.75 and 32.77 by region.
- No tooth counts with `sayi` on B-spline faces (kernel dependent); the 20 teeth are counted as separate tip-cone lands
  (analytic cone, `ayri_yuzler`).
- Tier "shape" (index): the blank is trivial but the teeth need exact B-spline flank input; with the poles given it is
  a moderate task. I would keep "shape" only if the lead accepts that the spec hands over the flank poles; otherwise
  it is "hard".
- Undetermined: the generating method of the flank form (stated in the spec; poles are authoritative).
