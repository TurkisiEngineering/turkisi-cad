# P2 spec verification

Independent rebuild of the spec text (`is/s04_rebuild.py`: revolve about X ∩ plan prism, grip revolve, bore) compared
in memory with the master STEP (triangulation 0.005 mm, 20 000 samples per direction).

| Body | spec V mm3 | master V (B-rep / mesh) | rebuild V (B-rep / mesh) | dV % | dCoM mm | dBbox mm | dev P95 / max mm |
|---|---|---|---|---|---|---|---|
| P01 Crank handle | 39620 | 39621.11 / 39613.60 | 39618.48 / 39613.49 | 0.007 | 0.003 | 0.000 | 0.0018 / 0.0053 (both ways) |

- Every arc of the two revolve profiles was fitted on the master with residual < 1e-9 mm (R2.5, R18, R30, R37.5,
  R10.5, R0.5, R17.1, R40.502, sphere R4.1); plan blends R22.5 / R13.5 are exact cylinders tangent to the strip lines
  and the circles (centre distances 38.000 = 22.5 + 15.5 and 21.500 = 13.5 + 8).
- The outer arm face sits at x = 52.68507 (not a round number) and its arc meets it with a 2.3 deg kink; the R37.5 /
  R10.5 junction has a 7 deg kink; these are source facts and are stated in the spec.
- Master contains 16 empty zero-area shells (96 faces) at (48.0, -53.626, -6.249); stated in the spec as an artefact.
- Feature recipes (26) and drawing rows (6 with recipes) reproduce on the master; the 80 and 67 mm rows run to the
  spherical tip and are left as hand measurements.
- C recipes reproduce on the C rebuild (CR=120, bore 12) except bbox X, which read 125.58 on the exported test STEP
  because the test kernel drops the spherical cap on STEP export (in memory 128.0). Y extent expectation is 145.5
  (grip barrel radius 10, not the boss radius 8).
- Test-kernel note for the lead: writing the grip revolve (arc touching the axis) to STEP with build123d 0.11.1 lost
  the R4.1 cap face; producers on that tool may hit the same problem.
- Undetermined: draft / casting tolerances; nothing else.
