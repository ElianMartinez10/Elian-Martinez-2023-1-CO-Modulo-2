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


    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))    

    def draw(self, screen, x = half_screen_width, y = half_screen_height ):
        screen.blit(self.text, self.text_rect)
    
    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)