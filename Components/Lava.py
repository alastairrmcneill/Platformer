import pygame
from Components.Constants import LAVA_IMGS

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.IMGS = LAVA_IMGS
        self.image = self.IMGS[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animateCount = 0
        self.animateLoop = 10


    def update(self):
        self.animateCount += 1

        if self.animateCount < self.animateLoop:
            self.image= self.IMGS[0]
        elif self.animateCount < self.animateLoop * 2:
            self.image = self.IMGS[1]
        else:
            self.image = self.IMGS[0]
            self.animateCount = 0

