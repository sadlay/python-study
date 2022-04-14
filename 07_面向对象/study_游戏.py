import random


class Game(object):
    __top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("游戏帮助")

    @classmethod
    def show_top_score(cls):
        print("最高得分：{}".format(cls.__top_score))

    def start_game(self):
        score = random.randint(1, 100)
        print("{} 游戏得分: {}".format(self.player_name, score))
        Game.__top_score = score if score > Game.__top_score else Game.__top_score


xiaoMing = Game("小明")
xiaoHong = Game("小红")
xiaoMing.start_game()
xiaoHong.start_game()
Game.show_top_score()
