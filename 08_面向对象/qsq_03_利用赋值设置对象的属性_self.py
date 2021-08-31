class Cat:
    """这是一个猫类"""
    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("{0:}爱吃鱼！".format(self.name))

    def drink(self):
        print("{0:}爱喝水！".format(self.name))


# 创建猫对象
tom = Cat()
tom.name = "Tom"  # 可以通过 .属性名 利用赋值的方式给对象添加一个属性（不推荐使用），添加的对象的属性只对该对象有效
tom.drink()
tom.eat()

lazy_cat = Cat()
lazy_cat.name = "大懒猫"  # 需要给lazy_cat再添加属性，Tom添加的name属性对lazy_cat这个对象没有效
lazy_cat.drink()
lazy_cat.eat()
