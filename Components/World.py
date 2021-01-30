import pygame
from Components.Lava import Lava
from Components.Enemy import Enemy
from Components.Exit import Exit
from Components.Constants import WORLD_DATA, DIRT_IMG, GRASS_IMG, TILE_SIZE


class World:
    def __init__(self, level):
        self.level = level
        self.tiles = []
        self.lava_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()

        row_count = 0
        for row in WORLD_DATA[self.level]:
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
                if elem == 3:
                    enemy = Enemy(col_count * TILE_SIZE + 2, row_count * TILE_SIZE - 17)
                    self.enemy_group.add(enemy)
                if elem == 6:
                    lava = Lava(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    self.lava_group.add(lava)
                if elem == 8:
                    level_exit = Exit(col_count * TILE_SIZE, row_count * TILE_SIZE - 13)
                    self.exit_group.add(level_exit)
                col_count += 1
            row_count += 1

    def update(self):
        self.enemy_group.update()
        self.lava_group.update()


    def draw(self, screen):
        for tile in self.tiles:
            screen.blit(tile[0], tile[1])

        self.lava_group.draw(screen)
        self.enemy_group.draw(screen)
        self.exit_group.draw(screen)