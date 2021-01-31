import pygame
from Components.Constants import COVID_IMGS

class Covid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.IMGS = COVID_IMGS
        self.image = self.IMGS[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animateCount = 0
        self.animateLoop = 5


    def update(self):
        self.animateCount += 1

        if self.animateCount < self.animateLoop:
            self.image= self.IMGS[0]
        elif self.animateCount < self.animateLoop * 2:
            self.image = self.IMGS[1]
        elif self.animateCount < self.animateLoop * 3:
            self.image = self.IMGS[2]
        elif self.animateCount < self.animateLoop * 4:
            self.image = self.IMGS[3]
        elif self.animateCount < self.animateLoop * 5:
            self.image = self.IMGS[2]
        elif self.animateCount < self.animateLoop * 6:
            self.image = self.IMGS[1]
        else:
            self.image = self.IMGS[0]
            self.animateCount = 0

