import pygame
import json
from Components.Covid import Covid
from Components.Enemy import Enemy
from Components.Exit import Exit
from Components.Platform import Platform
from Components.Life import Life
from Components.PressurePad import PressurePad
from Components.Constants import OUTER_BRICK_IMG, BRICK_IMG, BRICK_TOP_IMG, TILE_SIZE


class World:
    def __init__(self, world_num, level):
        self.level = level
        self.world_data = []
        self.player_starting_x = 0
        self.player_starting_y = 0
        self.load_level_data(world_num)
        if self.world_data != []:
            self.width = len(self.world_data[0]) * TILE_SIZE
            self.height = len(self.world_data) * TILE_SIZE
        else:
            self.width = 0
            self.height = 0


        self.tiles = []
        self.covid_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()
        self.life_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        self.pad_group = pygame.sprite.Group()

        row_count = 0
        for row in self.world_data:
            col_count = 0
            for elem in row:
                if elem == 1:
                    img_rect = OUTER_BRICK_IMG.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (OUTER_BRICK_IMG, img_rect)
                    self.tiles.append(tile)
                if elem == 2:
                    img_rect = BRICK_IMG.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (BRICK_IMG, img_rect)
                    self.tiles.append(tile)
                if elem == 3:
                    img_rect = BRICK_TOP_IMG.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (BRICK_TOP_IMG, img_rect)
                    self.tiles.append(tile)
                if elem == 4:
                    covid = Covid(col_count * TILE_SIZE, row_count * TILE_SIZE + 10)
                    self.covid_group.add(covid)
                if elem == 5:
                    path = self.enemy_paths.pop(0)
                    enemy = Enemy(col_count * TILE_SIZE + 2, row_count * TILE_SIZE - 12, path)
                    self.enemy_group.add(enemy)
                if elem == 6:
                    level_exit = Exit(col_count * TILE_SIZE, row_count * TILE_SIZE - 30)
                    self.exit_group.add(level_exit)
                if elem == 7:
                    path = self.platform_paths.pop(0)
                    platform = Platform(col_count * TILE_SIZE, row_count * TILE_SIZE, path)
                    self.platform_group.add(platform)
                if elem == 8:
                    life = Life(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    self.life_group.add(life)
                if elem == 9:
                    pad = PressurePad(col_count * TILE_SIZE + 4, row_count * TILE_SIZE + 21)
                    self.pad_group.add(pad)
                col_count += 1
            row_count += 1

    def update(self):
        self.enemy_group.update()
        self.covid_group.update()
        self.platform_group.update()

        if len(self.enemy_group.sprites()) == 0:
            self.exit_group.update()


    def draw(self, screen, camera):

        for sprite in self.pad_group:
            screen.blit(sprite.image, (sprite.rect.x - camera.offset.x, sprite.rect.y - camera.offset.y))
        for tile in self.tiles:
            x = tile[1].x
            y = tile[1].y
            screen.blit(tile[0], (x - camera.offset.x, y - camera.offset.y))

        for sprite in self.covid_group:
            screen.blit(sprite.image, (sprite.rect.x - camera.offset.x, sprite.rect.y - camera.offset.y))
        for sprite in self.enemy_group:
            screen.blit(sprite.image, (sprite.rect.x - camera.offset.x, sprite.rect.y - camera.offset.y))
        for sprite in self.exit_group:
            screen.blit(sprite.image, (sprite.rect.x - camera.offset.x, sprite.rect.y - camera.offset.y))
        for sprite in self.platform_group:
            screen.blit(sprite.image, (sprite.rect.x - camera.offset.x, sprite.rect.y - camera.offset.y))
        for sprite in self.life_group:
            screen.blit(sprite.image, (sprite.rect.x - camera.offset.x, sprite.rect.y - camera.offset.y))

    def load_level_data(self, world_num):
        with open(f"Worlds/World {world_num}.json", "r") as jsonFile:
            data = json.load(jsonFile)


        for level in data["Levels"]:
            if level["Level"] == self.level:
                self.world_data = level["World Data"]
                self.enemy_paths = level["Enemy Walking Paths"]
                self.platform_paths = level["Platform Movement Paths"]
                pos = level["Starting Position"]
                self.player_starting_x = pos[0]
                self.player_starting_y = pos[1]

