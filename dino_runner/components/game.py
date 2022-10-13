import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacle_manager import ObstacleManager
from dino_runner.components.score import Score
from dino_runner.utils.constants import BG, DINO_START, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.running = False
        self.death_count = 0
        
    
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()    
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()
#        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        
        pos_center_x = SCREEN_WIDTH // 2
        pos_center_y = SCREEN_HEIGHT // 2

        font = pygame.font.Font(FONT_STYLE, 30)
        
        text = self.status_game(font)
        
        text_rect = text.get_rect()
        text_rect.center = (pos_center_x, pos_center_y)
        self.screen.blit(text, text_rect)

        dino_rect = DINO_START.get_rect()
        dino_rect.center = (pos_center_x, pos_center_y - 80)
        self.screen.blit(DINO_START, dino_rect)

        pygame.display.update()

        self.handle_menu_events()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()
    
    def status_game(self, font):
        if self.death_count == 0:
            text = font.render("Press any key to start", True, (0, 0, 0))
        else:
            text = font.render("Press any key to Restart", True, (0, 0, 0))
            score = font.render(f"Your Score: {self.score.score}", True, (0, 0, 0))
            score = font.render(f"Veces que haz muerto: {self.death_count}", True, (0, 0, 0))
            score_rect = score.get_rect()
            score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            self.screen.blit(score, score_rect)
        
        return text
