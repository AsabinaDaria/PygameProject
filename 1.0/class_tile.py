import pygame
from pygame.color import Color
from pygame import *
import os
from constants import *
from class_basic import *
#


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.tile_images = {'wall': load_image(
            'box.png'), 'empty': load_image('grass.png')}
        self.image = self.tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
