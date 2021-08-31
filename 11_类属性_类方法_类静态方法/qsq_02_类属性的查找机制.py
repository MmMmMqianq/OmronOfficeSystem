"""
1.类名.属性
2.对象名.属性（不建议使用）
这两种方法都可以访问类属性，
对象调用类属性遵循向上查找机制；
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
print(kuaizi.count)  # 用对象调用类属性时，首先会在对象的属性里查找是否有count属性，如果没有回向上查找类属性里
                     # 查找是否有count属性。如果有的话正常输出，如果的话就会报错。
                     # 注意：不建议使用对象调用类属性。
