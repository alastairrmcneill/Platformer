import pygame
from Scenes.Manager import Manager
from Scenes.Splash import Splash
from Scenes.Intro import Intro
from Scenes.Game import Game
from Scenes.Win import Win
from Scenes.Lost import Lost
from Components.Constants import WIN_WIDTH, WIN_HEIGHT

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Platformer")

scene_dict = {"Splash": Splash(),
              "Intro": Intro(),
              "Game": Game(),
              "Win": Win(),
              "Lost": Lost ()}

starting_scene = "Splash"

def main():
    clock = pygame.time.Clock()
    running = True

    manager = Manager()
    manager.setup_scenes(scene_dict, starting_scene)

    while running:
        clock.tick(manager.FPS)

        if manager.scene.done:
            manager.swap_scenes()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            manager.scene.handle_event(event)

        manager.scene.update()
        manager.scene.draw(WIN)
        pygame.display.update()


if __name__ == "__main__":
    main()