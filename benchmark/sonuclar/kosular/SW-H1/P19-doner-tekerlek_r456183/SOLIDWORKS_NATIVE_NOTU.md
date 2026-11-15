# SolidWorks native dosyaları nasıl açılır

Bu klasörde yapımcının SolidWorks'te kurduğu native dosyalar var:

- `Caster_Assembly.SLDASM`
- `H1_AxlePin.SLDPRT`
- `P01_Fork.SLDPRT`
- `P02_TopPlate.SLDPRT`
- `P03_Kingpin.SLDPRT`
- `P04_BearingWasher.SLDPRT`
- `P05_HexBearingRing.SLDPRT`
- `P06_BrakePedal.SLDPRT`
- `P07_WheelTread.SLDPRT`
- `P08_WheelInsertRing.SLDPRT`
- `P09_WheelCoreDisc.SLDPRT`
- `P10a_CoreFlange_negZ.SLDPRT`
- `P10b_CoreFlange_posZ.SLDPRT`

- SolidWorks ile açın (koşular SolidWorks'ün kurulu sürümüyle kaydedildi; daha eski bir sürüm açamaz). Özellik ağacı ve isimli ölçüler (`parametreler.md`) olduğu gibi durur.
- Montaj (`Caster_Assembly.SLDASM`) parçalara kayıt anındaki mutlak yollarla bağlı. Açarken SolidWorks parçaları bulamazsa aynı klasördekileri gösterin ya da önce bütün klasörü bir yere kopyalayıp montajı oradan açın; SolidWorks aynı klasördeki aynı adlı parçaları kendisi arar.
- SolidWorks yoksa `final.step` aynı geometridir (FreeCAD, Fusion, Onshape vb. açar).
- Dosyaların içinde SolidWorks'ün kendi yazdığı kayıt yolu ve kullanıcı adı gibi kayıt bilgileri bulunur; geometriyi etkilemez.
- Yeniden üretmek için: `yeniden_kur.md` ve klasördeki pywin32 betikleri.
