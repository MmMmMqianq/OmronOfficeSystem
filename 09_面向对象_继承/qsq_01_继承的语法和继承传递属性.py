"""
继承的语法结构：
class A(object):  # 父类A
    def a(self):
    pass


class B(A, object):  # B为子类，继承了A类的属性和方法
    def b(self):
    pass

    def bb(self):
    print("bb")


class C(B, object):  #C 是B的子类，C继承A和B的所有属性，！！！继承具有传递性！！！
    def c():

    def bb()  # 如果子类中定义了一个和父类同名的方法，那么在调用时执行子类中定义的方法
    print("bbbbb")
    super().bb()  # 用super()方法可以在子类中调用父类的方法;
                  # 也可以使用 父类名.父类方法(self),一定要传递给自己，否则会报错；
    print("bbbbbbbb")

重点：
定义类时，
2.x版本的Python，如果Class A():括号里什么都不写的话，
默认是不继承Object这个父类的，那么很多自带的方法是不能使用的；

3.x版本的python，如果Class A():括号里什么也不写的话，
默认是继承Object这个父类的，那么自带的方法可以直接使用；

在定义类时不管是哪个版本的Python建议都写上父类object
"""


class Animal(object):
	def __init__(self, name):
		self.name = name

	def sleep(self):
		print("{0}在睡觉".format(self.name))

	def drink(self):
		print("喝水")

	def eat(self):
		print("吃饭")


class Dog(Animal, object):
	def bark(self):
		print("狗叫")


class cat(Animal, object):
	def miaomiao(self):
		print("miaomiao叫")


class person(Animal, object):
	def study(self):
		print("学习")


wangcai = Dog("wangcai")
miaomiao = cat("miaomiao")
xiaoming = person("xiaoming")

wangcai.sleep()
wangcai.bark()
miaomiao.sleep()
miaomiao.miaomiao()
xiaoming.sleep()
xiaoming.study()
