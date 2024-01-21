# 1.satır alfabetik sayı içeriyorsa True,değilse False
# 2.satır harf içeriyorsa True değilse False
# 3.satır sayı içeriyorsa  True değilse false
# 4.satır küçük harf içeriyorsa True yoksa False
# 5.satır büyük harf içeriyorsa True yoksa False yazdırılacak

# Sample Input:
# qA2

# ********************

# Sample Output:
# True
# True
# True
# True
# True



if __name__ == '__main__':
    S = input()
    print(any([i.isalnum() for i in S]))
    print(any([i.isalpha() for i in S]))
    print(any([i.isdigit() for i in S]))
    print(any([i.islower() for i in S]))
    print(any([i.isupper() for i in S]))