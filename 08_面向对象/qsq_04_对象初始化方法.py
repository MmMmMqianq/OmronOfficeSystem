class Cat:
    """这是一个猫类"""
    def __init__(self):
        self.name = "Tom"  # 在初始化时初始化属性

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("{0:}爱吃鱼！".format(self.name))

    def drink(self):
        print("{0:}爱喝水！".format(self.name))


# 创建猫对象
# 当使用类名()创建对象时，会自动执行以下操作：
# ① 在内存中为对象分配空间--创建对象
# ② 为对象的属性设置初始值--使用_init_方法
tom = Cat()
tom.drink()
tom.eat()
