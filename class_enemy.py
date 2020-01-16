from constants import *
from class_basic import *
from mel import *


### ну тут понятно я думаю ###


class Enemy(Basic):

    def make_pew(self, kind_of_pew, pos):
        if kind_of_pew == 'mel':
            self.make_pew_mel(pos)

    def follow(self, tar):
        tar_x, tar_y = tar.get_pos()
        if tar_y - 40 > self.y:
            self.rect.top += 1
            self.y_change(1)
        elif tar_y + 40 < self.y:
            self.rect.top -= 1
            self.y_change(-1)
        if tar_x - 40 > self.x:
            self.rect.left += 1
            self.x_change(1)
        elif tar_x + 40 < self.x:
            self.rect.left -= 1
            self.x_change(-1)

    def follow_and_hit(self, tar):
        u1, u2 = True, True
        tar_x, tar_y = tar.get_pos()
        print(tar_x, tar_y)
        print(self.x, self.y)
        if tar_y - 40 > self.y:
            self.rect.top += 1
            self.y_change(1)
            u1 = False
        elif tar_y + 40 < self.y:
            self.rect.top -= 1
            self.y_change(-1)
            u1 = False
        # else:
        #    u1 = True
        if tar_x - 40 > self.x:
            self.rect.left += 1
            self.x_change(1)
            u2 = False
        elif tar_x + 40 < self.x:
            self.rect.left -= 1
            self.x_change(-1)
            u2 = False
        if u1 and u2:
            self.make_pew(self.get_chars(
                'kind_of_pew')[0], self.get_pos())

    def make_pew_mel(self, pos):
        new_bullet = Mel(load_image("mel.jpg",
                                    Color('White')), 1, 1, pos[0], pos[1])
