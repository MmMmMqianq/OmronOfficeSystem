# 全局变量
num = 10


def demo1():
    # 希望改变函数里的全局变量--使用global函数申明变量
    # global 关键字会告诉解释器后面的变量是全局变量，执行赋值语句时，
    #
    global num
    num = 99
    print("num ==> %d" % num)


def demo2():

    print("num ==> %d" % num)


demo1()  # 输出num的值为99
demo2()  # 输出num的值为99
