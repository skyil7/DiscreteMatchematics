def gcd(a, b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

a = int(input('a 입력:'))
b = int(input('b 입력:'))

print(gcd(a,b))