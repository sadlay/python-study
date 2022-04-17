import pygame

here_rect = pygame.Rect(100, 500, 120, 125)

print("英雄的原点 {} {}".format(here_rect.x,here_rect.y))
print("英雄的尺寸 {} {}".format(here_rect.width,here_rect.height))
print("{} {}".format(*here_rect.size))