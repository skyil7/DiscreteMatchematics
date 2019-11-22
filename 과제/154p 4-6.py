"""
A와 B의 관계 R은 b가 a로 나누어 떨어질 때, aRb이다. 이때 R을 구하라.
"""

A = [2,3,4,7]
B = [2,3,4,5,6]


R = []
for a in A:
    for b in B:
        if b % a == 0:
            R.append((a,b))

print(R)