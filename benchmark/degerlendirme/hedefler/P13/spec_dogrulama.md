# P13 spec verification

Master: 2 solids. The plate solid carries 22 empty zero-area shells (132 faces) at (38.1, -22.225, 3.402) mm; olc drops
them (`bos_kabuk_atilan` 22); the spec names them as an artefact. Targets are GProp values (GProp vs mesh volume:
plate -0.005 %, tube 0.027 %).

## Independent rebuild of the spec text (`is/s03_rebuild.py`, build123d)

Block minus 4 U channels; tube = annulus (OD 0.375, wall 0.02) swept along the 7-segment centreline.

| Body | spec V mm3 | master V (B-rep / mesh) | rebuild V | master − rebuild | rebuild − master | rebuild A vs master |
|---|---|---|---|---|---|---|
| P01 plate | 122692.25 | 122692.25 / 122697.98 | 122692.25 | 0.000 | 0.000 | 41698.549 / 41698.549 |
| P02 tube | 11956.98 | 11956.98 / 11953.74 | 11956.98 | 0.000 | 0.000 | 47103.520 / 47103.520 |

Analytic check: tube volume = π(4.7625² − 4.2545²) × centreline 830.895 mm = 11956.98 mm3. ΔCoM, Δbbox 0.000 mm.

## Self-check with olc.py (original vs itself)

`is/olc_kendi/olcum.md`: **85.00 / 85** (features 26 / 26, drawing 4 / 4). `paket_denetle.py P13`: 2 bodies = STEP,
volume Δ 0.0 %, assembly bbox Δ 0.0 mm. Plate/tube common volume 0.000 mm3 (contact only), `girisimler` empty.

## Notes

- Drawing (4 dimensions, all modelled): 6in plate length (tol 0.5 by written precision), 3.5in width (0.05),
  0.375in tube OD (0.0005), 0.5in thickness (0.05).
- Tier "hard" (index): the geometry is simple (block with 4 U channels + one swept tube, both rebuilt exactly with a
  few operations). I would rate it "shape"; the only traps are the frame (tube axis at z = 0, plate top at 0.1875) and
  the hollow tube. Lead to decide; no hub file changed.
- Undetermined: none.
