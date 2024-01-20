# n içerisindeki her bir farklı sayı bir rengi temsil etmektedir. örneğin: 10-> Mavi , 20->kırmızı, 30->Yeşil, 50->Sarı gibi..
# her bir sayı bir çorabın tekini temsil ediyor. Aynı sayıdan her iki adet olması bir çift çorabı temsil ediyor. 
# Kaç çift çorap olduğunu bulunuz. 

n =[10,20,20,10,10,30,50,10,20,50]


def Socks(n):
    socks=0
    c={}
    for i in n:
        if i not in c:
            c[i]=1
        else:
            c[i]+=1
            if c[i]%2==0 :
                socks+=1
    return c,socks

num,socks=Socks(n)
print(f"{num} listesi içerisinde  \n{socks} çift çorap vardır.")
        
            