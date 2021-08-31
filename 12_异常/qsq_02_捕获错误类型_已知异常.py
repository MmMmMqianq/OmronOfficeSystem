"""
捕获异常语法：
try:
    尝试执行代码
except 错误信息1：
    出现错误信息1的处理代码
except (错误信息2, 错误信息3)
    出现错误信息2和3的处理代码
except 错误信息4：
    出现错误信息4的处理代码
"""

try:
    num = int(input("输入一个被除数："))
    result1 = 8 / num
except ZeroDivisionError:
    print("除数不能为0！")
except ValueError:
    print("输入的不是一个整数！")
