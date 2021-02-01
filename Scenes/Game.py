import pygame
from datetime import datetime
from Scenes.Scene import Scene
from Components.World import World
from Components.Player import Player
from Components.Constants import BG_IMG, LIFE_IMG

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.life_img = LIFE_IMG
        self.reset()

    def reset(self):
        self.level = 1
        self.lives = 3
        self.world = World(self.level)
        self.player = Player(self.world)

    def startup(self, persist):
        self.persist = persist
        self.start_time = datetime.now().replace(microsecond = 0)
        self.reset()

    def cleanup(self):
        self.done = False
        end_time = datetime.now().replace(microsecond = 0)
        game_time = end_time - self.start_time
        self.persist = {"Game time": game_time}
        return self.persist

    def handle_event(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.reset()

    def update(self):
        self.world.update()
        self.player.update()

        if self.player.dead:
            self.reset_level()


        if self.player.level_complete:
            self.next_level()


    def draw(self, screen):
        screen.blit(BG_IMG, (0,0))
        self.world.draw(screen)
        self.player.draw(screen)
        self.draw_lives(screen)

    def draw_lives(self, screen):
        for i in range(self.lives):
            screen.blit(self.life_img, (i* 30, 570))


    def next_level(self):
        self.level += 1
        self.world = World(self.level)
        self.player = Player(self.world)
        if self.world.tiles == []:
            self.done = True
            self.next = "Win"

    def reset_level(self):
        self.lives -= 1
        if self.lives == 0:
            self.done = True
            self.next = "Lost"
            return
        self.world = World(self.level)
        self.player = Player(self.world)
