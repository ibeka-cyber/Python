class Araba:
    def __init__(self, marka, model, yil, renk):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.renk = renk
        self.calisti_mi = False

    def calistir(self):
        if not self.calisti_mi:
            self.calisti_mi = True
            print(f"{self.renk} {self.marka} {self.model} çalıştırıldı.")
        else:
            print(f"{self.renk} {self.marka} {self.model} zaten çalışıyor.")

    def durdur(self):
        if self.calisti_mi:
            self.calisti_mi = False
            print(f"{self.renk} {self.marka} {self.model} durduruldu.")
        else:
            print(f"{self.renk} {self.marka} {self.model} zaten durdurulmuş.")

# Örnek kullanım
araba1 = Araba("Toyota", "Corolla", 2022, "Beyaz")
araba2 = Araba("Renault", "Clio", 2021, "Mavi")

araba1.calistir()
araba2.calistir()
araba1.durdur()
araba2.durdur()
araba1.calistir()
