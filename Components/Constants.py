"""
Constants for the game
"""
import os
import pygame
pygame.font.init()

# Window variables
WIN_WIDTH = 600
WIN_HEIGHT = 600

# Game Constants
TILE_SIZE = 30


# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Paths
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
IMGS_PATH = os.path.join(BASE_PATH, "Imgs")
FONTS_PATH = os.path.join(BASE_PATH, "Fonts")

# Images
OUTER_BRICK_IMG = pygame.image.load(os.path.join(IMGS_PATH, "Bricks outline.png"))
BRICK_IMG = pygame.image.load(os.path.join(IMGS_PATH, "Bricks.png"))
BRICK_TOP_IMG = pygame.image.load(os.path.join(IMGS_PATH, "Bricks Top.png"))
LIFE_IMG = pygame.image.load(os.path.join(IMGS_PATH, "Mask.png"))


COVID_IMGS = [pygame.image.load(os.path.join(IMGS_PATH, "Covid 1.png")),
              pygame.image.load(os.path.join(IMGS_PATH, "Covid 2.png")),
              pygame.image.load(os.path.join(IMGS_PATH, "Covid 2.png")),
              pygame.image.load(os.path.join(IMGS_PATH, "Covid 3.png"))]

SPLASH_IMG = pygame.image.load(os.path.join(IMGS_PATH, "Splash Screen.png"))
SPLASH_WALKING_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_PATH, "Splash Walking 3.png"))),
                       pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_PATH, "Splash Walking 2.png"))),
                       pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_PATH, "Splash Walking 1.png"))),
                       pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_PATH, "Splash Walking 4.png"))),
                       pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_PATH, "Splash Walking 5.png")))]

EVIL_BILL = pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_PATH, "Evil Bill.png")))
GOOD_BILL = pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_PATH, "Good Bill.png")))
BG_IMG = pygame.image.load(os.path.join(IMGS_PATH, "Background.png"))

REDHAT_IMGS = [pygame.image.load(os.path.join(IMGS_PATH, "RedHat 1.png")),
               pygame.image.load(os.path.join(IMGS_PATH, "RedHat 2.png")),
               pygame.image.load(os.path.join(IMGS_PATH, "RedHat 3.png"))]

BILL_WALKING_IMGS = [pygame.image.load(os.path.join(IMGS_PATH, "Walking 3.png")),
                     pygame.image.load(os.path.join(IMGS_PATH, "Walking 2.png")),
                     pygame.image.load(os.path.join(IMGS_PATH, "Walking 1.png")),
                     pygame.image.load(os.path.join(IMGS_PATH, "Walking 4.png")),
                     pygame.image.load(os.path.join(IMGS_PATH, "Walking 5.png"))]

SYRINGE_IMG = pygame.image.load(os.path.join(IMGS_PATH, "Syringe Tip.png"))

BULLET_IMG = pygame.image.load(os.path.join(IMGS_PATH, "Bullet.png"))

DOOR_IMGS = [pygame.image.load(os.path.join(IMGS_PATH, "Door off.png")),
             pygame.image.load(os.path.join(IMGS_PATH, "Door open.png"))]

WIN_IMG = pygame.image.load(os.path.join(IMGS_PATH, "Win.png"))
GAME_OVER_IMG = pygame.image.load(os.path.join(IMGS_PATH, "Game over.png"))
# Fonts

