# -*- coding: utf-8 -*-
# basit hesap makinesi yapalım
print("1-Topla")
print("2-Çıkar")
print("3-Çarp")
print("4-Böl"),

secim=input("Operasyonu Seçiniz: ")
sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))

def Topla(sayi1,sayi2):
    return sayi1+sayi2
def Cıkar(sayi1,sayi2):
    return sayi1-sayi2
def Carp(sayi1,sayi2):
    return sayi1*sayi2
def Bol(sayi1,sayi2):
    return sayi1/sayi2

if secim=='1':
   print("Toplam: "+str(Topla(sayi1,sayi2)))
elif secim=='2':
    print("Fark: "+str(Cıkar(sayi1,sayi2)))
elif secim=='3':
    print("Çarpım: "+str(Carp(sayi1,sayi2)))
elif secim=='4':
    print("Bölüm: "+str(Bol(sayi1,sayi2)))
else:
    print("Yanlış seçim yaptınız!")
    