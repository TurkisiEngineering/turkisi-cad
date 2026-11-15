# skills: NX dışı CAD skill'leri ve ajanları

Bu klasörde Claude Code için hazırlanmış, araçtan bağımsız (çoğu build123d / OCP tabanlı) CAD skill'leri ve ajan
tanımları var. Her alt klasör olduğu gibi kullanılabilen bir **Claude Code skill klasörüdür** (`SKILL.md` + varsa ek
dosyalar). Skill metinleri özgün hâliyle İngilizce kaldı; bu README Türkçedir.

> **NX yok.** Türkişi Engineering'in Siemens NX harness'i (`nx-*` skill'leri, journal yardımcıları) özeldir ve bu repoya
> girmez. Buradakiler, F23 yarışmasında NX-H2 dışındaki herkesin de kurabileceği genel kalite kapılarıdır.

## Skill'ler

| Klasör | Ne işe yarar |
|---|---|
| [`cad-qa-gate/`](cad-qa-gate/SKILL.md) | Çok ajanlı bir CAD döngüsünü durum makinesi gibi yürütür: her turda durum başlığı, hedef başına en çok 3 iterasyon (devre kesici), yalnız yol + ölçü taşıyan yalın veri aktarımı, `DESIGN_SPEC.md`'ye bağlı sayısal + görsel kabul kapısı. Başarısız geometri asla "APPROVED" yazılmaz. |
| [`cad-section/`](cad-section/SKILL.md) | build123d gövdesinden kırpılmamış 2B kesit / siluet PNG'si üretir (matplotlib, genişletilmiş eksen sınırları). Görsel QA için. |
| [`interference-check/`](interference-check/SKILL.md) | Montajda gövde çiftlerinin boolean kesişim hacmini (mm³) ölçer, gövde ile yerleştirilen parça arasındaki boşluğu doğrular. Girişimi göz kararıyla değil sayıyla kapatır. |
| [`printability-check/`](printability-check/SKILL.md) | FDM / SLA baskıya uygunluk: baskı tablasına sığma, en küçük et kalınlığı, desteksiz sarkmalar. Ölçülen değerlerle geçti / kaldı raporu. |
| [`step-registry/`](step-registry/SKILL.md) | Dış STEP bileşenlerini build123d'ye alır, ölçer, ortak montaj çerçevesine yerleştirir; yer tutucu bir STEP'i tek satır değişiklikle başkasıyla değiştirir (kayıt sözlüğü deseni). |

## Ajanlar (`agents/`)

Claude Code alt ajan tanımları. Birlikte bir "tasarımcı → baş mühendis → render → doküman" hattı kurarlar.

| Dosya | Rol |
|---|---|
| [`agents/cad-designer.md`](agents/cad-designer.md) | Parametrik tasarımcı: build123d ile modeller, STEP + STL + kesit PNG + ölçülmüş REPORT üretir. Kendi işini onaylamaz. |
| [`agents/cad-lead-engineer.md`](agents/cad-lead-engineer.md) | Baş mühendis / kalite kapısı: STEP'i bağımsız yeniden ölçer, kesitlere bakar, girişim ve baskı kontrollerini koşar, `RV##` APPROVED / REVISE kararı yazar. |
| [`agents/cad-render-expert.md`](agents/cad-render-expert.md) | STEP'i mesh'e çevirip Blender (headless) ile stüdyo render'ları alır. Geometriye dokunmaz. |
| [`agents/cad-doc-expert.md`](agents/cad-doc-expert.md) | Ölçülendirilmiş 2B resim seti, konsept sayfası ve teslim PDF'i hazırlar; her ölçü spec'ten ya da QA ölçümünden gelir. |

## Kurulum

1. Bu repoyu indir ya da klonla.
2. Skill'leri kopyala:
   - **Bütün projelerde:** `skills/<ad>/` klasörünü `~/.claude/skills/<ad>/` altına kopyala.
   - **Tek projede:** projenin kökünde `.claude/skills/<ad>/` altına kopyala.
3. Ajanları kopyala: `skills/agents/*.md` dosyalarını `~/.claude/agents/` (ya da projede `.claude/agents/`) altına koy.
4. Claude Code'u yeniden başlat. Skill'ler açıklamalarına göre kendiliğinden devreye girer; `/<ad>` ile de çağrılabilir.

Gerekenler: Python 3.10+, `build123d` (OCP ile birlikte gelir), `matplotlib`. Render ajanı için Blender ve isteğe bağlı
FreeCAD (`freecadcmd`), doküman ajanı için bir LaTeX dağıtımı (ör. MiKTeX) gerekir.

## Uyarlaman gerekenler

- **Yer tutucu yollar:** ajan metinlerinde `<CADWORK>` (yerel, bulutla eşitlenmeyen iş klasörü), `<FREECAD_DIR>`,
  `<BLENDER_DIR>`, `<MIKTEX_BIN>` geçer. Kendi makinendeki yollarla değiştir.
- **Paylaşılmayan şablonlar:** ajanlar bir proje hattının dosyalarına atıf yapar: `DESIGN_SPEC.md` (§5 kapı tablosu,
  §6 varsayım defteri), `_PIPELINE/templates/DELIVERY_STANDARDS.md`, `_PIPELINE/templates/VERDICT_TEMPLATE.md`,
  `GATE_LIBRARY` §P. Bunlar bu repoda **yok**; kendi projende aynı adla kendi şablonunu yaz ya da ajan metninden çıkar.
- `step-registry` içindeki bileşen adları (`lidar.step`, `wheel_left.stp` …) yalnız örnektir.
- build123d / OCP sürümüne göre `offset`, `&` (kesit) gibi çağrıların davranışı değişebilir; skill'ler bunu kendi
  "Gotchas / Notes" bölümlerinde söylüyor.

## Lisans

Repo kökündeki [MIT lisansı](../LICENSE) geçerlidir.
