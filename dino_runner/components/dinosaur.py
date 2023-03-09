import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, RUNNING_SHIELD, JUMPING_SHIELD, DUCKING_SHIELD, DEFAULT_TYPE, SHIELD_TYPE

RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}


class Dinosaur(Sprite):
    X_POS = 80 
    Y_POS = 310
    JUMP_SPEED = 8.5

    def __init__ (self): # Metodo constructor y definicion de variables
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_speed = self.JUMP_SPEED
        self.has_power_up = False
        self.power_time_up = 0
        
    def update(self, user_input): # Actualizacion y llamado de metodos
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
            
        if user_input[pygame.K_DOWN] and not self.dino_jump: # Presionar abajo para agacharse, sino esta saltando
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
            
        elif user_input[pygame.K_UP] and not self.dino_jump: # Presionar arriba para saltar, sino esta agachado
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False

        elif not self.dino_jump:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        if self.step_index >= 10:
            self.step_index = 0

    def run(self): # Metodo de Correr
        self.image = RUN_IMG[self.type][self.step_index // 5]  # Alternar imagenes de Correr
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self): #Metodo de Salto
        self.image = JUMP_IMG[self.type]
        self.dino_rect.y -= self.jump_speed * 4
        self.jump_speed -= 0.8

        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED

    def duck(self): # Metodo de Agacharse
        self.image = DUCK_IMG[self.type][self.step_index // 5] # Alternar imagenes de agachado
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 40 # Se Agrega +40 de posicion para que no se distorsione el juego
        self.step_index += 1

    def sound(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def reset(self):
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False