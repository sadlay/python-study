class MusicPlayer(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            print("创建对象，分配空间")
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag:
            return
        print("播放器初始化")
        MusicPlayer.init_flag = True


player1 = MusicPlayer()
player2 = MusicPlayer()
print(player1)
print(player2)
