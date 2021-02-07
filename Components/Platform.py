import pygame
from Components.Constants import PLATFORM_IMG

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, path):
        super().__init__()
        self.image = PLATFORM_IMG
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.left = path[0]
        self.right = path[1]
        self.moveDirection = path[2]
        self.orientation = path[3]
        self.moveCount = 0

        self.animateCount = 0
        self.animateLoop = 3

        self.previous_move_direction = self.moveDirection

    def update(self):
        if self.orientation == 1:
            self.rect.x += self.moveDirection
        else:
            self.rect.y += self.moveDirection

        self.moveCount += self.moveDirection

        self.previous_move_direction = self.moveDirection

        if self.moveCount > self.right:
            self.moveDirection *= -1
        elif self.moveCount < self.left:
            self.moveDirection *= -1












