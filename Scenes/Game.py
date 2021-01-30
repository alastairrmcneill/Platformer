import pygame
from Scenes.Scene import Scene
from Components.World import World
from Components.Player import Player
from Components.Constants import BG_IMG

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.reset(self.level)

    def reset(self, level):
        self.world = World(level)
        self.player = Player(50, 200, self.world)

    def startup(self, persist):
        self.persist = persist
        self.level = self.persist["Level"]
        self.reset(self.level)

    def cleanup(self):
        self.done = False
        return self.persist

    def handle_event(self, event):
        pass

    def update(self):
        self.world.update()
        self.player.update()

        if self.player.dead:
            self.done = True
            self.next = "Game"
            next_level = self.level
            self.persist = {"Level": next_level}


        if self.player.level_complete:
            next_level = self.level + 1
            self.persist = {"Level": next_level}
            self.done = True
            self.next = "Game"


    def draw(self, screen):
        screen.blit(BG_IMG, (0,0))
        self.world.draw(screen)
        self.player.draw(screen)