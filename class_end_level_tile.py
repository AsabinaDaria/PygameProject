import pygame
from pygame.color import Color
from pygame import *
import os
from constants import *
from class_basic import *
from class_no_go_tile import *


class End_level_tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(end_level_tiles_group, all_sprites)
        self.image = load_image('end_level_locked_door.jpg')
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)

    def unlock_door(self):
        self.image = load_image('end_level_unlocked_door.jpg')
