#Kullanıcıdan listeye yapılacak işlemi ve sayıları alıp listeye gereken işlemleri yapınız.
# Sample İnput       
# 12                
# insert 0 5        
# insert 1 10       
# insert 0 6        
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

#*********************************************
# Sample output
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

N = int(input())
lst=[]
s=[]

def liste(a):
    if a[0]=="insert":
        lst.insert(int(a[1]), int(a[2]))
    elif a[0]=="append":
        lst.append(int(a[1]))
    elif a[0]=="sort":
        lst.sort()
    elif a[0]=="pop":
        lst.pop()
    elif a[0]=="reverse":
        lst.reverse()
    elif a[0]=="remove":
        lst.remove(int(a[1]))
    elif a[0]=="print":
        print(lst)

for i in range(N):
    a = input()
    a=a.split()
    liste(a)