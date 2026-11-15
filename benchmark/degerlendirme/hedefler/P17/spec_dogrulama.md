# P17 spec verification

Independent rebuild of the spec text (`is/s03_rebuild.py`: outline extruded +/-1.524 mm, obround slot, R0.39687 rounds
on the handle part, 10 degree conical run-outs) compared with the master STEP by `is/cmp.py` (triangulation 0.002 mm,
20 000 samples per direction) and by `olc.py` (`is/olc_rebuild`).

| Body | spec V mm3 | master V (B-rep) | rebuild V (B-rep / mesh) | dV % | dCoM mm | dBbox mm | dev P95 / max mm |
|---|---|---|---|---|---|---|---|
| P01 Spanner | 3416.715 (0.208501 in3) | 3416.715 | 3416.717 / 3416.669 | 0.0001 | < 0.0005 | 0.000 | 0.0000 / 0.0002 (both ways) |

- Every outline vertex and arc centre comes from the master's edge list (`is/dump_P17_0.txt`); arc tangencies
  checked: R15/32 to R0.707013 (centre distance = sum of radii), R0.707013 to R5/64 (difference), hook top line
  tangent to R5/64. Pin angles 56.710 / 65.000 degrees from the face normals.
- Rounds R1/64 in: 4 straight cylinders + 2 tori; run-out cones (half-angle 10, about the round centre lines) reach the
  sharp corner at x = -12.146 mm (cone radius 0.56126 = corner distance from the centre line).
- Master artefact: 19 empty micro-boxes (114 zero-area faces) inside the solid near (-35.36, 0.335, -3.173) mm; no
  volume; stated in the spec; face count 27 excludes them.
- `olc.py` original vs itself (`is/olc_kendi`): **85.00 / 85** (single body: §1 50, §2 10, §4 26 / 26, §5 4 / 4).
- `olc.py` original vs the spec rebuild (`is/olc_rebuild`): 85.00 / 85.
- Drawing rows: 4.331 in, 0.12 in, 0.625 in and (16 mm) reproduce; 0.063 in has no recipe: my reading is the pin
  underside length 0.0625 in (to be confirmed); 0.781 in / (20 mm) are the range's upper end, not in the model.
- Undetermined: material / finish (product data only).
