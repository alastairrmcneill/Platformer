import pygame
from Scenes.Scene import Scene
from Components.World import World
from Components.Player import Player
from Components.Constants import BG_IMG

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.world = World()
        self.player = Player(self.world)

    def startup(self, persist):
        self.persist = persist

    def cleanup(self):
        self.done = False
        return self.persist

    def handle_event(self, event):
        pass

    def update(self):
        self.world.update()
        self.player.update()

    def draw(self, screen):
        screen.blit(BG_IMG, (0,0))
        self.world.draw(screen)
        self.player.draw(screen)