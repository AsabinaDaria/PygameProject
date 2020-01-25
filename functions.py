import pygame
from pygame.color import Color
from pygame import *
import os
from constants import *
from class_basic import *
from class_gg import *
from class_enemy import *
from heart import *
from class_no_go_tile import *
from class_player_dote import *
from class_tile import *
from class_end_level_tile import *
from class_medpack import *
#


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


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, 'n'), level_map))
    # return list(map(lambda x: x, level_map))


# class Tile(pygame.sprite.Sprite):
#    def __init__(self, tile_type, pos_x, pos_y):
#        super().__init__(tiles_group, all_sprites)
#        self.tile_images = {'wall': load_image(
#            'wall.jpg'), 'empty': load_image('floor.jpg')}
#        self.image = self.tile_images[tile_type]
#        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


def generate_level(level):
    no_go_dotes = []
    end_level_counter = 0
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == ' ':
                Tile('nothing', x, y)
            elif level[y][x] == 'm':
                Tile('empty', x, y)
                new_medpack = Medpack(load_image(
                    "medpack.jpg", Color('White')), 1, 1, x * 50, y * 50)
                new_medpack.add(items_group)
            elif level[y][x] == '#':
                No_go_tile('wall', x, y)
            elif level[y][x] == 'e':
                End_level_tile('end_level_locked_door', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Gg(load_image(
                    "just_dote.jpg", Color('White')), 4, 1, x * 50, y * 50, ['basic'])
                new_player.add(player_group)
            elif level[y][x] == '!':
                Tile('empty', x, y)
                new_enemy = Enemy(load_image(
                    "mar.png", Color('White')), 4, 1, x * 50, y * 50, ['mel', 2])
                new_enemy.add(enemy_group)
            elif level[y][x] == 'b':
                Tile('empty', x, y)
                new_enemy = Enemy(load_image(
                    "boss.jpg", Color('White')), 1, 1, x * 50, y * 50, ['mel', 20])
                new_enemy.add(enemy_group)

    heart1 = Heart(load_image("heart.jpg", Color('white')), 1, 1,
                   0, 0)
    heart2 = Heart(load_image("heart.jpg", Color('white')), 1, 1,
                   20, 0)
    heart3 = Heart(load_image("heart.jpg", Color('white')), 1, 1,
                   40, 0)
    heart4 = Heart(load_image("heart.jpg", Color('white')), 1, 1,
                   60, 0)
    heart5 = Heart(load_image("heart.jpg", Color('white')), 1, 1,
                   80, 0)

    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


def pause_screen():
    intro_text = ["press F to continue"]

    fon = pygame.transform.scale(load_image('nothing.png'), (1500, 1000))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 10
    for line in intro_text:
        string_rendered = font.render(line, 2, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 600
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 102:
                    return
        pygame.display.flip()
        clock.tick(60)


def dead_screen():
    intro_text = ["You died :("]

    fon = pygame.transform.scale(load_image('nothing.png'), (1500, 1000))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 20
    for line in intro_text:
        string_rendered = font.render(line, 2, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 15
        intro_rect.top = text_coord
        intro_rect.x = 650
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                running = False
        pygame.display.flip()
        clock.tick(60)


def start_screen():
    intro_text = ["Lazy Reborn", "",
                  "your goal is to get to the end and defeat all the enemies",
                  "hero movement with arrows and keyboard",
                  "shoot with spacebar",
                  "good luck!",
                  "",
                  "--press any button to continue--"]

    fon = pygame.transform.scale(load_image('fon.png'), (1500, 1000))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 20
    for line in intro_text:
        string_rendered = font.render(line, 2, pygame.Color('blue'))
        intro_rect = string_rendered.get_rect()
        text_coord += 15
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(60)
