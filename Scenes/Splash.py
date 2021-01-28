import pygame
from Scenes.Scene import Scene
from Components.Constants import WHITE, SPLASH_IMG

class Splash(Scene):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.loop = 50
        self.img = SPLASH_IMG

    def startup(self, persist):
        self.persist = persist

    def cleanup(self):
        self.done = False
        return self.persist

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.done = True
            self.next = "Intro"

    def update(self):
        self.count += 1
        if self.count == self.loop:
            self.done = True
            self.next = "Intro"

    def draw(self, screen):
        screen.blit(self.img, (0,0))