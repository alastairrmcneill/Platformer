import pygame
from Components.Constants import LAVA_IMG

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = LAVA_IMG
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

