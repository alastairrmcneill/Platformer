import pygame
from Scenes.Scene import Scene
from Components.Button import Button
from Components.Constants import GAME_OVER_IMG, BLACK, WIN_WIDTH, WIN_HEIGHT, WORLD1_THUMBNAIL, MENU_BG_IMG

pygame.font.init()

class Main_menu(Scene):
    def __init__(self):
        super().__init__()
        self.bg = MENU_BG_IMG
        self.world_buttons = []
        self.world_buttons_setup()


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
                self.done = True
                self.next = "Game"
                self.world = button.index
                button.done = False
                button.clicked = False

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.bg, (0,0))
        for button in self.world_buttons:
            button.draw(screen)


    def world_buttons_setup(self):
        self.world_buttons.append(Button(WORLD1_THUMBNAIL, (WIN_WIDTH // 2 - 175), 500, 1))
        self.world_buttons.append(Button(WORLD1_THUMBNAIL, (WIN_WIDTH // 2), 500, 2))
        self.world_buttons.append(Button(WORLD1_THUMBNAIL, (WIN_WIDTH // 2 + 175), 500, 1))


