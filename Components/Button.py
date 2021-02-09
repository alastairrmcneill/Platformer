import pygame

class Button:
    def __init__(self, images, x, y, index = 0):
        self.inactive_image = images[0]
        self.active_image = images[1]
        self.pressed_image = images[2]
        self.image = self.inactive_image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.index = index
        self.clicked = False
        self.done = False
        self.hide = False

    def run(self):
        self.image = self.inactive_image

        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            self.image = self.active_image
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.image = self.pressed_image
                self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                if self.clicked:
                    self.done = True
        else:
            self.clicked = False


    def draw(self, screen):
        if not self.hide:
            screen.blit(self.image, self.rect)


    def update(self, images):
        self.inactive_image = images[0]
        self.active_image = images[1]
        self.pressed_image = images[2]
        self.image = self.inactive_image

