# P11 spec verification

Independent rebuild of the spec text (`is/s06_rebuild.py`: core cylinder + helical tooth swept in 2-turn pieces,
trimmed by the 30 degree end envelope, bore, chamfers, set-screw hole; set screw with hex socket) compared with the
master STEP by `is/cmp.py` (triangulation 0.003 mm, 20 000 samples per direction) and by `olc.py` (`is/olc_rebuild`).

| Body | spec V mm3 | master V (B-rep / mesh) | rebuild V (B-rep / mesh) | dV % | dCoM mm | dBbox mm | dev P95 / max mm |
|---|---|---|---|---|---|---|---|
| P01 Worm | 5415.1 | 5415.09 / 5414.03 | 5414.76 / 5414.21 | 0.006 | 0.026 (B-rep) / 0.000 (mesh) | 0.000 | 0.0005 / 0.003 (both ways) |
| H1 Set screw | 41.948 | 41.948 / 41.942 | 41.948 / 41.942 | 0.000 | 0.000 | 0.000 | 0.0002 / 0.0004 |

- Lead 3.144821 from 12 helical edges (fit residual < 2e-4 mm); right-hand. Flank axial section: straight to
  0.0002 mm on each side of r = 8, slopes 0.36545 (r < 8) and 0.36491 (r > 8); tooth = pi/2 at r = 8; root land
  0.72842, tip land 0.84 (measured on edges). End cones 60 degree half-angle through (r 6.84298, z +/-16).
- Master CoM: OCC GProp gives x = +0.0118, the triangulated value is -0.0137 (the rebuild agrees with the mesh value);
  `hedef.json` uses the mesh CoM. Volume GProp vs mesh differs 0.02 % (< 0.5 %): GProp volume kept.
- `olc.py` original vs itself (`is/olc_kendi`): **83.00 / 85** (§1 40, §2 10, §3 8.00, §4 30 / 30, §5 4 / 4).
  Shortfall 2.00 = §3 pose of H1: the set screw is nearly axisymmetric (its principal axes are degenerate), so olc.py
  falls back to ICP, which returns 0.69 degrees for the identical body. Not caused by the lists; caused by the body's
  symmetry. Same effect on any rebuild: olc on the spec rebuild gave H1 1.78 degrees and P01 34.8 degrees (P01 is also
  axisymmetric to the inertia, Ixx ~ Iyy) -> §3 pose 0 / 4 for a near-perfect rebuild. Lead decision needed (see report).
- `olc.py` original vs the spec rebuild: 81.00 / 85 (geometry 40.00, features 30 / 30, drawing 4 / 4, pose 0).
- Features: 30 items (thread flanks are free-form, checked by regional deviation; no kernel-dependent counts).
  Drawing rows: 18 / 6 / 32 / M4 reproduce; 16 mm pitch diameter has no face (modelde_var false).
- Interference: the screw fills the hole at the same diameter; overlap 0 (no pair > 8 mm3).
- Undetermined: thread of the set screw and its hole (not modelled in the master); flank form type (involute vs
  straight) beyond the measured axial section.
