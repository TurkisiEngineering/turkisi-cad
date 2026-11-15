# Mimari: yapımcı, guard, koşucu, puanlayıcı, panel

F23 "Agentic CAD Ligi" beş parçalı bir düzenektir. Her parçanın tek bir işi var ve birbirinin işine karışmaz.
Amaç basit: **aynı model** (Opus 5.5), **aynı parça**, **aynı kurallar**; değişen yalnız CAD aracı ve elindeki
yardımcılar (harness).

```
            spec.md (yalnız bu)
                  │
   ┌──────────────▼──────────────┐      her araç çağrısı      ┌───────────────┐
   │ YAPIMCI (Opus 5.5, taze     │ ─────────────────────────▶ │ GUARD         │
   │ oturum, tek config, tek     │ ◀──── izin / ret ───────── │ (PreToolUse   │
   │ parça)                      │                            │  kancası)     │
   └──────────────┬──────────────┘                            └───────┬───────┘
                  │ teslim/ (final.step, kaynak, yeniden_kur.md,      │ guard.log
                  │          parametreler.md, build_log.md)           │
   ┌──────────────▼──────────────┐                                    │
   │ KOŞUCU (runner)             │ ◀──────────────────────────────────┘
   │ run_id, paket kopyası, brif,│
   │ süre tavanı, ekran kaydı,   │──── koşu kaydı ────┐
   │ kayıt satırı                │                    │
   └──────────────┬──────────────┘                    │
                  │ final.step + run_id               │
   ┌──────────────▼──────────────┐                    │
   │ PUANLAYICI (olc.py + kör    │── puan satırı ─────┤
   │ puanlayıcı ajan)            │                    │
   └─────────────────────────────┘                    ▼
                                         ┌──────────────────────────┐
                                         │ PANEL: istasyonlar, kuyruk│
                                         │ skor tablosu, yayın sayfası│
                                         └──────────────────────────┘
```

## 1. Yapımcı (builder)

- Her koşu **taze bir Claude Code oturumu**: Opus 5.5, aynı effort, aynı izin modu. Önceki koşunun sohbeti taşınmaz.
- Gördüğü tek şey parçanın `spec.md`'si ([benchmark/specs/](../benchmark/specs/)). Spec araçtan bağımsız dilde yazılır:
  global çerçeve, birim, gövde listesi ve adetleri, gövde başına hedefler (hacim, alan, ağırlık merkezi, sınır kutusu),
  geometri olarak özellik tarifleri, ölçülemeyen yerler için "belirsiz".
- Yalnız kendi koşu klasörüne yazar ve aynı beş kalemi teslim eder:
  1. `final.step`: bütün gövdeler, spec'in global çerçevesinde ve biriminde;
  2. aracın native kaynağı (betik, makro, native dosya);
  3. `yeniden_kur.md`: modeli temiz kopyada sıfırdan üreten adımlar;
  4. `parametreler.md`: isimli parametreler;
  5. `build_log.md`: ne yaptı, nerede takıldı, neyi bilerek basitleştirdi.
- Soru sorarsa tek cevap: "Spec'teki bilgiyle devam et; belirsiz olanı build_log'a yaz." İnsan müdahalesi sıfır.

## 2. Guard (kör koşu kancası)

Claude Code'un `PreToolUse` kancası. Yapımcının **her** araç çağrısını çalışmadan önce görür ve kurala göre izin verir
ya da reddeder:

- **Ortak yasaklar:** cevap anahtarı klasörü, başka koşuların klasörleri, gizli değerlendirme dosyaları, web (arama,
  sayfa çekme, `curl`, `pip download`, `git clone`), parça numarası ya da satıcı adı geçen her çağrı.
- **Basamak yasakları:**
  - H0 (çıplak): config'in kendi aracı dışında bütün MCP sunucuları, bütün skill'ler, alt ajanlar kapalı.
  - H1 (topluluk MCP'si): kendi aracının seçilen MCP'si açık; skill'ler kapalı.
  - H2 (uzman harness): H1 + uzman skill'ler (bu turda yalnız NX'te var, özel).
- Her karar bir satır olarak `guard.log`'a yazılır (zaman, oturum, run_id, araç, karar). Bir ret koşu notuna girer
  (denemenin kendisi bir veridir); bir yasak **geçtiyse** koşu geçersizdir ve yeniden koşulur.
- Koşulardan önce bir sızıntı testi yapıldı: yapımcıya bilerek anahtarı okutmaya, web'e çıkmaya, skill çağırmaya
  çalışıldı; hepsi reddedildi.

Kodu ve ayarları: [benchmark/kosu/](../benchmark/kosu/).

## 3. Koşucu (runner)

