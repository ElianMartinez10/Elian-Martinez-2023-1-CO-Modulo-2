import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu

class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu('Press any key to start...', self.screen)
        self.running = False
        pygame.mixer.music.load('dino_runner/assets/Sound/Song.wav')
        pygame.mixer.music.play(-1)
        self.score = 0
        self.high_score = 0
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
        
        
    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.game_speed = self.GAME_SPEED
        self.score = 0
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_heigth = SCREEN_HEIGHT // 2

        if self.death_count == 0:
            self.menu.draw(self.screen)
        else:
            self.menu.update_message('GAME OVER. Press any key to restart...')
            self.menu.draw(self.screen)

            font = pygame.font.Font(FONT_STYLE, 30)
            score_text = font.render(f'Score: {self.score}', True, (0, 0, 0))
            high_score_text = font.render(f'High Score: {self.high_score}', True, (0, 0, 0))
            death_count_text = font.render(f'Death Count: {self.death_count}', True, (0, 0, 0))

            score_rect = score_text.get_rect(bottomleft=(half_screen_width - 100, half_screen_heigth + 50))
            high_score_rect = high_score_text.get_rect(bottomleft=(half_screen_width - 100, score_rect.bottom + 50))
            death_count_rect = death_count_text.get_rect(bottomleft=(half_screen_width - 100, high_score_rect.bottom + 50))

            self.screen.blit(score_text, score_rect)
            self.screen.blit(high_score_text, high_score_rect)
            self.screen.blit(death_count_text, death_count_rect)
        

        self.screen.blit(ICON, (half_screen_width - 50, half_screen_heigth - 140))

        self.menu.update(self)

    def update_score(self):
        self.score += 1

        if self.score > self.high_score:
            self.high_score = self.score

        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)