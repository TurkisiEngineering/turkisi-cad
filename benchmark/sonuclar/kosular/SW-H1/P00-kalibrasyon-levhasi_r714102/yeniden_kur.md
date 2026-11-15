# Yeniden kurulum — P01 Plate

Gereksinim: Windows, SolidWorks 2024 (kurulu, lisanslı), Python 3 + `pywin32`.

```
cd <bu klasör>
python build_p01.py            # çıktı klasörü = betiğin klasörü
python build_p01.py C:\yol\cikti   # ya da başka bir klasör
```

Betik:
1. SolidWorks'e COM ile bağlanır (çalışmıyorsa başlatır), varsayılan parça şablonuyla yeni parça açar, birimi MMGS yapar.
2. Global değişkenleri (`L, W, T, R_corner, D_hole, E_hole, D_pocket, H_pocket`) Equation Manager'a ekler.
3. Özellikleri spec sırasıyla kurar: F1 blok → F2 köşe radyüsü (fillet özelliği) → F3 4 delik (Through All Both kesim) → F4 Ø20 × 4 kör cep (Z=10 düzleminden).
4. Boyutları global değişkenlere bağlar, gövdeyi `P01 Plate` olarak adlandırır, her adımda hacim/alan/ağırlık merkezi/sınır kutusu yazdırır.
5. `P01_Plate.SLDPRT` ve `final.step` (AP214, mm) kaydeder; yalnız kendi açtığı belgeyi kapatır (hata olursa da kapatır).

Doğrulama (isteğe bağlı): `python verify_step.py <tam_yol>\final.step` — STEP'i SolidWorks'e geri okur, hacim/alan/CoM/kutu/yüz sayısını yazar ve belgeyi kapatır.
