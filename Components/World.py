import pygame
import json
from Components.Covid import Covid
from Components.Enemy import Enemy
from Components.Exit import Exit
from Components.Constants import BRICK_IMG, BRICK_TOP_IMG, TILE_SIZE


class World:
    def __init__(self, level):
        self.level = level
        self.world_data = []
        self.player_starting_x = 0
        self.player_starting_y = 0
        self.load_level_data()
        self.tiles = []
        self.covid_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()

        row_count = 0
        for row in self.world_data:
            col_count = 0
            for elem in row:
                if elem == 1:
                    img_rect = BRICK_IMG.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (BRICK_IMG, img_rect)
                    self.tiles.append(tile)
                if elem == 2:
                    img_rect = BRICK_TOP_IMG.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (BRICK_TOP_IMG, img_rect)
                    self.tiles.append(tile)
                if elem == 3:
                    covid = Covid(col_count * TILE_SIZE, row_count * TILE_SIZE + 10)
                    self.covid_group.add(covid)
                if elem == 4:
                    path = self.enemy_paths.pop(0)
                    enemy = Enemy(col_count * TILE_SIZE + 2, row_count * TILE_SIZE - 12, path)
                    self.enemy_group.add(enemy)
                if elem == 5:
                    level_exit = Exit(col_count * TILE_SIZE, row_count * TILE_SIZE - 13)
                    self.exit_group.add(level_exit)
                col_count += 1
            row_count += 1

    def update(self):
        self.enemy_group.update()
        self.covid_group.update()


    def draw(self, screen):
        for tile in self.tiles:
            screen.blit(tile[0], tile[1])

        self.covid_group.draw(screen)
        self.enemy_group.draw(screen)
        self.exit_group.draw(screen)


    def load_level_data(self):
        with open("Components/Levels.json", "r") as jsonFile:
            data = json.load(jsonFile)


        for level in data["Levels"]:
            if level["Level"] == self.level:
                self.world_data = level["World Data"]
                self.enemy_paths = level["Enemy Walking Paths"]
                pos = level["Starting Position"]
                self.player_starting_x = pos[0]
                self.player_starting_y = pos[1]

