"""
A에 대해 aRb ⇔ a < b 일때, R과 정의역, 치역, 공변역은?
"""

A = [1,2,3,4,5]

R = []
for a in A:
    for b in A:
        if a<b:
            R.append((a,b))

print('R:', R)

DOM = set(a for (a,b) in R)

print('Domain:', DOM)

RAN = set(b for (a,b) in R)

print('Range:', RAN)

COD = A

print('Codomain:', COD)