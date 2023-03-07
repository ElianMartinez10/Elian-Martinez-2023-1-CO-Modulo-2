import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    half_screen_height = SCREEN_HEIGHT // 2
    half_screen_width = SCREEN_WIDTH // 2

    def __init__ (self, message, screen):
        screen.fill((255, 255, 255)) # Color del Menu
        self.font = pygame.font.Font(FONT_STYLE, 30) # Tipo de fuente
        self.text = self.font.render(message, True, (0, 0, 0)) # texto y caracteristicas
        self.text_rect = self.text.get_rect() # rectangulo de texto
        self.text_rect.center = (self.half_screen_width, self.half_screen_height) # posicion del texto 


    def update(self):
        pass

    def draw(self, screen):
        pass