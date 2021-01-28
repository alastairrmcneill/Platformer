import pygame
from Scenes.Scene import Scene

class End(Scene):
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
        pass

    def draw(self, screen):
        pass