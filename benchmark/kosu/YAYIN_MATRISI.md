# Faz Yayın: canlı yayın koşu matrisi

2026-11-11 canlı yayınında çeşitlilik olsun ve kullanım hakları dolmasın diye 45 parça 5 config'e paylaştırıldı.
Her config 9 farklı parça aldı. Her parça **tek bir config'te, tek tekrarla** koşulur. `MATRIS.md`'deki Faz 1 / Faz 2
bundan ayrıdır.

## Kurallar

- **Config'ler:** NX-H2, SW-H1, SC-H0, B3D-H0, B3D-H1. Tanımları `MATRIS.md`'deki gibi.
- **Akış:** her config aynı anda **bir** parçada çalışır; parçası bitince sıradaki parçasını alır. Bu yüzden aynı anda
  en fazla **5** tasarım açık olur. CAD uygulamalarının tek penceresi zaten birden fazla koşuya izin vermez.
- **Görev:** yalnız A (spec'ten kör yapım). Kör koşu, guard, rubrik ve süre tavanları aynı.
- **Puanlama:** `yayin_puanla.py` en çok 3 ölçümü birlikte koşar, boş bellek 4 GB'ın altındayken yenisini başlatmaz.
- **Ekran kaydı:** SW ve SC koşularında alınır (`ekran_kayit.py`).
- **Spec:** parçanın spec'i hazır değilse koşu başlamaz. Kalan parçaların spec'i yayın sırası geldikçe yazıldı.
- **Liderlik tablosu:** config'ler farklı parçaları çizer. Zorluk her config'e dengeli dağıtıldı (aşağıdaki tablo).
  Sıralama, seviye başına puan ortalamasıyla yapılır; aynı parçada kafa kafaya karşılaştırma bu fazda yoktur. Yayın
  sırasında kontrol panelinden bazı parçalar birden çok istasyona verildi (P10, P16, P17, P19); bunlar kafa kafaya
  örnektir.

## Zorluk dağılımı

45 parça: 9 şekil, 22 zor, 14 çok zor.

| Config | Şekil | Zor | Çok zor |
|---|---|---|---|
| NX-H2 | 2 | 4 | 3 |
| SW-H1 | 2 | 4 | 3 |
| SC-H0 | 2 | 4 | 3 |
| B3D-H0 | 2 | 5 | 2 |
| B3D-H1 | 1 | 5 | 3 |

## Planlanan sıra (her sütunda yukarıdan aşağı)

| # | NX-H2 | SW-H1 | SC-H0 | B3D-H0 | B3D-H1 |
|---|---|---|---|---|---|
| 1 | P1 iç dişli (ş) | P2 krank kolu (ş) | P3 rulman kapağı (ş) | P9 konumlama kızağı (çz) | P5 rot başı (z) |
| 2 | P6 flanşlı yatak (z) | P4 elektronik kutusu (z) | P10 tırtıllı topuz (ş) | P11 sonsuz vida (ş) | P12 çapraz dişli (ş) |
| 3 | P7 kollu pres (çz) | P8 mengene (çz) | P13 soğutma plakası (z) | P14 bilyalı vida (ş) | P15 havalı redüktör (z) |
| 4 | P16 konik dişli (ş) | P17 kanca anahtar (ş) | P18 talaş siperi (z) | P19 tekerlek (z) | P20 darbe valfi (z) |
| 5 | P21 kardan (z) | P22 raf konsolu (z) | P23 kilit (z) | P24 ayar kolu (z) | P25 debimetre (z) |
| 6 | P26 iğne valf (z) | P27 gergi (z) | P28 filtre gövdesi (z) | P29 kaldırma halkası (z) | P30 gaz valfi (z) |
| 7 | P31 manometre (z) | P32 fan (z) | P33 döner mandal (çz) | P34 hava silindiri (z) | P35 dişli pompa (çz) |
| 8 | P36 vidalı kriko (çz) | P37 kabin rafı (çz) | P38 AC redüktör (çz) | P39 termometre (z) | P40 tork sınırlayıcı (çz) |
| 9 | P41 kavrama-fren (çz) | P42 kiriş arabası (çz) | P43 merdiven (çz) | P44 bilyalı mil (çz) | P45 ısı emici (çz) |

ş = şekil, z = zor, çz = çok zor. Her config'in ilk parçası spec'i hazır bir çekirdek parça olduğundan yayın hemen
başlayabildi. Gerçekte koşan parçalar ve sonuçları: `benchmark/sonuclar/`.

## Notlar

- **P14 (bilyalı vida) yayından çıkarıldı:** yaklaşık 900 mm boyunca tek yüzey olan vida dişi yüzünden bir koşunun
  puanlanması 2,5–4 saat sürüyordu. B3D-H0 bu fazda 8 parça koşacaktı. Çıkarmalar kontrol panelinden yapılır,
  satır silinmez.
- Cevap anahtarı yapımcının erişemediği ayrı bir sürücüde durdu; guard o sürücüye her başvuruyu reddetti.
- P10–P45 paketleri yalnız A görevi için (B / C yok).
- **P7 (kollu pres) yayında NX-H2'den B3D-H1'e taşındı.**
- `istasyonlar/<config>/kuyruk.csv` dosyaları yayın sonundaki hâlidir: yayın sırasında kontrol panelinden satır eklendi
  ve çıkarıldı, bu yüzden yukarıdaki planlanan sıradan farklıdır.
