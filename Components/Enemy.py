import pygame
from Components.Constants import REDHAT_IMGS

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.IMGS = REDHAT_IMGS
        self.image = self.IMGS[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.moveDirection = 1
        self.moveCount = 0

        self.animateCount = 0
        self.animateLoop = 3

    def update(self):
        self.rect.x += self.moveDirection
        self.moveCount += 1

        if abs(self.moveCount) == 50:
            self.moveDirection *= -1
            self.moveCount *= -1

        self.animateCount += 1
        if self.animateCount < self.animateLoop:
            index = 0
        elif self.animateCount < self.animateLoop * 2:
            index = 1
        elif self.animateCount < self.animateLoop * 3:
            index = 2
        elif self.animateCount < self.animateLoop * 4:
            index = 1
        else:
            index = 0
            self.animateCount = -1

        if self.moveDirection == -1:
            self.image = pygame.transform.flip(self.IMGS[index], True, False)
        elif self.moveDirection == 1:
            self.image = self.IMGS[index]












