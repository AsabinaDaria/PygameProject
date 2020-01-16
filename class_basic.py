from constants import *
from class_bullets import *
from class_basic_bullets import *

### похоже что это материнский класс для гг и нпс ###


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

    def cut_sheet(self, sheet, columns, rows):
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

    def update_via_counter(self, counter, direction):
        self.i += 1
        if self.i >= counter:
            self.i = 0
            if self.cur_frame % 3 == 2:
                self.update()
            else:
                self.update()

    def get_pos(self):
        return self.x, self.y

    def make_pew(self, kind_of_pew, pos, move_up, move_down, move_left, move_right):
        self.direction = (move_up, move_down, move_left, move_right)
        if kind_of_pew == 'basic':
            self.make_basic_pew(self.direction, pos)

    def make_basic_pew(self, direction, pos):
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
