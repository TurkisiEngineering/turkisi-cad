# Build log — P01 Plate (r172610)

## Ne yapıldı
- Kaynak: yalnız `girdi/spec.md`. Birim mm, global çerçeve spec'teki gibi (alt yüz Z = 0, XY'de orijine ortalı,
  uzunluk X boyunca). Taşıma/yeniden hizalama yok; her şey yerinde kuruldu.
- Araç: SolidCraft CLI, komut dizisi `plate_build.json` (`solidcraft-cli run`). Tamamen aracın kendi özellikleriyle
  kuruldu; içe aktarma yok.
- Sıra spec'teki gibi:
  1. Parametreler: `L, W, T, R_corner, D_hole, E_hole, D_pocket, H_pocket` (bkz. `parametreler.md`).
  2. **F1**: `SK_F1_Plate` (XY) üzerinde (−L/2, −W/2)–(L/2, W/2) dikdörtgeni, `F1_Plate_Block` ile +Z yönünde `T`
     ekstrüzyon, gövde adı **`P01 Plate`**.
  3. **F2**: `solid.fillet`, 4 dikey köşe kenarı (X = ±50, Y = ±30), yarıçap `R_corner`. Üst/alt kenarlar keskin.
  4. **F3**: `SK_F3_Holes` (XY) üzerinde 4 daire Ø`D_hole`, merkezler (±(L/2−E_hole), ±(W/2−E_hole)) = (±42, ±22);
     `F3_Corner_Holes` ile Z 0→T kesme (tam kalınlık, düz delik; havşa/fatura yok).
  5. **F4**: `SK_F4_Pocket` (XY, ofset `T`, yani Z = 10) üzerinde Ø`D_pocket` daire, `F4_Central_Pocket` ile −Z yönünde
     `H_pocket` kesme: düz taban Z = 6, taban ve ağız kenarları keskin.
- Çıktılar: `plate.sc` (native belge), `final_ap242_raw.step` (SolidCraft'ın ham STEP çıktısı), `final.step` (AP214).

## Nerede takıldım / çözüm
- **STEP şeması:** `file.export_step`, `file.export` ve `run --out` için şema seçme parametresi yok. SolidCraft her
  zaman `AP242_MANAGED_MODEL_BASED_3D_ENGINEERING_MIM_LF` yazıyor (`--param-check strict` altında `schema`, `protocol`,
  `ap`, `step_schema`, `format` anahtarlarının hepsi "unknown key" diye reddedildi). Teslim AP214 istediği için
  `step_to_ap214.py` yazıldı. Betik yalnız şunları değiştiriyor: `FILE_SCHEMA` →
  `'AUTOMOTIVE_DESIGN { 1 0 10303 214 1 1 1 1 }'`, `APPLICATION_CONTEXT` ve `APPLICATION_PROTOCOL_DEFINITION` →
  `automotive_design`, `PRODUCT` adı → `P01 Plate` (dosya adından gelen "final" yerine).
  Dosyadaki varlık tiplerinin hepsi (MANIFOLD_SOLID_BREP, ADVANCED_BREP_SHAPE_REPRESENTATION, ADVANCED_FACE, PLANE,
  CYLINDRICAL_SURFACE, LINE, B_SPLINE_CURVE_WITH_KNOTS / RATIONAL_B_SPLINE_CURVE, PRODUCT*, SHAPE_REPRESENTATION*,
  SI_UNIT…) AP214 AUTOMOTIVE_DESIGN şemasında da var. Bu yüzden başlığı değiştirmek geçerli bir AP214 dosyası verir;
  geometri varlıkları değişmez. Dönüştürülen dosya SolidCraft'a geri okutularak doğrulandı (aşağıdaki tablo
  `final.step`'ten ölçüldü). Harici bir AP214 doğrulayıcıyla şema denetimi yapılmadı (kurulu değil).
- Başka takılma olmadı; tüm özellikler uyarısız hesaplandı (`warning: null`, `error: null`).

## Bilerek yapılan yorum / basitleştirme
- Spec'te belirsiz madde yok. Tek yorum: gövde adı spec'teki tam adıyla **"P01 Plate"** verildi (ID + ad).
- Delikler `solid.hole` yerine eskiz daireleri ve kesme ekstrüzyonuyla açıldı. Spec "plain through-hole, no chamfer/
  counterbore" diyor; sonuç geometrisi aynı, eskiz tabanlı yolda konumlar parametrelere daha açık bağlanıyor.
- Native belgede SolidCraft silindirik yüzleri ikiye bölüyor (21 yüz); STEP çıktısında bunlar birleşik, 16 yüz
  (spec'teki bilgi amaçlı sayıyla aynı).

## Ölçüm: spec hedef tablosuna karşı
`solidcraft-cli eval --in teslim/final.step` (AP214 dosyası) ile:

| Büyüklük | Spec | Ölçülen | Fark | Tolerans |
|---|---|---|---|---|
| Hacim mm³ | 57535.133 | 57535.326 | +0.193 (+0.0003 %) | ±0.5 % ✔ |
| Alan mm² | 15912.159 | 15912.157 | −0.002 | — ✔ |
| CoM X | 0.0000 | 0.0000 (1.6e−8) | 0 | ±0.05 ✔ |
| CoM Y | 0.0000 | 0.0000 | 0 | ±0.05 ✔ |
| CoM Z | 4.9345 | 4.93448 | −0.00002 | ±0.05 ✔ |
| Xmin / Xmax | −50 / 50 | −50.000 / 50.000 | 0 | ±0.01 ✔ |
| Ymin / Ymax | −30 / 30 | −30.000 / 30.000 | 0 | ±0.01 ✔ |
| Zmin / Zmax | 0 / 10 | 0.000 / 10.000 | 0 | ±0.01 ✔ |
| Yüz sayısı | 16 | 16 | 0 | bilgi ✔ |
| Gövde / kabuk | 1 katı | 1 gövde, 1 kapalı kabuk | — | ✔ |

Analitik kontrol: 100·60·10 − (4−π)·3²·10 − 4·π·3²·10 − π·10²·4 = 59640 − 670π = 57535.133 mm³ (spec'le birebir).
Ölçülen +0.19 mm³ fark SolidCraft'ın hacim ölçümündeki sayısal hatadır.

Ek kontroller (`model.faces`, native belge): yuvarlatma eksenleri (±47, ±27), R 3; delik eksenleri (±42, ±22), R 3;
cep ekseni (0, 0), R 10; cep tabanı Z = 6 düzleminde; üst yüz Z = 10, alt yüz Z = 0.
Parametrik test: `H_pocket` 4'ten 5'e çıkınca hacim 314.14 mm³ (= π·10²·1) azaldı. Temiz bir klasörde
`yeniden_kur.md` adımlarıyla sıfırdan kurulum aynı sonucu verdi (`../dogrulama/temiz/`).

## Dosyalar
- `final.step`: AP214, tek gövde `P01 Plate`, mm.
- `plate.sc`: SolidCraft native belge (parametreler + zaman çizelgesi).
- `plate_build.json`: modeli sıfırdan kuran komut dizisi.
- `step_to_ap214.py`: STEP başlığını AP242'den AP214'e çevirir.
- `final_ap242_raw.step`: SolidCraft'ın dönüştürülmemiş ham çıktısı (izlenebilirlik için).
- `../dogrulama/`: ölçüm JSON'ları, parametre testi ve temiz yeniden kurulum denemesi.
- Not: komut listesini incelemek için birkaç geçici dosya (`solidcraft-cli commands` dökümü, örnek betik) oturumun
  geçici scratchpad klasörüne yazıldı. Teslimle ilgileri yok.
