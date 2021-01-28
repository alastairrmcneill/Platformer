import pygame
from Scenes.Scene import Scene
from Components.Constants import RED

class Intro(Scene):
    def __init__(self):
        super().__init__()

    def startup(self, persist):
        self.persist = persist

    def cleanup(self):
        self.done = False
        return self.persist

    def handle_event(self, event):
        pass

    def update(self):
        self.done = True
        self.next = "Game"

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (0,0,100,100))