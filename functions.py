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
            elif level[y][x] == 'n':
                Tile('nothing', x, y)
            elif level[y][x] == '#':
                No_go_tile('wall', x, y)
            elif level[y][x] == 'e':
                No_go_tile('end_level_locked_door', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Gg(load_image(
                    "just_dote.jpg", Color('White')), 4, 1, x * 50, y * 50, ['basic'])
                new_player.add(player_group)
                player_dote = Player_dote(load_image(
                    'player_dote.jpg'), 1, 1, x * 50, y * 50)
            elif level[y][x] == '!':
                Tile('empty', x, y)
                new_enemy = Enemy(load_image(
                    "mar.png", Color('White')), 4, 1, x * 50, y * 50, ['mel', 2])
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
    return new_player, no_go_dotes, x, y
