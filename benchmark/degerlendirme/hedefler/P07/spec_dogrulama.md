# P7 · spec target table vs original STEP

Measured with OCP (GProp volume/area/CoM, optimal bbox) on the original STEP, in its own frame, no alignment.
Spec values are as printed in `A/spec.md` (inch to 4 decimals, mm3 / mm2 to 0.1).

| Body | ΔV % (mm3 col) | ΔA % (mm2 col) | ΔCoM mm | Δbbox mm (max of 6) |
|---|---|---|---|---|
| P01 | -0.000 | +0.000 | 0.0016 | 0.0013 |
| P02 | -0.000 | -0.000 | 0.0011 | 0.0000 |
| P03 | -0.000 | +0.000 | 0.0005 | 0.0000 |
| P04 | +0.000 | +0.000 | 0.0014 | 0.0012 |
| P05 | -0.000 | -0.000 | 0.0011 | 0.0000 |
| P06 | -0.000 | +0.000 | 0.0009 | 0.0001 |
| P07 | +0.001 | +0.001 | 0.0005 | 0.0000 |
| P08 | +0.000 | -0.001 | 0.0006 | 0.0011 |
| P09 | +0.000 | -0.000 | 0.0014 | 0.0002 |
| P10 | -0.000 | +0.001 | 0.0010 | 0.0010 |
| H1-a | -0.006 | -0.001 | 0.0021 | 0.0011 |
| H1-b | -0.006 | -0.001 | 0.0021 | 0.0011 |
| H1-c | -0.006 | -0.001 | 0.0021 | 0.0011 |
| H1-d | -0.006 | -0.001 | 0.0021 | 0.0011 |
| H2-a | -0.011 | -0.007 | 0.0007 | 0.0000 |
| H2-b | -0.011 | -0.007 | 0.0008 | 0.0011 |
| H2-c | -0.011 | -0.007 | 0.0009 | 0.0005 |
| H3-a | +0.012 | +0.003 | 0.0000 | 0.0002 |
| H3-b | +0.012 | +0.003 | 0.0000 | 0.0002 |
| H4-a | -0.009 | +0.013 | 0.0015 | 0.0000 |
| H4-b | -0.009 | +0.013 | 0.0015 | 0.0000 |
| H5 | +0.015 | -0.004 | 0.0015 | 0.0013 |
| H6 | +0.023 | -0.009 | 0.0013 | 0.0003 |
| H7 | +0.007 | -0.001 | 0.0009 | 0.0010 |
| H8 | +0.011 | +0.008 | 0.0015 | 0.0009 |

Largest: |ΔV| 0.0233 (H6) %, |ΔA| 0.0127 (H4-b) %, ΔCoM 0.0021 (H1-d) mm, Δbbox 0.0013 (P01) mm.
Hardware rows: the in3 column is rounded to 4 decimals (H6 0.0026 in3 = 0.67 % rounding); the mm3 column is exact to
0.1 mm3 and is what the table above compares. Assembly: V 2 931 707.9 mm3, A 404 508.6 mm2, CoM (-0.0813, 4.3380,
-2.9512) in, bbox X [-6.6986, 4.9100] Y [0, 15.0750] Z [-9.2500, 2.9689] in, all equal to spec §6.

## Body map and interference set

25 solids, each matched to its spec name by bbox (max error 0.00005 in), volumes equal (`is/s01_govdeler.py`).
Interference set of the original (common volume > 8 mm3): **P01-P09 321.76 mm3** (0.0196 in3: frame tip R0.25 x 0.1 inside
the handwheel hub), as spec §5 states. All other pairs: no volumetric overlap (`is/girisim_tum.json`).

## Hidden lists checked on the original

- `ozellikler.json`: 96 items, 96 reproduce `nom` within tol, every `bolge` regional deviation 0.000 and non-empty
  (`is/s03_log.txt`). Counts with no explicit spec number (F33 bead tori, F46 rack flank planes 54, F60 cones) were read
  from the original. F81 (spoke blends R0.15) has `olcum: null` (shape by region only): olc.py also counts the B-spline
  blend faces (13) where my counter sees 1 torus.
- `resim_olculeri.json`: 14 printed dims, 13 measurable all pass (tol 0.005 in), 1 `modelde_var: false` (max stroke 6.875).
  Two rows use olc.py extensions: 5.375 (`duzlem_mesafe_govdeler`, P01 head underside to P04 top) and 4 (`ekle_mm` 12.7:
  flange front to channel back wall 3.5 + 0.5).
- `parametreler.json`: ram section 1.0, base length 10.75, rack pitch 0.26, throat 4.0, ram length 9.75.

## Cross-check with the lead's olc.py 1.0 (original vs original)

`is/olc_kendi/olcum.md`: total §1-§5 84.69 / 85 (geometry 40, completeness 10, assembly 10, drawing 5/5, features 19.69).
The two non-`tam` items were fixed afterwards: F79 (point 1 sat nearest a coaxial cone -> moved to x = -3.70 on the boss
cylinder; `tarifler.olc` now gives 63.5461 mm, `is/s07_olc_kontrol.py`) and F81 (see above). Two reruns of olc.py after
the fix died silently mid-run (exit 255 / no output, OCC native crash, same symptom P9 reported); not re-confirmed by a
full olc.py run.

## Undetermined (spec §7, unchanged)

- Pinion tooth geometry, pitch circle and ram-to-shaft ratio (no pinion teeth in the source).
- Rotary plate pivot / retention (none in the geometry).
- Thread standards of studs and screws (only modelled pitch and profile known).
- Materials other than cast-iron frame and steel ram.
- Upper-end limit of ram travel beyond the cap and head geometry.
- Handwheel hub-to-shaft connection (they simply overlap 0.1).

## Source note for B

The catalogue PDF's view images are blank white in the source file itself (all three view images: min pixel 255); only
dimension lines, values and the small iso thumbnail are visible. `B/cizim.pdf` is therefore dimensions-only; B for P7
relies on the photos.

## Hidden-list addition (2026-11-11)
Backup: `is/lead_yedek_2026-11-11/`. Four items were added so the list covers the four local flaws of the old blind rebuild (`blind_run_01/out/assembly.step`). Each item has a real measurement plus an r 3 mm region on the original face at the flaw (about 50-200 global samples per region):
- F97 P01 concave R0.03 base-top/throat-flange-front fillet, +X flange-end corner blend (dia 1.524 on the fillet cylinder; region on corner blend face 211).
- F98 P01 concave R0.04 rim-to-base fillet, rear-end corner blend +X (dia 2.032; region on blend face 181).
- F99 P04 slot A mouth: -X wall top chamfer 45 deg running out into the plate rim chamfer (angle of chamfer plane 40 to wall plane 10; region on blend face 39).
- F100 P04 slot D mouth: +Z wall top chamfer 45 deg (planes 37 / 18; region on blend face 38).
olc.py: original vs itself (`k2c_pres_P7`) 85.00 / 85, all four tam; original vs old rebuild (`k1c_pres_P7`) S4 19.60 (98/100; the four items are yakin with regions 0.300 / 0.073 / 0.450 / 0.521 mm, the same as the old report), total 84.12.
