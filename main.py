import pygame
from pygame.color import Color
from pygame import *
import os

from functions import *
from constants import *
from class_basic import *
from class_gg import *
from class_bullets import *
from class_basic_bullets import *


pygame.init()
screen = pygame.display.set_mode(size)
gg_basic_bullets = BasicBullets([])
gg = Gg(x_gg, y_gg, ['body1.0'], [gg_basic_bullets])
clock = pygame.time.Clock()
# спрайты рождаются тут:
# спрайты гг:
gg_sprites = pygame.sprite.Group()
gg_basic_bullet_sprites = pygame.sprite.Group()
body1_image = load_image('body1.0.jpg', Color('White'))
basic_bullet_image = load_image('basic_bullet.jpg', Color('White'))

body_sprite = pygame.sprite.Sprite()
body_sprite.image = body1_image
body_sprite.rect = body_sprite.image.get_rect()
gg_sprites.add(body_sprite)

basic_bullet_sprite = pygame.sprite.Sprite()
basic_bullet_sprite.image = basic_bullet_image
basic_bullet_sprite.rect = basic_bullet_sprite.image.get_rect()
gg_basic_bullet_sprites.add(basic_bullet_sprite)

# противника:

while running:
    screen.fill((240, 240, 240))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 119:
                move_gg_up = True
            if event.key == 115:
                move_gg_down = True
            if event.key == 97:
                move_gg_left = True
            if event.key == 100:
                move_gg_right = True
            if event.key == 32:
                gg.make_basic_pew()
        if event.type == pygame.KEYUP:
            if event.key == 119:
                move_gg_up = False
            if event.key == 115:
                move_gg_down = False
            if event.key == 97:
                move_gg_left = False
            if event.key == 100:
                move_gg_right = False

    # движение гг
    gg.basic_move(move_gg_up, move_gg_down, move_gg_left, move_gg_right)
    body_sprite.rect.x = gg.get_pos()[0]
    body_sprite.rect.y = gg.get_pos()[1]
    gg_sprites.draw(screen)

    # движение пуль гг
    num_of_basic_bullets = len(gg_basic_bullets.get_pos())
    if num_of_basic_bullets:
        for n in range(num_of_basic_bullets):
            basic_bullet_sprite.rect.x = gg_basic_bullets.get_pos()[n][0]
            basic_bullet_sprite.rect.y = gg_basic_bullets.get_pos()[n][1]
            gg_basic_bullet_sprites.draw(screen)

    ###
    pygame.display.flip()
    clock.tick(60)
    ###
