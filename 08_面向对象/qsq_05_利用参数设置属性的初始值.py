class Cat:
    """这是一个猫类"""
    def __init__(self, cat_name):
        # 1. 把希望设置的属性值，定义成_init_方法的参数
        # 2. 在方法内部使用self.属性 = 形参接收外部传递的参数
        # 3. 在创建对象时，使用类名(属性1, 属性2, ...)调用
        self.name = cat_name  # 在初始化时初始化属性

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("{0:}爱吃鱼！".format(self.name))

    def drink(self):
        print("{0:}爱喝水！".format(self.name))


# 创建猫对象
# 当使用类名()创建对象时，会自动执行以下操作：
# ① 在内存中为对象分配空间--创建对象
# ② 为对象的属性设置初始值--使用_init_方法
tom = Cat("Tom")
tom.drink()
tom.eat()

lazy_cat = Cat("lazy_cat")
lazy_cat.eat()
lazy_cat.drink()