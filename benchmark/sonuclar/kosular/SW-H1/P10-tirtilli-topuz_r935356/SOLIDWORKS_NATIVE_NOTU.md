# SolidWorks native dosyaları nasıl açılır

Bu klasörde yapımcının SolidWorks'te kurduğu native dosyalar var:

- `P01_core.SLDPRT`
- `P02_coating.SLDPRT`
- `P03_insert.SLDPRT`
- `knob_assembly.SLDASM`

- SolidWorks ile açın (koşular SolidWorks'ün kurulu sürümüyle kaydedildi; daha eski bir sürüm açamaz). Özellik ağacı ve isimli ölçüler (`parametreler.md`) olduğu gibi durur.
- Montaj (`knob_assembly.SLDASM`) parçalara kayıt anındaki mutlak yollarla bağlı. Açarken SolidWorks parçaları bulamazsa aynı klasördekileri gösterin ya da önce bütün klasörü bir yere kopyalayıp montajı oradan açın; SolidWorks aynı klasördeki aynı adlı parçaları kendisi arar.
- SolidWorks yoksa `final.step` aynı geometridir (FreeCAD, Fusion, Onshape vb. açar).
- Dosyaların içinde SolidWorks'ün kendi yazdığı kayıt yolu ve kullanıcı adı gibi kayıt bilgileri bulunur; geometriyi etkilemez.
- Yeniden üretmek için: `yeniden_kur.md` ve klasördeki pywin32 betikleri.
