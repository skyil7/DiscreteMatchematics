mem = {}
def fibo(n):
    if n <= 1:
        return n
    mem[n] = fibo(n-1) + fibo(n-2)
    return mem[n]

n = int(input('정수 입력:'))
print(fibo(n))