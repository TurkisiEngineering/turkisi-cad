# Build log — P01 Plate (r106866)

**Araç:** SOLIDWORKS 2024 SP5 (rev 32.5.0), Python 3.13 + pywin32, late-bound COM. Betik: `build_plate.py`.

## Ne yaptım
- Spec'i (tek girdi) okudum; eksik bilgi yok (spec §5 "None").
- Çerçeve: SolidWorks Front Plane = XY düzlemi, normali +Z. Böylece model koordinatları spec ile birebir; taşıma yok.
  Birim MMGS (API metre alır, betik mm→m çevirir).
- Özellik sırası spec'teki gibi: F1 blok → F2 köşe radyüsleri (gerçek Fillet özelliği) → F3 4 delik (Through All kesim)
  → F4 merkez cep (üst yüzden 4 mm kör kesim, düz taban, keskin kenarlar).
- Tüm önemli ölçüler global değişken + denklem (bkz. `parametreler.md`). `Plate_L = 120` ile geçici test yapıldı
  (kaydedilmeden kapatıldı): bbox X = ±60, merkezli kaldı.
- Tek katı gövde, adı `P01 Plate` (STEP'te de bu adla yazılıyor).

## Takıldığım yerler
- pywin32 late binding: argümansız SolidWorks metodları bazen değer, bazen bound-method döndürüyor
  (`GetEquationMgr()` → "Member not found"). Çözüm: `g(obj, "Ad")` yardımcı fonksiyonu.
- `SelectByID2` ile koordinattan kenar / çizim segmenti seçimi başarısız oldu. Çözüm: B-rep kenarları/yüzleri ve
  çizim segmentleri nesne üzerinden bulunup `Select4` ile seçiliyor.
- F3 kesimi Front Plane'den (Z=0) yapıldığı için ilk yön (Dir=False) malzemesiz tarafa gidip başarısız oldu; betik
  iki yönü sırayla deniyor, Dir=True başarılı.

## Bilerek basitleştirdiğim / yorumladığım
- Delikler Hole Wizard yerine düz daire + Through All kesim (spec: düz delik, havşa/pah yok — geometri aynı).
- Delik çizimi Z=0 düzleminde; tam kalınlık boyunca kesildiği için sonuç spec ile özdeş.
- Çizimlerde tam tanımlı ilişki seti (tüm sabitler) yok; ölçüler + CenterRectangle'ın kendi ilişkileri yeterli.

## Ölçüm vs. spec hedefi (SolidWorks MassProperty + GetBodyBox, mm)

| Büyüklük | Spec | Model | Fark |
|---|---|---|---|
| Hacim mm³ | 57535.133 | 57535.133 | < 0.001 % |
| Alan mm² | 15912.159 | 15912.159 | < 0.001 % |
| CoM X | 0.0000 | 0.0000 (4e-16) | 0 |
| CoM Y | 0.0000 | 0.0000 (-7e-16) | 0 |
| CoM Z | 4.9345 | 4.93448 | < 0.0001 mm |
| X min/max | -50 / 50 | -50.000 / 50.000 | 0 |
| Y min/max | -30 / 30 | -30.000 / 30.000 | 0 |
| Z min/max | 0 / 10 | 0.000 / 10.000 | 0 |
| Yüz sayısı | 16 | 16 | 0 |

Tüm kabul kriterleri (hacim ±0.5 %, CoM ±0.05 mm, bbox ±0.01 mm) sağlanıyor. Ham değerler: `olcum.json`.
`final.step`: FILE_SCHEMA AUTOMOTIVE_DESIGN (AP214), uzunluk birimi mm, 1 MANIFOLD_SOLID_BREP.

## Teslim dosyaları
`final.step`, `P01_Plate.SLDPRT`, `build_plate.py`, `olcum.json`, `yeniden_kur.md`, `parametreler.md`, `build_log.md`.
