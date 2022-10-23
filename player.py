import pygame as pg
from node import Point
from character import Character

class Player(Character):
    def __init__(self, game, image, node, speed):
        super().__init__(game, image, node, speed)

    def adjustImageToDirection(self, direction):
        if self.atNode and self.directionNext != None:
            if direction == "UP" or direction == None:
                self.changeImage("images/pacman0.png")
            elif direction == "DOWN":
                self.changeImage("images/pacman1.png")
            elif direction == "LEFT":
                self.changeImage("images/pacman2.png")
            elif direction == "RIGHT":
                self.changeImage("images/pacman3.png")

