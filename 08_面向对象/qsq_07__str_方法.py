class Cat:
    def __init__(self, new_name):  # 对象被创建的时候会自动调用该方法
        self.name = new_name
        print("{0:s}来了".format(new_name))

    def __del__(self):  # 在对象被删除之前系统会自动调用该方法
        print("{0:s}去了".format(self.name))

    def __str__(self):
        # 在Python中，使用print()打印一个对象时，输出的是对象是有哪个类创建的，以及在内存中的地址
        # 如果在开发中想要print()输出对象变量时，能够对打印自定义的内容，就可以利用_str_这个内置方法了
        # 注意：_str_方法返回的必须是一个字符串
        return "我是一个小猫【{0:s}】".format(self.name)  # 必须返回一个字符串


tom = Cat("Tom")
print(tom)