import pygame
from Components.Constants import LIFE_IMG

class Life(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = LIFE_IMG
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y