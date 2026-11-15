# Sık sorulan sorular

## Bu kaça mal oldu? Hangi planla koştunuz?

Bütün yapımcı ve puanlayıcı oturumları Claude Code ile, Opus 5.5 modeliyle koşuldu. Koşulara token tavanı konmadı;
bunun yerine her koşunun girdi / çıktı / önbellek token'ı, süresi ve $ maliyeti koşu kaydına yazıldı
([benchmark/sonuclar/puanlar.csv](../benchmark/sonuclar/puanlar.csv)). 45 parça planlanmıştı; kullanım hakkı dolmasın
diye her parça yalnız bir config'te ve tek tekrarla koşulacaktı (tam matris 5 config × 45 parça olurdu). Yayın
bittiğinde 11 parça koşulmuştu; P10, P16, P17 ve P19 birden çok istasyonda kafa kafaya koşuldu.

Kendi denemende maliyeti düşürmek için: tek bir şekil seviyesindeki parçayla başla, süre tavanını koru (şekil 45 dk),
aynı anda tek ağır koşu çalıştır.

## Neden "kör"?

Katalog parçalarının orijinal modelleri internette var. Yapımcı web'e çıkabilseydi ya da cevap anahtarını okuyabilseydi,
"CAD çizebiliyor mu" yerine "dosyayı bulabiliyor mu" ölçülürdü. Bu yüzden:

- yapımcı yalnız `spec.md`'yi görür;
- web, cevap anahtarı, başka koşular ve parça numarası geçen her çağrı bir guard kancasıyla reddedilir;
- puanlayıcı da kördür: koşuları yalnız rastgele `run_id` ile görür, hangisinin hangi araç olduğunu bilmez.

Puanın 85'i STEP üzerinden betikle, araçtan habersiz hesaplanır. Betiğin "hakem" istediği birkaç sayım kaleminde
kararı insan değil, kör puanlayıcı ajan (Opus 5.5) verir ve gerekçesini yazar.

## Neden hizalama (alignment) yok?

- **Çerçeve, spec'in parçası.** Spec global çerçeveyi açıkça yazar ("şu yüz orijinde, şu eksen yukarı"). Gerçek bir
  mühendislik işinde parça montajdaki yerine oturmak zorundadır; yanlış çerçevede kurmak bir hatadır ve puana yansımalıdır.
- **Hizalama hataları gizler.** ICP gibi bir hizalama, kaymış bir gövdeyi ya da ters kurulmuş bir özelliği "en iyi
  oturan" konuma çekip sapmayı küçük gösterebilir. Montajlı parçalarda gövdelerin birbirine göre pozu da ölçülür;
  her gövdeyi ayrı hizalamak bunu anlamsız kılar.
- **Deterministik ve basit.** Hizalamasız ölçüm her seferinde aynı sonucu verir; hizalama ayarı tartışması çıkmaz.

## Neden model sabit?

Sorulan soru "hangi araç ve harness daha iyi çizdiriyor" idi. Modeli de değiştirseydik farkın modelden mi araçtan mı
geldiğini ayıramazdık. Bu turda model ekseni yok: her yapımcı oturumu Opus 5.5, aynı effort ve izin moduyla.

## NX neden yok?

NX-H2'nin uzman harness'i (NX skill'leri ve journal yardımcıları) Türkişi Engineering'in özel çalışmasıdır, açık kaynak
değildir. Yayında ekranda gösterildi ama bu repoda paylaşılmaz; NX-H2 koşularının çıktıları da paylaşılmaz. Bkz.
[tools/](../tools/).

## Orijinal STEP'ler neden paylaşılmıyor?

Orijinal katalog modelleri ve teknik resimleri bize ait değil; yeniden dağıtmak doğru olmaz. Repoda yalnız bizim
yazdığımız spec'ler, değerlendirme kodu ve kendi koşularımızın çıktıları var. `olc.py` her zaman bir referans STEP
ister: orijinalin yerine, varsa bizim en iyi koşumuzdan (≥ 84,5 / 85) üretilen
`benchmark/degerlendirme/hedefler/P##/referans.step` konuldu. Bu referansa karşı alınan puan, katalog orijinaline
değil **bizim en iyi koşumuza karşı** puandır. Bkz. [benchmark/degerlendirme/](../benchmark/degerlendirme/).

## Kendi aracımı / harness'ımı nasıl eklerim?

1. **Config'i tanımla:** araç + basamak. H0 = aracın kendi API'si, kod yazarak; H1 = H0 + o araç için seçilen MCP;
   H2 = H1 + uzman skill'ler. Kendi basamağını adlandırırken bu tanımlara uy, yoksa karşılaştırma anlamını yitirir.
2. **Kurulumu yaz:** aracın sürümü, birimi, STEP dışa aktarma ayarı (AP214; aracın yazamadığı durumda kendi biçimi,
   kayda yazılarak). Örnekler: [tools/](../tools/).
3. **Guard kurallarını ayarla:** ortak yasaklar aynen kalır; senin basamağında açık olan MCP / skill'leri izinli yap.
   Düzenek ve istemler: [benchmark/kosu/](../benchmark/kosu/).
4. **Duman testi:** önce basit bir kalibrasyon plakası (100 × 60 × 10 mm, 4 köşe deliği, ortada cep, R3 dikey köşe
   yuvarlatması) kurdur; `final.step` teslim edemiyorsa kurulumu düzelt.
5. **Koş ve puanla:** spec'lerden birini al, taze oturumla koş, teslim klasörünü
   [benchmark/degerlendirme/](../benchmark/degerlendirme/)'deki `olc.py` ile ölç. `olc.py` her zaman bir referans STEP
   ister: varsa `benchmark/degerlendirme/hedefler/P##/referans.step` (bizim en iyi koşumuz; puan ona karşıdır, katalog
   orijinaline değil). Referansı olmayan pakette kendi referansını hazırlaman gerekir.
6. Sonucu paylaşmak istersen repoda bir issue aç: config tanımı, sürümler, koşu kaydı ve puan dosyası yeter.

## Kendi skill'lerinizden hangileri paylaşılıyor?

NX dışındaki genel CAD kalite kapıları ve ajanlar: [skills/](../skills/).

## Lig devam edecek mi?

Yeni modeller ve harness'lar çıktıkça aynı spec'ler ve aynı kilitli rubrikle yeni koşular eklenebilir; tablo bu repoda
güncellenir.
