class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 属性名前面加两个下划线是私有属性，外界是不能调用的

    def __secret(self):  # 私有方法
        print("{0:}的年龄是{1:}".format(self.name, self.age))


xiaofang = Women("小芳", 18)
# print(xiaofang.__age)
# xiaofang.__secret()  # xiaofang.__age和xiaofang.__secret是私有属性，外界是不能调用的