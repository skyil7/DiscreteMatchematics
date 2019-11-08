A = [1,2,3,4,5]
B = A
R = []

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] < B[j]:
            R.append((A[i], B[j]))

print(R)