n = int(input('수 입력 : '))
f = 1

for i in range(2,n):
    if n % i == 0:
        f = 0
        break

if f:
    print('소수')
else:
    print('소수 아님')