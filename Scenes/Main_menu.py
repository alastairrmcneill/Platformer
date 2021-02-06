import pygame
import os
import json
from Scenes.Scene import Scene
from Components.Button import Button
from Components.Constants import GAME_OVER_IMG, BLACK, WIN_WIDTH, WIN_HEIGHT, WORLD1_THUMBNAIL, MENU_BG_IMG, WORLDS_PATH, LOCKED_THUMBNAIL, ARROW_LEFT, ARROW_RIGHT

pygame.font.init()

class Main_menu(Scene):
    def __init__(self):
        super().__init__()
        self.bg = MENU_BG_IMG
        self.page = 0
        self.world_buttons = []
        self.world_buttons_setup()
        self.page = 0
        self.arrow_buttons = [Button(ARROW_LEFT, 30, 500, 1), Button(ARROW_RIGHT, 570, 500, 2)]


    def startup(self, persist):
        self.persist = persist

    def cleanup(self):
        self.done = False
        self.persist = {"World": self.world,
                        "State": "New"}
        return self.persist

    def handle_event(self, event):
        for button in self.world_buttons:
            button.run()
            if button.done:
                if button.index != 0:
                    self.done = True
                    self.next = "Game"
                    self.world = button.index
                button.done = False
                button.clicked = False

        for button in self.arrow_buttons:
            button.run()
            if button.done:
                if button.index == 1:
                    self.page -= 1
                    if self.page < 0:
                        self.page = len(self.world_button_data) // 3
                elif button.index == 2:
                    self.page += 1
                    if self.page > len(self.world_button_data) // 3:
                        self.page = 0
                button.done = False
                button.clicked = False
                self.update_world_buttons()



    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.bg, (0,0))
        for button in self.world_buttons:
            button.draw(screen)

        for button in self.arrow_buttons:
            button.draw(screen)

    def update_world_buttons(self):
        for i in range(len(self.world_buttons)):
            try:
                button_data = self.world_button_data[self.page * 3 + i]
                print(button_data)
                self.world_buttons[i].hide = False


                if button_data["Unlocked"]:
                    self.world_buttons[i].index = self.page * 3 + i + 1
                    self.world_buttons[i].update(WORLD1_THUMBNAIL)
                    # call from a list of list of thumbnails

                else:
                    self.world_buttons[i].index = 0
                    self.world_buttons[i].update([LOCKED_THUMBNAIL, LOCKED_THUMBNAIL, LOCKED_THUMBNAIL])
            except:
                self.world_buttons[i].hide = True


        for button in self.world_buttons:
            print(button.index)



    def world_buttons_setup(self):
        self.world_button_data = []
        for i in range(len(os.listdir(WORLDS_PATH))):
            path = os.path.join(WORLDS_PATH, "World " + str(i + 1) + ".json")
            with open(path, "r") as jsonFile:
                data = json.load(jsonFile)
                world_dict = {"Unlocked": data["Unlocked"],
                                "Best time": data["Best time"]}
                self.world_button_data.append(world_dict)

        self.world_buttons = [Button(WORLD1_THUMBNAIL, (WIN_WIDTH // 2 - 175), 500, 1),
                              Button(WORLD1_THUMBNAIL, (WIN_WIDTH // 2), 500, 2),
                              Button(WORLD1_THUMBNAIL, (WIN_WIDTH // 2 + 175), 500, 1)]

        self.update_world_buttons()



