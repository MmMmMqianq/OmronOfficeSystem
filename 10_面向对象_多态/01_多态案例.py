class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("{}在愉快的玩耍。。。".format(self.name))


class XiaoTianQuan(Dog, object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("{}飞在空中愉快的玩耍。。。")


class Person(object):
    def __init__(self, name):
        self.name = name

    def person_game(self, dog):  # 在实参中传递不同的对象就会产生不同的执行结果；这就叫多态
        print("{} 和 {}在愉快的玩耍。。。".format(self.name, dog.name))


wangcai = Dog("旺财")
xiaotianquan = XiaoTianQuan("哮天犬")
xiaoming = Person("小明")
xiaoming.person_game(wangcai)
xiaoming.person_game(xiaotianquan)



