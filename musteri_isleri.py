class Musteri:
    def __init__(self, ad, soyad, email, telefon):
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.telefon = telefon
        self.adress = ""        
    def bilgileri_guncelle(self, ad=None, soyad=None, email=None, telefon=None):
        if ad:
            self.ad = ad
        if soyad:
            self.soyad = soyad
        if email:
            self.email = email
        if telefon:
            self.telefon = telefon

    def adres_ekle(self,adress):
        self.adress = adress 
    
    def adres_guncelle(self,adress):
        self.adress = adress