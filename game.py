import pygame as pg
from settings import Settings
from maze import Maze
from node import Nodes
import game_functions as gf
import sys


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Pacman")

        self.maze = Maze(game=self)
        self.nodes = Nodes(game=self, mapStringFile="mapstring.txt")

        self.settings.initialize_speed_settings()


    def reset(self):
        print('Resetting game...')

    def game_over(self):
        print('All ships gone: game over!')
        pg.quit()
        sys.exit()

    def play(self):
        running = True
        self.nodes.createNodes()
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.maze.update()
            self.nodes.update()
            pg.display.flip() 


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
