import pygame
import random
from Scenes.Scene import Scene
from Components.Constants import WIN_IMG, EVIL_BILL, GOOD_BILL, WHITE

pygame.font.init()

class Win(Scene):
    def __init__(self):
        super().__init__()
        self.bg_img = WIN_IMG
        self.good_bill = pygame.transform.flip(GOOD_BILL, True, False)
        self.evil_bill = pygame.transform.flip(EVIL_BILL, True, False)
        self.image = self.good_bill
        self.evilCount = 0
        self.font = pygame.font.Font("Fonts/FFFFORWA.TTF", 16)
        self.rand = random.randint(3, 10)

    def startup(self, persist):
        self.persist = persist
        self.game_time = self.persist["Game time"]

    def cleanup(self):
        self.done = False
        return self.persist

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.done = True
            self.next = "Intro"

    def update(self):
        self.evilCount += 1
        if self.evilCount <= 20:
            self.image = self.good_bill
        if self.evilCount > 20:
            self.image = self.evil_bill

    def draw(self, screen):
        screen.blit(self.bg_img, (0,0))
        screen.blit(self.image, (500,500))
        self.draw_time(screen)

    def draw_time(self, screen):
        time = self.format_time()
        text = self.font.render(time, True, WHITE)
        rect = text.get_rect(midleft = (187, 356))
        screen.blit(text, rect)

        time = self.format_Jeff_time()
        text = self.font.render(time, True, WHITE)
        rect = text.get_rect(midleft = (442, 406))
        screen.blit(text, rect)

    def format_time(self):
        hours = self.game_time.total_seconds() // 3600
        minutes = (self.game_time.total_seconds() % 3600) // 60
        seconds = (self.game_time.total_seconds() % 3600) % 60

        string = ""
        if hours > 0:
            string += str(int(hours)) + ":"
        if minutes == 0:
            string += "00:"
        elif minutes < 10:
            string += "0" + str(int(minutes)) + ":"
        else:
            string += str(int(minutes)) + ":"

        if seconds == 0:
            string += "00:"
        elif seconds < 10:
            string += "0" + str(int(seconds))
        else:
            string += str(int(seconds))

        return string


    def format_Jeff_time(self):
        total_seconds = self.game_time.total_seconds() - self.rand
        hours = total_seconds// 3600
        minutes = (total_seconds % 3600) // 60
        seconds = (total_seconds % 3600) % 60

        string = ""
        if hours > 0:
            string += str(int(hours)) + ":"
        if minutes == 0:
            string += "00:"
        elif minutes < 10:
            string += "0" + str(int(minutes)) + ":"
        else:
            string += str(int(minutes)) + ":"

        if seconds == 0:
            string += "00:"
        elif seconds < 10:
            string += "0" + str(int(seconds))
        else:
            string += str(int(seconds))

        return string
