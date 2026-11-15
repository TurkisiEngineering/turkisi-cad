# yeniden_kur.md — modeli sıfırdan üretme

Gereken: Windows, SOLIDWORKS 2024 (kurulu, lisanslı), Python 3.13 + pywin32.

1. SolidWorks tip kütüphanesi sarmalayıcılarını bir kez üret (yeni makinede):
   ```
   python -m win32com.client.makepy "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\sldworks.tlb"
   python -m win32com.client.makepy "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\swconst.tlb"
   ```
2. Parçaları kur, ölç, `.SLDPRT` olarak kaydet (SolidWorks açık değilse COM ile başlatılır):
   ```
   cd teslim\scripts
   python -u build.py            # 12 parçanın hepsi; tek parça için: python build.py P01
   ```
   Her parça için hacim/alan/ağırlık merkezi/sınır kutusu spec §6 ile karşılaştırılıp
   `scripts/measure_results.json` dosyasına yazılır.
3. Montajı kur (bütün bileşenler birim dönüşümle, orijinde), global değişkenleri yaz, STEP AP214 dışa aktar:
   ```
   python -u assemble.py         # -> Caster_Assembly.SLDASM, final.step
   ```
Betikler: `swlib.py` (COM yardımcıları, inç→metre), `parts.py` (PARAMS + tekerlek parçaları),
`parts_b.py` (P02–P06), `parts_fork.py` (P01), `build.py`, `assemble.py`.
Not: `build.py`/`assemble.py` yalnız kendi açtığı belgeleri kapatır. Süre: ~3–4 dk (çatal ~1 dk).
