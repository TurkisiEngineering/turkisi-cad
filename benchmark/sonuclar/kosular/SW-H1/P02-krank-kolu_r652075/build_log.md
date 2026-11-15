# Build log — P01 Crank handle

Araç: SolidWorks 2024, Python 3.13 + pywin32 (COM). Betik: `build_crank.py`. Doğrulama: `verify_step.py`.

## Ne yapıldı
Spec'in kurgusu birebir izlendi, global çerçevede (mm, göbek ekseni = X, alt yüz X=0, kol -Y yönünde,
kavrama ekseni Y=-100 Z=0) yerinde kuruldu; hiçbir taşıma/hizalama yok.

1. **A1** – Front Plane (XY) üzerinde 12 adımlı (x, r) profili (r = model +Y) çizildi, X ekseni etrafında 360° revolve.
2. **A2** – Right Plane (YZ) üzerinde plan konturu tek kapalı kontur olarak çizildi: R15.5 göbek çemberinin büyük yayı,
   2× R22.5 blend, 2× konik şerit çizgisi, 2× R13.5 blend, R8 kavrama-boss çemberinin büyük yayı. Teğet noktaları ve
   merkezler spec'ten aynen alındı. Extrude-cut, Through All, "flip side to cut" → A1 ∩ prizma.
3. **B** – Front Plane'de kavrama profili (r = Y-(-100), +Y yönünde), Y=-100 eksenli merkez çizgisi etrafında 360° revolve,
   gövdeye birleştirildi.
4. **C** – Ø10 delik + X=0'da 120° havşa (Ø13.4641 → Ø10, derinlik 1) revolve-cut.
5. Gövde adı `P01 Crank handle`; STEP AP214 (`swStepAP`=214) olarak `final.step`'e yazıldı, STEP'teki PRODUCT adı da
   `P01 Crank handle` yapıldı (SolidWorks dosya adını — "final" — yazıyordu; metin düzeltmesi, geometriye dokunulmadı).
6. 32 parametre Equation Manager'a global değişken olarak eklendi (bkz. `parametreler.md`).

## Takıldığım yerler
- `SketchManager.CreateArc` (merkez + yön bayrağı) A1'in R30 yayını sessizce oluşturmadı (nesne döndü ama segment
  yoktu) → profil açık kaldı, revolve başarısız. Tüm yaylar, açısal orta noktası hesaplanan 3-noktalı yay
  (`Create3PointArc`) ile çizilerek çözüldü.
- `FeatureCut4` çift yönlü Through All ile başarısız oldu (taslak düzlemi X=0'da, gövde yalnız +X tarafında) → tek yön,
  Through All, flip-side ile çalıştı.
- pywin32 karma bağlama (gen_py önbelleği + dinamik): argümansız COM yöntemleri bazen özellik bazen yöntem geliyor;
  `V()` yardımcı fonksiyonu ile ele alındı.

## Bilinçli yorumlar / basitleştirmeler
- Delik revolve-cut profili X=28 yerine X=29'a kadar uzatıldı (göbek üst yüzü ile çakışan kesme yüzeyi olmasın diye).
  X=28–29 arasında r<5 bölgesinde malzeme yok; geometri sonucu aynı.
- Spec'te yalnız koordinat olarak verilen teğet noktaları, yay merkezleri ve kink noktaları sabit sayı olarak
  kullanıldı; bunlara bağlı yarıçaplar `parametreler.md`'de "bilgi amaçlı" (ⓘ) işaretli.
- Ana (master) dosyadaki 16 boş sıfır-hacimli kabuk (kaynak artefaktı) spec gereği üretilmedi.
- Parametrik kaynak Python betiğidir; SLDPRT'teki taslaklar ölçülendirilmiş/kısıtlı değil (AddToDB ile mutlak
  koordinatta çizildi). SLDPRT'teki global değişkenler ölçü değerlerinin kayıtlı kopyasıdır, taslakları sürmez.

## Ölçüm — hedef tablo karşılaştırması
Ölçüm: SolidWorks mass properties, hem SLDPRT üzerinde (`measure.json`) hem de `final.step` geri içe alınarak
(`verify_step.py`); iki sonuç 0.01 mm³ içinde aynı.

| Büyüklük | Hedef | Ölçülen (final.step) | Fark |
|---|---|---|---|
| Hacim mm³ | 39620 (±0.05 %) | 39618.52 | −1.5 (−0.004 %) ✔ |
| Alan mm² | 12592.2 | 12592.67 | +0.47 (+0.004 %) ✔ |
| CoM X | 48.96 | 48.965 | ✔ |
| CoM Y | −48.59 | −48.589 | ✔ |
| CoM Z | 0.00 | 0.000 | ✔ |
| Xmin / Xmax | 0.000 / 128.000 | 0.000 / 128.000 | ✔ |
| Ymin / Ymax | −110.000 / 15.500 | −110.000 / 15.500 | ✔ |
| Zmin / Zmax | −15.500 / 15.500 | −15.500 / 15.500 | ✔ |
| Gövde / kabuk | 1 / 1 | 1 / 1 | ✔ |
| Yüz sayısı | 42 (+96 boş) | SolidWorks B-rep: 28; STEP içinde ADVANCED_FACE: 45 | bkz. not |

Yüz sayısı notu: SolidWorks 360° revolve yüzeylerini tek periyodik yüz olarak tutuyor (28); STEP yazıcısı periyodik
yüzleri bölüyor (45). Master'ın 42 yüzü farklı bir çekirdek bölümlemesinden geliyor; spec'in "yaklaşık 32–42" aralığına
yakın, topoloji farkı geometrik değil (hacim/alan/CoM/kutu hedefleri 0.005 % içinde tutuyor).

Kontrol ölçüleri (yapı gereği): göbek Ø28, boy 28, delik Ø10, yaka Ø31, krank yarıçapı 100, X boyu 128,
kavrama Ø20 (x=103.95), boss Ø16, Y kapsamı 125.5 (−110 → 15.5).
