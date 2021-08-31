# *args表示变量的类型为元组
# **kwargs表示变量类型为字典
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


# 1默认为num的值
# 2, 3, 4, 5元组默认为*args的参数
# name="小明", age=18默认为字典**kwargs的参数
demo(1, 2, 3, 4, 5, name="小明", age=18)


#多值函数举例，计算[1, 2, 3, 4, 5]的总和
def sum_num(*args):
    num = 0
    result = int()
    print("args 为：{}".format(args))
    for num in args:
        result = num + result
    return result


gl_result = sum_num(1, 2, 3, 4, 5, 6)
print("求和结果为：{}".format(gl_result))


def demo1(a=[], b=(), c={}):
    print(a)
    print(b)
    print(c)


demo1([1, 2], (3, 4), {"name": "小明", "age": 18})

