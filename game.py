import pygame as pg
from settings import Settings
from maze import Maze
from node import Nodes
from character import Character
from player import Player
from ghost import Ghost
from scoreboard import Scoreboard
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

        self.nodes.createNodes()
        self.speed = self.settings.player_speed

        self.pacman = Player(game=self, image="images/pacman0.png", node=self.nodes.nodeList[23][14], speed=self.speed)
        self.ghost1 = Ghost(game=self, image="images/blinky_right0.png", node=self.nodes.nodeList[14][14], speed=self.speed)

        self.scoreboard = Scoreboard(game=self)

    def reset(self):
        print('Resetting game...')

    def game_over(self):
        print('Game over!')
        pg.quit()
        sys.exit()

    def play(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            self.maze.update()
            self.nodes.update()
            self.pacman.update()
            self.ghost1.update()
            pg.display.flip() 

def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
