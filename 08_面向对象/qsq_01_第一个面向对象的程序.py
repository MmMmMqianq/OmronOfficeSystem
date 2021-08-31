# 定义只包方法的类：
# class 类名:  # 类名要符合大驼峰命名方式
#
#     def 方法1(self, 参数列表):  # 方法的定义格式和之前函数是一样的，只是第一个参数必须为self
#         pass
#
#     def 方法2(self, 参数列表):
#         pass


# tom猫爱喝水，也爱吃鱼
# 分析需求：类为猫，吃和喝两个行为定义为方法


class Cat:
    """这是一个猫类"""
    def eat(self, cat_name):
        print("{}爱吃鱼！".format(cat_name))

    def drink(self, cat_name):
        print("{}爱吃鱼！".format(cat_name))

# 创建猫对象
tom = Cat()

tom.drink("Tom")
tom.eat("Tom")

print(tom)  # print()打印一个对象可以打印出对象是由哪个类创建的，并且可以打印出对象的引用（以十六进制显示）
addr = id(tom)
print("{:#x}".format(addr))

