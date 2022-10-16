import pygame as pg

class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

class Node:
    def __init__(self, game, center, adjacent, type):
        self.screen = game.screen
        self.center = center
        self.adjacent = adjacent
        self.type = type
        self.size = 5

    def update(self):
        self.draw()

    def draw(self):
        if self.type == 1:
            pg.draw.circle(self.screen, (255, 255, 255), (self.center.x, self.center.y), self.size)

class Nodes:
    def __init__(self, game, mapStringFile):
        self.game = game
        self.screen = game.screen
        self.nodeList, self.locations = list(), list()

        self.xOffset, self.yOffset = 45, 50
        self.xScale, self.yScale = 26.5, 23.4

        file = open(mapStringFile, 'r')
        lines = file.readlines()
        for line in lines:
            self.locations.append(line)
    
    def createNodes(self):
        curY = self.yOffset
        for i in range(0, len(self.locations)):
            curX = self.xOffset
            self.nodeList.append(list())
            for j in range(0, len(self.locations[i])):
                type = 0
                point = Point(x=curX, y=curY)
                adjacent = list()
                if self.locations[i][j] == "1":
                    if self.locations[i - 1][j] == "1":
                        adjacent.append("UP")
                    if self.locations[i + 1][j] == "1":
                        adjacent.append("DOWN")
                    if self.locations[i][j - 1] == "1":
                        adjacent.append("LEFT")
                    if self.locations[i][j + 1] == "1":
                        adjacent.append("RIGHT")
                    type = 1
                node = Node(game=self.game, center=point, adjacent=adjacent, type=type)
                self.nodeList[i].append(node)
                curX += self.xScale
            curY += self.yScale

    def update(self):
        self.draw()

    def draw(self):
        for row in range(0, len(self.nodeList)):
            for node in self.nodeList[row]:
                node.update()