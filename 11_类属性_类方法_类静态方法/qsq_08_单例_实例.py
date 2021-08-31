"""
·单例--让类创建出来的对象，在系统中只有唯一的一个实例
    1.定义一个 类属性，初始值设置为None，用于记录单例对象的引用；
    2.重写_new_方法
    3.如果类属性 is None，调用父类_new_(cls)为对象分配对象，并在类属性中记录结果；
    4.返回类属性中记录的对象引用；
"""

class Musicplayer(object):

    # 记录第一个被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 1. 判断是否创建的是第一个对象
        if cls.instance is None:
            # 2. 如果是第一个对象，那么就用用_new_方法为对象分配地址
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance


player1 = Musicplayer()
player2 = Musicplayer()
print(player1, player2)  # player1和player是同一个对象，因为应用是相同的。
                         # 只要用Musicplayer创建出来的对象象都是相同的，这就是单例模式。

