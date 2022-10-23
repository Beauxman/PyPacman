import pygame as pg
from node import Point
from character import Character
import random

class Ghost(Character):
    def __init__(self, game, image, node, speed):
        super().__init__(game, image, node, speed)

        self.directionNext = "UP"

    def generateNextDirection(self): #VERY BASIC AI -- CHANGE LATER
        if random.randint(0, 2000) == 0:
            dirInt = random.randint(0, len(self.node.actions) - 1)
            self.directionNext = self.node.actions[dirInt]
        
    def update(self):
        self.generateNextDirection()
        self.nextDirection(self.directionNext, self.speed)
        self.draw()

