import pygame as pg
from settings import Settings
from maze import Maze
from node import Nodes
from character import Character
from player import Player
from ghost import Ghost
from menu import Menu
from sound import Sound
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

        self.sound = Sound()

        self.nodes.createNodes()
        self.speed = self.settings.player_speed

        self.pacman = Player(game=self, image="images/pacman0.png", node=self.nodes.nodeList[23][14], speed=self.speed)
        self.blinky = Ghost(game=self, image="images/blinky_right0.png", node=self.nodes.nodeList[14][14], speed=self.speed, type=0)
        self.pinky = Ghost(game=self, image="images/pinky_right0.png", node=self.nodes.nodeList[15][14], speed=self.speed, type=1)
        self.inky = Ghost(game=self, image="images/inky_right0.png", node=self.nodes.nodeList[14][13], speed=self.speed, type=2)
        self.clyde = Ghost(game=self, image="images/clyde_right0.png", node=self.nodes.nodeList[14][13], speed=self.speed, type=3)

        self.scoreboard = Scoreboard(game=self)

        self.highscore_file = "highscore.txt"
        self.file = open(self.highscore_file, "r")
        self.highscore = self.file.read()
        if self.highscore == "":
            self.file = open(self.highscore_file, "w")
            self.file.write("0")
            self.file.close()
            self.highscore = "0"
        self.highscore = int(self.highscore)

        self.menu = Menu(game=self)
        self.scene = 1
        self.sound.play_startup()

    def reset(self):
        print('Resetting game...')
    

    def change_highscore(self):
        if self.scoreboard.score > self.highscore:
            self.file = open(self.highscore_file, "w")
            self.file.write(str(self.scoreboard.score))
            self.file.close()
            print("New highscore added: " + str(self.scoreboard.score))
    

    def game_over(self):
        print('Game over!')
        self.change_highscore()
        self.sound.gameover()
        pg.quit()
        sys.exit()

    def play(self):
        running = True
        while running:
            self.screen.fill(self.settings.bg_color)

            if self.scene == 1:
                self.menu.update()
            elif self.scene == 2:
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