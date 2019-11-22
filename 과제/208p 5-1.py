"""
아래 정의된 A와 B에 대하여, f = {(1,a), (2,a), (3,d), (4,c)}일 때, f가 함수인지 판단하고, 함수라면 정의역 치역 공변역을 구하라.
"""

def DOM(f):
    d = set([])
    for (a,_) in f:
        d.add(a)
    return d

def vali(a,b,c,d):
    A = {1,2,3,4}
    B = [a,b,c,d]
    f = {(1, a), (2, a), (3, d), (4, c)}

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

    RAN = set([])
    for (_,b) in f:
        RAN.add(b)
    COD = B

    return (D, RAN, COD)

ANS = vali('a', 'b', 'c', 'd')

if ANS != 0:
    print('정의역 :',ANS[0])
    print('치역 :',ANS[1])
    print('공변역 :',ANS[2])