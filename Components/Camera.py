import pygame
from Components.Constants import WIN_WIDTH, WIN_HEIGHT

vec = pygame.math.Vector2

class Camera:
    def __init__(self, player):
        self.reset(player)

    def reset(self, player):
        self.player = player
        self.offset = vec(0,0)
        self.offset_float = vec(0,0)
        self.display_width = WIN_WIDTH
        self.display_height = WIN_HEIGHT
        self.constant = vec(-(self.display_width // 2 - self.player.rect.width // 2) ,-(self.display_height // 2 - self.player.rect.height // 2))
        self.border = (0, player.world.width, 0, player.world.height)

    def scroll(self):
        self.offset_float.x += (self.player.rect.x - self.offset_float.x + self.constant.x) * 0.1
        self.offset_float.y += (self.player.rect.y - self.offset_float.y + self.constant.y) * 0.1

        self.offset.x = int(self.offset_float.x)
        self.offset.y = int(self.offset_float.y)

        self.offset.x = max(self.border[0], self.offset.x)
        self.offset.x = min(self.offset.x, self.border[1] - self.display_width)

        self.offset.y = max(self.border[2], self.offset.y)
        self.offset.y = min(self.offset.y, self.border[3] - self.display_height)