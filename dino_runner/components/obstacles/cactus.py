import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2) # Llamar cualquiera de los 3 tipos de cactus 
        super().__init__(image, self.type)
        self.rect.y = 325 # Posicion de los cactus para que esten un poco alejados del dino