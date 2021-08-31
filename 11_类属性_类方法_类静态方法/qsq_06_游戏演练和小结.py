"""
实例方法：方法内部需要访问实例属性
类方法： 方法内部只要访问类属性
静态方法： 方法内部不需要访问实例属性和类属性
"""

class Game(object):
    highest_score = 0
    record_holder = '无'

    @classmethod
    def show_record_holder(cls):
        print("记录保持者：{}\n最高得分：{}".format(cls.record_holder,
                                         cls.highest_score))

    @staticmethod
    def game_information():
        print("这是一个游戏案例演练！")

    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def start_game(self):
        print("玩家：{}\n---开始游戏---".format(self.name))

    def player_score(self):
        print("{0} 得分为 {1:d}".format(self.name, self.score))
        if self.score >= Game.highest_score:
            Game.highest_score = self.score
            Game.record_holder = self.name


player1 = Game("小明", 300)
player1.start_game()
player1.player_score()

player2 = Game("小红", 200)
player2.start_game()
player2.player_score()

Game.show_record_holder()