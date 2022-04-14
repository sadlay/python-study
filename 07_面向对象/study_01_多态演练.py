class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("{} 蹦蹦跳跳".format(self.name))


class XiaoTianDog(Dog):
    def game(self):
        print("{} 飞到天上去玩耍".format(self.name))


class Person(object):
    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print("{} 和 {} 快乐的玩耍".format(self.name, dog.name))
        dog.game()


wangCai = Dog("旺财")
feiTianWangCai = XiaoTianDog("飞天旺财")

xiaoMing = Person("小明")
xiaoMing.play_with_dog(feiTianWangCai)

