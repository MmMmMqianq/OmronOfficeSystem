"""
1. 单例设计模式：
① 目的是让类创建的对象，在系统中只有唯一一个；
② 每次执行 类名()返回的对象内存地址是相同的；

2. 单例设计模式应用场景：
① 音乐播放器对象
② 回收站对象
③ 打印机对象

3. _new_方法：
① 使用类名()创建对象时，Python解释器首先会调用_new_方法为对象分配空间；
② _new_是一个由object基类提供的内置的静态方法，主要作用有两个：
    1）在内存中为对象分配空间；
    2）返回对象的引用
③ Python的解释器获得对象的引用作为第一个参数传递给_init_方法

4. _new_方法的重写：
① 重写_new_方法一定要 return super()._new_(cls)
② 如果不返回则Python的解释器得不到分配空间的对象的引用，就不会主动调用_init_初始化方法
③ 注意，_new_是一个静态的方法，在调用数据需要主动的传递 cls 参数
"""

# _new_方法的演练
class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

        # 1. 创建对象时自动调用_new_方法
        print("_new_方法自动被调用")

        # 2. _new_方法为对象分配空间
        instance = super().__new__(cls)

        # 3. 返回对象的引用
        return instance

    def __init__(self):
        print("执行初始换方法")


player1 = MusicPlayer()
print(player1)  # 输出：<__main__.MusicPlayer object at 0x00000195E6BE0160>
                # 如果不 return super().__new__(cls)，那么print()输出为None，_init_初始化方法不会被调用
