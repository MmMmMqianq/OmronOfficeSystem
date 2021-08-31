# 计算 0-100 之间所有偶数累计求和结果
i = 0
result = 0
while i <= 100:
    if (i % 2) == 0:
        # print(i)
        result += i  # result必须现在循环外部先定义好
    i += 1
print("0-100 之间所有偶数累计求和结果 %d" % result)