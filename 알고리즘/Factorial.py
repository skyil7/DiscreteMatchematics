def fact(n):
    if n < 2:
        return n
    return n * fact(n-1)

n = int(input('정수 입력 :'))
print(fact(n))