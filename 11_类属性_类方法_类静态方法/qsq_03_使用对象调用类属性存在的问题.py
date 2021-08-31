class Tableware(object):
    count = 0  # count是类属性

    def __init__(self, name):
        self.name = name
        # 用于记录改类创建对象的次数；
        Tableware.count += 1


kuaizi = Tableware("筷子")
shaozi = Tableware("勺子")
wan = Tableware("碗")

kuaizi.count = 99
print("====> {}".format(kuaizi.count))  # 输出的是99
print(Tableware.count)  # 输出的是3
# 为什么print(kuaizi.count)输出的是99，而print(Tableware.count)输出的是3。
# 是因为在执行kuaizi.count时，筷子对象会查找自己是否有count属性，
# 如果没有回会创建一个count属性（其实这种写法就是在外部为对象添加属性），实际并没有改变Tableware类中count的属性值) 。
# 而Tableware.count是在类属性里查找count属性，查到即输出3。