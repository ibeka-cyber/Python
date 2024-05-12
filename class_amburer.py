class Hamburger:
    def __init__(self, ad, fiyat,  icerikler=None):
        self.ad = ad
        self.fiyat = fiyat
        self.icerikler = icerikler if icerikler is not None else []

    def icerik_ekle(self, icerik):
        self.icerikler.append(icerik)

    def icerik_cikar(self, icerik):
        if icerik in self.icerikler:
            self.icerikler.remove(icerik)
        else:
            print(f"{self.ad} içerisinde {icerik} bulunmamaktadır.")

    def fiyat_guncelle(self, yeni_fiyat):
        self.fiyat = yeni_fiyat

    def __str__(self):
        return f"{self.ad}: {', '.join(self.icerikler)} - {self.fiyat} TL"

# Örnek kullanım
hamburger1 = Hamburger("Big Mac", 15, ["Kıyma", "Peynir", "Marul", "Sos"])
print(hamburger1)

hamburger1.icerik_ekle("Domates")
hamburger1.fiyat_guncelle(17)
print(hamburger1)

hamburger1.icerik_cikar("Marul")
print(hamburger1)
