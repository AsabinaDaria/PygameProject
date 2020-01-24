from constants import *
from class_basic import *
from heart import *


class Medpack(Basic):
    def used(self):
        for sprite in hearts_group:
            self.kill()
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
        self.kill()
