import pygame

pygame.init()
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像

# 1. 加载背景图像
bg = pygame.image.load("./images/background.png")
# 2. blit 绘制图像
screen.blit(bg, (0, 0))
# 3. update 更新屏幕显示
# pygame.display.update()

# 绘制英雄飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

clock = pygame.time.Clock()

# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)
while True:
    # 1.指定循环体内部的代码执行的频率
    clock.tick(60)

    # 2. 修改飞机位置
    hero_rect.y -= 1

    # 判断飞机位置
    if hero_rect.y <= 0:
        hero_rect.y = 700
    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # 4. 调用update方法更新显示
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
