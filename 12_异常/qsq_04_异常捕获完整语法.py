"""
异常捕获完整语法：
try:
    # 尝试执行的代码；
    pass
except 错误类型1：
    # 针对错误类型1，对应的代码处理；
    pass
except 错误类型2：
    # 针对错误类型2，对应的代码处理；
    pass
except (错误类型3, 错误类型4)：
    # 针对错误类型3和4，对应的代码处理；
    pass
except Exception as abnormal:
    # 打印错误信息
    print("错误信息为：{}".format(abnormal))
finally:
    # 无论是否有异常，都会执行以下代码；
    pass
"""


try:
    num = int(input("输入一个被除数："))
    result1 = 8 / num
except ZeroDivisionError:
    print("除数不能为0！")
except Exception as abnormal:
    print("异常为：{}".format(abnormal))
else:
    # try下的代码没有报错的情况下可能正常执行后，再执行else下的代码；
    print("try下的代码没有报错，已正常执行！\nresult = {}".format(result1))
finally:
    # 无论try下的代码是否正常执行，是否有异常该段代码都能正常执行；
    print("finally下的代码已经执行！")
    pass

