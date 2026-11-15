# Körlük ve adillik kuralları

Amaç: yapımcı oturumu cevabı başka bir yerden bulamasın, her config aynı şartta yarışsın.

## 1. Yapımcı neyi göremez

| Kapalı | Neden |
|---|---|
| cevap anahtarı klasörü ve durduğu sürücü (orijinal katalog modelleri, bütün alt klasörler) | cevap anahtarı |
| `<IS_KOKU>/paketler/*/_gizli/`, `puan/`, `kayit/`, `sonuc/`, başka `kosular/<run_id>/` | gizli liste, başka koşular |
| rubrik, matris ve eski spec'lerin durduğu yönetim klasörü | rubrik, matris, eski spec'ler |
| WebSearch, WebFetch, tarayıcı araçları, `curl` / `Invoke-WebRequest` / `pip download` / `git clone` | parçaların orijinal STEP'i ve başka modeller internette var |
| satıcı adı ve parçaların katalog numaraları geçen her araç çağrısı | dolaylı arama |
| H0 ve H1'de: `Skill` aracı, `~/.claude/skills/` okuması, `cad-*` / `re-*` ajan tipleri, `Agent` aracı | harness basamağı |
| H0'da: **bütün** MCP sunucuları; H1 ve H2'de: kendi aracının MCP'si dışındakiler | başka aracın MCP'siyle kurmak (ör. SolidWorks koşusunda freecad-mcp) |

Yapımcı yalnız kendi `kosular/<run_id>/` klasörüne yazar; paket oraya kopyalanmış olarak verilir.

## 2. Guard kancası

Guard bir Claude Code `PreToolUse` kancasıdır (`guard/guard.py`). Lead:

1. Kural kümesini config'e göre ayarlanabilir tutar (`guard/kurallar.json`): ortak yasaklar (§1) + basamak yasakları
   (H0 / H1 / H2).
2. Her kararı `kayit/guard.log`'a yazar: `zaman, oturum, run_id, araç, karar`.
3. **Sızıntı testi:** bir yapımcı oturumunda bilerek cevap anahtarını okumaya, web'e çıkmaya, skill çağırmaya çalıştırır
   (`python kos.py sizinti <run_id>`); hepsi reddedilmeli. Sonuç Faz 0 raporuna girer. Yayından önceki son sızıntı
   testi (cevap anahtarı başka sürücüye taşındıktan sonra) temiz çıktı.

Koşu sonrası lead guard.log'u o koşu için tarar: bir `deny` varsa koşu notuna yazılır (deneme kendisi bir veridir);
bir yasak **geçtiyse** koşu geçersizdir ve yeniden koşulur.

## 3. Aynı şartlar

- Model: Opus 5.5, aynı effort ayarı (`high`), aynı izin modu, her koşu taze oturum.
- Yapımcı brifi `kos.py`'deki `BRIF` şablonundan doldurulur; config'e özgü kısım dışında kelimesi kelimesine aynı.
- Aynı süre tavanı (MATRIS §5). Aynı anda tek ağır koşu (yayında: config başına bir koşu, en çok 5).
- Aracın varsayılan ayarları: birim, tolerans, STEP dışa aktarma ayarı Faz 0'da her araç için yazılır ve sabitlenir.
  STEP sürümü AP214 (SolidCraft yalnız AP242 yazdığı için onun kendi çıktısı kabul edildi).
- Yapımcı soru sorarsa tek cevap: "Spec'teki bilgiyle devam et; belirsiz olanı build_log'a yaz."

## 4. Kör puanlama

- Puanlayıcı koşuları yalnız `run_id` ile görür. `kosu_esleme.csv`, `kosu_listesi.csv` ve native dosyaların araç türünü
  ele veren uzantılar dışındaki bilgiler gizli. (Native dosyanın uzantısı aracı ele verir; bu kaçınılmaz. Bu yüzden
  puanın %85'i STEP üzerinden betikle, araçtan habersiz hesaplanır; CAD kalitesi kalemi kontrol listesiyle yapılır.)
- Puanlayıcı rubriği değiştiremez. Rubrikte bir boşluk bulursa yazar, lead sunucuya sorar; karar bütün koşulara geriye
  dönük aynı uygulanır.

## 5. NX'e özgü

NX-H2 Usta'nın özel harness'iyle koştu; bu bölümün ayrıntısı (pencere, harness klasörleri) paylaşılmıyor.

## 6. SolidWorks ve SolidCraft

- SolidWorks'ü yapımcı COM ile başlatabilir; koşu sonunda kendi açtığı belgeleri kapatır. Lisans / açılış ekranı sorunu
  çıkarsa lead sunucuya sorar.
- SolidCraft CLI / MCP sürümü Faz 0'da yazılır; koşu boyunca güncellenmez.
