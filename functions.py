import pygame
from pygame.color import Color
from pygame import *
import os
from constants import *
from class_basic import *
from class_gg import *
from class_enemy import *
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
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.tile_images = {'wall': load_image(
            'box.png'), 'empty': load_image('grass.png')}
        self.image = self.tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Gg(load_image(
                    "just_dote.jpg", Color('White')), 4, 1, hero_pos[0], hero_pos[1], ['basic'])
                new_player.add(player_group)
            elif level[y][x] == '!':
                Tile('empty', x, y)
                new_enemy = Enemy(load_image(
                    "mar.png"), 1, 1, hero_pos[0] + 100, hero_pos[1] + 100, ['mel'])
                new_enemy.add(enemy_group)

    # вернем игрока, а также размер поля в клетках
    return new_player, x, y

