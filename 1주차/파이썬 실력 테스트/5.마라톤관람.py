n = int(input('마라토너 수 : '))
nums = []
records = []
pair = []
for _ in range(n):
    num = int(input('등번호 : '))
    nums.append(num)

for _ in range(n):
    record = int(input('기록 : '))
    records.append(record)

for i in range(n):
    pair.append((nums[i],records[i]))

pair = sorted(pair, key= lambda item:item[1])

def time(record):
    min = record//60
    sec = record%60
    hour = min//60
    min = min%60
    return hour, min, sec

for i in range(3):
    print(pair[i][0], time(pair[i][1]))