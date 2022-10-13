import pygame
import random
from dino_runner.components.cactus import SmallCactus, LargeCactus
from dino_runner.components.bird import Bird, BirdBajo
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            suerte = random.randint(0, 3)
            if suerte == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif suerte == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif suerte == 2:
                self.obstacles.append(BirdBajo(BIRD))
            else:
                self.obstacles.append(Bird(BIRD))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                game.playing =  False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []