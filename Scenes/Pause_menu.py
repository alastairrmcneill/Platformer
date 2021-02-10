import pygame
from Scenes.Scene import Scene
from Components.Button import Button
from Components.Constants import MENU_BUTTON_IMGS, RESTART_BUTTON_IMGS, RESUME_BUTTON_IMGS, WIN_HEIGHT

class Pause_menu(Scene):
    def __init__(self):
        super().__init__()
        self.buttons = [Button(RESUME_BUTTON_IMGS, 200, WIN_HEIGHT + 100, 1),
                        Button(RESTART_BUTTON_IMGS, 400, WIN_HEIGHT + 100, 2),
                        Button(MENU_BUTTON_IMGS, 300, WIN_HEIGHT + 245, 3)]
        self.animateCount = 0
        self.animate_done = False

    def startup(self, persist):
        self.persist = persist
        self.game = self.persist["Game"]

    def cleanup(self):
        self.done = False
        return self.persist

    def handle_event(self, event):
        keys = pygame.key.get_pressed()
        if self.animate_done:
            if keys[pygame.K_p]:
                self.done = True
                self.next = "Game"
                self.persist["State"] = "Continue"

        for button in self.buttons:
            button.run()
            if button.done:
                self.done = True
                if button.index == 1:
                    self.next = "Game"
                    self.persist["State"] = "Continue"
                elif button.index == 2:
                    self.next = "Game"
                    self.persist["State"] = "Restart"
                elif button.index == 3:
                    self.next = "Main menu"
                button.done = False
                button.clicked = False

    def update(self):
        self.animate_buttons()

    def draw(self, screen):
        self.game.draw(screen)
        for button in self.buttons:
            button.draw(screen)

    def animate_buttons(self):
        self.animateCount += 1
        if self.animateCount < 9:
            # Animate
            for button in self.buttons:
                button.rect.centery -= 50
        else:
            self.animate_done = True

