import pygame
import random

from dino_runner.components.power_up.power_up import PowerUp
from dino_runner.utils.constants import SCREEN_WIDTH, HAMMER, HAMMER_TYPE, RUNNING_HAMMER, DUCKING_HAMMER, JUMPING_HAMMER

RUN_IMG = {HAMMER_TYPE: RUNNING_HAMMER}
JUMP_IMG = {HAMMER_TYPE: JUMPING_HAMMER}
DUCK_IMG = {HAMMER_TYPE: DUCKING_HAMMER}


class Hammer(PowerUp):
   
    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)
        