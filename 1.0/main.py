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
from class_camera import *
from class_tile import *
# всякая важная хрень
pygame.init()
camera = Camera()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

lvl = load_level('level.txt')
player, width, height = generate_level(lvl)
i = 0
direction = None
kind_of_pew = 'basic'
pos = (size[0] // 2, size[1] // 2)

while running:
    screen.fill((240, 240, 240))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 97:
                move_gg_left = True
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 100:
                move_gg_right = True
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 119:
                move_gg_up = True
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 115:
                move_gg_down = True
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 32:
                player.make_pew(kind_of_pew, pos, move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
        if event.type == pygame.KEYUP:
            if event.key == 119:
                move_gg_up = False
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 115:
                move_gg_down = False
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 97:
                move_gg_left = False
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 100:
                move_gg_right = False
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)

    if move_gg_down:
        player.rect.top += 1
    if move_gg_up:
        player.rect.top -= 1
    if move_gg_right:
        player.rect.left += 1
    if move_gg_left:
        player.rect.left -= 1

    # all_sprites.draw(screen)
    tiles_group.draw(screen)
    enemy_group.draw(screen)
    player_group.draw(screen)
    bullets_group.draw(screen)

    camera.update(player)
    for sprite in bullets_group:
        sprite.update()
    for sprite in enemy_group:
        sprite.update()
    for sprite in all_sprites:
        camera.apply(sprite)
    ###
    pygame.display.flip()
    clock.tick(60)
    ###
