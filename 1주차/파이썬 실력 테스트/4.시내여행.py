n = int(input("관광지 수 : "))
places = []
for i in range(n):
    cost = int(input("관광지 입장료 : "))
    star = int(input('관광지 만족도 : '))
    gasungbi = star/cost
    places.append((cost,star,gasungbi))

hyeja = max(places, key = lambda item:item[2])

print(hyeja[0], hyeja[1])