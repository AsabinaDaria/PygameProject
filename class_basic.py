from constants import *
from class_bullets import *
from class_basic_bullets import *

###материнский класс для гг и нпс ###

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    color_key = colorkey
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Basic(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, chars=[]):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.chars = chars
        self.x, self.y = x, y
        self.i = 0
        self.rect_top_to_work = 0
        self.rect_left_to_work = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.alive = True  # проверка на то, жив ли гг
        self.tics = 0
        self.sp = [0, 20, 40, 60, 80] # жизни гг
        self.score = 0  # счет
        self.robot_hit = pygame.mixer.Sound("Data/robot_hit.wav")  # урон врага

    def cut_sheet(self, sheet, columns, rows): # для анимации спрайтов
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

    def dir_move(self, move_up, move_down, move_left, move_right):
        if move_up == True and move_right != True and move_left != True:
            self.cur_frame = 3
            self.image = self.frames[self.cur_frame]
        if move_down == True and move_right != True and move_left != True:
            self.cur_frame = 0
            self.image = self.frames[self.cur_frame]
        if move_left == True:
            self.cur_frame = 1
            self.image = self.frames[self.cur_frame]
        if move_right == True:
            self.cur_frame = 2
            self.image = self.frames[self.cur_frame]

    def x_change(self, x):
        self.x += x

    def y_change(self, y):
        self.y += y

    def update_via_counter(self, counter, direction=None):
        self.i += 1
        if self.i >= counter:
            self.i = 0
            if direction == None:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]

    def get_pos(self):  # позиция гг
        return self.x, self.y

    def make_pew(self, kind_of_pew, pos, move_up, move_down, move_left, move_right):
        self.direction = (move_up, move_down, move_left, move_right)
        if move_up == False and move_down == False and move_left == False and move_right == False:
            pass
        elif kind_of_pew[0] == 'basic':
            self.make_basic_pew(self.direction, pos)

    def make_basic_pew(self, direction, pos):  # новая пуля
        new_bullet = BasicBullet(load_image("basic_bullet.jpg",
                                            Color('White')), 1, 1, pos[0], pos[1], direction)

    def rect_top(self, speed):
        if (speed + self.rect_top_to_work) % 1 != 0:
            self.rect_top_to_work += speed % 1
            self.rect.top += speed // 1
        else:
            self.rect.top += speed + self.rect_top_to_work
            self.rect_top_to_work = 0

    def rect_left(self, speed):
        if (speed + self.rect_left_to_work) % 1 != 0:
            self.rect_left_to_work += speed % 1
            self.rect.left += speed // 1
        else:
            self.rect.left += speed + self.rect_left_to_work
            self.rect_left_to_work = 0

    def get_chars(self, recv=None):
        if recv == 'kind_of_bullet':
            return self.chars[0]
        else:
            return self.chars

    def get_score(self):
        return self.score

    def change_score(self, n):
        self.score += n

    def follow_pos(self, pos, move_gg_up, move_gg_down,
                   move_gg_left, move_gg_right):
        tar_x, tar_y = pos[0], pos[1]
        # and abs(tar_y - self.y) < 200 and abs(tar_x - self.x) < 200:
        if tar_y > self.rect.top:
            self.rect.top += 2
            self.y_change(2)
            move_gg_down = True
            self.dir_move(move_gg_up, move_gg_down,
                          move_gg_left, move_gg_right)
            self.rect.top += 2
            if pygame.sprite.spritecollideany(self, no_go_tiles_group):
                self.rect.top -= 2
                self.y_change(-2)
            self.rect.top -= 2
        # and abs(tar_y - self.y) < 200 and abs(tar_x - self.x) < 200:
        elif tar_y < self.rect.top:
            self.rect.top -= 2
            self.y_change(-2)
            move_gg_up = True
            self.dir_move(move_gg_up, move_gg_down,
                          move_gg_left, move_gg_right)
            self.rect.top -= 2
            if pygame.sprite.spritecollideany(self, no_go_tiles_group):  # проверка на наличие непроходимых спрайтов
                self.rect.top += 2
                self.y_change(+2)
            self.rect.top += 2
        # and abs(tar_x - self.x) < 200 and abs(tar_y - self.y) < 200:
        if tar_x - 40 > self.rect.left:
            self.rect.left += 2
            self.x_change(2)
            move_gg_right = True
            self.dir_move(move_gg_up, move_gg_down,
                          move_gg_left, move_gg_right)
            self.rect.left += 2
            if pygame.sprite.spritecollideany(self, no_go_tiles_group):
                self.rect.left -= 2
                self.x_change(-2)
            self.rect.left -= 2
        # and abs(tar_x - self.x) < 200 and abs(tar_y - self.y) < 200:
        elif tar_x + 40 < self.rect.left:
            self.rect.left -= 2
            self.x_change(-2)
            move_gg_left = True
            self.dir_move(move_gg_up, move_gg_down,
                          move_gg_left, move_gg_right)
            self.rect.left -= 2
            if pygame.sprite.spritecollideany(self, no_go_tiles_group):
                self.rect.left += 2
                self.x_change(+2)
            self.rect.left += 2

    def get_cur_frame(self):
        return self.cur_frame
