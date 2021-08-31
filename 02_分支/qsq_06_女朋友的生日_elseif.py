"""
elif什么时候使用：同时判断多个条件，每个条件都是平级的，每个条件都会执行一段代码。
if a>b and c<d:这种是条件同时成立时执行一段代码
elif语法：
if 条件1:
    执行动作1
elif 条件2:
    执行动作2
elif 条件3:
    执行动作3
else:
    所有条件都不满足时执行动作
"""
# 定义一个 holiday_name 字符串记录节日的名称
holiday_name = input("请输入节日：")

# 如果是情人节应该“买玫瑰，看电影”
if holiday_name == "情人节":
    print("买玫瑰，看电影")

# 如果是平安夜应该“买苹果，吃大餐”
elif holiday_name == "平安夜":
    print("买苹果，吃大餐")

# 如果是过生日应该“买蛋糕，吃大餐”
elif holiday_name == "生日":
    print("买蛋糕，吃大餐")
# 除了节日“天天都是情人节啊”
else:
    print("天天都是情人节啊")
