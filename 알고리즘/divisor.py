n = int(input('정수 입력:'))
divs = set()

for i in range(1, n//2):
    if n%i==0:
        divs.add(i)
divs.add(n//2)

print(divs)