import pygame
import json
from Components.Projectile import Projectile
from Components.Constants import WHITE, RED, WIN_HEIGHT, TILE_SIZE, BILL_WALKING_IMGS, SYRINGE_IMG

class Player:
    def __init__(self, world):
        self.lives = 3
        self.reset(world)

    def reset(self, world):
        self.world = world
        self.bullet_group = pygame.sprite.Group()
        self.syringe = SYRINGE_IMG
        self.syringe_img = self.syringe
        self.IMGS = BILL_WALKING_IMGS
        self.croching_IMGS = BILL_WALKING_IMGS
        self.image = self.IMGS[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.world.player_starting_x
        self.rect.y = self.world.player_starting_y
        self.syringe_rect = self.syringe.get_rect()
        self.animateCount = 0
        self.animateLoop = 3
        self.vel_y = 0
        self.vel_x = 5
        self.jumpForce = 0
        self.direction = 1
        self.bulletCount = 0
        self.shooting = False
        self.dead = False
        self.level_complete = False
        self.on_platform = False
        self.platform_vel = 0
        self.skills = {}
        self.load_skills()
        self.double_jump_enabled = False
        self.can_jump = True
        self.can_double_jump = self.skills["Double jump"]
        self.jump_pressed = False
        self.crouching = False
        self.trapped = False


    def load_skills(self):
        with open("Worlds/Player Skills.json", "r") as jsonFile:
            data = json.load(jsonFile)

        for key in data["Skills"]:
            result = data["Skills"][key] <= data["Current world"]
            self.skills[key] = result

    def update(self):
        dx = 0
        dy = 0
        self.update_counters()

        # Get key press
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.bulletCount == 0:
            if self.direction > 0:
                bullet = Projectile(self.rect.x + self.rect.width + self.syringe_rect.width, self.rect.y + 21, self.direction)
            else:
                bullet = Projectile(self.rect.x - self.syringe_rect.width, self.rect.y + 21, self.direction)
            self.bullet_group.add(bullet)
            self.shooting = True

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if not self.crouching:
                self.rect.top += 13
                self.rect.height = 29
            self.crouching = True
            if self.on_floor:
                self.vel_x = 2

        if not (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            if self.crouching:
                self.rect.top -= 13
                self.rect.height = 42
            self.crouching = False
            self.vel_x = 5

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and (self.can_jump or self.can_double_jump) and not self.jump_pressed and not self.crouching:
            if self.can_jump:
                # Implement jump, set can_jump to be false, set jump_pressed to True
                self.on_platform = False
                self.on_floor = False
                self.jumpForce += 1
                if self.jumpForce == 1:
                    self.vel_y = -10
                elif self.jumpForce < 5:
                    self.vel_y -= 2
                else:
                    self.can_jump = False
                    self.jump_pressed = True

            elif self.can_double_jump:
                # Implement jump set can_double_jump to be false and set jump_pressed to be true
                self.on_platform = False
                self.on_floor = False
                self.jumpForce -= 1
                if self.jumpForce == -1:
                    self.vel_y = -10
                elif self.jumpForce > -5:
                    self.vel_y -= 2
                else:
                    self.can_double_jump = False
                    self.jump_pressed = True

        if not (keys[pygame.K_UP] or keys[pygame.K_w]):
            if self.jumpForce > 0:
                self.can_jump = False
            if self.jumpForce < 0:
                self.can_double_jump = False
            self.jumpForce = 0
            self.jump_pressed = False

        if self.trapped:
            self.vel_x = 2

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += self.vel_x
            self.direction = 1
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= self.vel_x
            self.direction = -1

        # Add gravity
        dy = self.add_gravity(dy)

        # Check for tile collisions
        dx, dy = self.check_tile_collisions(dx, dy)

        # Check for platform collisions
        dx, dy = self.check_platform_collisions(dx, dy)

        # Check for collisions with enemies
        if pygame.sprite.spritecollide(self, self.world.enemy_group, False):
            self.dead = True

        # Check for collisions with covid
        if pygame.sprite.spritecollide(self, self.world.covid_group, False):
            self.dead = True

        # Check for collision with exit
        if pygame.sprite.spritecollide(self, self.world.exit_group, False) and len(self.world.enemy_group.sprites()) == 0:
            self.level_complete = True

        # Check for collision with life
        if pygame.sprite.spritecollide(self, self.world.life_group, True if self.lives < 3 else False):
            self.lives += 1
            if self.lives > 3:
                self.lives = 3

        # Check for collision with pressure pad
        for pad in self.world.pad_group:
            hit = pygame.sprite.spritecollide(self, self.world.pad_group, False)
            if hit:
                pad.apply()
            else:
                pad.reset()


        # Animate
        self.animate(dx, dy)

        # Update player pos
        self.rect.y += dy
        self.rect.x += dx

        # Update syringe pos
        self.update_syringe()

        # Update Bullets
        self.bullet_update()

    def draw(self, screen, camera):
        screen.blit(self.image, (self.rect.x - camera.offset.x, self.rect.y - camera.offset.y))
        screen.blit(self.syringe_img, (self.syringe_rect.x - camera.offset.x, self.syringe_rect.y - camera.offset.y ))
        for sprite in self.bullet_group:
            screen.blit(sprite.image, (sprite.rect.x - camera.offset.x, sprite.rect.y - camera.offset.y))

    def add_gravity(self, dy):
        if self.on_platform:
            new_dy = self.platform_vel
        else:
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
        self.on_floor = False
        self.on_ceiling = False
        self.trapped = False

        for tile in self.world.tiles:
            # check x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                # If on left side, move to left side
                if self.rect.centerx < tile[1].centerx:
                    new_dx = tile[1].left - self.rect.right

                # If on right side, move right
                if self.rect.centerx > tile[1].centerx:
                    new_dx = tile[1].right - self.rect.left

            # Check in y direction (include new_dx??)
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.vel_y < 0:
                    new_dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                    self.on_ceiling = True
                elif self.vel_y > 0:
                    if self.rect.top < tile[1].bottom and self.rect.top > tile[1].top:
                        self.on_ceiling = True
                    self.on_floor = True
                    new_dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.can_jump = True
                    self.can_double_jump = self.skills["Double jump"]

        if self.on_ceiling and self.on_floor:
            new_dx = dx
            new_dy = 0
            self.rect.top += 13
            self.rect.height = 29
            self.crouching = True
            self.vel_x = 2
            self.trapped = True


        return new_dx, new_dy


    def check_platform_collisions(self, dx, dy):
        new_dx = dx
        new_dy = dy
        col_thresh = 16
        self.on_platform = False

        for platform in self.world.platform_group:
            if platform.orientation == 1:
                # check x direction
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                    # Check if moving right
                    if dx > 0:
                        new_dx = platform.rect.left - self.rect.right
                    # Check if moving left
                    if dx < 0:
                        new_dx = platform.rect.right - self.rect.left
                    # Check if stationary
                    if dx == 0:
                        if platform.moveDirection > 0 and platform.previous_move_direction > 0:
                            new_dx = platform.rect.right - self.rect.left

                        elif platform.moveDirection < 0 and platform.previous_move_direction < 0:
                            new_dx = platform.rect.left - self.rect.right


                # # Check in y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                    #check if below platform
                    if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        new_dy = platform.rect.bottom - self.rect.top
                    # #check if above platform
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top
                        self.vel_y = 0
                        self.can_jump = True
                        self.can_double_jump = self.skills["Double jump"]
                        new_dy = 0
                        #move sideways with the platform
                        self.rect.x += platform.moveDirection * platform.vel

            elif platform.orientation == 2:
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy + 1, self.rect.width, self.rect.height):
                    #check if below platform
                    if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        new_dy = platform.rect.bottom - self.rect.top
                    # #check if above platform
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top
                        self.vel_y = 0
                        self.can_jump = True
                        self.can_double_jump = self.skills["Double jump"]
                        self.on_platform = True
                        self.platform_vel = platform.vel
                        new_dy = 0
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y + new_dy, self.rect.width, self.rect.height):
                    # Check if moving right
                    if dx > 0:
                        new_dx = platform.rect.left - self.rect.right
                    # Check if moving left
                    if dx < 0:
                        new_dx = platform.rect.right - self.rect.left

        return new_dx, new_dy

    def update_counters(self):
        # Update bullet timer
        if self.shooting:
            self.bulletCount += 1

            if self.bulletCount > 20 or len(self.bullet_group.sprites()) == 0:
                self.bulletCount = 0
                self.shooting = False

    def animate(self, dx, dy):
        index = 2
        # Update image
        if dx == 0 and dy == 0:
            self.image = self.IMGS[2]
        else:
            self.animateCount += 1
            if self.animateCount < self.animateLoop:
                index = 0
            elif self.animateCount < self.animateLoop * 2:
                index = 1
            elif self.animateCount < self.animateLoop * 3:
                index = 2
            elif self.animateCount < self.animateLoop * 4:
                index = 3
            elif self.animateCount < self.animateLoop * 5:
                index = 4
            elif self.animateCount < self.animateLoop * 6:
                index = 3
            elif self.animateCount < self.animateLoop * 7:
                index = 2
            elif self.animateCount < self.animateLoop * 8:
                index = 1
            else:
                index = 0
                self.animateCount = -1

        if self.direction == -1:
            self.image = pygame.transform.flip(self.IMGS[index], True, False)
        elif self.direction == 1:
            self.image = self.IMGS[index]

        if self.crouching:
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        else:
            self.image = self.image



    def bullet_update(self):
        self.bullet_group.update()

        for bullet in self.bullet_group:
            hit = pygame.sprite.spritecollide(bullet, self.world.enemy_group, True)
            if hit:
                bullet.kill()
                continue

            hit = pygame.sprite.spritecollide(bullet, self.world.platform_group, False)
            if hit:
                bullet.kill()
                continue

            for tile in self.world.tiles:
                if tile[1].colliderect(bullet.rect):
                    bullet.kill()
                    continue

    def update_syringe(self):
        # Update syringe pos
        if self.direction == 1:
            self.syringe_rect.x = self.rect.x + self.rect.width
            self.syringe_img = pygame.transform.flip(self.syringe, False, False)
        else:
            self.syringe_rect.x = self.rect.x - self.syringe_rect.width
            self.syringe_img = pygame.transform.flip(self.syringe, True, False)

        self.syringe_rect.y = self.rect.y + 18
