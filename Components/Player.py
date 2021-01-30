import pygame
from Components.Projectile import Projectile
from Components.Constants import WHITE, WIN_HEIGHT, TILE_SIZE, BILL_WALKING_IMGS

class Player:
    def __init__(self, x, y, world):
        self.world = world
        self.bullet_group = pygame.sprite.Group()
        self.IMGS = BILL_WALKING_IMGS
        self.image = self.IMGS[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animateCount = 0
        self.animateLoop = 3
        self.vel_y = 0
        self.jumped = False
        self.jumpForce = 0
        self.direction = 1
        self.bulletCount = 0
        self.shooting = False
        self.dead = False
        self.level_complete = False

    def update(self):
        dx = 0
        dy = 0
        self.update_counters()
        # Get key press
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.bulletCount == 0:
            if self.direction > 0:
                bullet = Projectile(self.rect.x + self.rect.width, self.rect.y + 21, self.direction)
            else:
                bullet = Projectile(self.rect.x, self.rect.y + 21, self.direction)
            self.bullet_group.add(bullet)
            self.shooting = True

        if keys[pygame.K_UP] and not self.jumped:
            self.jumpForce += 1
            if self.jumpForce == 1:
                self.vel_y = -10
            elif self.jumpForce < 5:
                self.vel_y -= 2
            else:
                self.jumped = True
        if not keys[pygame.K_UP]:
            self.jumpForce = 0
            self.jumped = True

        if keys[pygame.K_RIGHT]:
            dx += 5
            self.direction = 1
        if keys[pygame.K_LEFT]:
            dx -= 5
            self.direction = -1

        # Add gravity
        dy = self.add_gravity(dy)

        # Check for tile collisions
        dx, dy = self.check_tile_collisions(dx, dy)

        # Check for collisions with enemies
        if pygame.sprite.spritecollide(self, self.world.enemy_group, False):
            self.dead = True

        # Check for collisions with lava
        if pygame.sprite.spritecollide(self, self.world.lava_group, False):
            self.dead = True

        # Check for collision with exit
        if pygame.sprite.spritecollide(self, self.world.exit_group, False) and len(self.world.enemy_group.sprites()) == 0:
            self.level_complete = True

        # Animate
        self.animate(dx, dy)

        # Update player pos
        self.rect.y += dy
        self.rect.x += dx

        # Update Bullets
        self.bullet_update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullet_group.draw(screen)

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

    def update_counters(self):
        # Update bullet timer
        if self.shooting:
            self.bulletCount += 1

            if self.bulletCount > 20 or len(self.bullet_group.sprites()) == 0:
                self.bulletCount = 0
                self.shooting = False

    def animate(self, dx, dy):
        index = 0
        # Update image
        if dx == 0 and dy == 0:
            self.image = self.IMGS[0]
        else:
            self.animateCount += 1
            if self.animateCount < self.animateLoop:
                index = 0
            elif self.animateCount < self.animateLoop * 2:
                index = 1
            elif self.animateCount < self.animateLoop * 3:
                index = 2
            elif self.animateCount < self.animateLoop * 4:
                index = 1
            else:
                index = 0
                self.animateCount = -1

        if self.direction == -1:
            self.image = pygame.transform.flip(self.IMGS[index], True, False)
        elif self.direction == 1:
            self.image = self.IMGS[index]


    def bullet_update(self):
        self.bullet_group.update()

        for bullet in self.bullet_group:
            hit = pygame.sprite.spritecollide(bullet, self.world.enemy_group, True)
            if hit:
                bullet.kill()
                continue

            for tile in self.world.tiles:
                if tile[1].colliderect(bullet.rect):
                    bullet.kill()
                    continue
