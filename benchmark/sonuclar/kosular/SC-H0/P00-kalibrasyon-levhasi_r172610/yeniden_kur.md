# Yeniden kurulum — P01 Plate

Gerekli: SolidCraft (`C:\Program Files\SolidCraft\solidcraft-cli.exe`) ve Python 3 (yalnız STEP başlığını AP214'e çevirmek için).

Temiz bir klasöre `plate_build.json` ve `step_to_ap214.py` dosyalarını kopyalayıp o klasörde (Git Bash):

```sh
SC="/c/Program Files/SolidCraft/solidcraft-cli.exe"

# 1) Komut dizisini çalıştır: parametreler, F1 blok, F2 köşe yuvarlatma, F3 delikler, F4 cep.
#    Native belgeyi ve SolidCraft'ın STEP çıktısını (AP242 başlıklı) yazar.
"$SC" run plate_build.json --save plate.sc --out final_ap242_raw.step

# 2) STEP şemasını AP214'e (AUTOMOTIVE_DESIGN) çevir; geometriye dokunmaz.
python step_to_ap214.py final_ap242_raw.step final.step

# 3) (İsteğe bağlı) Doğrula: hacim, alan, ağırlık merkezi, sınır kutusu, yüz sayısı.
"$SC" eval --in final.step
```

PowerShell'de:

```powershell
& "C:\Program Files\SolidCraft\solidcraft-cli.exe" run plate_build.json --save plate.sc --out final_ap242_raw.step
python step_to_ap214.py final_ap242_raw.step final.step
```

Beklenen (`eval`): 1 gövde `P01 Plate`, hacim ≈ 57535.33 mm³, alan ≈ 15912.16 mm², CoM ≈ (0, 0, 4.9345),
kutu X −50…50, Y −30…30, Z 0…10, 16 yüz, kapalı.

Parametre değiştirip yeniden üretme örneği (cep derinliği 5 mm), `p.json`:

```json
{"commands":[{"command":"parameters.change","params":{"name":"H_pocket","expression":"5 mm"}}]}
```

```sh
"$SC" run p.json --in plate.sc --save plate_h5.sc --out plate_h5_ap242.step
```

Not: `plate.sc` SolidCraft GUI'de (`solidcraft.exe`) açılabilir; zaman çizelgesi ve parametreler düzenlenebilir.
`"$SC" script plate.sc --out x.json` belgenin geçmişini yeniden komut dizisine döker.
