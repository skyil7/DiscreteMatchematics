budget = int(input("보유 금액 : "))
coupon = int(input("쿠폰 유무(1/0) : "))
rank = int(input("탑승 클래스 : "))

cost = [0,2000000,1000000,500000, 0]
discount = [0, 0.7, 0.8, 0.9, 0]

if coupon:
    budget -= cost[rank]*discount[rank]
else:
    budget -= cost[rank]

print("남은 돈 :",int(budget))