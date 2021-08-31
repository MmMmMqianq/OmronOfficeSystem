class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_falg = False

    def __new__(cls, *args, **kwargs):
        # 1. 判断是否创建的是第一个对象
        if cls.instance is None:
            # 2. 如果是第一个对象，那么就用用_new_方法为对象分配地址
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        # 判断是否执行过 初始化动作
        if MusicPlayer.init_falg:
            return
        else:
            MusicPlayer.init_falg = True
            print("初始化动作")
            pass  # pass可替换为诶具体的初始化动作


player1 = MusicPlayer()
player2 = MusicPlayer()
print(player1, player2)
