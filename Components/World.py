import pygame

from Components.Constants import WORLD_DATA, DIRT_IMG, GRASS_IMG, TILE_SIZE


class World:
    def __init__(self):
        self.tiles = []
        row_count = 0
        for row in WORLD_DATA:
            col_count = 0
            for elem in row:
                if elem == 1:
                    img_rect = DIRT_IMG.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (DIRT_IMG, img_rect)
                    self.tiles.append(tile)
                if elem == 2:
                    img_rect = GRASS_IMG.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (GRASS_IMG, img_rect)
                    self.tiles.append(tile)
                col_count += 1
            row_count += 1

    def update(self):
        pass


    def draw(self, screen):
        for tile in self.tiles:
            screen.blit(tile[0], tile[1])