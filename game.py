import pygame as pg
import time
from settings import Settings
from maze import Maze
from node import Nodes
from character import Character
from player import Player
from ghost import Ghost
from menu import Menu
from sound import Sound
from scoreboard import Scoreboard
from fruit import Fruit
import game_functions as gf
import sys


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Pacman")

        self.lives = 2
        self.difficultyMulti = 0

        self.sound = Sound()
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

    def initializeAssets(self):
        self.maze = Maze(game=self)
        self.nodes = Nodes(game=self, mapStringFile="maze.txt")

        self.nodes.createNodes()
        self.speed = self.settings.player_speed

        self.pacman = Player(game=self, image="images/pacman0.png", node=self.nodes.nodeList[23][14], speed=self.speed)
        self.blinky = Ghost(game=self, image="images/blinky_right0.png", node=self.nodes.nodeList[13][14], speed=self.speed, type=0)
        self.pinky = Ghost(game=self, image="images/pinky_right0.png", node=self.nodes.nodeList[14][14], speed=self.speed, type=1)
        self.inky = Ghost(game=self, image="images/inky_right0.png", node=self.nodes.nodeList[14][13], speed=self.speed, type=2)
        self.clyde = Ghost(game=self, image="images/clyde_right0.png", node=self.nodes.nodeList[13][13], speed=self.speed, type=3)
        self.fruit = Fruit(game=self, node=self.nodes.nodeList[23][14])

    def reset(self):
        print('Resetting Game...')
        if self.lives > 0:
            self.lives -= 1
            self.initializeAssets()
            self.sound.play_startup()
            self.maze.update()
            self.nodes.update()
            self.pacman.update()
            self.blinky.update()
            self.pinky.update()
            self.inky.update()
            self.clyde.update()
            self.scoreboard.update()
            pg.display.flip()
            time.sleep(4)
        else:
            self.game_over()

    def change_highscore(self):
        if self.scoreboard.score > self.highscore:
            self.file = open(self.highscore_file, "w")
            self.file.write(str(self.scoreboard.score))
            self.file.close()
            print("New highscore added: " + str(self.scoreboard.score))

    def checkWinCondition(self):
        won = True
        for i in range(0, len(self.nodes.nodeList)):
            for node in self.nodes.nodeList[i]:
                if node.type == 1 or node.type == 3:
                    won = False
                    i = len(self.nodes.nodeList) - 1
                    break
        if won:
            self.lives += 1
            self.reset()
            self.difficultyMulti += 0.1
            self.blinky.speed += self.difficultyMulti
            self.pinky.speed += self.difficultyMulti
            self.inky.speed += self.difficultyMulti
            self.clyde.speed += self.difficultyMulti


    def game_over(self):
        print('Game Over!')
        self.change_highscore()
        pg.quit()
        sys.exit()

    def play(self):
        self.initializeAssets()
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
                self.scoreboard.update()
                self.fruit.update()
                self.checkWinCondition()
            pg.display.flip() 

def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()