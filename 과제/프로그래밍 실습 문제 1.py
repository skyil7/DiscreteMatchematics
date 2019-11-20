"""
집합 A에 관한 관계가 입력으로 주어질 때, 그 관계가 함수인지를 판별하는 프로그램을 작성하라.
"""

def DOM(f):
    d = set([])
    for (a,_) in f:
        d.add(a)
    return d

def vali(A, f):
    B = A

    #f가 A에서 B로의 관계인지 확인
    ab = set([])
    for a in A:
        for b in B:
            ab.add((a,b))

    if not f.issubset(ab):
        print('함수 아님(f가 (a,b) 이외의 값을 갖고 있음)')
        return 0

    D = DOM(f)

    if A!=D:
        print('함수 아님(f가 모든 a에 대응하지 않음)')
        return 0

    checker = []
    for (a,_) in f:
        checker.append(a)

    if len(D) != len(checker):
        print('함수 아님(y가 단 하나에만 대응하지 않음)')
        return 0
    print('함수임!')
    return 1

A = {i for i in range(1,11)}
f1 = set([(1,1), (2,1), (3,1), (3,4), (6,5), (6,6), (7,1), (7,2), (9,9), (10,10)])
f2 = set([(1,3), (2,4), (3,1), (4,2), (5,6), (6,7), (7,4), (8,3), (9,1), (10,9)])

print(A)

print('f1은 ', end='')
vali(A, f1)
print('f2는 ', end='')
vali(A, f2)