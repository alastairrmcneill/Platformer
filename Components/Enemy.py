import pygame
from Components.Constants import ENEMY_IMG

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = ENEMY_IMG
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.moveDirection = 1
        self.moveCount = 0

    def update(self):
        self.rect.x += self.moveDirection
        self.moveCount += 1

        if abs(self.moveCount) == 50:
            self.moveDirection *= -1
            self.moveCount *= -1



