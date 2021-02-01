import pygame
from Components.Constants import DOOR_IMGS

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imgs = DOOR_IMGS
        self.image = self.imgs[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = self.imgs[1]