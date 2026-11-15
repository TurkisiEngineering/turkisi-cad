# Yeniden kurma

Gerekenler: Windows, SolidWorks (2024 / API rev 32 ile denendi), Python 3 ve `pywin32`.

```
cd teslim\betikler
python build_gear.py               # çıktı: teslim\ (P01_Miter_gear.SLDPRT + final.step)
python build_gear.py <cikti_klasoru>   # isteğe bağlı: başka bir çıktı klasörü
python close_docs.py               # yalnızca betiğin açtığı P01_Miter_gear belgesini kapatır
```

Betik açık bir SolidWorks oturumuna bağlanır, açık değilse COM ile başlatır. Sonra şunları yapar:

1. Varsayılan parça şablonundan yeni parça açar ve birimi MMGS (mm) yapar.
2. Parametreleri global değişken olarak ekler.
3. `Axis_Y` referans eksenini oluşturur (Ön ∩ Sağ düzlem = global Y).
4. `Sk_BlankProfile`: Ön düzlemde (global XY) 9 kenarlı (r, y) profili çizer, Y ekseni etrafında 360° döndürür
   (`Blank_Revolve`).
5. `Sk3D_SectionA_heel` / `Sk3D_SectionB_toe`: 3B eskizlerde, spec'teki kutuplardan doğrudan B-spline'lar kurar
   (kübik, düğüm vektörü (0,0,0,0,.5,.5,1,1,1,1); kök Bezier). Sırası: sol yanak, sol dib yuvarlatması, kök, sağ dib
   yuvarlatması, sağ yanak, kapatma çizgisi.
6. `ToothSpace_Cut`: iki kesit arasında loft kesimi (teğet yüzler birleştirilmez). Ardından `Remove_SpaceSlug`
   (Gövde Sil/Tut) ile ayrılan boşluk parçasını siler (nedeni `build_log.md`'de).
7. `ToothSpace_Pattern`: Y ekseni etrafında 20 adet, eşit aralıklı dairesel çoğaltma (adet = `NTeeth`).
   `Remove_PatternSlugs` yalnızca birden fazla gövde kalırsa eklenir; son koşuda gerekmedi.
8. Hacim, alan, ağırlık merkezi, sınır kutusu ve yüz sayısını yazdırır. SLDPRT ve AP214 STEP olarak kaydeder.

Modelin tamamı global çerçevede, yerinde kuruluyor; sonradan taşıma ya da döndürme yok.
