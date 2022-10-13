import pygame
import random
from dino_runner.components.cactus import Cactus
from dino_runner.components.bird import Bird
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD
from dino_runner.components.dinosaur import Dinosaur

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            number_random = random.randint(0, 2)
            if number_random == 0:
                self.obstacles.append(Cactus(images=SMALL_CACTUS, value_y=325))
            elif number_random == 1:
                self.obstacles.append(Cactus(images=LARGE_CACTUS, value_y=300))
            else:
                self.obstacles.append(Bird(BIRD))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(300)
                game.death_count += 1
                game.playing = False
                break   

    def draw(self, game):
        for obstacle in self.obstacles:
            obstacle.draw(game.screen)

    def reset_obstacles(self):
        self.obstacles = []