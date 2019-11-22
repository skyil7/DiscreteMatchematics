"""
예제 4-5의 관계를 관계행렬로 나타내라.
"""
import numpy as np

A = [1,2,3,4,5]

R = []
for a in A:
    for b in A:
        if a<b:
            R.append((a-1,b-1))

# 5*5 zero matrix
M = np.zeros((5,5))

for (a,b) in R:
    M[a][b] = 1
    
print(M)