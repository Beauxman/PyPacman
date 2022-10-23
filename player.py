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

    def checkCollisions(self):
        toX, toY = self.nextNode.center.x, self.nextNode.center.y
        rDistanceX, rDistanceY = toX - self.rect.centerx, toY - self.rect.centery
        if rDistanceX <= self.nextNode.size / 2 or rDistanceY <= self.nextNode.size / 2:
            if self.nextNode.type == 3:
                pass
                #CONSUME FRUIT FUNCTION HERE
            self.nextNode.type = 0

    def checkInput(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.directionNext = "UP"
        if keys[pg.K_DOWN]:
            self.directionNext = "DOWN"
        if keys[pg.K_LEFT]:
            self.directionNext = "LEFT"
        if keys[pg.K_RIGHT]:
            self.directionNext = "RIGHT"

    def update(self):
        self.checkInput()
        self.checkCollisions()
        self.nextDirection(self.directionNext, self.speed)
        self.draw()
