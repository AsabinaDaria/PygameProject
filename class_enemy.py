from constants import *
from class_basic import *
from pygame import *
from heart import *
from functions import *


### ну тут понятно я думаю ###


class Enemy(Basic):

    def make_pew(self, kind_of_pew, pos):
        if kind_of_pew == 'mel':
            self.make_pew_mel(pos)

    def follow(self, tar):  # ИИ врага
        if self.alive:
            tar_x, tar_y = tar.get_pos()
            if tar_y - 40 > self.y and abs(tar_y - self.y) < 200 and abs(tar_x - self.x) < 200:
                self.rect.top += 1
                self.y_change(1)
            elif tar_y + 40 < self.y and abs(tar_y - self.y) < 200 and abs(tar_x - self.x) < 200:
                self.rect.top -= 1
                self.y_change(-1)
            if tar_x - 40 > self.x and abs(tar_x - self.x) < 200 and abs(tar_y - self.y) < 200:
                self.rect.left += 1
                self.x_change(1)
            elif tar_x + 40 < self.x and abs(tar_x - self.x) < 200 and abs(tar_y - self.y) < 200:
                self.rect.left -= 1
                self.x_change(-1)

            if (tar_y - 40 <= self.y and tar_y + 40 >= self.y and  # атака врага
                    tar_x - 40 <= self.x and tar_x + 40 >= self.x):
                if self.tics + 500 < pygame.time.get_ticks():
                    self.tics = pygame.time.get_ticks()
                    self.hit = pygame.mixer.Sound("Data/hit.wav")  # звук атаки
                    self.hit.play()
                    self.ht = self.counter_hp()
                    if self.alive:
                        self.heart = Heart(load_image("dead_heart.jpg", Color('white')), 1, 1,
                                           self.ht, 0)  # убавление жизней

    def counter_hp(self):
        if self.sp:  # проверка на количество жизней гг
            return self.sp.pop()
        self.alive = False
        self.dead_screen()

    def dead_screen(self):  # экран смерти
        intro_text = ["You died :("]

        fon = pygame.transform.scale(load_image('nothing.png'), (1500, 1000))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 20
        for line in intro_text:
            string_rendered = font.render(line, 2, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 15
            intro_rect.top = text_coord
            intro_rect.x = 650
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    running = False
            pygame.display.flip()
            clock.tick(60)

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

    def get_hitted(self, player):  # урон врага
        self.robot_hit.play()
        self.chars[1] -= 1
        if self.chars[1] == 0:
            self.kill()
            player.change_score(1)

    def is_alive(self):  # проверка на то, жив ли гг
        return(self.alive)
