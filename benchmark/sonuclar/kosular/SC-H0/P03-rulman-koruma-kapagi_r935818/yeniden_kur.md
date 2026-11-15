# Yeniden kurulum: P01 Guard

Gerekli: SolidCraft (`C:\Program Files\SolidCraft\solidcraft-cli.exe`), Git Bash (bash + awk). Python gerekmez.

Kaynaklar (bu klasörde):
- `gen.sh` — komut dizisini üreten betik (parametreler, taslaklar, özellikler; tek doğruluk kaynağı).
- `P01_Guard_build.json` — `gen.sh 4` çıktısı: SolidCraft komut dizisi (doğrudan çalıştırılabilir).
- `P01_Guard.sc` — SolidCraft belgesi (zaman çizelgesi + parametreler).

## Adımlar (temiz bir kopyada, Git Bash)

```bash
cd teslim
# 1) komut dizisini üret (isteğe bağlı; P01_Guard_build.json zaten hazır)
( bash gen.sh 4; echo "]}" ) > P01_Guard_build.json   # boss taban R0.1 icin: BOSS_ROUND=1 (bu SolidCraft surumunde basarisiz)
# 2) modeli sıfırdan kur, belgeyi kaydet, STEP (AP242) yaz
"/c/Program Files/SolidCraft/solidcraft-cli.exe" run P01_Guard_build.json \
    --save P01_Guard.sc --out final.step
# 3) kontrol: hacim, alan, ağırlık merkezi, sınır kutusu, yüz sayısı
"/c/Program Files/SolidCraft/solidcraft-cli.exe" eval --in P01_Guard.sc
```

Kurulum ~5 dakika sürer (yuvarlatma ve birleştirmeler yavaş). Parametre değiştirmek için `gen.sh` başındaki
`par ...` satırları ya da belgede `parameters.change` kullanılır, ör.:

```bash
"/c/Program Files/SolidCraft/solidcraft-cli.exe" exec parameters.change '{"name":"wall","expression":"0.125"}'
```

## Kurulum sırası (özet)
1. `document.units in`, isimli parametreler.
2. Dış çadır: XY profili (uç duvarlar, eğimler, tepe yayı) simetrik ekstrüzyon → YZ yan duvar dilimiyle kesişim →
   her yan için R_side yuvarlatma.
3. Dış tümsek: XY U-profili → YZ uç yüzü dilimiyle kesişim → her yan için R_hump yuvarlatma → çadırla birleştir →
   her yan için R_conc içbükey yuvarlatma.
4. Aynı 2–3 adımları `wall` içe kaydırılmış değerlerle ayrı "Cavity" gövdesi olarak (tabanı y_cav'e uzatılmış).
5. Flanş: XZ düzleminde y_bot ofsetli taslak, fl_t yukarı ekstrüzyon, birleştir.
6. Bosslar: uzun silindir birleştir → üst düzlemde silindirle kırp (üst + 2 eğim). Taban R0.1 yuvarlatma yalnız BOSS_ROUND=1 ile (çekirdek desteklemiyor, teslimde yok).
7. Cavity gövdesini çıkar; üç girinti silindirini kes.
8. Alt ağız kenarına R_open yuvarlatma.
