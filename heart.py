from constants import *


class Heart(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(hearts_group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.i = 0
        self.x = x
        self.y = y

    def cut_sheet(self, sheet, columns, rows):  # обрезка спрайтов
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def follow(self, tar):
        tar_x, tar_y = tar.get_pos()
        if tar_y > self.y:
            self.rect.top += 3
            self.y_change(3)
        elif tar_y < self.y:
            self.rect.top -= 3
            self.y_change(-3)
        if tar_x > self.x:
            self.rect.left += 3
            self.x_change(3)
        elif tar_x < self.x:
            self.rect.left -= 3
            self.x_change(-3)

    def x_change(self, x):
        self.x += x

    def y_change(self, y):
        self.y += y

    def update(self, tar):
        tar_x, tar_y = tar.get_pos()
        self.rect = self.rect.move(tar_x, tar_y)
