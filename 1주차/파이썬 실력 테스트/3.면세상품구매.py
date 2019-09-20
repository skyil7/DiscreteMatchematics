budget = int(input())
cnt = 0
while True:
    cost = int(input())
    quantity = int(input())
    price = cost*quantity
    if quantity>1:
        if quantity>2:
            price*=0.8
        else:
            price*=0.9
    if price ==0:
        break
    if budget - price < 0:
        break
    budget-=price
    cnt += quantity

print(cnt, budget)