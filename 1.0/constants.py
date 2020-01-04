import pygame
from pygame.color import Color
from pygame import *
import os

### более-пельменее важные константы ###
size = width, height = 800, 600  # размер окна
running = True  # работает игра или нет (хотя это, наверно, понятно)
fps = 50  # ну кол-во кадров в секунду что же ещё
x_gg, y_gg = 0, 0  # начальная позиция гг
### остальные константы ###
# отвечают за движение гг
# изначально равны False чтобы никуда не двигался без нажатия клавиши
move_gg_up = False
move_gg_down = False
move_gg_left = False
move_gg_right = False

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()

# для клеточного поля
tile_width = tile_height = 50
