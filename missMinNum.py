def solution(A):
    temp=[]
    for i in A:
        if i>0:
            temp.append(i)
    temp.sort()
    positive=1
    for i in temp:
        if i==positive:
            positive+=1    
        else:
            positive=positive
    return positive

A=[1,3,6,4,1,2]
print(solution(A))