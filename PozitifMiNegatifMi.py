# -*- coding: utf-8 -*-
sayi=int(input("bir Sayı Giriniz: "))

if sayi>0:
    print("Pozitif sayı girdiniz.")
elif sayi==0:
    print("Sıfır.")
elif sayi<0:
    print("Negatif Sayı girdiniz.")
else:
    print("Yanlış değer girdiniz.")

#kullanıcıdan 3 sayı alıp en büyüğünü bulan program

s1=int(input("Birinci Sayıyı Giriniz: "))
s2=int(input("İkinci Sayıyı Giriniz: "))
s3=int(input("Üçüncü Sayıyı Giriniz: "))


if (s1 > s2) and (s1>s3) :
    print(" en büyük sayı : ",s1)
elif (s2>s1) and (s2>s3):
    print("En büyük sayı: ",s2)
elif (s3>s1) and (s3>s2):
    print("En büyük sayı: ",s3)

