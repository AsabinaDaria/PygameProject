from constants import *

### материнский класс пуль ###


class Bullet(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, direction, chars=[]):
        super().__init__(all_sprites, bullets_group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.chars = chars
        self.i = 0
        self.alive = True
        self.move_up, self.move_down, self.move_left, self.move_right = direction
        self.mask = pygame.mask.from_surface(self.image)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):  #  движение пуль
        if self.alive:
            if self.move_up == True and self.move_right != True and self.move_left != True:
                self.rect.top -= 3
            if self.move_down == True and self.move_right != True and self.move_left != True:
                self.rect.top += 3
            if self.move_left == True:
                self.rect.left -= 3
            if self.move_right == True:
                self.rect.left += 3
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]

    def dead(self):
        self.alive = False