Lead oturumu koşucuyu çalıştırır; yapımcının brifi ve araçları koşucudan habersizdir.

- Rastgele bir `run_id` üretir (`r` + 6 hane). Config ile eşleme yalnız gizli bir eşleme dosyasındadır; puanlayıcı onu görmez.
- Paketi (yalnız `spec.md`) koşu klasörüne kopyalar, yapımcı brifini config'e göre doldurur, oturumu başlatır.
- Süre tavanı (duvar saati): şekil 45 dk, zor 90 dk, çok zor 180 dk. Tavanda oturum durur, o ana kadarki çıktı
  puanlanır, koşu `tavan` olur.
- GUI'si olan araçlarda (SolidWorks, SolidCraft, NX) aracın ana penceresini kaydeder (10 fps, 720p); masaüstü ve
  terminal kayda girmez.
- Her koşu kayıt dosyasına bir satır yazar: config, parça, başlangıç / bitiş, süre, token, durum
  (`tamam | tavan | cokme | yardimli`), not.

Kodu, istemler ve matris: [benchmark/kosu/](../benchmark/kosu/).

## 4. Puanlayıcı (scorer)

İki katman:

1. **`olc.py` (betik, araçtan habersiz):** `final.step`'i bir referans STEP ile **hizalamasız**, aynı global çerçevede
   karşılaştırır. Yayında referans katalog orijinaliydi; repoda orijinaller olmadığı için yayımlanan referans
   (`benchmark/degerlendirme/hedefler/P##/referans.step`) bizim en iyi koşumuzdur.
   - Gövdeleri Macar algoritmasıyla eşleştirir (ağırlık merkezi + sınır kutusu + hacim).
   - Gövde başına IoU, iki yönlü yüzey sapması (P95 ve maks, kesin B-rep mesafesiyle), hacim / alan / ağırlık merkezi /
     sınır kutusu tolerans kontrolleri, montaj pozu ve girişim kümesi, gizli özellik listesi, teknik resim ölçüleri.
   - Her OCC boolean ayrı işçi süreçte, bellek ve süre sınırıyla koşar. Bir adım çökerse işaretlenir, gerisi ölçülür;
     çıktı hiç boş kalmaz. Deterministiktir (sabit tohumlar).
2. **Kör puanlayıcı ajan (Opus 5.5):** koşuları yalnız `run_id` ile görür. Betiği koşar, betiğin "hakem" önerdiği
   sayım kalemlerinde karar verir ve gerekçesini yazar, sapmaları neden sınıfına ayırır
   (S: spec, B: yapımcı, K: kaynak çelişkisi, A: aracın sınırı). Rubriği değiştiremez.

Rubrik koşulardan **önce** kilitlendi: 100 puan = geometri 40, tamlık 10, montaj ve poz 10, özellik sadakati 20,
teknik resim 5, CAD kalitesi 15. Tek gövdeli parçada montajın 10 puanı geometriye eklenir. Canlı yayın tablosu
betiğin ölçtüğü **85 puanı** gösterir; CAD kalitesi (15) ayrı bir kontrol listesiyle puanlanır.

Ölçüm kodu, rubrik ve hedef listeleri: [benchmark/degerlendirme/](../benchmark/degerlendirme/). Bu klasör yapımcıya
**asla** gösterilmez.

## 5. Panel

Yerel bir web sunucusu ve üç sayfa:

- **Kontrol paneli:** beş istasyon (her config bir istasyon), her birinin kuyruğu ve o an çizdiği parça, makinenin CPU /
  RAM durumu. İki mod: her istasyon **kendi kuyruğunu** çizer ya da bütün istasyonlara **aynı parça** verilir
  (kafa kafaya). Bir parça kuyruktan panelden çıkarılır, kayda elle dokunulmaz.
- **Skor tablosu:** puan dosyasını okur (iptal edilen koşular hariç, aynı `run_id`'nin son satırı), config başına
  ortalama ve parça başına puanları gösterir.
- **Yayın sayfası:** izleyiciye dönük tek sayfa: beş yarışmacının kartları (araç, harness basamağı, linkler), 45 parçalık
  matris ve canlı durum.

Kodu: [panel/](../panel/).

## Bellek ve sıra kuralları

- Aynı anda her config yalnız **bir** parçada çalışır: en çok 5 tasarım açık olur.
- Planlanan kural: aynı anda yalnız **bir** `olc.py`. Canlı yayında `yayin_puanla.py` bunu gevşetti: yeterli boş bellek
  varken (≥ 4 GB) en çok **3** `olc.py`'yi paralel koştu. Her `olc.py` ağır adımlarından önce yine boş bellek bekler.
- Her şey kayıtta kalır: başarısız, iptal edilen ya da tavana takılan koşu silinmez.
