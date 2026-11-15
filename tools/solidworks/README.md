# SolidWorks: SW-H0 (çıplak COM API) ve SW-H1 (+ SolidworksMCP-TS)

| Config | Yapımcının elinde |
|---|---|
| **SW-H0** | Python + `pywin32` ile SolidWorks COM API'si (ajan kendi betiğini yazar) |
| **SW-H1** | SW-H0 + topluluk MCP'si [`vespo92/SolidworksMCP-TS`](https://github.com/vespo92/SolidworksMCP-TS/tree/ea5539948b816cd34571a4eda00a3a93f4bd86bb) |

Yayında SW-H1 koştu. SolidWorks MCP'leri arasında GitHub'da en çok yıldızlı olan seçildi (2026-11-11'de 252★).

## 1. Ön koşullar

| Bileşen | Bizdeki | Not |
|---|---|---|
| İşletim sistemi | Windows 11 (derleme 26200) | COM yalnız Windows'ta |
| SolidWorks | **SOLIDWORKS 2024** (`SLDWORKS.exe` dosya sürümü 32.5.0.0048), lisanslı | MCP'nin README'si 2021–2025 sürümlerini destekler diyor |
| Python | 3.13.13 | SW-H0 ve fiilen SW-H1 için |
| pywin32 | 312 | `pip install pywin32` |
| Node.js | v24.15.0 | MCP için; MCP'nin README'si Node 20+ istiyor |
| C++ derleme araçları | **yoktu** | MCP'nin `winax` modülü için gerekli; aşağıdaki sorun giderme bölümüne bakın |

## 2. SW-H0: pywin32 ile COM

```bash
pip install pywin32
python -c "import win32com.client as w; sw = w.Dispatch('SldWorks.Application'); sw.Visible = True; print('bağlandı')"
```

Ajan SolidWorks'ü COM ile kendisi başlatabilir; koşu sonunda yalnız kendi açtığı belgeleri kapatır. Yapımcıya verilen
araç cümlesi (koşu brifinden aynen):

> SolidWorks (kurulu). Python + pywin32 ile SolidWorks COM API'sini kullanarak modelle; gerekirse SolidWorks'ü COM
> ile başlat, koşu sonunda yalnız kendi belgelerini kapat. Native: `.SLDPRT` / `.SLDASM` + betikler.

STEP: COM `SaveAs3` ile AP214 (`AUTOMOTIVE_DESIGN`), SI mm başlığıyla çıktı.

## 3. SW-H1: SolidworksMCP-TS kurulumu

Kullandığımız sürüm: commit
[`ea5539948b816cd34571a4eda00a3a93f4bd86bb`](https://github.com/vespo92/SolidworksMCP-TS/commit/ea5539948b816cd34571a4eda00a3a93f4bd86bb)
(2026-09-20), paket sürümü `3.1.3`, sunucu **86 araç** listeledi.

```bash
git clone https://github.com/vespo92/SolidworksMCP-TS
cd SolidworksMCP-TS
git checkout ea5539948b816cd34571a4eda00a3a93f4bd86bb
npm ci
npm run build          # dist/index.js oluşur
```

Claude Code'a bağlama (yayındaki tanım; `env` boş bırakıldı):

```json
{
  "mcpServers": {
    "solidworks": {
      "type": "stdio",
      "command": "node",
      "args": ["<KÖK>/mcp/SolidworksMCP-TS/dist/index.js"],
      "env": {}
    }
  }
}
```

ya da

```bash
claude mcp add solidworks -- node "<KÖK>/mcp/SolidworksMCP-TS/dist/index.js"
```

Aynı tanım dosya olarak: [`ornek/mcp.json`](ornek/mcp.json). MCP'nin kendi README'si ayrıca `SOLIDWORKS_PATH` ve
`ADAPTER_TYPE` ortam değişkenlerini öneriyor; biz vermedik.

Yapımcıya verilen araç cümlesi: SW-H0'daki cümle + "Ek olarak `solidworks` MCP sunucusunun araçlarını kullanabilirsin."

Bağlantı denemesi: sunucu başlayınca kendi log'una şunu yazdı (2026-11-11):
`"SolidWorks MCP Server started", version 3.1.3, macroRecording: true, pdmIntegration: false, sqlIntegration: false`.
Her yapımcı oturumunun ilk satırında `solidworks: connected` ve 86 `mcp__solidworks__*` aracı görünüyordu.

## 4. Gerçekte ne oldu (dürüst not)

- **Kayıtlarımızdaki 7 SW-H1 koşusunun (yayında 6 + duman testinde 1) hiçbirinde yapımcı bir MCP aracı çağırmadı.** Akış kayıtlarında
  `mcp__solidworks__*` çağrısı sıfır; ajanlar her seferinde pywin32 ile kendi COM betiğini yazdı. Birkaç `build_log.md`
  bunu açıkça söylüyor: "MCP sunucusu kullanılmadı." Yani SW-H1 puanları fiilen SW-H0 yöntemiyle alındı.
- **Bizim kurulumumuzda `winax` modülü yoktu.** `npm ci` hata vermeden bitti, ama `node_modules/winax` oluşmadı
  (makinede Visual Studio C++ derleme araçları bulunamadı; `winax` isteğe bağlı bağımlılık olduğu için npm hatayı gizler).
  Sunucu açılıp araçları listeliyor, ama COM'a dokunan bir araç çağrılsaydı büyük olasılıkla "`winax` native module is
  not available" hatası verecekti. Bunu ayrıca denemedik: ajanlar hiç çağırmadığı için bu hata koşularda görünmedi.
  **Doğrulanmadı:** `winax` kurulu bir makinede MCP araçlarının SolidWorks 2024'te çalışıp çalışmadığı.

Kendi kurulumunuzda MCP araçlarını gerçekten kullanmak istiyorsanız önce `winax`'ı kurun (aşağıda).

## 5. Sorun giderme

**`winax` kurulmadı / "Cannot find package 'winax'" / "`winax` native module is not available"**

Kontrol:

```bash
cd SolidworksMCP-TS
node -e "import('winax').then(()=>console.log('winax VAR')).catch(e=>console.log('winax YOK', e.code))"
```

Bizde sonuç `winax YOK ERR_MODULE_NOT_FOUND` idi. MCP'nin kendi `TROUBLESHOOTING.md` dosyası nedenini şöyle anlatıyor:
`winax` her makinede yerelde derlenmek zorunda; Windows 11 26200+ ve VS 2022 Build Tools 17.14+ ile ATL başlıkları
uyumsuz (upstream [issue #23](https://github.com/vespo92/SolidworksMCP-TS/issues/23)). Önerdikleri yollar (biz
denemedik):

1. "Desktop development with C++" iş yükü ve "C++ ATL for latest v143 build tools" bileşeniyle VS 2022 Build Tools
   kurun (README 17.10 ya da daha eskisini öneriyor), sonra `npm ci` / `npm run build`'i tekrarlayın.
2. Daha eski bir `winax` sürümünü sabitleyin: `npm install winax@3.4.2 --save-optional --foreground-scripts`.
3. COM gerektirmeyen iş için (araç listesi, MCP bağlantısı) `USE_MOCK_SOLIDWORKS=true` ile sahte adaptörle çalıştırın.

**MCP araçları listede ama ajan kullanmıyor**

Bizim bütün koşularımızda böyle oldu: Opus 5.5 pywin32 ile doğrudan COM yazmayı tercih etti. MCP'nin README'sindeki
araç tablosu da çoğu kategoriyi "Untested" / "Partially tested" diye işaretliyor. MCP'nin katkısını ölçmek istiyorsanız
ajanın MCP'yi kullandığını akış kaydından (`"name":"mcp__solidworks__..."` satırları) kontrol edin.

**pywin32 COM tuzakları** (yapımcıların `build_log.md`'lerinden; SW-H0 ve SW-H1'de aynı)

- Geç bağlama (dinamik dispatch) bazı argümansız yöntemleri özellik sanıyor, bazen tersini yapıyor. Birkaç ajan
  `sldworks.tlb` / `swconst.tlb` tür kütüphanelerinden `makepy` ile **erken bağlamaya** geçerek çözdü.
- `SelectByID2("EDGE", ...)` ile koordinattan kenar seçmek her zaman tutmadı; gövdenin kenarlarını dolaşıp
  `GetClosestPointOn` ile verilen noktaya en yakın kenarı seçmek işe yaradı.
- Çok kenarlı tek yuvarlatma özelliği bazen başarısız oldu; kenarları gruplara bölmek ya da ayrı özellik yapmak gerekti.
- Çift yönlü "Through All" kesim, gövde yalnız bir taraftayken başarısız oldu; tek yön verildi.
- Dairesel çoğaltma API'den `None` döndü: `DName = "NULL"` ve `GeometryPattern = False` ile başarısız, `DName = ""` ve
  `GeometryPattern = True` ile çalıştı.

## 6. Ekran kaydı

SolidWorks penceresi görünen bir araç olduğu için yayında her SW koşusunun ekranı kaydedildi. Bu, kurulumun parçası
değil; koşu başlatıcı yapımcıdan habersiz başlatır.
