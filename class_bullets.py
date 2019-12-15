from constants import *

### материнский класс пуль ###


class Bullets():
    def __init__(self, list_of_listes_of_poses_and_names=[]):
        self.list_of_listes_of_poses_and_names = list_of_listes_of_poses_and_names

    def make_pew(self, list_of_poses_and_names):
        self.list_of_listes_of_poses_and_names.append(list_of_poses_and_names)

    def get_pos(self):  # выводит координаты кортежем из двух циферок
        return (self.list_of_listes_of_poses_and_names)
