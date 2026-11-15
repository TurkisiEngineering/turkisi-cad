# P10 spec verification

Master: 3 solids, no empty shells. Targets (hedef.json) are GProp values; GProp vs fine-mesh volume differs by
0.006 % (P01, P02) and 0.077 % (P03, helical thread), all < 0.5 %, so GProp is kept.

## Independent rebuild of the spec text (`is/s05_rebuild.py`, build123d, inch values x 25.4)

The core and the coating were rebuilt exactly as written in spec §4 / §5 and compared by boolean difference with the
master (`is/s06_cmp.py`):

| Body | spec V mm3 | master V (B-rep / mesh) | rebuild V | master − rebuild | rebuild − master | ΔA % |
|---|---|---|---|---|---|---|
| P01 core | 33952.27 | 33952.27 / 33950.18 | 33952.42 | 0.029 mm3 | 0.000 mm3 | 0.0002 |
| P02 coating | 11952.84 | 11952.84 / 11952.09 | 11952.86 | 0.000 mm3 | 0.025 mm3 | 0.0000 |

The residual 0.02–0.03 mm3 sits on the domes (6-decimal inch rounding of the dome centre / radius) and is spread over
~1900 mm2, i.e. < 0.0001 mm thick. ΔCoM and Δbbox are 0.000 mm.

P03 insert (thread) was not rebuilt as a solid; instead every mesh node of the master insert (20 481 nodes, chord
0.002 mm) was tested against the analytic description of spec §6 (profile, P/8 flats, 30° flanks, RH, phase
z = -0.379218 in at θ = 0, 45° countersinks): worst radial deviation 0.0018 mm (`is/s07_thread.py`).

## Self-check with olc.py (original vs itself)

`is/olc_kendi/olcum.md`: **85.00 / 85** (geometry 40, completeness 10, assembly 10, features 45 / 45, drawing 7 / 7).
`paket_denetle.py P10`: 3 bodies = STEP, volume Δ 0.0 %, assembly bbox Δ 0.0 mm.

## Notes

- Body order in the master: solid 0 = coating (P02), 1 = core (P01), 2 = insert (P03). Pairwise common volume 0.000 mm3
  (contact only), so `girisimler` is empty.
- Construction findings that the spec states explicitly because a naive build differs: (a) the 45° ceiling cone of the
  cavity is clipped by the rim-inner outline Lci (scallop walls run up to z 0.27); (b) the coating's three R0.06 rounds:
  a direct fillet fails in the OCC kernel if applied on the finished coating (the round consumes a whole face: liner
  0.06 thick, top flat ring of zero width at the scallop centres), so the spec builds the rounds on the lobed cup B
  before the dome cap and the cuts; result identical to the master.
- Drawing (catalogue PDF, 7 dimensions, all modelled): 2.52 head dia, 3/8"-16, 1.25 hub dia (taken at z -16.75 mm just
  above the hub end round, 31.80 mm = 1.252 in, inside the 0.005 in written precision), 0.50 hub length, 0.50 thread depth,
  0.68 head thickness, 0.86 head height.
- Tier "shape" (index): confirmed in spirit, but note it is a 3-body part with a modelled helical thread and an
  offset-type coating; harder than a single moulded body.
- Undetermined: none.
