import pygame as pg
from node import Point
import math

class Character:
    def __init__(self, game, image, node, speed):
        self.screen = game.screen
        self.settings = game.settings
        self.game = game
        self.image = pg.image.load(image)
        self.imageScalePx = 32
        self.image = pg.transform.scale(self.image, (self.imageScalePx, self.imageScalePx))
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()

        self.node = node
        self.rect.centerx, self.rect.centery = self.node.center.x, self.node.center.y
        self.center = Point(self.rect.centerx, self.rect.centery)

        self.speed = speed
        self.direction = None
        self.directionNext = None
        self.atNode = True
        self.nextNode = self.node

    def moveTowards(self, node, speed):
        self.atNode = False
        self.nextNode = node
        toX, toY = node.center.x, node.center.y
        rDistanceX, rDistanceY = toX - self.rect.centerx, toY - self.rect.centery
        sign = lambda x: math.copysign(1, x)

        distanceX, distanceY = toX - self.node.center.x, toY - self.node.center.y
        if distanceX != 0:
            self.center.x += sign(distanceX) * speed
        else:
            self.center.y += sign(distanceY) * speed

        if abs(rDistanceX) < abs(speed) and abs(rDistanceY) < abs(speed):
            self.rect.centerx, self.rect.centery = self.center.x, self.center.y = node.center.x, node.center.y
            self.node = node
            self.atNode = True

    def checkAction(self, action):
        for item in self.node.actions:
            if item == action:
                return True
        return False

    def moveDirection(self, direction, speed):
        if self.checkAction(direction):
            actionIndex = -1
            for i in range(len(self.node.actions)):
                if self.node.actions[i] == direction:
                    actionIndex = i

            if actionIndex > -1:
                self.moveTowards(self.node.adjacent[actionIndex], speed)

    def nextDirection(self, direction, speed):
        if self.direction == None or self.atNode:
            for item in self.node.actions:
                if item == direction:
                    self.direction = direction
                    self.adjustImageToDirection(direction)
        self.moveDirection(self.direction, speed)

    def changeImage(self, image):
        self.image = pg.image.load(image)
        self.image = pg.transform.scale(self.image, (self.imageScalePx, self.imageScalePx))
        self.rect = self.image.get_rect()

    def adjustImageToDirection(self, direction):
        pass

    def update(self):
        self.nextDirection(self.directionNext, self.speed)
        self.draw()

    def draw(self):
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y
        self.screen.blit(self.image, self.rect)