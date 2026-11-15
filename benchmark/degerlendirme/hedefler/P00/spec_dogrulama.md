# P0 spec verification

Reference = `orijinal.step` (repoda: referans.step), built by `is/p0_build.py` (build123d 0.11.1, AP214, mm); measured back with OCP by
`is/p0_measure.py` / `is/p0_gizli.py`.

| Body | spec V mm3 | STEP V mm3 | dV % | dCoM mm | dBbox mm |
|---|---|---|---|---|---|
| P01 Plate | 57535.133 | 57535.1329 | 0.0000 | 0.0000 | 0.000 |

Analytic cross-check: 100*60*10 - 4*(3^2 - pi*3^2/4)*10 - pi*10^2*4 - 4*pi*3^2*10 = 57535.13 mm3 (agrees).
Every recipe in `ozellikler.json` (14 items) and `resim_olculeri.json` (9 rows) reproduces its `nom` on the reference.
Undetermined items: none. No PDF, no B, no C for P0.
