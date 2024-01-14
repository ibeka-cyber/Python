# -*- coding: utf-8 -*-
import numpy as np
def solution(A):
    k=np.arange(1,100000)
    ar=[]
    for i in A:
        if i not in ar:
            ar.append(i) #[1,2,3,4,6]
    for i in ar:
        for j in k:
            if j == i:
                k = np.delete(k, np.where(k == i))
    return min(k)
                
          
A = [1,3,4,6,1,2]
B = [1, 2, 3]
C = [-1, -3]
print(solution(A))
print(solution(B))
print(solution(C))
