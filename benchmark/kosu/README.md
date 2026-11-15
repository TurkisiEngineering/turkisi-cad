# Koşu düzeneği (`benchmark/kosu/`)

F23 "Agentic CAD Ligi" yayınında her parçayı kuran **kör yapımcı** oturumlarını açan, kilitleyen ve kaydeden kod.
Referans koddur: yayında nasıl çalıştığını gösterir, kendi kurulumunuzda yolları ve gizli listeleri doldurarak
kullanabilirsiniz. Usta'nın NX harness'i (NX-H2) özeldir; NX'e özgü her şey çıkarıldı ya da "özel harness,
paylaşılmıyor" yer tutucusuna indirildi.

## İçerik

| Dosya | Ne işe yarar |
|---|---|
| `kos.py` | koşuyu hazırlar (`hazirla`), başlatır (`baslat`), sızıntı testi koşar (`sizinti`) |
| `guard/guard.py` | yapımcının her araç çağrısını denetleyen Claude Code `PreToolUse` kancası |
| `guard/kurallar.json` | guard kural kümesi (yer tutuculu: gizli klasör adlarınızı ve katalog numaralarınızı yazın) |
| `guard/test_guard.py` | guard birim testi (`python test_guard.py` → 31 / 31) |
| `ekran_kayit.py` | SolidWorks / SolidCraft penceresinin ekran kaydı (Windows, ffmpeg `gdigrab`) |
| `mcp_yokla.py` | bir stdio MCP sunucusunu başlatıp araç listesini yazar (duman testi) |
| `yayin_puanla.py` | biten yayın koşularını `../degerlendirme/olc/olc.py` ile puanlar: en çok 3 ölçüm aynı anda (`ISCI = 3`), yeni ölçüm yalnız boş bellek ≥ 4 GB iken başlar |
| `istasyonlar/` | yayındaki istasyon orkestratörlerinin istemleri (`ORTAK_KURALLAR.md`, config başına `PROMPT.md` + `kuyruk.csv`; kuyruklar yayın sonundaki hâlidir, bkz. `KUYRUK_NOTU.md`) |
| `KOR_KOSU.md` | körlük ve adillik kuralları |
| `MATRIS.md` | planlanan tam deneyin matrisi (config'ler, basamaklar, süre tavanları, kayıt biçimi) |
| `YAYIN_MATRISI.md` | canlı yayında 45 parçanın 5 config'e dağılımı |

## Model ve plan

- **Yapımcı:** her koşu taze bir `claude -p` oturumu, model `claude-opus-5-5`, effort `high`, izin modu
  `bypassPermissions` (guard kancası her çağrıyı yine denetler). Aynı brif şablonu (`kos.py` içindeki `BRIF`),
  config'e özgü tek paragraf dışında kelimesi kelimesine aynı.
- **İstasyon orkestratörü:** Fable 5.2 (yedek yol; asıl yol token harcamayan kontrol paneliydi, bkz. `panel/`).
  Orkestratör modeli kurmaz, yalnız `kos.py`'yi çağırır.
- **Süre tavanı:** şekil 45 dk, zor 90 dk, çok zor 180 dk (duvar saati). Token tavanı yok, kullanım kaydedilir.
- Yayında koşan config'ler: SW-H1, SC-H0, B3D-H0, B3D-H1 ve NX-H2 (özel). Faz 0 dumanında ayrıca SW-H0, SC-H1,
  B3D-H1b denendi.

## Bir koşu nasıl hazırlanır ve başlatılır

Önkoşullar: Claude Code CLI (`claude`), Python 3.11+ (`yayin_puanla.py` için ayrıca `psutil`), aracın kendisi (build123d, SolidWorks + pywin32, SolidCraft),
H1 config'leri için ilgili MCP sunucusunun kurulumu (`tools/` altındaki rehberler). Üçüncü taraf MCP kodu bu repoda
yoktur.

1. İş kökünü seçin ve paketi koyun:
   ```
   set TCAD_IS_KOKU=C:\cad-is            (varsayılan: bu klasörün altında _is\)
   <IS_KOKU>\paketler\P02\A\spec.md       (benchmark/specs/P02-krank-kolu/spec.md'nin kopyası)
   ```
   H1 için MCP sunucuları `<IS_KOKU>\mcp\` (ya da `TCAD_MCP_KOKU`) altında beklenir.
2. `guard/kurallar.json`'daki `<...>` yer tutucularını doldurun: cevap anahtarınızın durduğu klasör adı, yasak sürücü
   harfi (`yasak_surucu`), satıcı adı, katalog numaraları.
3. Hazırla (run_id yazar, girdiyi kopyalar, settings / mcp / brif dosyalarını üretir):
   ```
   python kos.py hazirla --config B3D-H0 --parca P02 --gorev A --faz Y --tekrar 1 --sure-dk 45
   ```
4. Başlat (süre tavanında süreç ağacı kapatılır, koşu `tavan` olur):
   ```
   python kos.py baslat r123456
   ```
5. Bittiğinde son satır JSON'dur: `{"run": ..., "durum": "tamam|tavan|cokme", "dk": ..., "usd": ..., "arac": ..., "red": ...}`.
   Kayıt `<IS_KOKU>\kayit\kosu_listesi.csv`'ye bir satır olarak eklenir; teslim `<IS_KOKU>\kosular\<run_id>\teslim\`.
6. Puanlama: `python yayin_puanla.py --bir-kez` (`pip install psutil` gerekir). Her paket için gizli klasörü
   hazırlayın: `benchmark/degerlendirme/hedefler/P##/` altındaki hedef dosyalarını `<IS_KOKU>\paketler\<paket>\_gizli\`
   içine kopyalayın ve yanına `{"orijinal_step": "<referans STEP yolu>"}` içeren bir `kaynak.json` yazın. Referans STEP
   olarak aynı klasördeki `referans.step` (yayının en iyi koşusu) kullanılabilir; yayındaki orijinal katalog modelleri
   paylaşılmıyor. Bu klasör yapımcıya hiç gösterilmez.

Sızıntı testi: `python kos.py sizinti <run_id>` yapımcıya 16 yasak denemeyi tek tek yaptırır; hepsinin
`reddedildi` dönmesi gerekir. Metindeki `<...>` yolları kendi gizli yollarınızla doldurun.

## Yapımcı oturumu nasıl kilitlenir

`kos.py baslat` şu bayraklarla açar:

- `--setting-sources project`: kullanıcı ayarları, eklentiler ve kullanıcı kancaları yüklenmez.
- `--settings oturum/<run>/settings.json`: tek kanca, guard; ayrıca WebSearch / WebFetch izin listesinde reddedilir.
- `--mcp-config oturum/<run>/mcp.json --strict-mcp-config`: yalnız config'in kendi MCP'si (H0'da hiçbiri).
- `--disallowedTools`: web, workflow, artifact, zamanlayıcı, mesajlaşma, worktree araçları; H0 / H1'de ayrıca
  `Skill`, `Agent`, `Task` ve `--disable-slash-commands`.
- `cwd` = koşu klasörü. Yapımcı brifi stdin'den gider.

## Guard neyi engeller

Her araç çağrısında (`PreToolUse`) şu sırayla:

1. **Araç adı:** web araçları, tarayıcı / bilgisayar kontrolü, uygulama içi araçlar, zamanlayıcılar, alt oturum ve
   mesajlaşma araçları; config'in izinli listesinde olmayan her MCP aracı; H0 / H1'de `Skill`, `Agent`, `Task`;
   H2'de uzman önekiyle başlamayan skill.
2. **Metin:** çağrının bütün girdisi (yollar, komutlar, yazılan içerik) küçük harfe çevrilip taranır; kendi koşu
   klasörü çıkarıldıktan sonra kalan metinde yasak kelime (cevap anahtarı klasörü, satıcı adı, masaüstü / indirilenler,
   guard'ın kendi dosyaları), katalog numarası, yasak sürücü, ağ komutu (`curl`, `wget`, `Invoke-WebRequest`,
   `urllib`, `requests`, `socket`...), paket kurma (`pip install`, `npm install`, `npx`, `uv add`), `git clone`,
   üst klasöre çıkma (`..\..`, `cd ..`) ya da başka bir koşunun klasörü geçerse reddedilir.
3. **`.claude`:** kullanıcı skill / bellek klasörlerine erişim reddedilir (H2'de yalnız uzman skill klasörü açık).
4. **Yazma yeri:** `Write` / `Edit` yalnız kendi koşu klasörüne.

Red mesajı yapımcıya genel bir cümleyle gider ("Bu işlem bu görevde kapalı..."); hangi kuralın tuttuğu yalnız
`guard.log`'da yazar. Bir kanca hatası da güvenli tarafta kalır (red). Koşudaki red sayısı `kosu_listesi.csv`'nin
`not` sütununa ve `benchmark/sonuclar/puanlar.csv`'nin `guard_red` sütununa geçer. Reddedilen bir deneme koşuyu
geçersiz yapmaz (yapımcı denemiş ama geçememiştir); bir yasak **geçseydi** koşu geçersiz sayılıp yeniden koşulurdu.

## Akış kaydı nedir

`kos.py baslat`, `claude -p --output-format stream-json --verbose` çıktısını satır satır
`<IS_KOKU>\kayit\akis\<run_id>.jsonl` dosyasına yazar: yapımcının her mesajı, her araç çağrısı ve sonucu, en sonda
`result` satırı (token kullanımı ve $ maliyeti). Dosya koşu klasörünün dışındadır; yapımcı göremez. `kos.py` bitişte
bu dosyadan token / maliyet / araç çağrısı sayısını okuyup `kosu_listesi.csv`'ye yazar; yayın paneli de canlı kartları
bu akıştan çizer. Akış kayıtları yerel yolları ve oturum kimliklerini içerdiği için bu repoya konmadı; sayısal özetleri
`benchmark/sonuclar/puanlar.csv`'dedir.
