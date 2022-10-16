import pygame as pg

class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

class Node:
    def __init__(self, game, center, actions, type):
        self.screen = game.screen
        self.center = center
        self.actions = actions
        self.adjacent = list()
        self.type = type

        self.size = 1
        if type == 1:
            self.size = 5
        elif type == 3:
            self.size = 10

    def __repr__(self):
        return "[NODE]: x = " + str(self.center.x) + ", y = " + str(self.center.y) + ", type = " + str(self.type)

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
                actions = list()
                if self.locations[i][j] != "0":
                    if self.locations[i - 1][j] != "0":
                        actions.append("UP")
                    if self.locations[i + 1][j] != "0":
                        actions.append("DOWN")
                    if self.locations[i][j - 1] != "0":
                        actions.append("LEFT")
                    if self.locations[i][j + 1] != "0":
                        actions.append("RIGHT")
                node = Node(game=self.game, center=point, actions=actions, type=type)
                self.nodeList[i].append(node)
                curX += self.xScale
            curY += self.yScale

        for i in range(0, len(self.nodeList) - 1):
            for j in range(0, len(self.nodeList[i]) - 1):
                node = self.nodeList[i][j]
                if node.type != 0:
                    if "UP" in node.actions:
                        node.adjacent.append(self.nodeList[i - 1][j])
                    if "DOWN" in node.actions:
                        node.adjacent.append(self.nodeList[i + 1][j])
                    if "LEFT" in node.actions:
                        node.adjacent.append(self.nodeList[i][j - 1])
                    if "RIGHT" in node.actions:
                        node.adjacent.append(self.nodeList[i][j + 1])

    def update(self):
        self.draw()

    def draw(self):
        for i in range(0, len(self.nodeList)):
            for node in self.nodeList[i]:
                    node.update()