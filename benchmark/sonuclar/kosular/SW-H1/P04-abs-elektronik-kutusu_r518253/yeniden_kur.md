# Yeniden kurulum

Gereken: Windows, SolidWorks 2024 (COM ile erişilebilir), Python 3 + `pywin32`.

```powershell
cd <kopya>\teslim\betikler
python build_all.py
```

Betik şunları sırayla yapar (SolidWorks açık değilse COM onu başlatır):

1. `build_base.py` → `P01_Base.SLDPRT` (taban, P01)
2. `build_lid_screw.py` → `P02_Lid.SLDPRT` (kapak, P02) ve `H1_Screw.SLDPRT` (vida, H1)
3. `Kutu_Hepsi.SLDPRT`: üç parça *Insert Part* ile (bağlı, taşıma/döndürme yok, birim matris) tek çok-gövdeli parçada
4. Gövde çiftleri arasında girişim hacmi ölçümü (IBody2.Operations2 kesişimi)
5. `final.step` (AP214, inch): `Kutu_Hepsi.SLDPRT`'den. Sistemdeki `swStepAP` seçeneği yalnız bu export için 214 yapılır, sonra eski değerine döndürülür.
6. Ölçümler `betikler/olcum.json` dosyasına yazılır, hedef tabloyla karşılaştırma ekrana basılır.

Notlar
- Hiçbir parça sonradan taşınmaz; her şey spec'in global çerçevesinde kurulur (SolidWorks *Front Plane* = XY, normal +Z = açılma yönü).
- Bütün ölçüler `betikler/params.py` içinde; bir değeri değiştirip `build_all.py`'yi yeniden çalıştırmak modeli yeniden üretir.
- `teslim` içindeki eski `.SLDPRT` / `final.step` dosyaları betik tarafından silinip yeniden yazılır. Bu yüzden önce SolidWorks'te bu belgeleri kapatın.
- İlk çalıştırmada girişim ölçümü için pywin32, `sldworks.tlb` dosyasından makepy önbelleği üretir (`gencache.EnsureModule`); bu birkaç saniye sürer.
- Tek tek parça kurmak için: `python build_base.py` ya da `python build_lid_screw.py lid screw` (kaydetmez, yalnız kurar ve adım adım ölçüm basar).
