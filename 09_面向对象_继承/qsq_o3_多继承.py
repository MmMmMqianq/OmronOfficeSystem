"""
多继承可以让一个对象拥有多个父类的属性和方法；
多继承语法：
class D(A, B, C):
    pass
"""
class A(object):
    def demoA(self):
        print("I'm class A")


class B(object):
    def demo(self):
        print("I'm class B")


class C(object):
    def demo(self):
        print("I'm class C")


class D(A, B, C, object):  # B类和C类都有demo方法时，在用多继承是要注意；
    pass           # 在多个父类里有相同的方法时，取决于继承时父类的顺序，那个写在前面就就会执行哪个父类的方法；
                   # 可以通过 类名.__mro__来查看子类的方法的搜索顺序
d = D()
d.demo()

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)
