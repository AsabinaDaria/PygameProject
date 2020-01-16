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
hero_speed = 2

pygame.mixer.music.load("Data/space_dreams_-_Space_Dreams.mp3")  #  нужно будет найти трек
pygame.mixer.music.play()
pewpew = pygame.mixer.Sound("Data/pew.wav")  #  выстрел

while running:
    screen.fill((240, 240, 240))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 97 or event.key == 276:
                move_gg_left = True
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 100 or event.key == 275:
                move_gg_right = True
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 119 or event.key == 273:
                move_gg_up = True
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 115 or event.key == 274:
                move_gg_down = True
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 32:
                player.make_pew(player.get_chars('kind_of_pew'), hero_pos, move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
                pewpew.play()
                # player.get_pos()
        if event.type == pygame.KEYUP:
            if event.key == 119 or event.key == 273:
                move_gg_up = False
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 115 or event.key == 274:
                move_gg_down = False
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 97 or event.key == 276:
                move_gg_left = False
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)
            if event.key == 100 or event.key == 275:
                move_gg_right = False
                player.dir_move(move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)

    if move_gg_down:
        player.y_change(hero_speed)
        player.rect.top += hero_speed
    if move_gg_up:
        player.y_change(-hero_speed)
        player.rect.top -= hero_speed
    if move_gg_right:
        player.x_change(hero_speed)
        player.rect.left += hero_speed
    if move_gg_left:
        player.x_change(-hero_speed)
        player.rect.left -= hero_speed
    # all_sprites.draw(screen)
    tiles_group.draw(screen)
    enemy_group.draw(screen)
    player_group.draw(screen)
    mels_group.draw(screen)
    bullets_group.draw(screen)
    camera.update(player)
    for sprite in bullets_group:
        sprite.update()
    for sprite in enemy_group:
        sprite.update()
        sprite.follow(player)
        # sprite.get_pos()
    for sprite in all_sprites:
        camera.apply(sprite)
    ###
    pygame.display.flip()
    clock.tick(fps)
    ###
