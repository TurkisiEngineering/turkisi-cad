# Yeniden kurma — P0 kalibrasyon plakası (P01 Plate)

## Gerekenler
- SolidCraft (`C:\Program Files\SolidCraft\solidcraft-cli.exe`)
- Python 3 (yalnız STEP başlığını AP242 → AP214 çevirmek için, standart kütüphane)
- Git Bash / herhangi bir POSIX `sh`

## Tek komut
Temiz bir kopyada (yalnız `P0_plate_script.json`, `step_to_ap214.py`, `yeniden_kur.sh` yeter):

```sh
sh yeniden_kur.sh
```

Üretir: `P0_plate.sc` (SolidCraft belgesi, parametrik geçmişiyle), `final.step` (AP214, mm),
`olcum_final_step.json` (STEP'in yeniden ölçümü). CLI başka yerdeyse `SOLIDCRAFT_CLI=/yol/solidcraft-cli.exe sh yeniden_kur.sh`.

## Elle adımlar (betiğin yaptığı)
```sh
CLI="/c/Program Files/SolidCraft/solidcraft-cli.exe"
"$CLI" run P0_plate_script.json --save P0_plate.sc --out _ap242_raw.step   # modeli komut dizisinden kur
python step_to_ap214.py _ap242_raw.step final.step "P01 Plate"              # şema başlığı AP214
"$CLI" eval final.step                                                      # hacim/alan/CoM/bbox kontrolü
```

## Komut dizisi (P0_plate_script.json) özet
1. Parametreler: `L, W, T, corner_r, hole_d, hole_inset, pocket_d, pocket_depth`
2. `PlateSketch` (XY, Z=0): merkez dikdörtgen L×W, merkezi orijine çakışık (dof 0)
3. `F1_PlateBlock`: ekstrüzyon +Z, `T`
4. `F2_CornerRounds`: 4 düşey köşe kenarı, yarıçap `corner_r`
5. `F3_CornerHole`: Ø`hole_d` silindir kesimi, merkez (-(L/2-hole_inset), -(W/2-hole_inset)), Z=-1…T+1
6. `F3_CornerHoles`: 2×2 dikdörtgen desen, aralıklar `L-2*hole_inset`, `W-2*hole_inset`
7. `F4_CentralPocket`: Ø`pocket_d` silindir kesimi, Z=`T-pocket_depth` … T+1 (düz taban)
8. Gövde adı `P01 Plate`

Belgeyi açıp geçmişi tekrar betiğe dökmek için: `"$CLI" script P0_plate.sc --out yeni_script.json`.
