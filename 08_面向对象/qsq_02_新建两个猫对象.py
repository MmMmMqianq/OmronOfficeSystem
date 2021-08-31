class Cat:
    """这是一个猫类"""
    def eat(self):

        print("{0:}爱吃鱼！".format())

    def drink(self):
        print("{0:}爱喝水！".format())


# 创建猫对象
tom = Cat()
tom.drink()
tom.eat()

lazy_cat = Cat()
lazy_cat.drink()
lazy_cat.eat()

lazy_cat1 = lazy_cat
lazy_cat1.drink()
lazy_cat1.eat()

print(tom)
print(lazy_cat)  # 使用类创建tom和lazy_cat是两个不同的对象，对象的引用不同
print(lazy_cat1)  # 使用赋值的方式创建的对象lazy_cat1和lazy_cat是同一个对象，引用相同
