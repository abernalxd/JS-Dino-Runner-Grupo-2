from random import randint
from .obstacle import Obstacle


class Cactus(Obstacle):
    def __init__(self, images, value_y):
        self.type = randint(0, 2)
        super().__init__(images, self.type)
        self.rect.y = value_y
