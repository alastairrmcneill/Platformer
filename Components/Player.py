import pygame
from Components.Constants import WHITE, WIN_HEIGHT, TILE_SIZE

class Player:
    def __init__(self, world):
        self.world = world
        self.rect = pygame.rect.Rect(50, 50, 20, 60)
        self.vel_y = 0
        self.jumped = False
        self.jumpForce = 0

    def update(self):
        dx = 0
        dy = 0
        # Get key press
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumped:
            self.jumpForce += 1
            if self.jumpForce == 1:
                self.vel_y = -10
            elif self.jumpForce < 5:
                self.vel_y -= 2
            else:
                self.jumped = True
        if not keys[pygame.K_SPACE]:
            self.jumpForce = 0
            self.jumped = True

        if keys[pygame.K_RIGHT]:
            dx += 5
        if keys[pygame.K_LEFT]:
            dx -= 5

        # Add gravity
        dy = self.add_gravity(dy)

        # Check for tile collisions
        dx, dy = self.check_tile_collisions(dx, dy)


        # Check for collisions with lava
        if pygame.sprite.spritecollide(self, self.world.enemy_group, False):
            print("Hit enemy")

        # Check for collisions with enemies
        if pygame.sprite.spritecollide(self, self.world.lava_group, False):
            print("Hit lava")


        # Update pos
        self.rect.y += dy
        self.rect.x += dx

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

    def add_gravity(self, dy):
        old_dy = dy

        # Add Gravity
        self.vel_y += 1
        if self.vel_y > 15:
            self.vel_y = 15
        new_dy = old_dy + self.vel_y

        return new_dy

    def check_tile_collisions(self, dx, dy):
        new_dx = dx
        new_dy = dy

        for tile in self.world.tiles:
            # check x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                new_dx = 0

            # Check in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.vel_y < 0:
                    new_dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y > 0:
                    new_dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.jumped = False

        return new_dx, new_dy
