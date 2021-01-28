import pygame
from Components.Constants import WHITE, WIN_HEIGHT, TILE_SIZE

class Player:
    def __init__(self, world):
        self.world = world
        self.rect = pygame.rect.Rect(50, 50, 20, 60)
        self.vel_y = 0
        self.jumped = False
        self.jumpCount = 0

    def update(self):
        dx = 0
        dy = 0
        # Get key press
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumped:
            self.jumpCount += 1
            if self.jumpCount == 1:
                self.vel_y = -10
            elif self.jumpCount < 5:
                self.vel_y -= 2
            else:
                self.jumped = True
        if not keys[pygame.K_SPACE]:
            self.jumpCount = 0
            self.jumped = True

        if keys[pygame.K_RIGHT]:
            dx += 5
        if keys[pygame.K_LEFT]:
            dx -= 5

        # Add Gravity
        self.vel_y += 1
        if self.vel_y > 15:
            self.vel_y = 15
        dy += self.vel_y

        # Check for collisions
        for tile in self.world.tiles:
            # check x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0

            # Check in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.jumped = False


        # Update pos
        self.rect.y += dy
        self.rect.x += dx

        if self.rect.bottom > WIN_HEIGHT - TILE_SIZE:
            self.rect.bottom = WIN_HEIGHT - TILE_SIZE
            dy = 0
            self.jumped = False


    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

