# P22 spec verification

Master: one solid. Outer shell 42 faces; plus **16 empty micro void shells** (6 planar faces each, 0.0001 mm cubes,
volume ~3e-13 mm3, around (-129.54, 38.598, -16.1925) mm inside the web), a writer artefact. `olc_cekirdek.load_step`
drops them (`bos_kabuk_atilan: 16`); hedef.json gives `yuz_sayisi` 42 (the raw solid has 138 faces). The spec does not
mention them.

| Body | spec V mm3 | master V (B-rep / mesh 0.01) | dV % | dA % | dCoM mm | dBbox mm |
|---|---|---|---|---|---|---|
| P01 Bracket | 105108.06 | 105108.059 / 105105.495 | +0.0000 (mesh -0.0024) | -0.0000 | 0.0014 (inch rounding of the table) | 0.0000 |

(`is/s05_hedef.py`, `is/s08_dogrulama.py`.)

- **Independent rebuild** from the spec values only (`is/s04_yeniden.py` -> `is/rb_yeniden.step`): one solid, volume
  diff +0.000001 %, bbox identical; two-way face-sampled deviation to the master (`is/s04b_sapma.py`) <= 0.005 mm on
  every real face (the only larger residues are the 16 micro void shells, 0.18 mm from any rebuilt face).
- Thickness 3.0378 mm = 0.11960 in (11 gauge). Inside bend radius = t, outside = 2 t, both bends 90 deg; bend axes
  X = -5.7608 / Y = 3.8804, Z = -0.5108 in.
- All 37 `ozellikler.json` recipes and 4 measurable `resim_olculeri.json` rows reproduce their `nom` on the master
  (`is/s07_kontrol.py`, BAD 0); every recipe point lies on its face (max 3e-4 mm).
- Drawing: catalogue sheet with 12in, 8in, 1.5in and notes (11 ga., No. 12 screw, right side mount). Gauge row measured
  as the sheet thickness; screw size and mounting position have no geometric counterpart (`modelde_var: false`). No
  drawing / 3D conflicts.
- Gate: `olc.py` original vs itself (`is/olc_kendi/`): **85.00 / 85** (geometry 50, completeness 10, assembly 0 (single body, not applicable), features 20 / 20, drawing 5 / 5); IoU 1.000000, max dev 0. Audit `paket_denetle.py P22`: 1 body = 1 body in the STEP, volume diff 0.0 %, bbox diff 0.0 mm.

## Undetermined
- Flat blank / bend allowance (K-factor) of the master: cannot be measured from the formed solid. The spec describes the
  formed part only and says so.
- Paint layer: not modelled in the master.

## Tier
- Index tier "hard" looks too high: one sheet-metal solid, two plain 90 deg bends with R = t, 8 round holes, two R 0.25
  corner rounds and one corner relief cut. No threads, gears or freeform faces. The only traps are the odd decimals
  (multiples of t = 0.1196 in), the staggered hole rows and the corner relief geometry. Suggested tier: medium (easy for
  a tool with sheet-metal features).
