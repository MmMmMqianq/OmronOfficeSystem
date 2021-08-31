"""
需求：
1. 士兵许三多有一把AK47
2. 士兵可以开火
3. 枪能够发射子弹
4. 枪能够装填子弹

封装：
1. 封装是面向对象编程的一大特点；
2. 面向对象编程的第一步---将属性和方法封装到一个抽象的类中；
3. 外界使用类创建对象，然后让对象调用方法；
4. 对象的细节被封装在类的内部；

重点：一个对象的属性可以是另外一个类创建的对象
"""


class Gun:
    def __init__(self, name):
        self.name = name
        self.bullet_count = 50

    def shoot(self, choose_shoot):
        if self.bullet_count > 0:
            if choose_shoot in ["1", "2"]:
                if choose_shoot == "1":
                    while True:
                        print("{0:}当前子弹数{1:}".format(self.name, self.bullet_count), end="==>>")
                        self.bullet_count -= 1
                        print("{0:}剩余子弹数{1:}".format(self.name, self.bullet_count))
                        if self.bullet_count == 0:
                            break
                else:
                    self.bullet_count -= 1
            else:
                print("请输入正确的指令，输入1为连续扫射，输入2为点射！！！")
        else:
            print("{0:}已经没有子弹，请装弹！！！".format(self.name))
            return

    def add_bullet(self):
        self.bullet_count = 50


class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun  # 士兵的枪属性可以是枪类创建的枪对象
# class Soldier:
#     def __init__(self, name):
#         self.name = name
#         self.gun = None  # 这种写法也可以，在主程序里通过赋值的方法改变self.gun属性值

    def fire(self, choose_shoot):
        # if self.gun == None:  #用=判断也可以，用于判断变量=的值是否相等
        if self.gun is None:  # is 为身份运算符，用于判断对象的引用是否相同
            print("这还是个新兵蛋子，没有枪！！！")
            return
        else:
            self.gun.shoot(choose_shoot)
            if choose_shoot == "1":
                print("{2:}打了一梭子子弹，{0:}剩余子弹数量为{1:}".format(self.gun.name, self.gun.bullet_count, self.name))
            else:
                print("{2:}点射一次，{0:}剩余子弹数量为{1:}".format(self.gun.name, self.gun.bullet_count, self.name))

    def add_bullet(self):
        self.gun.add_bullet()
        print("{0:}当前子弹为{1:}发，子弹已经装满！！！".format(self.gun.name, self.gun.bullet_count))


ak47 = Gun("ak47")

xu_san_duo = Soldier("许三多", None)
xu_san_duo.gun = ak47
click_fire = input("输入1表示连续开火,输入2表示点射：")
xu_san_duo.fire(click_fire)
xu_san_duo.add_bullet()
