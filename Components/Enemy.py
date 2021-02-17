import pygame
from Components.Constants import REDHAT_IMGS

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, path):
        super().__init__()
        self.IMGS = REDHAT_IMGS
        self.image = self.IMGS[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.left = path[0]
        self.right = path[1]
        self.moveDirection = path[2]
        self.moveCount = 0

        self.animateCount = 0
        self.animateLoop = 3

        self.hurt_box = None
        self.update_hurt_box()

    def update(self):
        self.rect.x += self.moveDirection
        self.moveCount += self.moveDirection

        if self.moveCount > self.right:
            self.moveDirection *= -1
        elif self.moveCount < self.left:
            self.moveDirection *= -1

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

        self.update_hurt_box()


    def update_hurt_box(self):
        x = self.rect.x + 3
        y = self.rect.y
        width = self.rect.width - 6
        height = 5
        self.hurt_box = pygame.Rect(x, y, width, height)
