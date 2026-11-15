# P37 spec verification (freestanding 24-unit electronics rack, 9 bodies)

Source: original STEP (inch-based model, read in mm by OCC), loaded with `olc_cekirdek.load_step`: 9 solids,
**16 empty shells dropped** (`bos_kabuk_atilan: 16`). Spec unit: inch. Scripts: `_gizli\is\` (s01 structure, s02 /
s02b face dumps, g_stud / g_hand thread analysis, s03 interference, s05 targets, s06 hidden lists, s07 recipe check,
s08 target back-check, r_govde rebuild from the spec text).

## s08: spec section 6 table against the original

| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| H1-a | -0.0000 | -0.0012 | 0.0008 | 0.0006 |
| H1-b | -0.0000 | -0.0012 | 0.0008 | 0.0006 |
| H1-c | -0.0005 | -0.0012 | 0.0018 | 0.0006 |
| H1-d | -0.0005 | -0.0012 | 0.0018 | 0.0006 |
| P01-a | +0.0000 | +0.0000 | 0.0005 | 0.0006 |
| P01-b | +0.0000 | +0.0000 | 0.0005 | 0.0006 |
| P02-a | +0.0000 | -0.0000 | 0.0010 | 0.0006 |
| P02-b | +0.0000 | -0.0000 | 0.0010 | 0.0006 |
| P03 | +0.0000 | +0.0000 | 0.0003 | 0.0006 |

All 9 bodies in the table; residuals are rounding of the 4-decimal inch table only.

## Rebuild from the spec text (r_govde.py, build123d)

Feet, uprights and cap rebuilt from the section 4 profiles, hole tables and rounds alone (P01-b / P02-b as mirrors):

| body | dV % | dA % | dCoM mm | dbbox mm | faces rebuild / original |
|---|---|---|---|---|---|
| P01-a | +0.0000 | +0.0000 | 0.0000 | 0.0000 | 16 / 18 |
| P01-b | +0.0000 | +0.0000 | 0.0000 | 0.0000 | 16 / 18 |
| P02-a | -0.0000 | +0.0000 | 0.0000 | 0.0000 | 211 / 408 |
| P02-b | -0.0000 | +0.0000 | 0.0000 | 0.0000 | 211 / 408 |
| P03 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 22 / 26 |

Face-count differences are kernel splits only (the source writes each hole as two half-cylinders per sheet). The
right upright is an exact mirror of the left (also proves the web holes are identical on both). The studs (helical
modelled 10-32 thread) were not rebuilt; their description is measured (major 0.19, root 0.1494 from the B-spline flank
samples, pitch 1/32 from the crest-land helix slope 0.03172 in/turn, right hand on all four, 45 deg end chamfer from
the cone faces, length 0.63). A UN basic profile at pitch diameter 0.1697 over 0.63 gives about 0.0142 in3, consistent
with the measured 0.01429 in3.

## Interference (s03, capped BoolWorker after bbox pre-filter)

10 bbox-overlapping pairs checked (feet-uprights, cap-uprights, studs-uprights): every common volume 0.0 mm3.
`hedef.json girisimler` = [] (all contacts are face-to-face touching).

## GProp vs mesh volume

Sheet parts differ by < 0.001 %; studs by 0.36-0.38 % (fine helical faces): below 0.5 %, so the GProp volumes stay the
targets.

## Hidden lists

- `ozellikler.json`: 75 items (feet 17, uprights 32, cap 10, studs 13, assembly 3): extents, sheet thicknesses, bend radii,
  hole counts (72 / 24 / 4 / 2 / 4 per body), hole diameters, hole pitches (0.625, 0.5, 1.75), hole positions from the
  end faces / web face, corner-round counts (cap with `ayri_yuzler`, since its rounds share two cylinder surfaces),
  thread / chamfer regions on the studs. **s07: BAD 0** (every recipe reproduces its `nom` on the original).
- `resim_olculeri.json`: 7 rows, all printed values of the catalogue drawing (20.46, 48.12, 15.00, 3.00, 1.75, 19,
  10-32); 6 measured OK, "19 in component width" `modelde_var: false` (nominal panel width, no feature).
- `parametreler.json`: rack unit pitch 1.75, unit count 24, hole column spacing 18.31, upright thickness 0.1, depth 15.0.
- `kaynak.json`: `step_govde_sirasi` = P01-a, P01-b, P03, P02-a, P02-b, H1-a, H1-c, H1-d, H1-b.

## Undetermined items

Threads of the equipment holes (plain in the source), fasteners between parts (none modelled), purpose of the dia 0.15
and web holes, levelling feet / casters, paint. Stud thread start phase is given as measured (crest on +Y at 0.0332 from
the free end), effect marginal.

## Source conflicts

None. The drawing agrees with the model on every checkable printed value. Note for producers: the two stud pairs are
not mirror-placed (left pair around y +7.29, right pair around y -7.21); the spec states this explicitly.

## Tier

Index tier very-hard (cok_zor) **confirmed**: 9 bodies, 2 x 408-face uprights with 101 patterned holes each in an
irregular rack-unit pattern, bent sheet sections, and 4 studs with modelled helical threads.

## olc self-check result

`olc.py` original vs itself (2026-11-12, `_gizli\is\olc_kendi\`): **85.00 / 85** (geometry 40.00, completeness 10.00, assembly 10.00, features 20.00, drawing 5.00). 9 / 9 bodies matched, IoU 1.000000 each, interference 0 / 0.
