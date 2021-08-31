# 全局变量
num = 10


def demo1():
    # ①在Python中，是不允许在函数里直接修改全局变量的 引用
    # ②如果使用赋值语句修改全局变量的值，那么Python会在函数内新建一个局部变量，
    #   只是名字和调用的全局变量是一样的
    num = 99
    print("num ==> %d" % num)


def demo2():

    print("num ==> %d" % num)


demo1()  # 输出num的值为99
demo2()  # 输出num的值为10

