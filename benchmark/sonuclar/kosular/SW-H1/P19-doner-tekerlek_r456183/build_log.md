# build_log.md — döner tablalı tekerlek (swivel caster), SolidWorks 2024 + Python/pywin32

## Ne yaptım
- Spec'in global çerçevesi ve birimi (inç, +Y yukarı, döner eksen = Y, tekerlek ekseni x=1.515 y=-0.75) aynen kullanıldı.
  Bütün parçalar yerinde kuruldu; hiçbir taşıma yok. Belgeler IPS (inç) birimine ayarlandı; API'ye metre
  çevirisi yalnız `swlib.py` içinde (IN = 0.0254).
- Her gövde ayrı `.SLDPRT` (12 dosya; P10-a ve P10-b ayrı ayna parçalar), `Caster_Assembly.SLDASM` içinde
  birim dönüşümle (kontrol edildi) yerleştirildi. `final.step`: AP214 (FILE_SCHEMA AUTOMOTIVE_DESIGN),
  12 MANIFOLD_SOLID_BREP, birim INCH.
- Eskizler model koordinatlarında verilip `ModelToSketchTransform` ile eskiz koordinatına çevrilir; yaylar
  spec'teki merkez/yön (cw/ccw) bilgisinden hesaplanan 3 nokta ile çizilir. Profiller spec'teki noktaların aynısı.
- Özellikler: P01 = OUTER extrude (mid 2.058) − arka kırpma (R1.029 dışı, x<0) + RIDGE extrude (mid 2.266) − arka kırpma
  (R1.133) − GAP (ön: profil cut mid 1.66; arka: R0.83 revolve-cut) − kingpin deliği − aks deliği + yuvarlatmalar.
  P02 = bastırılmış merkez revolve + delikli/slotlu plaka extrude. P03 = kesit revolve + lug extrude (y 2.502→2.6).
  P04 revolve; P05 altıgen extrude + konik delik revolve-cut. P06 = gövde extrude + ayak yan profili extrude ∩ plan
  (plan dışı bölge cut ile) + 6 kaburga silindiri. P07/P08/P10 tekerlek ekseni düzleminde (y=-0.75 ref. düzlemi) revolve;
  P09, H1 Front düzleminden mid-plane extrude.
- Önemli ölçüler `scripts/parts.py` → `PARAMS` (bkz. `parametreler.md`); aynı adlar montajda global değişken.

## Nerede takıldım
- pywin32 geç bağlama SolidWorks'te çalışmadı → `sldworks.tlb`/`swconst.tlb` makepy ile erken bağlama.
- `IMathUtility.CreatePoint` için Python listesi yanlış aktarılıyordu → VT_ARRAY|VT_R8 VARIANT.
- P02: bastırılmış merkezin revolve'u kesilmiş plakayla birleşmedi → sıra değişti (önce revolve, sonra r=0.75 delikli
  plaka; kesit plakaya 0.01 bindirildi).
- P01: Top düzleminden çift yönlü R0.83 kesimi yanlış yöne gitti (tavanı da kesti) → revolve-cut ile çözüldü.
- **P01 R0.06 yuvarlatmaları:** 27 kenar tek özellikte başarısız oldu (R0.125 uç ve R0.06'lar ile R2.5/taç kesişimindeki
  blend'ler). Kenar kenar denemede yalnız 6/27 kenar yuvarlandı; kalan 21 kenar keskin. Bu yüzden çatal hacmi +0.28%
  büyük, CoM z = −0.0005 (yuvarlanan kenarlar simetrik çift değil). R0.125 (2 kenar) ve R0.04 sırt yuvarlatmaları (14 kenar) tamam.
- **P06 R0.04 ayak plakası yuvarlatmaları** (22 kenar) tek özellikte başarısız → bilerek atlandı (süre). Hacim etkisi küçük (+0.06%).

## Bilerek basitleştirdiğim / yorumladığım
- P01 R0.06'ların 21 kenarı ve P06 R0.04'ler eksik (yukarıda). Spec'teki küçük "blend" yamaları yok.
- P07 sırt (tread) R0.2 kenarları kesit profiline dahil edildi (revolve), ayrı fillet değil — geometri aynı.
- Silindirik yüzler SolidWorks'te tek yüz (spec'te periyodik bölünmeyle 2) → yüz sayıları farklı; spec bunu "bilgi" sayıyor.
- P09–H1 girişimi (0.17671 in³) spec gereği korunmuştur; başka çakışma yok.
- Global değişkenler montaj denklemlerinde belgeleme amaçlıdır; parça boyutları betikteki PARAMS'tan sürülür
  (eskizler boyutsuz, `AddToDB` ile çizildi).

## Ölçüm — spec §6 hedeflerine karşı (SolidWorks mass properties, gövde başına; bbox = GetExtremePoint)
| ID | Hacim in³ | ΔHacim | ΔAlan | max ΔCoM (in) | max ΔBBox (in) |
|---|---|---|---|---|---|
| P01 | 5.08147 | +0.276% | +0.92% | 0.0021 | 0.0000 |
| P02 | 0.83201 | −0.004% | −0.00% | 0.0001 | 0.0000 |
| P03 | 0.23071 | −0.005% | −0.01% | 0.0000 | 0.0000 |
| P04 | 0.12991 | −0.006% | +0.01% | 0.0000 | 0.0000 |
| P05 | 0.07254 | −0.005% | +0.00% | 0.0000 | 0.0000 |
| P06 | 1.90592 | +0.059% | +0.50% | 0.0005 | 0.0000 |
| P07 | 5.89432 | +0.036% | +0.03% | 0.0000 | 0.0000 |
| P08 | 0.60427 | −0.001% | −0.00% | 0.0000 | 0.0001 |
| P09 | 4.49923 | +0.000% | +0.00% | 0.0000 | 0.0001 |
| P10-a | 2.93142 | −0.003% | −0.00% | 0.0000 | 0.0001 |
| P10-b | 2.93142 | −0.003% | −0.00% | 0.0000 | 0.0001 |
| H1 | 0.58471 | +0.001% | −0.00% | 0.0000 | 0.0000 |

Toplam hacim 25.69794 in³ (hedef 25.68092, +0.066%); toplam alan 212.43 in² (hedef 211.90, +0.25%).
Bütün gövdeler önerilen toleransın içinde (hacim ≤ %0.5, CoM ≤ 0.02, bbox ≤ 0.005). Montaj kutusu
X [−1.8125, 4.2985], Y [−2.75, 2.75], Z [−1.25, 1.25] (gövde kutularından). Ayrıntı: `scripts/measure_results.json`.
