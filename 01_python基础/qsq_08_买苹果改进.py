# 1.提示用户输入苹果单价
price = float(input("请输入苹果的单价："))

# 2. 提示用户输入苹果的重量
weight = float(input("请输入苹果的重量："))

# 3. 计算金额
money = price * weight

print( "苹元果单价%f元/斤，购买了%f斤，总价为%f" % (price, weight, money))