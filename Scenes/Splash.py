import pygame
from Scenes.Scene import Scene
from Components.Constants import WHITE, BLACK, SPLASH_IMG, SPLASH_WALKING_IMGS, EVIL_BILL

class Splash(Scene):
    def __init__(self):
        super().__init__()
        self.bg = SPLASH_IMG
        self.BILL_IMGS = SPLASH_WALKING_IMGS
        self.EVIL_BILL = pygame.transform.flip(EVIL_BILL, True, False)
        self.image = self.BILL_IMGS[0]
        self.rect = self.image.get_rect()
        self.rect.x = 620
        self.rect.y = 500

        self.moveDirection = -1

        self.animateCount = 0
        self.animateLoop = 5

        self.evilCount = 0

    def startup(self, persist):
        self.persist = persist

    def cleanup(self):
        self.done = False
        return self.persist

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.done = True
            self.next = "Intro"

    def update(self):
        if self.rect.x > 400:
            self.rect.x += self.moveDirection * 1

            self.animateCount += 1
            if self.animateCount < self.animateLoop:
                index = 0
            elif self.animateCount < self.animateLoop * 2:
                index = 1
            elif self.animateCount < self.animateLoop * 3:
                index = 2
            elif self.animateCount < self.animateLoop * 4:
                index = 3
            elif self.animateCount < self.animateLoop * 5:
                index = 4
            elif self.animateCount < self.animateLoop * 6:
                index = 3
            elif self.animateCount < self.animateLoop * 7:
                index = 2
            elif self.animateCount < self.animateLoop * 8:
                index = 1
            else:
                index = 0
                self.animateCount = -1

            if self.moveDirection == -1:
                self.image = pygame.transform.flip(self.BILL_IMGS[index], True, False)
        else:
            self.evilCount += 1
            if self.evilCount <= 20:
                self.image = pygame.transform.flip(self.BILL_IMGS[2], True, False)
            if self.evilCount > 20:
                self.image = self.EVIL_BILL
            if self.evilCount > 50:
                self.done = True
                self.next = "Intro"

    def draw(self, screen):
        screen.fill(BLACK)
        screen.blit(self.bg, (0,0))
        screen.blit(self.image, self.rect)