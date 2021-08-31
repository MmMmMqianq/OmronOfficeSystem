"""
捕获位置错误语法：
捕获异常语法：
try:
    尝试执行代码
except Exception as abnormal：
    print("异常为：{}".format(abnormal))
    pass  # pass可以替换为在出现异常时执行的操作
"""

try:
    num = int(input("输入一个被除数："))
    result1 = 8 / num
except ZeroDivisionError:
    print("除数不能为0！")
except Exception as abnormal:
    print("异常为：{}".format(abnormal))