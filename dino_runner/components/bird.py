from .obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = 230
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.images[self.index//5], self.rect)
        self.index += 1

class BirdBajo(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = 315
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.images[self.index//5], self.rect)
        self.index += 1