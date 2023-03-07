import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Birds

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__ (self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
          obstacle_type = random.choice([SMALL_CACTUS, LARGE_CACTUS])
          obstacle = Cactus(obstacle_type)        
          self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                print("Colision")
                pygame.time.delay(100)
                pygame.playing = False
                break 

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)