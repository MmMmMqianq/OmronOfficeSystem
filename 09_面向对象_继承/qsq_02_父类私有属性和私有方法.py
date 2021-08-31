class A:
    def __init__(self):
        self.__num1 = 100  # 在方法或者属性名字前面加属两个下划线即可表示私有性
        self.__num2 = 200

    def __test(self):
        print("私有方法")


class B(A):
    pass

a = A()
print(a._A__num2)  # 私有属性强置调用方法:_类名__方法名或者属性名
b = B()
# b.num1  # b是不能调用A类的私有属性和私有方法，私有属性和方法不能继承
print(b._A__num1)
b._A__test()  # 在子类中调用父类的私有方法或者私有属性要格式为 子类创建的对象名._父类字__私有属性

