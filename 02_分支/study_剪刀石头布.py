# 从控制台输入要出的拳头 —— 石头（1） / 剪刀（2）/ 布（3）
import random

player = int(input("请输入您要出的拳 石头（1） / 剪刀（2）/ 布（3）："))

# 电脑随机出拳——假定电脑只会出石头，完善整体代码功能
computer = random.randint(1, 3)
print("玩家选择的拳是 %d - 电脑出的拳是 %d" % (player, computer))

# 比较胜负
# 玩家胜利
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家获胜！")

# 平局
elif player == computer:
    print("平局！")
# 电脑胜利
else:
    print("电脑获胜！")
