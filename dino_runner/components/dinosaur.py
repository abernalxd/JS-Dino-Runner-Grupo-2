import pygame
from pygame.sprite import Sprite
import os
from dino_runner.utils.constants import HAMMER_TYPE,RUNNING_HAMMER, JUMPING_HAMMER, DUCKING_HAMMER, DEFAULT_TYPE, DUCKING, DUCKING_SHIELD, JUMPING, JUMPING_SHIELD, RUNNING, RUNNING_SHIELD, SHIELD_TYPE, SOUNDS_DIR

RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE : RUNNING_SHIELD, HAMMER_TYPE : RUNNING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE : JUMPING_SHIELD, HAMMER_TYPE : JUMPING_HAMMER}
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE : DUCKING_SHIELD, HAMMER_TYPE : DUCKING_HAMMER}

class Dinosaur(Sprite):
    Y_POS = 310
    X_POS = 80
    Y_POS_DUCK = 340
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.duck_img = DUCKING
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_running =  True
        self.dino_jumping = False 
        self.dino_ducking = False 
        self.jump_velocity = self.JUMP_VELOCITY
        self.has_power_up = False
        self.power_up_time_up = 0

    def update(self, user_input):
        if self.dino_running:
            self.run()
        elif self.dino_jumping:
            self.jump()
        elif self.dino_ducking:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jumping:
#            sound_jump = pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "jump.ogg"))
#            sound_jump.play()
            self.dino_jumping = True
            self.dino_running = False
            self.dino_ducking = False
        elif user_input[pygame.K_DOWN] and not self.dino_jumping:
            self.dino_jumping = False
            self.dino_running = False
            self.dino_ducking = True
        elif not self.dino_jumping or self.dino_ducking:
            self.dino_jumping = False
            self.dino_running = True
            self.dino_ducking = False        
        if self.step_index >= 9:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.dino_rect.y -= self.jump_velocity *4
        self.jump_velocity -= 0.8

        if self.jump_velocity < -8.5:
            self.dino_jumping = False 
            self.dino_rect.y = self.Y_POS
            self.jump_velocity = self.JUMP_VELOCITY

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def on_pick_power_up(self, start_time, duration, type):
        self.has_power_up = True
        self.power_up_time_up = start_time + (duration * 1000)
        self.type = type