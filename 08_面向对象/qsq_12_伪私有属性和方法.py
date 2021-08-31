"""
伪私有属性和方法
1.在个属性和方法命名时，实际是对名称做了一些特殊的处理，是的外界无法访问到私有属性
2.Python私有属性和方法的名字的处理：在名字的前面加了 _类名即私有属性和方法的名字变成了_类名__名称
注意：在日常开发中，不要使用这种方法访问对象的私有属性或私有方法，Python其实没有真正意义上的私有
"""
class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 属性名前面加两个下划线是私有属性，外界是不能调用的

    def __secret(self):  # 私有方法
        print("{0:}的年龄是{1:}".format(self.name, self.__age))

    # def _Women__secret(self):
    #     pass


xiaofang = Women("小芳", 18)
print(xiaofang._Women__age)  # _类名__属性名
xiaofang._Women__secret()  # _类名__方法名
