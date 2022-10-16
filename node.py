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

        self.size = 1
        if type == 1:
            self.size = 5
        elif type == 3:
            self.size = 10

    def update(self):
        self.draw()

    def draw(self):
        if self.type != 0:# and self.type != 2: #NOTE COMMENTED OUT FOR SHOWING OTHERWISE INVISIBLE NODES
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
            for j in range(0, len(self.locations[i]) - 1):
                type = int(self.locations[i][j])
                point = Point(x=curX, y=curY)
                adjacent = list()
                if self.locations[i][j] != "0":
                    if self.locations[i - 1][j] != "0":
                        adjacent.append("UP")
                    if self.locations[i + 1][j] != "0":
                        adjacent.append("DOWN")
                    if self.locations[i][j - 1] != "0":
                        adjacent.append("LEFT")
                    if self.locations[i][j + 1] != "0":
                        adjacent.append("RIGHT")
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