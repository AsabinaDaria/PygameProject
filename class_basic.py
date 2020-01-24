from constants import *
from class_bullets import *
from class_basic_bullets import *

### похоже что это материнский класс для гг и нпс ###

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

def pause_screen():
    intro_text = ["press F to continue"]

    fon = pygame.transform.scale(load_image('nothing.png'), (1500, 1000))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 10
    for line in intro_text:
        string_rendered = font.render(line, 2, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 600
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 102:
                    return
        pygame.display.flip()
        clock.tick(60)


def dead_screen():
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


def start_screen():
    intro_text = ["Lazy Reborn", "",
                  "your goal is to get to the end and defeat all the enemies",
                  "hero movement with arrows and keyboard",
                  "shoot with spacebar",
                  "good luck!",
                  "",
                  "--press any button to continue--"]

    fon = pygame.transform.scale(load_image('fon.png'), (1500, 1000))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 20
    for line in intro_text:
        string_rendered = font.render(line, 2, pygame.Color('blue'))
        intro_rect = string_rendered.get_rect()
        text_coord += 15
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(60)


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
        self.alive = True
        self.tics = 0
        self.sp = [0, 20, 40, 60, 80]

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

    def update_via_counter(self, counter, direction=None):
        self.i += 1
        if self.i >= counter:
            self.i = 0
            if direction == None:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]

    def get_pos(self):
        return self.x, self.y

    def make_pew(self, kind_of_pew, pos, move_up, move_down, move_left, move_right):
        self.direction = (move_up, move_down, move_left, move_right)
        if move_up == False and move_down == False and move_left == False and move_right == False:
            pass
        elif kind_of_pew[0] == 'basic':
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
