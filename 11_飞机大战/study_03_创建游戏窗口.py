import sys

import pygame

pygame.init()
pygame.display.set_mode((480, 700))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
