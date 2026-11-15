# P1 spec verification

Independent rebuild of the spec text (`is/s05_rebuild.py`, build123d, involute flanks as 60-point splines, R0.16775
rounds, filleted space at -3 deg) compared with the master STEP by `is/cmp.py` (triangulation 0.003 mm, 20 000 samples
per direction, exact point-to-triangle distance).

| Body | spec V mm3 | master V (mesh) | rebuild V (mesh / B-rep) | dV % | dCoM mm | dBbox mm | dev P95 / max mm |
|---|---|---|---|---|---|---|---|
| P01 Gear | 6272.1 | 6272.05 | 6271.51 / 6272.17 | < 0.01 | < 0.001 | 0.000 | 0.0013 / 0.0029 (both ways) |

- Master B-rep volume (OCC GProp) reads 6258.29, 0.22 % low: integration error on the 120 freeform flank faces. Area
  agrees (4231.202 vs 4231.204). The target table uses 6272.1; the grader should use the mesh volume (RUBRIK §1 note).
- Involute fit on all 120 flanks: base radius 14.09536 (= 15 cos 20 = 14.09539), rms 1.6e-5 mm, flank spans r 14.5 to
  15.625; tooth = space = 3.000 deg at r = 15 -> profile shift 0.
- Feature recipes (15) reproduce `nom` on the master. On the rebuild, F10/F11 (root-fillet count and diameter) fail
  because the test kernel's rolling-ball fillet on a spline flank is a freeform face, not a cylinder; the region check
  passes. A producer who draws the fillet as an arc in the profile gets a cylinder like the master.
- Drawing rows: 50.0 / 29.0 / 5.0 / 60 teeth reproduce; pitch diameter, module, pressure angle have no face
  (modelde_var false, covered by F7-F9 flank regions).
- C recipes: all 7 reproduce on the C rebuild (72 teeth, face width 8).
- Undetermined: none.
