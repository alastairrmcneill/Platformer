import pygame
import json
import os
from datetime import datetime
from Scenes.Scene import Scene
from Components.World import World
from Components.Player import Player
from Components.Camera import Camera
from Components.Constants import BG_IMG, LIFE_IMG, WORLDS_PATH

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.life_img = LIFE_IMG

    def reset(self):
        self.level = 5
        self.world = World(self.world_num, self.level)
        self.player = Player(self.world)
        self.camera = Camera(self.player)

    def startup(self, persist):
        self.persist = persist
        if self.persist["State"] == "New":
            self.start_time = datetime.now().replace(microsecond = 0)
            self.world_num = self.persist["World"]
            self.reset()
        elif self.persist["State"] == "Restart":
            self.reset()
        elif self.persist["State"] == "Continue":
            pass


    def cleanup(self):
        self.done = False
        if self.next == "Pause menu":
            self.persist = {"Game": self}
            return self.persist

        end_time = datetime.now().replace(microsecond = 0)
        game_time = end_time - self.start_time
        self.persist = {"Game time": game_time}
        return self.persist

    def handle_event(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.reset()
        if keys[pygame.K_p]:
            self.done = True
            self.next = "Pause menu"

    def update(self):
        self.world.update()
        self.player.update()

        if self.player.dead:
            self.reset_level()


        if self.player.level_complete:
            self.next_level()

        self.camera.scroll()

    def draw(self, screen):
        screen.blit(BG_IMG, (0 - self.camera.offset.x, 0 - self.camera.offset.y))
        self.world.draw(screen, self.camera)
        self.player.draw(screen, self.camera)
        self.draw_lives(screen)

    def draw_lives(self, screen):
        for i in range(self.player.lives):
            screen.blit(self.life_img, (i* 30, 570))


    def next_level(self):
        self.level += 1
        self.world = World(self.world_num, self.level)
        self.player.reset(self.world)
        if self.world.tiles == []:
            self.world_complete()
        self.camera.reset(self.player)

    def reset_level(self):
        self.player.lives -= 1
        if self.player.lives == 0:
            self.done = True
            self.next = "Lost"
            return
        self.world = World(self.world_num, self.level)
        self.player.reset(self.world)
        self.camera.reset(self.player)

    def world_complete(self):
        self.done = True
        self.next = "Win"

        path = os.path.join(WORLDS_PATH, "World Info.json")
        # Write to the next work that world is now unlocked.
        with open(path, "r+") as f:
            data = json.load(f)
            for world in data["Worlds"]:
                if world["World"] == self.world_num + 1:
                    world["Unlocked"] = True
            f.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, f, indent=4)
            f.truncate()     # remove remaining part

        # Write time to this game file if faster

        # Update player file
        path = os.path.join(WORLDS_PATH, "Player Skills.json")
        with open(path, "r+") as f:
            data = json.load(f)
            data["Current world"] = self.world_num + 1
            f.seek(0)
            json.dump(data, f, indent = 4)
            f.truncate()

