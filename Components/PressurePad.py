import pygame
from Components.Constants import PRESSURE_PAD_IMG, OUTER_BRICK_IMG, BRICK_TOP_IMG, BRICK_IMG, TILE_SIZE

class PressurePad(pygame.sprite.Sprite):
    def __init__(self, world, x, y, action_data):
        super().__init__()
        self.world = world
        self.image = PRESSURE_PAD_IMG
        self.rect = self.image.get_rect()
        self.starting_x = x
        self.starting_y = y
        self.rect.x = x
        self.rect.y = y
        self.action_data = action_data
        self.animateCount = 0
        self.animateLoop = 9
        self.animateDone = False
        self.actionDone = False


    def update(self):
        pass

    def apply(self):
        if not self.animateDone:
            self.animate()
        else:
            if not self.actionDone:
                self.action()

    def animate(self):
        self.animateCount += 1

        if self.animateCount < self.animateLoop:
            self.rect.y += 1
        else:
            self.animateDone = True

    def reset(self):
        if not self.actionDone:
            self.animateCount = 0
            self.animateDone = False
            self.rect.y = self.starting_y

    def action(self):
        # determine the method selected. call that one
        if self.action_data["Action"] == "Remove tile":
            self.remove_tile()
        elif self.action_data["Action"] == "Add tile":
            self.add_tile()
        elif self.action_data["Action"] == "Move platform":
            self.move_platform()

        self.actionDone = True

    def remove_tile(self):
        for tile in self.action_data["Tiles"]:
            self.world.tiles.pop(tile)

    def add_tile(self):
        for data in self.action_data["Tiles"]:
            elem = data["Elem"]
            col = data["Col"]
            row = data["Row"]

            if elem == 1:
                img_rect = OUTER_BRICK_IMG.get_rect()
                img_rect.x = col * TILE_SIZE
                img_rect.y = row * TILE_SIZE
                tile = (OUTER_BRICK_IMG, img_rect)
                self.world.tiles.append(tile)
            if elem == 2:
                img_rect = BRICK_IMG.get_rect()
                img_rect.x = col * TILE_SIZE
                img_rect.y = row * TILE_SIZE
                tile = (BRICK_IMG, img_rect)
                self.world.tiles.append(tile)
            if elem == 3:
                img_rect = BRICK_TOP_IMG.get_rect()
                img_rect.x = col * TILE_SIZE
                img_rect.y = row * TILE_SIZE
                tile = (BRICK_TOP_IMG, img_rect)
                self.world.tiles.append(tile)

    def move_platform(self):
        platform_list = self.world.platform_group.sprites()
        platform = platform_list[self.action_data["Platform index"]]
        platform.vel = self.action_data["Vel"]

