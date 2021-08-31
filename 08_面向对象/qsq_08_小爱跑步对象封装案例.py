"""
封装
1. 封装是面向对象编程的一大特点；
2. 面向对象编程的第一步---将属性和方法封装到一个抽象的类中；
3. 外界使用类创建对象，然后让对象调用方法；
4. 对象的细节被封装在类的内部；
注意：在对象的方法的内部是可以直接访问对象属性的！！！
"""
class Person:

    def __init__(self, name, weight):  # 初始化方法里定义属性，定义好的属性在下面的方法里可以直接使用，理解为“类里的全局变量”
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5  # 在对象的方法的内部是可以直接访问对象属性的！！！

    def eat(self):
        self.weight += 1

    def __str__(self):

        return "我的名字叫{0:s}，体重是{1:.1f}".format(self.name, self.weight)  # 在对象的方法的内部是可以直接访问对象属性的！！！


xiaoming = Person("xiaoming", 75.5)
xiaoming.run()
xiaoming.eat()
print(xiaoming)