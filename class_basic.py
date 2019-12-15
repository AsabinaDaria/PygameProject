from constants import *

### похоже что это материнский класс для гг и нпс ###


class Basic():
    def __init__(self, pos_x, pos_y, parts, list_of_bullets, name='перс какой-то'):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.parts = parts
        self.list_of_bullets = list_of_bullets

    def __str__(self):  # выводит строку в которой координаты и имя перса
        return str(self.pos_x) + '|' + str(self.pos_y) + '|' + self.name

    def get_pos(self):  # выводит координаты кортежем из двух циферок
        return (self.pos_x, self.pos_y)

    def make_basic_pew(self):
        for i in range(len(self.list_of_bullets)):
            if str(self.list_of_bullets[i]) == 'basic_bullets':
                self.list_of_bullets[i].make_pew(
                    [self.pos_x, self.pos_y, 'basic_bullet'])
