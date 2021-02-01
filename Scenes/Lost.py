import pygame
from Scenes.Scene import Scene
from Components.Constants import GAME_OVER_IMG, BLACK, WIN_WIDTH, WIN_HEIGHT

pygame.font.init()

class Lost(Scene):
    def __init__(self):
        super().__init__()
        self.image = GAME_OVER_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (WIN_WIDTH // 2 , WIN_HEIGHT // 2)

    def startup(self, persist):
        self.persist = persist
        self.game_time = self.persist["Game time"]

    def cleanup(self):
        self.done = False
        return self.persist

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.done = True
            self.next = "Intro"

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BLACK)
        screen.blit(self.image, self.rect)
