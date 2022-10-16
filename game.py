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
        self.nodes = Nodes(game=self, mapStringFile="maze.txt")

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

        ###### FOR TESTING #########
        x, y = 1, 5
        spot = self.nodes.nodeList[y][x]
        for item in spot.actions:
            print(item)

        ###########################
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.maze.update()
            pg.draw.circle(self.screen, (255, 0, 0), (spot.center.x, spot.center.y), 20) # FOR TESTING
            pg.draw.circle(self.screen, (0, 0, 255), (spot.adjacent[0].center.x, spot.adjacent[0].center.y), 20) # FOR TESTING
            pg.draw.circle(self.screen, (0, 255, 0), (spot.adjacent[2].center.x, spot.adjacent[2].center.y), 20) # FOR TESTING
            self.nodes.update()
            pg.display.flip() 

def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
