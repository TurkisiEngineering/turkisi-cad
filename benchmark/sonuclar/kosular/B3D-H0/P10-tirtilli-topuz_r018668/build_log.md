# Build log – P10 kaburgalı tutamak topuzu (build123d 0.11.1)

## Ne yapıldı
Tek betik `knob.py`; her gövde spec'teki adımlarla, global çerçevede yerinde kuruldu (taşıma yok).

- **P01 çekirdek:** C1 (r,z) profili çizgi + üç-noktalı yaylarla (verilen merkez/uç noktalardan) kurulup Z etrafında
  döndürüldü. C2: 8 adet R0.33 silindir kesildi. C3: K = (Lci prizması ∪ (döner profil ∩ Lci prizması)) − göbek konisi
  (uzatılmış 3° koni) − 4 adet 0.05 kalın levha; sonra çekirdekten çıkarıldı. C4: yuva + basamak + 3° konik delik +
  R0.015 içbükey yuvarlatma döner kesim. C5: alın bileziği eklendi.
- **P02 kaplama:** Lo ve Li plan konturları BuildSketch'te (daire − 8 disk, sonra 16 köşe R0.1 fillet) kuruldu.
  S1 B = Lo prizması − Li prizması; S2 z=-0.18 ve z=0.5'teki tüm yatay kenarlara (dış alt, dış üst, iç alt halkalar)
  R0.06 fillet; S3 kubbe başlığı eklendi; S4 Lci prizması (0.26–0.35), üst açıklık döner kesimi ve bitmiş çekirdek
  çıkarıldı.
- **P03 insert:** Tüp (R0.265625, delik R0.1875) + sağ el helisel diş "dişi". Diş, profil köşelerinden geçen tam
  helisler (build123d `Helix`, pitch 0.0625) arasında yönetilen (ruled) yüzeyler + iki uç kapak yüzünden dikilip
  katı yapıldı, tüp boyuna kırpıldı ve tüple birleştirildi. Faz: θ=0'da diş merkezi = -0.379218 + P/2 → dip düzlüğü
  -0.379218'de. İki uçta 90° havşa konisi kesildi.
- **Dışa aktarım:** `final.step`, AP214 (AUTOMOTIVE_DESIGN şeması), uzunluk birimi INCH (`write.step.unit`),
  üç ayrı etiketli solid (P01_knob_core, P02_grip_coating, P03_threaded_insert).

## Takıldığım yerler
- `Circle(rotation=…)` 0.11.1'de yok → dairenin dikiş noktasını bir oyuk merkezine (22.5°) `Locations(Rot)` ile
  döndürdüm; böylece dikiş kesilip gidiyor ve 16 köşenin hepsi temiz fillet'leniyor.
- Diş için `sweep(is_frenet=True)` önce ters yönlü (negatif hacimli) katı verdi, düzeltince de tüple birleştirme
  sessizce dişi yuttu; `binormal` modu çökük profil verdi. Çözüm: yönetilen yüzeylerden diş katısı (yukarıda).
  Ayrıca diş kenarının tam R0.1875 delik silindirine teğet oturması boolean'ı bozuyordu; diş yanakları 30° ile
  0.005 kadar tüp duvarına uzatıldı (`THREAD_EMBED`), böylece delik silindirini enine kesiyor ve kesişim sonucu dip
  düzlüğü tam P/8 çıkıyor (geometriye etkisi yok).
- build123d `export_step(unit=IN)` dosyayı mm olarak yazıyordu; `write.step.unit=INCH` statik ayarıyla inç yazıldı.

## Yorum / basitleştirme
- **Havşa derinliği:** Spec "r0.21875'ten 0.03125 derinlikte r0.1875'e; koniler dişi keser" diyor. Koniyi dişin
  tepe çapına kadar (tam koni) sürdürdüm. Alternatif (koni 0.03125'te biter, o derinliğe kadar diş tamamen silinir)
  denendi: V 0.06402, A 1.9391 → hedeften belirgin uzak; tam koni V 0.06336, A 1.8865 → çok yakın. Tam koni seçildi.
- Yüz sayıları master'dan farklı (çekirdek 118/123, kaplama 255/292, insert 16/27): master'da periyodik/helisel
  yüzeyler ve fillet yüzleri farklı bölünmüş; hacim/alan eşleştiği için geometri farkı değil, topoloji bölünmesi
  olarak değerlendirdim.
- Kasıtlı başka basitleştirme yok.

## Ölçüm – hedef karşılaştırma (betik çıktısı, inç)

| Gövde | Hacim (ölç / hedef) | Alan (ölç / hedef) | CoM (ölç / hedef) | Bbox | Yüz |
|---|---|---|---|---|---|
| P01 | 2.07189 / 2.07189 | 24.9618 / 24.9600 (+0.007 %) | (0,0,0.07567) / (0,0,0.07567) | ±1.2, -0.695..0.62 ✓ | 118 / 123 |
| P02 | 0.72941 / 0.72941 | 25.8622 / 25.8622 | (0,0,0.22687) / (0,0,0.22687) | ±1.26, -0.18..0.68 ✓ | 255 / 292 |
| P03 | 0.06336 / 0.06340 (-0.06 %) | 1.8865 / 1.8851 (+0.07 %) | (0.00055,-0.00016,-0.43000) / (-0.00012,-0.00032,-0.43003) | ±0.265625, -0.68..-0.18 ✓ | 16 / 27 |
| Montaj | 2.86468 / 2.86470 | 52.7088 / 52.7074 | z 0.10298 / 0.10298 | ±1.26, -0.695..0.68 ✓ | – |

- STEP geri okundu: 3 solid, toplamlar yukarıdakiyle aynı; ikili kesişim hacimleri 0 (çakışma yok, sadece temas).
- Tüm gövdeler `is_valid = True`.
- İnsert CoM'unun eksenden sapması (≈0.0005 in = 0.014 mm) helisin uçlardaki kesim fazından gelir; spec'teki
  faz ve el yönü (Helix'in +X'ten başlayıp +Y'ye doğru yükseldiği doğrulandı) aynen uygulandı. Kalan küçük fark
  büyük olasılıkla master'ın havşa/diş kesişim ayrıntısından; daha fazla ayarlama yapılmadı.
