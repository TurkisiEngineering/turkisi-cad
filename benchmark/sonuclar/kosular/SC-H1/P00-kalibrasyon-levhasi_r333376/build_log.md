# Build log — P0 kalibrasyon plakası (P01 Plate)

## Ne yaptım
- `girdi/spec.md` okundu; tek gövde, belirsiz madde yok.
- Önce hedef hacim analitik hesaplandı:
  60000 − 4·3²·(1−π/4)·10 (77.257) − 4·π·3²·10 (1130.973) − π·10²·4 (1256.637) = **57535.133 mm³** → spec ile birebir.
- Model SolidCraft komut dizisi olarak yazıldı (`P0_plate_script.json`) ve `solidcraft-cli run` ile kuruldu; spec'teki
  sırayla F1 → F2 → F3 → F4, tümü yerinde, global çerçevede (alt yüz Z=0, X/Y orijinde ortalı). Sonradan taşıma yok.
  - F1: XY taslakta merkez dikdörtgen (L×W), merkez orijine çakışık, dof 0; +Z yönünde T ekstrüzyon.
  - F2: 4 düşey kenar R3 fillet (üst/alt kontur kenarları keskin kaldı).
  - F3: bir Ø6 silindir kesimi (Z=−1…11, tam delik) + 2×2 dikdörtgen desen (84 × 44).
  - F4: Ø20 silindir kesimi Z=6…11 → düz taban Z=6, keskin taban-duvar kenarı, keskin ağız.
  - Gövde adı `P01 Plate`.
- Aynı komutlar MCP oturumunda da çalıştırılıp `body_topology` ile silindirler tek tek kontrol edildi ve
  `check_parameters` ile parametre takibi denendi (bkz. `parametreler.md`).
- Temiz bir klasöre yalnız betik + çevirici kopyalanıp `yeniden_kur.sh` çalıştırıldı; çıkan STEP teslimdekiyle
  (FILE_NAME satırı dışında) bayt bayt aynı.

## Nerede takıldım
- İlk denemede taslak dof 2 kaldı (dikdörtgen merkezi orijine bağlı değildi; geometri yine doğru yerdeydi). Merkez
  noktasına (`p5`) orijinle çakışıklık eklendi → dof 0.
- **STEP şeması:** SolidCraft'ın `file.export_step` komutunun şema seçeneği yok, her zaman AP242
  (`AP242_MANAGED_MODEL_BASED_3D_ENGINEERING_MIM_LF`) yazıyor. Dosyadaki tüm varlıklar (MANIFOLD_SOLID_BREP,
  ADVANCED_FACE, PLANE, CYLINDRICAL_SURFACE, LINE, rasyonel B_SPLINE_CURVE, ürün/bağlam varlıkları) AP214'te de
  geçerli olduğu için `step_to_ap214.py` yalnız başlığı değiştiriyor: `FILE_SCHEMA` → `AUTOMOTIVE_DESIGN { 1 0 10303 214 1 1 1 1 }`,
  `APPLICATION_CONTEXT` / `APPLICATION_PROTOCOL_DEFINITION` → automotive_design, ürün ve şekil temsili adları →
  `P01 Plate`. Geometriye dokunulmadı; çevrilen dosya SolidCraft'ta yeniden açılıp ölçüldü (aşağıdaki tablo bu ölçüm).
  Bu, "kendi özellikleriyle kur" kuralını bozmuyor: geometri SolidCraft'ta kuruldu, yalnız dosya başlığı çevrildi.

## Bilerek basitleştirdiğim / yorum
- Yok denecek kadar: spec tam. Delik ve cep kesicileri yüzeylerle çakışık yüz olmasın diye 1 mm taşırıldı
  (delik Z=−1…11, cep Z=6…11); sonuç geometrisi aynı.
- Delik konumları `solid.hole` yerine parametrik silindir kesimi + desenle kuruldu (aynı geometri: düz, havşasız,
  tam boy silindirik delik).

## Hedef tablo karşılaştırması (`final.step` yeniden açılıp SolidCraft ile ölçüldü)

| Büyüklük | Spec | Ölçülen | Fark |
|---|---|---|---|
| Hacim mm³ | 57535.133 | 57535.326 | +0.193 (+0.0003 %) — tolerans 0.5 % ✔ |
| Alan mm² | 15912.159 | 15912.157 | −0.002 ✔ |
| CoM X | 0.0000 | 0.0000 | ✔ |
| CoM Y | 0.0000 | 0.0000 | ✔ |
| CoM Z | 4.9345 | 4.9345 (4.93448) | < 0.0001 — tolerans 0.05 ✔ |
| X min/max | −50 / 50 | −50.000 / 50.000 | < 1e-12 ✔ |
| Y min/max | −30 / 30 | −30.000 / 30.000 | < 1e-12 ✔ |
| Z min/max | 0 / 10 | 0.000 / 10.000 | < 1e-12 ✔ |
| Yüz sayısı | 16 | 16 (7 düzlem + 9 silindir) | ✔ |

(.sc belgesinin kendi ölçümü: hacim 57535.336, alan 15912.144, CoM Z 4.93448 — STEP ile aynı.)

Kontrol değerleri (`body_topology`, kesin silindirler):
- 4 delik Ø6 (r=3.000), eksenler (±42, ±22), Z 0…10 boyunca tam delik ✔
- Cep Ø20 (r=10.000), eksen (0,0), Z 6…10 (derinlik 4.000) ✔, taban düz
- Köşe yuvarlakları r=3.000, merkezler (±47, ±27), Z 0…10 ✔
- Plaka 100 × 60 × 10 ✔

## Teslim dosyaları
- `final.step` — AP214, mm, tek gövde `P01 Plate`
- `P0_plate.sc` — SolidCraft belgesi (parametreler + özellik geçmişi)
- `P0_plate_script.json` — SolidCraft komut dizisi (kaynak)
- `step_to_ap214.py` — STEP başlık çevirici; `yeniden_kur.sh` — tek komutla yeniden kurma
- `yeniden_kur.md`, `parametreler.md`, `build_log.md`
- `top_view.png`, `section_xz.png` — görsel kontrol; `olcum_final_step.json` — STEP ölçümü
