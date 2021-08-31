"""
1.利用异常的传递性，当函数/方法执行出现异常时，会将异常传递给函数/方法调用一方；
2.如果传到主程序，仍然没有异常处理，程序才会被终止；
"""

def demo1():
    return  int(input("输入一个整数："))

def demo2():
    return demo1()


try:
    print(demo1())  # 在开发中，可以在主函数中增加异常捕获；
                    # 而在主函数中调用的其他函数，只要出现异常，都会传递到主函数的异常捕获中；
                    # 这样就不需要在函数的代码中，增加大量的异常捕获，保证代码的整洁；
except Exception as abnormal:
    print("未知错误为：{}".format(abnormal))