from random import randint
from .obstacle import Obstacle


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300