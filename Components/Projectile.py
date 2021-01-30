import pygame
from Components.Constants import BULLET_IMG

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = BULLET_IMG
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 6
        self.direction = direction
        if self.direction == 1:
            self.rect.x -= self.vel
        self.lifeCount = 0


    def update(self):
        self.lifeCount += 1
        if self.lifeCount == 30:
            self.kill()

        self.rect.x += self.direction * self.vel




