# 1.输入苹果的价格
price_str = input("输入苹果的价格:")

# 2.输入苹果的重量
weight_str = input("输入苹果的重量:")

# 3.计算苹果的总金额
# 注意：两个字符串之间是不能直接用乘法的
# money = price_str * weight_str
# >1 将价格转换浮点数
price = float(price_str)

# >2 将重量转换为浮点数
weight = float(weight_str)

# >3 浮点数相乘计算出总金额
money = price * weight

print(money)