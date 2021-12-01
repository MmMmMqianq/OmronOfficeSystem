"""
python 使用 lambda 来创建匿名函数：

1. lambda只是一个表达式，函数体比def简单很多。
2. lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
3. lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
4. 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

表达式：
lambda [arg1 [,arg2,.....argn]]:expression
信号和槽连接时通常会用到
"""
# 可写函数说明
sum1 = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print(type(sum1))
print("相加后的值为 : ", sum1(10, 20))
print("相加后的值为 : ", sum1(20, 20))
