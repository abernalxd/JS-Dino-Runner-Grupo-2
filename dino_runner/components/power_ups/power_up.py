from pygame.sprite import Sprite
from random import randint
from dino_runner.utils.constants import SCREEN_WIDTH


class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + randint(800, 1000)
        self.rect.y = randint (150, 250)
        self.start_time = 0
        self.duration = randint (3, 5)

    def update (self, game_speed, powers_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            powers_ups.pop()

    def draw (self, screen):
        print(self.image)
        print(self.rect.x, self.rect.y)
        screen.blit(self.image, (self.rect.x, self.rect.y))