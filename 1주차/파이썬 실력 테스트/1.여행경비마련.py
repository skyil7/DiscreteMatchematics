stock = int(input("주식 펀드 투자 금액 : "))
bank = int(input("정기 예금 저축 금액 : "))
stockFloat = (float(input("주식 펀드 이자율 : "))+100)/100
bankFloat = (float(input("정기 예금 이자율 : "))+100)/100

stock, bank = bank, stock

print("총 수익 :",int(bank*bankFloat + stock*stockFloat))