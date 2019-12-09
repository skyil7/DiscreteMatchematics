n = int(input('정수 입력 : '))
num = [i for i in range(2, n)]
res = []
c = 0

while(len(num)):
    p = min(num)
    res.append(p)
    num.remove(p)
    c+=1

    for i in num:
        if i % p == 0:
            num.remove(i)
            c+=1

print(res)