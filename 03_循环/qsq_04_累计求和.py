# 计算 0-100 之间所有数据累计求和结果

i = 0
result = 0
while i <= 100:
    print(i)
    result += i
    i += 1
print("0-100 之间所有数据累计求和结果为 %d" % result)
