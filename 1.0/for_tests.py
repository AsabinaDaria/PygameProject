import pygame
from pygame.color import Color
from pygame import *
import os

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    color_key = colorkey
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


# image = pygame.Surface([100, 100])
# image.fill(pygame.Color("red"))
image = load_image('im_for_tests.jpg', Color('White'))

move_testgg_up = False
move_testgg_down = False
move_testgg_left = False
move_testgg_right = False

fps = 50
x_testgg, y_testgg = 0, 0
startflag = False
clock = pygame.time.Clock()
running = True
r = 0
while running:
    screen.fill((240, 240, 240))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 119:
                move_testgg_up = True
            if event.key == 115:
                move_testgg_down = True
            if event.key == 97:
                move_testgg_left = True
            if event.key == 100:
                move_testgg_right = True
        if event.type == pygame.KEYUP:
            if event.key == 119:
                move_testgg_up = False
            if event.key == 115:
                move_testgg_down = False
            if event.key == 97:
                move_testgg_left = False
            if event.key == 100:
                move_testgg_right = False

    if move_testgg_up:
        y_testgg -= 2
    if move_testgg_down:
        y_testgg += 2
    if move_testgg_left:
        x_testgg -= 2
    if move_testgg_right:
        x_testgg += 2
    screen.blit(image, (x_testgg, y_testgg))

    ###
    pygame.display.flip()
    clock.tick(60)
    ###
