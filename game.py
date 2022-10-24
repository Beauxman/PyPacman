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
        self.blinky = Ghost(game=self, image="images/blinky_right0.png", node=self.nodes.nodeList[14][14], speed=self.speed, type=0)
        self.pinky = Ghost(game=self, image="images/pinky_right0.png", node=self.nodes.nodeList[15][14], speed=self.speed, type=1)
        self.inky = Ghost(game=self, image="images/inky_right0.png", node=self.nodes.nodeList[14][13], speed=self.speed, type=2)
        self.clyde = Ghost(game=self, image="images/clyde_right0.png", node=self.nodes.nodeList[14][13], speed=self.speed, type=3)

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
            self.blinky.update()
            self.pinky.update()
            self.inky.update()
            self.clyde.update()
            pg.display.flip() 

def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
