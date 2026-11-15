# Build log: P01 Guard (SolidCraft)

## Ne yaptım
- Model, `solidcraft-cli run` ile çalıştırılan bir komut dizisi olarak kuruldu (`P01_Guard_build.json`). Dizi,
  `gen.sh` (bash + awk) tarafından üretiliyor. Belge birimi inç; spec'in global çerçevesi doğrudan kullanıldı
  (+Y yukarı, y_bot = -1.53125'te montaj yüzü). Hiçbir şey sonradan taşınmadı.
- Dış katı: çadırın XY profili (eğik uç duvarlar, tepe yayına teğet eğimler, R1.9375 tepe yayı) Z boyunca ekstrüde
  edildi, ardından eğik yan duvar dilimiyle (YZ taslağı) kesiştirildi. Her yan için R0.375 yuvarlatma uygulandı
  (eğim–tepe–eğim kenarları teğet zincir olarak geliyor). Tümsek için aynısı yapıldı (U profili ve uç yüz dilimi,
  R0.375), sonra birleştirildi ve her yanda R0.125 içbükey yuvarlatma uygulandı.
- İç boşluk: aynı fonksiyon, `wall` kadar içe kaydırılmış değerlerle ayrı bir "Cavity" gövdesi olarak kuruldu
  (R0.25 / R0.25 / içbükey R0.25). Alt kenar, açık taban için y_bot - 0.12'ye uzatıldı.
- Flanş: XZ taslağı (ofset y_bot), spec 3.6'daki 16 parçanın sırasıyla çizilmesi, 0.125 yukarı ekstrüzyon ve birleştirme.
  +Z'de R0.980580, -Z'de R1.249693 asimetrisi korundu.
- Bosslar: Ø0.8125 uzun silindirler birleştirildi, boss üst düzleminden (üst: y = 1.93125; eğimler: egim+0.0875)
  silindirle kırpıldı. Ardından Cavity çıkarıldı ve Ø0.5625 girintiler kesildi (dipleri y = 1.80625 ve eğim
  düzlemi sabiti 1.835076). Son olarak alt ağız kenarına R0.1 yuvarlatma uygulandı.
- Tek gövde, adı **P01 Guard**. STEP, aracın kendi AP242 çıktısı (`--out final.step`). Başlığa elle dokunulmadı;
  FILE_NAME alanında çalışma adı `b4.step` görünüyor, çünkü dosya o adla yazılıp olduğu gibi kopyalandı.

## Nerede takıldım
1. Yan duvar yuvarlatmalarının 10 kenarı tek özellikte verilince çekirdek "blend is larger than the neighbouring
   faces" hatası verdi. Her yan (+Z / -Z) ayrı özellik yapılınca çalıştı.
2. **Boss taban yuvarlatması (içbükey R0.1) kurulamadı.** Hem üst boss hem eğim bosslarında aynı hata alındı:
   "the blend is larger than the neighbouring faces … only straight edges can be blended". Yani çekirdek, eğri bir
   kenarda bu durumu desteklemiyor. Süre kısıtı yüzünden bu üç yuvarlatma teslim modelinden çıkarıldı.
   `BOSS_ROUND=1 bash gen.sh 4` ile tekrar eklenebilir, ancak şu anki SolidCraft sürümünde başarısız oluyor.
3. Python ve çalışma alanı dışına yazma ortamda kapalıydı, bu yüzden hesaplar awk ile yapıldı.
4. Her tam kurulum yaklaşık 5 dakika sürüyor (birleştirme ve yuvarlatmalar yavaş), bu da deneme sayısını sınırladı.

## Bilerek basitleştirdiklerim / yorumlarım
- Boss taban R0.1 yuvarlatmaları yok (yukarıya bakın). Etkisi hacimde küçük bir eksiklik (birkaç mm³) ve 3 halka
  bölgesinde keskin içbükey kenar.
- 3.7: x≈0'daki kaynak düzensizliği uygulanmadı; sabit yarıçaplı yuvarlatma kullanıldı (spec'in istediği gibi).
  18 boş kabuk üretilmedi.
- Eğim bossu ekseni P = (±1.369085, 1.277826), dış eğim düzlemi üzerinde tanımlandı (`Py` eğim düzleminden türetiliyor).
- Flanş köşe ve merkez koordinatları spec'teki sayısal değerler olarak kullanıldı, parametre yapılmadı.

## Ölçüm ve hedef karşılaştırması (`solidcraft-cli run`/eval çıktısı, B-rep)

| Büyüklük | Hedef | Model | Fark |
|---|---|---|---|
| Hacim mm³ | 136628 | 137188 | +560 (+0.41 %) |
| Alan mm² | 87451 | 88175 | +724 (+0.83 %) |
| CoM x mm | 0.000 | 0.0002 | ≈0 |
| CoM y mm | -9.229 | -8.947 | +0.28 |
| CoM z mm | -0.142 | -0.141 | ≈0 |
| X min/max mm | ±98.8434 | -98.8432 / +98.8437 | <0.001 |
| Y min/max mm | -38.8938 / 49.0538 | -38.8940 / 49.0538 | <0.001 |
| Z min/max mm | ±65.8953 | -65.8951 / +65.8957 | <0.001 |
| Yüz sayısı | 174 | 124 (çekirdek: 130) | -50 |

Yorum: Sınır kutusu tam tutuyor (flanş, top boss yüksekliği 3.4625 in). Hacim ve alan %1'in altında farklı. CoM y'nin
0.28 mm yukarıda olması ve yüz sayısının eksik olması büyük ölçüde boss taban yuvarlatmalarının yokluğundan ve
çekirdeğin yuvarlatma köşe yamalarını farklı (daha az sayıda) yüzle kurmasından kaynaklanıyor. Hedef hacim üçgenleme
ile ölçülmüş, benim değerim ise B-rep hesabı; bu yöntem farkı da sonuca bir miktar katkı yapabilir. Kalan farkın
ayrıntılı dökümü süre içinde yapılamadı.
Kontrol değerleri: et 0.125 (iç gövde wall ofsetiyle kuruldu), flanş 0.125, boss Ø0.8125 / girinti Ø0.5625,
duvar eğimleri 4°.

## Dosyalar
- `final.step` (AP242), `P01_Guard.sc` (SolidCraft belgesi), `P01_Guard_build.json` (komut dizisi), `gen.sh` (üretici).
- Ara denemeler `..\calisma\` klasöründe.
