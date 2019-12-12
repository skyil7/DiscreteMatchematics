def hanoi(n, start, end, mid):
    if n == 1:
        print(start, "->", end)
        return
    hanoi(n - 1, start, mid, end)
    print(start, "->", end)
    hanoi(n - 1, mid, end, start)

n = int(input('옮길 원반 수 :'))
hanoi(n,'A','C','B')