soru_veriler = [{
    "metin": "Köknar, iğne yapraklı bir ağaçtır.",
    "cevap": "Doğru"
}, {
    "metin": "Uçaklarda pilot kabinine kokpit adı verilir.",
    "cevap": "Doğru"
}, {
    "metin": "Ses, en hızlı gaz ortamda yayılır.",
    "cevap": "Yanlış"
}]


class Soru:

  def __init__(self, metin, cevap):
    self.metin = metin
    self.cevap = cevap


class Quiz:

  def __init__(self, liste):
    self.soru_numarasi = 0  # corrected the variable name
    self.puan = 0
    self.soru_listesi = liste
    print("initialize metodu çağırıldı")

  def soru_kaldi_mi(self):
    return self.soru_numarasi < len(self.soru_listesi)

  def sonraki_soru(self):
    mevcut_soru = self.soru_listesi[self.soru_numarasi]
    self.soru_numarasi += 1
    kullanici_cevap = input(
        f"S.{self.soru_numarasi} : {mevcut_soru.metin} (Doğru/Yanlış) : ")
    self.cevap_kontrol(kullanici_cevap, mevcut_soru.cevap)

  def cevap_kontrol(self, kullanici_cevap, dogru_cevap):
    if kullanici_cevap.lower() == dogru_cevap.lower():
      self.puan += 1
      print("Doğru cevap")
    else:
      print(f"Yanlış cevap. Doğru cevap : {dogru_cevap}")

  def quiz_bitti_mesaji(self):
    print(f"Quiz bitti. Puanınız : {self.puan}/{self.soru_numarasi}")
    print("\n")


soru_bankasi = []
for soru in soru_veriler:
  soru_metni = soru["metin"]
  soru_cevap = soru["cevap"]
  yeni_soru = Soru(soru_metni, soru_cevap)
  soru_bankasi.append(yeni_soru)

quiz = Quiz(soru_bankasi)

while quiz.soru_kaldi_mi():
  quiz.sonraki_soru()

print("Kısa sınavı tamamladınız")
print(f"Sınav puanınız : {quiz.puan}/{quiz.soru_numarasi}")

