from constants import *
from class_basic import *
from mel import *
from pygame import *
from heart import *


### ну тут понятно я думаю ###


class Enemy(Basic):

    def make_pew(self, kind_of_pew, pos):
        if kind_of_pew == 'mel':
            self.make_pew_mel(pos)

    def follow(self, tar):
        if self.alive:
            tar_x, tar_y = tar.get_pos()
            if tar_y - 40 > self.y and abs(tar_y - self.y) < 200 and abs(tar_x - self.x) < 200:
                self.rect.top += 1
                self.y_change(1)

                #self.rect.top += 1
                # if pygame.sprite.spritecollideany(self, no_go_tiles_group):
                #    self.rect.top -= 1
                #    self.y_change(-1)
                #self.rect.top -= 1
            elif tar_y + 40 < self.y and abs(tar_y - self.y) < 200 and abs(tar_x - self.x) < 200:
                self.rect.top -= 1
                self.y_change(-1)

                #self.rect.top -= 1
                # if pygame.sprite.spritecollideany(self, no_go_tiles_group):
                #    self.rect.top += 1
                #    self.y_change(+1)
                #self.rect.top += 1
            if tar_x - 40 > self.x and abs(tar_x - self.x) < 200 and abs(tar_y - self.y) < 200:
                self.rect.left += 1
                self.x_change(1)

                #self.rect.left += 1
                # if pygame.sprite.spritecollideany(self, no_go_tiles_group):
                #    self.rect.left -= 1
                #    self.x_change(-1)
                #self.rect.left -= 1
            elif tar_x + 40 < self.x and abs(tar_x - self.x) < 200 and abs(tar_y - self.y) < 200:
                self.rect.left -= 1
                self.x_change(-1)

                #self.rect.left -= 1
                # if pygame.sprite.spritecollideany(self, no_go_tiles_group):
                #    self.rect.left += 1
                #    self.x_change(+1)
                #self.rect.left += 1

            if (tar_y - 40 <= self.y and tar_y + 40 >= self.y and
                    tar_x - 40 <= self.x and tar_x + 40 >= self.x):
                if self.tics + 500 < pygame.time.get_ticks():
                    self.tics = pygame.time.get_ticks()
                    self.hit = pygame.mixer.Sound("Data/hit.wav")
                    self.hit.play()
                    self.ht = self.counter_hp()
                    if self.alive:
                        self.heart = Heart(load_image("dead_heart.jpg", Color('white')), 1, 1,
                                           self.ht, 0)

    def counter_hp(self):
        if self.sp:
            return self.sp.pop()
        self.alive = False
        dead_screen()

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
            pass

    def make_pew_mel(self, pos):
        new_bullet = Mel(load_image("mel.jpg",
                                    Color('White')), 1, 1, pos[0], pos[1])

    def get_hitted(self):
        self.chars[1] -= 1
        if self.chars[1] == 0:
            self.kill()

    def is_alive(self):
        return(self.alive)
