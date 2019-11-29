def DOM(f):
    d = set([])
    for (a,_) in f:
        d.add(a)
    return d
def vali(A,B,R, functionCheck=False):
    A=set(A)
    B=set(B)
    f=set(R)
    fc = functionCheck
    #f가 A에서 B로의 관계인지 확인
    ab = set([])
    for a in A:
        for b in B:
            ab.add((a,b))

    if not f.issubset(ab) and fc:
        print('함수 아님(f가 (a,b) 이외의 값을 갖고 있음)')
        return 0

    D = DOM(f)

    if A!=D and fc:
        print('함수 아님(f가 모든 a에 대응하지 않음)')
        return 0

    checker = []
    for (a,_) in f:
        checker.append(a)

    if len(D) != len(checker) and fc:
        print('함수 아님(y가 단 하나에만 대응하지 않음)')
        return 0

    RAN = set([])
    for (_,b) in f:
        RAN.add(b)
    COD = B

    return (D, RAN, COD)

if __name__ == '__main__':
    A = [1,2,3,4]
    B = [1,2,3]
    R = [(1,1), (2,2), (1,2), (3,1), (4,2)]
    print(vali(A,B,R,True))