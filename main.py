# go to terminal (@ bottom of screen) and write "pip install pygame" after PS C: line
import pygame
import math
import random

# color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)

# math constants

# game constants
DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 500
FPS = 60

############################################################
############################################################

pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

rect_x = 50
x_velo = 5
rect_y = 50
y_velo = 5
rect_side = 50

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if rect_x + rect_side > DISPLAY_WIDTH or rect_x < 0:
        x_velo *= -1

    if rect_y + rect_side > DISPLAY_HEIGHT or rect_y < 0:
        y_velo *= -1


    pygame.display.flip()

    screen.fill(WHITE)


    pygame.draw.rect(screen, PINK, [rect_x, rect_y, rect_side, rect_side])
    rect_x += x_velo
    rect_y += y_velo

    clock.tick(FPS)

pygame.quit()