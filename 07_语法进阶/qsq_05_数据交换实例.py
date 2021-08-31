# a = 10,b = 20, 要求:将a,b两个变量里面的数据交换；

a = 10
b = 20

# 方法1：
# c = a
# a = b
# b = c
# print("a的数据为{}".format(a))
# print("b的数据为{}".format(b))

# 方法2
# a = a+b
# b = a-b
# a = a-b
# print("a的数据为{}".format(a))
# print("b的数据为{}".format(b))

# 方法3 python独有的方法：将元祖的两个元素分别传送给变量a和b
a, b =(b, a)  # 也可以写成：a, b = b, a  元祖的括号可以省略
print("a的数据为{}".format(a))
print("b的数据为{}".format(b))
