# Benchmark: spec'ten kör CAD yapımı

F23 "Agentic CAD Ligi" yayınının sınavı. Bir yapımcı ajan, yalnız yazılı bir tasarım spec'ini okuyarak parçayı kendi CAD
aracıyla sıfırdan kurar ve `final.step` teslim eder. Ayrı bir değerlendirici, teslimi hedef listelerine karşı ölçer ve
puanlar. Kendi CAD harness'inizi (araç + MCP / CLI + istemler + skill'ler) bu 46 paketle sınayabilirsiniz.

| Klasör | Kimin için | İçerik |
|---|---|---|
| [`specs/`](specs/) | **yapımcı ajan** | `P##-<ad>/spec.md`: parça başına tek tasarım belgesi (İngilizce), ve [`INDEX.csv`](specs/INDEX.csv) |
| [`degerlendirme/`](degerlendirme/) | **değerlendirici** | ölçüm kodu (`olc.py`), [rubrik](degerlendirme/RUBRIK.md), paket başına hedef listeleri |
| [`kosu/`](kosu/) | koşuyu düzenleyen | F23 koşu düzeneği: başlatıcı, guard kancası, istemler |
| [`sonuclar/`](sonuclar/) | herkes | F23 puanları ve bitmiş çıktılar |

## Kör koşu kuralı

**Yapımcı ajan yalnız `specs/P##-<ad>/` klasörünü görür.** `degerlendirme/`, `sonuclar/` ve bu reponun geri kalanı onun
erişiminin dışında kalır. Hedef listelerini gören bir yapımcı ölçüleri spec'ten değil cevap anahtarından okur; o koşunun
puanı anlamsızdır.

En sağlam yol fiziksel ayrımdır: yapımcıyı boş bir çalışma klasöründe başlatın ve oraya yalnız o paketin `spec.md`'sini
kopyalayın. Repoyu yapımcının erişebileceği bir yerde tutmayın.

```bash
mkdir -p ~/kor-kosu/P02 && cp benchmark/specs/P02-krank-kolu/spec.md ~/kor-kosu/P02/
cd ~/kor-kosu/P02 && claude        # yapımcı oturumu yalnız bu klasörü görür
```

Aynı makinede repo da duruyorsa ikinci bir kilit ekleyin. Claude Code'da `settings.json` içindeki `Read(...)` reddi
dosya okuyan yerleşik araçları (Read, Grep, Glob) keser; kabuk komutlarını ise bir PreToolUse kancası keser (F23'teki tam guard: [`kosu/guard/`](kosu/guard/)):

```json
{
  "permissions": {
    "deny": [
      "Read(//**/benchmark/degerlendirme/**)",
      "Read(//**/benchmark/sonuclar/**)"
    ]
  },
  "hooks": {
    "PreToolUse": [
      { "matcher": "*", "hooks": [{ "type": "command", "command": "python C:/kor-guard/kor_guard.py" }] }
    ]
  }
}
```

```python
# kor_guard.py: aracın girdisinde yasak bir yol geçerse çağrıyı reddeder (çıkış kodu 2 = engelle)
import json, sys
YASAK = ("degerlendirme", "sonuclar", "hedefler", "olc.py")
girdi = json.dumps(json.load(sys.stdin).get("tool_input", {})).lower()
if any(y in girdi for y in YASAK):
    print("Kör koşu: değerlendirme dosyalarına erişim yasak.", file=sys.stderr)
    sys.exit(2)
```

Guard dosyasını (`kor_guard.py`) ve `settings.json`'ı yapımcının çalışma klasörünün **dışında** tutun ve kancada mutlak
yolla çağırın (örnekte `C:/kor-guard/kor_guard.py`; Linux / macOS'ta ör. `/opt/kor-guard/kor_guard.py`). Klasörün
içindeki bir guard'ı yapımcı okuyabilir ya da değiştirebilir.

Değerlendirici ajan ise yalnız teslim klasörünü ve `degerlendirme/` klasörünü görür; nasıl çalıştırılacağı
[`degerlendirme/README.md`](degerlendirme/README.md)'de.

## Paketler ve seviyeler

46 paket: **P00** kalibrasyon levhası (araç kurulumunu denemek için; sıralamaya girmez) ve **P01–P45** gerçek mekanik
parçalar. Gövde sayısı 1'den 248'e kadar. Tam liste: [`specs/INDEX.csv`](specs/INDEX.csv).

| Seviye | Paket | Süre tavanı | Örnek |
|---|---|---|---|
| `sekil` (şekil) | P00 + 9 | 45 dk | iç dişli, krank kolu, tırtıllı topuz, sonsuz vida |
| `zor` | 22 | 90 dk | ABS elektronik kutusu, rotil başı, döner tekerlek, manometre |
| `cok_zor` (çok zor) | 14 | 180 dk | kollu pres, havalı mengene, platform merdiven (248 gövde) |

Süre tavanı dolunca o ana kadar teslim edilen puanlanır. Birim (`mm` / `in`) spec'te yazar; ölçüm her zaman mm'dir.

## F23'te yarışan 5 config

Model hepsinde aynı (Opus 5.5); değişen yalnız araç ve harness. Kurulum rehberleri [`../tools/`](../tools/) altında.

| Config | Bir satırda |
|---|---|
| NX-H2 | Siemens NX + Usta'nın özel harness'i. **Paylaşılmıyor**; bkz. [`../tools/nx/`](../tools/nx/) |
| SW-H1 | SolidWorks + açık kaynak SolidworksMCP-TS sunucusu: [`../tools/solidworks/`](../tools/solidworks/) |
| SC-H0 | SolidCraft, yalnız kendi komut satırı aracıyla (MCP yok): [`../tools/solidcraft/`](../tools/solidcraft/) |
| B3D-H0 | build123d (Python), MCP yok; ajan betik yazıp koşar: [`../tools/build123d/`](../tools/build123d/) |
| B3D-H1 | build123d + açık kaynak build123d-mcp sunucusu: [`../tools/build123d/`](../tools/build123d/) |

Ajan tarafı (Claude Code kurulumu, MCP bağlama): [`../tools/claude-code/`](../tools/claude-code/). Koşu düzeneği:
[`kosu/`](kosu/). Puanlar ve çıktılar: [`sonuclar/`](sonuclar/).

## Teslim

Yapımcıdan beklenen 5 kalem (RUBRIK §2): `final.step` (AP214; spec'in global çerçevesinde, hizalamasız), native kaynak
(araç dosyası ya da betik), `yeniden_kur.md`, `parametreler.md`, `build_log.md`.

## Uyarı: bu 45 parça artık kör değil

Hedef listeleri (`degerlendirme/hedefler/`) bu repoyla **herkese açıktır**. Bu listeleri okumuş bir insan ya da ajan
için, ve bu repoyu eğitim verisinde görmüş olabilecek gelecekteki modeller için, P01–P45 artık kör bir sınav değildir.
Sonuçlarınızı paylaşırken bunu belirtin. Gerçekten kör bir ölçüm istiyorsanız aynı yöntemle (spec + gizli listeler +
`olc.py`) kendi yeni parçalarınızı hazırlayın ve listeleri yapımcının göremeyeceği yerde tutun.
