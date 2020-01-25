import pygame
from pygame.color import Color
from pygame import *
import os
from constants import *
from class_basic import *
#


class Tile(pygame.sprite.Sprite):  # спрайты
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.tile_images = {'hor': load_image('hor.png'), 'nothing': load_image('nothing.png'), 'ver': load_image('ver.png'), 'wall': load_image(
            'wall.jpg'), 'empty': load_image('floor.jpg')}
        self.image = self.tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
