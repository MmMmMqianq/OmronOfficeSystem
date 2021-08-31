"""
类方法语法：
@classmthod
def 方法名(cls):
    #在方法调用类属性可以用cls.属性名
    pass
"""

class Tableware(object):
    count = 0  # count是类属性
    @classmethod
    def show_count(cls):
        # 在方法调用类属性可以用cls.属性名
        print(cls.count)

    def __init__(self, name):
        self.name = name
        # 用于记录改类创建对象的次数；
        Tableware.count += 1


kuaizi = Tableware("筷子")
Tableware.show_count()