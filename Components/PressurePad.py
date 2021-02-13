import pygame
from Components.Constants import PRESSURE_PAD_IMG

class PressurePad(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = PRESSURE_PAD_IMG
        self.rect = self.image.get_rect()
        self.starting_x = x
        self.starting_y = y
        self.rect.x = x
        self.rect.y = y
        self.animateCount = 0
        self.animateLoop = 9
        self.animateDone = False
        self.actionDone = False

    def update(self):
        pass

    def apply(self):
        if not self.animateDone:
            self.animate()
        else:
            if not self.actionDone:
                self.action()

    def animate(self):
        self.animateCount += 1

        if self.animateCount < self.animateLoop:
            self.rect.y += 1
        else:
            self.animateDone = True

    def reset(self):
        if not self.actionDone:
            self.animateCount = 0
            self.animateDone = False
            self.rect.y = self.starting_y

    def action(self):
        # determine the method selected. call that one
        self.actionDone = True