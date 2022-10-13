import pygame as pg
from settings import Settings
from maze import Maze
import game_functions as gf
import sys


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Pacman")

        self.maze = Maze(game=self)

        self.settings.initialize_speed_settings()


    def reset(self):
        print('Resetting game...')

    def game_over(self):
        print('All ships gone: game over!')
        pg.quit()
        sys.exit()

    def play(self):
        running = True
        while running:     # at the moment, only exits in gf.check_events if Ctrl/Cmd-Q pressed
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.maze.update()
            pg.display.flip() 


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
