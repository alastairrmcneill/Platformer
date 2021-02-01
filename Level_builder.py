import pygame

# Variables
WIN = pygame.display.set_mode((800,600))
SCREEN = pygame.Surface((600,600))
CLOCK = pygame.time.Clock()
ROWS = 20
COLS = 20
TILE_SIZE = 600 // ROWS
WORLD = [[0 for j in range(COLS)] for i in range(ROWS)]

# IMGS
SAVE = pygame.image.load("Imgs/Save.png")
OUTER_BRICKS = pygame.image.load("Imgs/Bricks outline.png")
BRICKS = pygame.image.load("Imgs/Bricks.png")
BRICKS_TOP = pygame.image.load("Imgs/Bricks top.png")
COVID = pygame.image.load("Imgs/Covid 1.png")
ENEMY = pygame.image.load("Imgs/RedHat 1.png")
EXIT = pygame.image.load("Imgs/Door.png")


# Button
class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		#draw button
		WIN.blit(self.image, self.rect)

		return action


def get_row_col_from_pos(pos):
    row = pos[1] // TILE_SIZE
    col = pos[0] // TILE_SIZE

    return row, col

def draw_world(screen, world):
    screen.fill((255, 255, 255))

    for i in range(len(world)):
        for j in range(len(world[0])):
            x = j * TILE_SIZE
            y = i * TILE_SIZE

            elem = world[i][j]

            if elem == 0:
                pass
            if elem == 1:
                screen.blit(OUTER_BRICKS, (x, y))
            if elem == 2:
                screen.blit(BRICKS, (x, y))
            if elem == 3:
                screen.blit(BRICKS_TOP, (x, y))
            if elem == 4:
                screen.blit(COVID, (x, y + 10))
            if elem == 5:
                screen.blit(ENEMY, (x, y - 12))
            if elem == 6:
                screen.blit(EXIT, (x, y - 13))

def main():
    run = True
    save_buton = Button(650, 100, SAVE)
    while run:
        CLOCK.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] < 600:
                    row, col = get_row_col_from_pos(pos)

                    WORLD[row][col] += 1
                    if WORLD[row][col] > 6:
                        WORLD[row][col] = 0

        if save_buton.draw():
            run = False
            print(WORLD)

        draw_world(SCREEN, WORLD)
        WIN.blit(SCREEN, (0,0))
        pygame.display.update()

main()