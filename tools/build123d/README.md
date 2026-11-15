# build123d: B3D-H0 (düz Python) ve B3D-H1 (+ build123d-mcp)

| Config | Yapımcının elinde |
|---|---|
| **B3D-H0** | build123d 0.11.1, düz Python betikleri (ajan `.py` yazar, `final.step`'i betik üretir) |
| **B3D-H1** | B3D-H0 + topluluk MCP'si [`pzfreo/build123d-mcp`](https://github.com/pzfreo/build123d-mcp/tree/49023cd809092daa10dea0e9648a87006591d1f1) |

İkisi de yayında koştu.

## 1. B3D-H0: build123d kurulumu

| Bileşen | Bizdeki sürüm |
|---|---|
| Python | 3.13.13 (Windows, sistem Python'u) |
| build123d | **0.11.1** |
| OCP (OpenCascade bağlaması) | `cadquery-ocp` 7.9.3.1.1 (sistem Python'unda); MCP ortamında `cadquery-ocp-novtk` 7.9.3.1.1 |

```bash
python -m pip install build123d==0.11.1
python -c "import build123d; print(build123d.__version__)"     # 0.11.1
```

Not: Bizim sistem Python'umuzda `cadquery` 2.8.0 da kuruluydu, bu yüzden orada OCP paketi `cadquery-ocp` adıyla
geldi. Temiz bir ortamda build123d 0.11.1 kendi bağımlılığı olarak `cadquery-ocp-novtk`'yı getirir (MCP'nin
`pyproject.toml` notu). İkisini aynı ortama kurmayın; build123d-mcp'nin notuna göre aynı yolda iki OCP derlemesi
`import build123d`'yi bozar. Ayrı bir sanal ortam en temizidir:

```bash
python -m venv .venv
.venv\Scripts\activate          # Linux / macOS: source .venv/bin/activate
pip install build123d==0.11.1
```

Kurulumu deneyin: [`ornek/plaka.py`](ornek/plaka.py) 80 × 50 × 8 mm, ortasında Ø12 delik olan bir plaka kurar.

```bash
cd tools/build123d/ornek
python plaka.py
# hacim = 31095.2 mm3, govde sayisi = 1
# final.step yazildi
```

Çıkan `final.step` AP214'tür (`AUTOMOTIVE_DESIGN`, SI mm, Open CASCADE). Biz bunu build123d 0.11.1 ile denedik.

Yapımcıya verilen araç cümlesi (koşu brifinden): "build123d 0.11.1 (Python). Native: `.py` betikleri; `final.step`'i
betik üretir."

## 2. B3D-H1: build123d-mcp kurulumu

Kullandığımız sürüm: commit
[`49023cd809092daa10dea0e9648a87006591d1f1`](https://github.com/pzfreo/build123d-mcp/commit/49023cd809092daa10dea0e9648a87006591d1f1)
(2026-11-09), paket sürümü `0.3.92.dev0`, sunucu **48 araç** listeledi. build123d MCP'leri arasında GitHub'da en çok
yıldızlı ikinci; birincisi (agentcad) aşağıda anlatılan nedenle seçilmedi.

Biz MCP'yi kendi sanal ortamına, sabit commit'ten kurduk:

```bash
git clone https://github.com/pzfreo/build123d-mcp
cd build123d-mcp
git checkout 49023cd809092daa10dea0e9648a87006591d1f1
python -m venv .venv                       # biz Python 3.13 kullandık; pyproject ">=3.11,<3.15" istiyor
.venv\Scripts\python -m pip install build123d==0.11.1 -e .
```

Kurulunca `.venv\Scripts\build123d-mcp.exe` oluşur. Bu ortamdaki ilgili sürümler: build123d 0.11.1,
build123d-mcp 0.3.92.dev0, `mcp` 2.3.0, `build123d-drafting-helpers` 0.15.5, `cadquery-ocp-novtk` 7.9.3.1.1.

Claude Code'a bağlama (yayındaki tanım):

```json
{
  "mcpServers": {
    "build123d": {
      "type": "stdio",
      "command": "<KÖK>/mcp/build123d-mcp/.venv/Scripts/build123d-mcp.exe",
      "args": [],
      "env": {}
    }
  }
}
```

ya da

```bash
claude mcp add build123d -- "<KÖK>/mcp/build123d-mcp/.venv/Scripts/build123d-mcp.exe"
```

Aynı tanım dosya olarak: [`ornek/mcp.json`](ornek/mcp.json). MCP'nin kendi README'si kurmadan çalıştırmayı da öneriyor:
`uv tool run --python 3.12 build123d-mcp@latest`. Biz bunu kullanmadık: `@latest` her gün değişir, ligde bileşenler
sabit olmalıydı.

Yapımcıya verilen araç cümlesi: B3D-H0 cümlesi + "Ek olarak `build123d` MCP sunucusunun araçlarını kullanabilirsin."

**Kör koşuda dikkat:** MCP'nin `install_skill` aracı ajanın proje klasörüne skill / talimat dosyası yazabiliyor
(MCP'nin README'si). H1 basamağında skill yoktur; bu araç bizim koşularımızda çağrılmadı.

## 3. Gerçekte ne oldu (dürüst not)

Kayıtlarımızdaki 6 B3D-H1 koşusunun (yayında 5 + duman testinde 1) yalnız **birinde** yapımcı MCP araçlarını kullandı (`execute` 1 kez, `render_view`
2 kez). Kalan 5 koşuda MCP bağlı olduğu halde (`build123d: connected`, 48 araç) ajan düz Python betiği yazıp
çalıştırdı. Yani B3D-H0 ile B3D-H1 arasındaki fark çoğu koşuda yalnız "MCP'nin elde olması"dır, kullanılması değil.

## 4. agentcad kullanıldı mı?

**Yayında hayır.** [`jdilla1277/agentcad`](https://github.com/jdilla1277/agentcad/tree/bedc4a92fb1de9b0c09bc056f43bf78866ecf448)
(commit `bedc4a92fb1de9b0c09bc056f43bf78866ecf448`, 2026-11-10) seçim günü GitHub'da en çok yıldızlı build123d
MCP'siydi (212★). Aday olarak kuruldu ve tek bir duman testi koşusu yapıldı (config adı B3D-H1b), sonra şu iki nedenle
ligden çıkarıldı:

1. **build123d sürümü:** agentcad `build123d>=0.10,<0.11` istiyor; kurulum build123d 0.10.0 getirdi. Ligin build123d
   sürümü 0.11.1'dir.
2. **İnternete çıkan araçlar:** listelediği 26 aracın 11'i `cloud_*` araçlarıdır ve internete çıkar; kör koşu kuralı
   (web yok) ile çelişir. Duman testinde guard bu araçları ayrıca kapatıyordu.

Kurulum denemesinden bir not: agentcad Python 3.13'e kurulamadı (`requires-python = ">=3.10,<3.13"`); Python 3.12 ile
`uv` sanal ortamına `pip install -e .[mcp]` ile kuruldu, sunucu `python -m agentcad.mcp` ile açıldı.

Yerine bir sonraki yıldızlı MCP olan `pzfreo/build123d-mcp` seçildi (karar 2026-11-11).

## 5. Sorun giderme

- **İki OCP paketi çakışması:** `cadquery-ocp` ile `cadquery-ocp-novtk` aynı ortamda olunca `import build123d`
  hata verebilir (MCP'nin `pyproject.toml` notu). Her araç için ayrı sanal ortam kullanın.
- **Windows konsolunda Türkçe karakter:** betiğin `print` ettiği Türkçe karakterler `cp1252` konsolda
  `UnicodeEncodeError` verebilir. Çıktıyı ASCII tutun ya da `python -X utf8 betik.py` ile çalıştırın.
- **macOS:** build123d-mcp'nin `pyproject.toml` notuna göre `cadquery-ocp-novtk` 7.9.3.1.1'in macOS paketi bozuk
  (`OCP.GccEnt` modülü yok). Biz macOS'ta denemedik; MCP'nin kendi notuna bakın.
