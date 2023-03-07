from dino_runner.components.obstacles.obstacle import Obstacle
import random

from dino_runner.utils.constants import SCREEN_HEIGHT, BIRD

class Birds(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0,1) # Posicion al azar
        super().__init__(image, self.type)
        self.rect.y = random.choice([50, 125, 200]) # Calcula la posición vertical según la posición elegida        