# -*- coding: utf-8 -*-
#%%
f1=int(input("faktöriyeli hesaplanacak sayıyı giriniz: "))
sayac=1
if f1<0:
    print("Negatif sayıların faktöriyeli hesaplanamaz")
elif f1==0:
    print("sonuç: 1")
elif f1==1:
    print("sonuç: 1")
else:
    for x in range(2,f1+1):
       sayac=sayac*x
    print("Sonuç: ",sayac)


#%%
#matris toplama işlemi
    
#    1 3 5       3 3 4       4 6 9
#    2 4 1       2 4 1       4 8 2
#    1 5 7       3 5 4       4 10 11
     
x=[[1,3,5],[2,4,1],[1,5,7]]    
y=[[3,3,4], [2,4,1],[3,5,4]]

sum=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        sum[i][j]=x[i][j]+y[i][j]
    
print(sum)    
    
# %%
#cümledeki kelimeleri alfabetik olarak alt alta yazdıran program

sentence="İrem bahar koç"
info = sentence.split()
info.sort()
print (info)
for x in info:
    print(x)



































