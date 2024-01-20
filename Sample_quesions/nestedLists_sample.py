#Kullanıcıdan bir sayı girecek. Bu sayı kadar sırayla öğrenci adı, aldığı notu girecek.
#notu en düşük 2. öğrenci ekrana yazdırılacak.
#eğer başka bir öğrencinin notu da aynıysa öğrenciler alfabetik sıraya göre ekrana yazdırılacak.
#(Nested List ile yapılacak!)

if __name__ == '__main__':
    records=[]
scores=[]
names=[]
temp=0
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
    scores.append(score)
    scores.sort()
    for i in scores:
        if i>min(scores):
            temp=i
            break
for j, k in records:
    if k==temp:
        names.append(j)
        names.sort()
for i in names:
    print(i)
        
        