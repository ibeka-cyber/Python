class BankaHesabi:
    def __init__(self, isim, bakiye=0):
        self.isim = isim
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"{self.isim} adlı hesaba {miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")

    def para_cek(self, miktar):
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            print(f"{self.isim} adlı hesaptan {miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL")
        else:
            print(f"Yetersiz bakiye. {self.isim} adlı hesapta {self.bakiye} TL bulunmaktadır.")

    def bakiye_sorgula(self):
        print(f"{self.isim} adlı hesabın bakiyesi: {self.bakiye} TL")

# # Örnek kullanım
#hesap1 = BankaHesabi("Ahmet Yılmaz", 1000)
# hesap1.bakiye_sorgula()
# hesap1.para_yatir(500)
# hesap1.para_cek(2000)
# hesap1.bakiye_sorgula()


