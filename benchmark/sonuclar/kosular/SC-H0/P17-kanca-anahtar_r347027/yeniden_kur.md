# Yeniden kurma — P01 Spanner

Gerekenler: SolidCraft (`C:\Program Files\SolidCraft\solidcraft-cli.exe`), Python 3 (yalnız betik üretmek için).

Bu klasörün temiz bir kopyasında (Git Bash):

```sh
# 1) Komut dizisini üret (spanner_build.json zaten teslimde var; bu adım onu sıfırdan yeniden yazar)
python gen_script.py spanner_build.json

# 2) Modeli sıfırdan kur, SolidCraft belgesini kaydet, STEP (AP242) dışa aktar
"/c/Program Files/SolidCraft/solidcraft-cli.exe" run spanner_build.json --save P01_Spanner.sc --out final.step

# 3) (isteğe bağlı) Ölçüm: hacim, alan, ağırlık merkezi, bbox, yüz sayısı (mm cinsinden yazar)
"/c/Program Files/SolidCraft/solidcraft-cli.exe" eval spanner_build.json
"/c/Program Files/SolidCraft/solidcraft-cli.exe" eval final.step
```

PowerShell'de aynısı:

```powershell
python gen_script.py spanner_build.json
& "C:\Program Files\SolidCraft\solidcraft-cli.exe" run spanner_build.json --save P01_Spanner.sc --out final.step
```

Dosyalar:
- `gen_script.py` — parametreleri ve tüm özellikleri tanımlayan üretici; `spanner_build.json`'u yazar.
- `spanner_build.json` — SolidCraft komut dizisi (74 komut; `solidcraft-cli run/eval` ile oynatılır).
- `P01_Spanner.sc` — SolidCraft belgesi (zaman çizelgesi + parametreler; GUI'de açılıp parametre düzenlenebilir).
- `final.step` — SolidCraft'ın kendi AP242 çıktısı, tek gövde `P01 Spanner`.

Parametre değiştirmek için: `gen_script.py` başındaki `P` listesindeki ifadeyi değiştirip 1–2'yi tekrarlayın,
ya da belgeyi açıp `parameters.change` kullanın (fillet kenar seçimleri sayısal noktadır; bkz. build_log §4).
