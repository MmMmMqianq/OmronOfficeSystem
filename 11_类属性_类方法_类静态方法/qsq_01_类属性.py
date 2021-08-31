"""
1.类属性就是给类对象定义的属性；
2.类属性通常是用于记录类的一些特征；
3.类属性不会记录具体对象的特征；
"""
class Tableware(object):
    count = 0  # count是类属性
    def __init__(self, name):
        self.name = name
        # 用于记录改类创建对象的次数；
        Tableware.count += 1


kuaizi = Tableware("筷子")
shaozi = Tableware("勺子")
wan = Tableware("碗")
print(Tableware.count)