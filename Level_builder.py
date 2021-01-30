import pygame

WIN = pygame.display.set_mode((800,600))
SCREEN = pygame.Surface((600,600))
CLOCK = pygame.time.Clock()

def get_row_col_from_pos(pos):


run = True
while run:
    CLOCK.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    SCREEN.fill((255,255,255))
    WIN.blit(SCREEN, (0,0))
    pygame.display.update()