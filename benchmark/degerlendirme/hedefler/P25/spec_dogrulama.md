# P25 spec verification

Master: 6 solids (P01 case 379 faces, P02 window tube 6, P03 flow tube with scale 240, P04 float ball 2, H1-a / H1-b
nuts 24 each). **No empty or zero-volume shells**: olc's loader drops 0 bodies, 0 empty shells, 0 free shells
(`is/s01_yapi.py`). The file is inch (SolidWorks AP203 export); OCC reads it in mm. STEP solid order:
P02, P03, P04, P01, H1-a, H1-b (`kaynak.json` `step_govde_sirasi`).

## Target table back-check (`is/s08_dogrulama.py P25`, spec section 8 vs the master)

| Body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | +0.0000 | -0.0000 | 0.0009 | 0.0000 |
| P02 | +0.0000 | -0.0000 | 0.0000 | 0.0000 |
| P03 | +0.0001 | -0.0001 | 0.0006 | 0.0000 |
| P04 | +0.0102 | +0.0025 | 0.0000 | 0.0000 |
| H1-a | +0.0002 | -0.0001 | 0.0013 | 0.0013 |
| H1-b | +0.0002 | -0.0001 | 0.0013 | 0.0013 |

(Differences are the 4-5 digit rounding of the inch table; `hedef.json` holds the unrounded mm values.)

GProp vs mesh integral (0.01 mm chord, `is/s06_hedef.py`): P01 +0.027 %, P02 -0.024 %, P03 -0.28 %, P04 -0.66 %,
nuts +0.03 %. P03 / P04 differ only because of the coarse check mesh on very small radii (0.125 / 0.0625 in); at olc's
0.002 mm chord the difference falls below 0.5 % (see the olc log), so all targets are GProp values.

Interference (capped boolean worker, bbox pre-filter, `is/s03c_girisim.py`): all 8 candidate pairs have common volume
0 (P01-P02, P01-P03, P01-P04, P02-P03, P02-P04, P03-P04, P01-H1-a, P01-H1-b). `girisimler` = [].

## How the geometry was read

- Face census and 6-digit face dumps (`is/s02_dump.py`, `is/s02b_dump6.py`, `is/b/dump*_NN.txt`); section of the
  valve / knob in the plane x = 0 (`is/kesit2.py`).
- Threads (`is/s05_dis.py`, `is/s05b_alt.py`, results `is/s05_dis.txt`, `is/s05b_alt.txt`): half-plane sections of both
  fittings. External 18 TPI: crest r 0.28125, root r 0.24517, crest / root flats 0.00694, 30 deg flanks; internal 27 TPI
  taper: root r = 0.2025 - 0.031135 d (fit over 10-11 root flats per half plane, residual < 1e-5), crest = root -
  0.02357, root flat 0.0052, crest flat 0.00463. Phases measured in +X, +Y, -X, -Y half planes of the upper fitting
  (each quarter turn +P/4: right hand) and in +X, +Y of the lower fitting: identical, so the lower fitting is a pure
  translation of the upper one.
- Scale (`is/s04_halka.py`, `is/s03_yazi.py`, `is/s03c_rakam.py`, picture `is/yazi.png`): 20 marks, lower faces
  y = -1.5 + k 0.1584375 (fit residual < 1e-6), ring sector r 0.125-0.135, ends on radial planes at +-1 rad; numerals
  0 / 10 / 20 / 30 / 40 / 50 raised 0.01, read from a rendering of the raised faces.
- Knob: 64 land faces (cylinder r 0.40625) and 128 flank planes (normals at +-15 deg to the tangent), groove bottom
  r 0.39125.

## Hidden lists

- `ozellikler.json`: 64 items; every recipe evaluated on the master with `tarifler.olc` (`is/s07_kontrol.py P25`): all
  numeric items reproduce `nom` (points lie on the master faces within 6e-6 mm); 12 items are region-only (chamfers,
  emblem, numerals, threads). Thread items come from `is/s05c_dis_noktalar.py` (crest points chosen from the measured
  phases, not on face seams).
- `resim_olculeri.json`: 8 rows = every dimension printed on the catalogue drawing (1.25, 5.5, 4.5, 1.4, 2.34, 0.575,
  9/16-18 x2, 1/8 NPT x2); 7 measured on the master and reproduced exactly; "1/8 NPT" is a nominal pipe-size call-out
  with no single-number recipe (`olcum: null`, the modelled taper thread is in the features list).
  The drawing's 5.5 is end face to end face (the master's top button adds 0.0625; stated in the spec).
- `parametreler.json`: case height 5.5, case width 1.25, fitting spacing 4.5, knob diameter 0.8125, graduation pitch
  0.1584375.

## Gate

**olc.py original vs itself = 84.33 / 85** (`is/olc_kendi/`, 1076 s, peak 1.07 GB): geometry 40.00, completeness 10.00,
assembly 9.33 (pose 3.33 / 4, assembly 3.00, interference 3.00), features 20.00 (64 / 64), drawing 5.00 (7 / 7). Every
body has IoU 1.000000, dV / dA / dCoM / dbbox 0, max deviation <= 0.0005 mm.

**Shortfall 0.67 = pose of P04 only, caused by the original file, not by the lists:** P04 is a perfect sphere (two
spherical faces), so its three principal moments are equal and its principal axes are undefined; olc's orientation step
returns 7.88 deg for the master against itself (numerical noise of a degenerate inertia tensor), which zeroes P04's pose
share (4 x 1/6 = 0.67). No list change can remove it; the grader may treat the P04 orientation as not applicable.

Audit `paket_denetle.py P25`: 6 bodies = 6, volume difference 0.0000 %, assembly bbox difference 0.0000 mm; spec leak
scan `spec_tara.py P25`: 0 findings.

## Undetermined

- The numeral typeface (glyph outlines): only position, extent, height (about 0.065) and the raised height 0.01 are
  given; the three numeral features are region checks.
- Nothing else. Internals (flow passages, seals, valve needle) are not in the master and the spec says so.

## Tier

"zor" (hard) confirmed: 6 bodies; two modelled threads per fitting (straight 9/16-18 external and 1/8-27 tapered
internal, with phases), a 64-groove knurl, a raised crescent emblem, a scale with 20 raised marks and raised numerals
(free-form glyph faces), a valve seat cut with 8:15 ramps.
