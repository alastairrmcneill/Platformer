import pygame

# Variables
WIN = pygame.display.set_mode((800,600))
SCREEN = pygame.Surface((600,600))
CLOCK = pygame.time.Clock()
ROWS = 40
COLS = 40
TILE_SIZE = 600 // ROWS
WORLD = [[0 for j in range(COLS)] for i in range(ROWS)]

# IMGS
SAVE = pygame.image.load("Imgs/Save.png")
OUTER_BRICKS = pygame.transform.scale(pygame.image.load("Imgs/Bricks outline.png"), (TILE_SIZE, TILE_SIZE))
BRICKS = pygame.transform.scale(pygame.image.load("Imgs/Bricks.png"), (TILE_SIZE, TILE_SIZE))
BRICKS_TOP = pygame.transform.scale(pygame.image.load("Imgs/Bricks top.png"), (TILE_SIZE, TILE_SIZE))
COVID = pygame.transform.scale(pygame.image.load("Imgs/Covid 1.png"), (TILE_SIZE, int(TILE_SIZE * (2/3))))
ENEMY = pygame.transform.scale(pygame.image.load("Imgs/RedHat 1.png"), (int(TILE_SIZE * (4/5)), int(TILE_SIZE * (7/5))))
EXIT = pygame.transform.scale(pygame.image.load("Imgs/Door closed.png"), (TILE_SIZE, TILE_SIZE *2))
PLATFORM = pygame.transform.scale(pygame.image.load("Imgs/Platform.png"), (TILE_SIZE, int(TILE_SIZE * (2/3))))


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
                screen.blit(COVID, (x, y + int(TILE_SIZE / 3)))
            if elem == 5:
                screen.blit(ENEMY, (x, y - int(TILE_SIZE * (2/5))))
            if elem == 6:
                screen.blit(EXIT, (x, y - TILE_SIZE))
            if elem == 7:
                screen.blit(PLATFORM, (x, y))

def save_world(world):
    f = open("Worlds/RAW_DATA.txt", "a")
    text = ""
    text += "["
    for row in world:
        text += "["
        for elem in row:
            text += str(elem) + ","
        text = text[:-1]
        text += "], \n"
    text = text[:-3]
    text += "] \n \n"

    f.write(text)
    f.close()


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
                    if WORLD[row][col] > 7:
                        WORLD[row][col] = 0

        if save_buton.draw():
            run = False
            save_world(WORLD)

        draw_world(SCREEN, WORLD)
        WIN.blit(SCREEN, (0,0))
        pygame.display.update()

main()