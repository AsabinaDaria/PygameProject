import random
import pygame
from pygame.color import Color
from pygame import *
import os
from heart import *

from functions import *
from constants import *
from class_basic import *
from class_bullets import *
from class_basic_bullets import *
from class_camera import *
from class_tile import *


pygame.init()
camera = Camera()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

level_list = 0, 1, 2, 3, 'boss'  
lvl = load_level(f'level_{random.choice(level_list)}.txt')  # рандомный выбор уровня
player, width, height = generate_level(lvl)
mouse_pos = 0, 0  # для управления мышкой
i = 0
direction = None
kind_of_pew = 'basic'
hero_speed = 2
score = 0
control_type = 1  # для переключения управления в клавиатуры на мышку и обратно

pygame.mixer.music.load("Data/soundtr.wav")  # фоновая музыка
pygame.mixer.music.play(loops=-1)
pewpew = pygame.mixer.Sound("Data/pew.wav")  # выстрел


start_screen()  # заставка

while running:
    screen.fill(Color('Black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and control_type == 1:  # управление с клавиатуры
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

        if event.type == pygame.KEYUP and control_type == 1:
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

            if event.key == 32 and control_type == 1:  # выстрел
                pewpew.play()
                player.make_pew(player.get_chars('kind_of_pew'), hero_pos, move_gg_up, move_gg_down,
                                move_gg_left, move_gg_right)

        if event.type == pygame.KEYDOWN :
            if event.key == K_ESCAPE:  # пауза
                pause_screen()
            if event.key == K_RETURN:  # смена управления
                if control_type == 1:
                    control_type = 2
                else:
                    control_type = 1

        if event.type == pygame.MOUSEMOTION and control_type == 2:  # управление мышкой
            mouse_pos = event.pos

        if event.type == pygame.MOUSEBUTTONDOWN:  # выстрел
            cur_frame = player.get_cur_frame()
            pewpew.play()
            if cur_frame == 0:
                player.make_pew(player.get_chars('kind_of_pew'), hero_pos, False, True,
                                False, False)
            if cur_frame == 1:
                player.make_pew(player.get_chars('kind_of_pew'), hero_pos, False, False,
                                True, False)
            if cur_frame == 2:
                player.make_pew(player.get_chars('kind_of_pew'), hero_pos, False, False,
                                False, True)
            if cur_frame == 4:
                player.make_pew(player.get_chars('kind_of_pew'), hero_pos, True, False,
                                False, False)

            # player.get_pos()

    if move_gg_down:  # движение героя вниз
        player.y_change(hero_speed)
        player.rect.top += hero_speed

        player.rect.top += hero_speed
        if pygame.sprite.spritecollideany(player, no_go_tiles_group):
            player.rect.top -= hero_speed
            player.y_change(-hero_speed)
        player.rect.top -= hero_speed
    if move_gg_up:  # движение героя вверх
        player.y_change(-hero_speed)
        player.rect.top -= hero_speed

        player.rect.top -= hero_speed
        if pygame.sprite.spritecollideany(player, no_go_tiles_group):
            player.rect.top += hero_speed
            player.y_change(hero_speed)
        player.rect.top += hero_speed
    if move_gg_right:  # движение героя вправо
        player.x_change(hero_speed)
        player.rect.left += hero_speed

        player.rect.left += hero_speed
        if pygame.sprite.spritecollideany(player, no_go_tiles_group):
            player.rect.left -= hero_speed
            player.x_change(-hero_speed)
        player.rect.left -= hero_speed
    if move_gg_left:  # движение героя влево
        player.x_change(-hero_speed)
        player.rect.left -= hero_speed

        player.rect.left -= hero_speed
        if pygame.sprite.spritecollideany(player, no_go_tiles_group):
            player.rect.left += hero_speed
            player.x_change(+hero_speed)
        player.rect.left += hero_speed
    #  плюс проверка на наличие непроходимых спрайтов

    # all_sprites.draw(screen)
    end_level_tiles_group.draw(screen)
    tiles_group.draw(screen)
    no_go_tiles_group.draw(screen)
    items_group.draw(screen)
    enemy_group.draw(screen)
    player_group.draw(screen)
    mels_group.draw(screen)
    bullets_group.draw(screen)
    hearts_group.draw(screen)
    camera.update(player)
    if control_type == 2:  # управление мышкой
        player.follow_pos(mouse_pos, move_gg_up, move_gg_down,
                          move_gg_left, move_gg_right)

    for sprite1 in bullets_group:
        for sprite2 in enemy_group:
            if pygame.sprite.collide_mask(sprite1, sprite2):
                sprite1.kill()
                sprite2.get_hitted()
                if not sprite2.is_alive():
                    player.change_score(1)
    for sprite in bullets_group:
        sprite.update()
        if pygame.sprite.spritecollideany(sprite, no_go_tiles_group):
            sprite.kill()
    for sprite in enemy_group:
        sprite.update_via_counter(30)
        sprite.follow(player)
    for sprite in items_group:
        if pygame.sprite.collide_mask(player, sprite):
            sprite.used()
    for sprite in end_level_tiles_group:
        if pygame.sprite.collide_mask(player, sprite):
            lvl = load_level(f'level_{random.choice(level_list)}.txt')
            score += player.get_score()
            for sprite in all_sprites:
                sprite.kill()
            player, width, height = generate_level(lvl)
        # sprite.get_pos()
    for sprite in all_sprites:
        camera.apply(sprite)
    end_level_flag = False
    end_level_counter = 0
    for enemy in enemy_group:
        end_level_counter += 1
        if enemy.is_alive() == False:
            end_level_counter -= 1
    if end_level_counter == 0:
        end_level_flag = True
    if end_level_flag == True:
        for sprite in end_level_tiles_group:
            sprite.unlock_door()
    # переходи между уровнями


    intro_text = [f"Your score: {player.get_score() + score}"]
    font = pygame.font.Font(None, 30)
    text_coord = 20
    for line in intro_text:
        string_rendered = font.render(line, 2, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 5
        intro_rect.top = text_coord
        intro_rect.x = 1200
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    # счет игрока

    ###
    pygame.display.flip()
    clock.tick(fps)
    ###
