# Yeniden kurulum — P01 Plate

Gereksinimler: Windows, SOLIDWORKS 2024 (COM kayıtlı, varsayılan parça şablonu tanımlı), Python 3 + `pywin32`.

```
cd <kopya>\teslim
python build_plate.py            # çıktılar betiğin klasörüne
python build_plate.py C:\yol\cikti   # ya da verilen klasöre
```

Betik:
1. SolidWorks'e COM ile bağlanır (çalışmıyorsa başlatır), varsayılan şablondan yeni parça açar, birimi MMGS yapar.
2. Global değişkenleri (`parametreler.md`) Equations'a yazar.
3. F1 Front Plane (= spec XY, normal +Z) üzerinde merkez dikdörtgen 100×60 → +Z yönünde 10 ekstrüzyon.
4. F2 dört dikey köşe kenarına R3 fillet (kenarlar B-rep'ten koordinatla bulunur).
5. F3 Front Plane üzerinde 4 × Ø6 daire (±42, ±22) → Through All kesim.
6. F4 üst yüz (Z = 10) üzerinde Ø20 daire (orijin izdüşümü merkezli) → 4 mm kör kesim.
7. Ölçüleri isimlendirir ve denklemlerle değişkenlere bağlar; gövdeyi `P01 Plate` olarak adlandırır.
8. Kütle özelliklerini `olcum.json`'a yazar, `P01_Plate.SLDPRT` ve `final.step` (AP214, mm) kaydeder, yalnız kendi belgesini kapatır.

Mevcut `P01_Plate.SLDPRT` / `final.step` üzerine yazılır. Belgeyi açık bırakmak için `--keep-open` ekleyin.
Taşıma/yeniden hizalama yoktur: model doğrudan spec çerçevesinde kurulur.
