from constants import *
from class_basic import *

### это класс для гг (вернее того, чем мы управляем) ###


class Gg(Basic):
    # отвечает за движение гг
    def basic_move(self, move_gg_up, move_gg_down, move_gg_left, move_gg_right):
        if move_gg_up:
            self.pos_y -= 2
        if move_gg_down:
            self.pos_y += 2
        if move_gg_left:
            self.pos_x -= 2
        if move_gg_right:
            self.pos_x += 2
