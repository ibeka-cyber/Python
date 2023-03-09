import random
def zarat():
    sayi = random.randint(1,6)
    return sayi
irem = 0
fatih = 0
while(irem < 100 or fatih < 100):
    irem = irem + zarat()
    fatih = fatih + zarat()
    print("irem ",irem)
    print("fatih ",fatih)
if(fatih > irem):
    print("fatih kazandı")
elif(irem > fatih ):
    print("hile")
