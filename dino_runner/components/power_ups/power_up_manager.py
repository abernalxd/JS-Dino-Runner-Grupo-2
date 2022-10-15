from .shield import Shields
from .hammer import Hammers
from random import randint
import pygame
import random

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appaers = 0

    def generate_power_up (self, score):
        if len(self.power_ups) == 0 and self.when_appaers  == score :
            self.when_appaers += randint (200, 300)
            power_append = random.randint(0,1)
            if power_append == 0:
                self.power_ups.append(Shields())
                print("Escudo")
            else: 
                self.power_ups.append(Hammers())
                print("Martillo")

    def update (self, game_speed, player, score):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                start_time = pygame.time.get_ticks()
                player.on_pick_power_up(start_time, power_up.duration, power_up.type)
                self.power_ups.remove(power_up)

    def draw (self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups (self):
        self.power_ups = []
        self.when_appaers = randint (200,300)
