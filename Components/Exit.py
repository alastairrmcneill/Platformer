import pygame
from Components.Constants import DOOR_IMG

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = DOOR_IMG
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y