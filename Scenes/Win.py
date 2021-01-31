import pygame
from Scenes.Scene import Scene
from Components.Constants import WIN_IMG, EVIL_BILL, GOOD_BILL

class Win(Scene):
    def __init__(self):
        super().__init__()
        self.bg_img = WIN_IMG
        self.good_bill = pygame.transform.flip(GOOD_BILL, True, False)
        self.evil_bill = pygame.transform.flip(EVIL_BILL, True, False)
        self.image = self.good_bill
        self.evilCount = 0

    def startup(self, persist):
        self.persist = persist

    def cleanup(self):
        self.done = False
        return self.persist

    def handle_event(self, event):
        pass

    def update(self):
        self.evilCount += 1
        if self.evilCount <= 20:
            self.image = self.good_bill
        if self.evilCount > 20:
            self.image = self.evil_bill

    def draw(self, screen):
        screen.blit(self.bg_img, (0,0))
        screen.blit(self.image, (500,500))