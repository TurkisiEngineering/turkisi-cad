# Build log: P01 Spanner (kancalı somun anahtarı, spec P17)

## Ne yaptım
SolidWorks 2024 + Python/pywin32 (COM, dinamik dispatch). Tek betik: `build_spanner.py`. Birim IPS (inch), spec'in
global çerçevesi aynen kullanıldı: plaka Y=-0.06..+0.06, profil XZ'de (SolidWorks Top Plane), sap +X, üst kenar Z=0.
Tüm noktalar model koordinatıyla verilip `ModelToSketchTransform` ile çizim koordinatına çevrildi; böylece düzlem
yönlenmesi (Top Plane'de çizim y = -Z) elle tahmin edilmedi.

Özellik ağacı:
| Özellik | Yöntem |
|---|---|
| SK_F1_Outline / F1_Outline | 11 segmentlik kapalı profil (5 yay 3-nokta yay olarak; ara nokta = kısa yayın ortası, seg 2 için spec'teki (2.1655, -0.194895)), mid-plane ekstrüzyon T=0.12 |
| SK_F2_Slot / F2_Slot | obround yuva, iki yönde Through All kesim |
| SK_F3_StraightRounds / F3a_HandleRounds | Right Plane (X=0) üzerinde 4 köşe profili (kare köşe − R1/64 çeyrek daire), iki yönde kör kesim: +X 1.970605, −X 0.441484 |
| PL_EndAxis, SK_F3_EndRound / F3b_EndRound | Z=-0.194895 düzleminde aynı köşe profili (±Y), eksen (x=1.970605, Z=-0.194895, ∥Y) etrafında mid-plane 180° döndürmeli kesim → toroidal yuvarlatma |
| PL_Runout_Pos/Neg, SK_F4_Runout1..4 / F4_Runout_* | Y=±0.044375 düzlemlerinde, köşe merkez çizgisi (∥X) etrafında 90° döndürmeli kesim; profil: koni çizgisi r(x)=0.015625+tan10°·(-0.441484-x) ile r=0.03 arası, x=-0.478189..-0.441484 |

Kenar yuvarlatmalarını SolidWorks Fillet yerine **kesim özellikleriyle** yaptım: spec yuvarlatmanın kenarın yalnız bir
kısmında (x ≥ -0.441484) olmasını ve konik run-out ile bitmesini istiyor; Fillet bunu doğrudan veremez. Kesimle elde
edilen yüzeyler geometrik olarak aynı (silindir R1/64, torus R0.17927/0.015625, koni 10°).

## Nerede takıldım
- pywin32 dinamik dispatch: `CreatePoint`, `CreateMassProperty` özellik gibi çağrıldı → `_FlagAsMethod` ile çözüldü;
  `SaveAs`'ın `ExportData` argümanı `None` yerine `VARIANT(VT_DISPATCH, None)` istedi.
- İlk denemede yardımcı düzlemin konumunu boş bir "sonda" çizimiyle doğrularken, boş çizim oluşmadığı için düzlemin
  kendisi silindi ve döndürmeli kesim başarısız oldu. Düzlemi artık `RefPlane.Transform` ile (normal·(P−orijin)=0)
  doğruluyorum.
- Kesim yönleri (iki yönlü ekstrüzyon ve 90° döndürmeler) API'de normal yönüne bağlı; betik her iki yönü deneyip
  hacim farkıyla doğru olanı seçiyor (F3a: analitik beklenen 4·(1−π/4)·r²·2.412089 = 5.0551e-4 in³ ile %1 içinde;
  F4: küçük kaldırılan hacim ≈6e-7 in³, yanlış yön ≈7e-6 in³). Silinen deneme özellikleri ağaçta kalmıyor.
- STEP dışa aktarıcı çene (R0.3125) ve kafa (R0.707) silindirlerini periyodik dikiş yerinden bölüp 29 yüz yazıyordu.
  Dışa aktarma sırasında `swStepExportSplitPeriodic` kapatıldı (sonra kullanıcının eski ayarı geri yüklendi) → STEP'te
  27 `ADVANCED_FACE`. (STEP AP ayarı 214 olarak bırakıldı; geri alınmadı.)

## Bilerek basitleştirdiğim / yorumladığım
- Kaynak modeldeki 19 boş mikro-kutu (114 sıfır alanlı yüz) spec gereği üretilmedi.
- 3-nokta yaylar verilen uç noktalardan geçtiği için yarıçaplar 1e-6 mertebesinde spec'ten sapıyor (örn. kafa yayı
  0.7070119 vs 0.707013) — spec'in koordinatları zaten 6 hane yuvarlatılmış; teğetlik ilişkisi eklenmedi.
- Global değişkenlerden yalnız `T` bir ölçüyü sürüyor; profil koordinatlarla çiziliyor (ölçü/kısıt yok), bu yüzden
  diğer değişkenleri değiştirmek için betikteki `P` sözlüğünü düzenleyip betiği yeniden çalıştırmak gerekiyor.
- Malzeme atanmadı (spec: yalnız ürün verisi).

## Ölçüm vs hedef (SolidWorks kütle özellikleri, kaydedilmiş SLDPRT; `verify_output.txt`)
| Büyüklük | Ölçülen | Hedef | Fark |
|---|---|---|---|
| Hacim in³ | 0.2085008 | 0.208501 | -0.0001 % |
| Alan in² | 4.6120355 | 4.612036 | -0.00001 % |
| CoM X | -0.0882374 | -0.088238 | 6e-7 |
| CoM Y | 0.0000000 | 0.000000 | 1e-8 |
| CoM Z | -0.2517186 | -0.251719 | 4e-7 |
| Xmin / Xmax | -2.165500 / 2.165500 | -2.165500 / 2.165500 | 0 |
| Ymin / Ymax | -0.060000 / 0.060000 | -0.06 / 0.06 | 0 |
| Zmin / Zmax | -0.707013 / 0.000000 | -0.707013 / 0 | 0 |
| Yüz sayısı | 27 (SLDPRT ve STEP) | 27 | 0 |
| Gövde | 1 katı, adı "P01 Spanner" | 1 | — |

STEP: `FILE_SCHEMA(('AUTOMOTIVE_DESIGN'))` (AP214), uzunluk birimi `INCH`, tek `MANIFOLD_SOLID_BREP('P01 Spanner')`.

## Teslim dosyaları
`final.step`, `P01_Spanner.SLDPRT`, `build_spanner.py`, `verify.py`, `build_output.txt`, `verify_output.txt`,
`yeniden_kur.md`, `parametreler.md`, `build_log.md`.
