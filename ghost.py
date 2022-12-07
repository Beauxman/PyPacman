import pygame as pg
from node import Point
from character import Character
import random
import math
from timer import Timer

class Ghost(Character):
    # initializing sprites for binky
    blinky_right = [pg.transform.scale(pg.image.load(f'images/blinky_right{n}.png'), (32, 32)) for n in range(2)]
    blinky_left = [pg.transform.flip(n, True, False) for n in blinky_right]
    blinky_up = [pg.transform.scale(pg.image.load(f'images/blinky_up{n}.png'), (32, 32)) for n in range(2)]
    blinky_down = [pg.transform.scale(pg.image.load(f'images/blinky_down{n}.png'), (32, 32)) for n in range(2)]

    # initializing sprites for pinky
    pinky_right = [pg.transform.scale(pg.image.load(f'images/pinky_right{n}.png'), (32, 32)) for n in range(2)]
    pinky_left = [pg.transform.flip(n, True, False) for n in pinky_right]
    pinky_up = [pg.transform.scale(pg.image.load(f'images/pinky_up{n}.png'), (32, 32)) for n in range(2)]
    pinky_down = [pg.transform.scale(pg.image.load(f'images/pinky_down{n}.png'), (32, 32)) for n in range(2)]

    # initializing sprites for inky
    inky_right = [pg.transform.scale(pg.image.load(f'images/inky_right{n}.png'), (32, 32)) for n in range(2)]
    inky_left = [pg.transform.flip(n, True, False) for n in inky_right]
    inky_up = [pg.transform.scale(pg.image.load(f'images/inky_up{n}.png'), (32, 32)) for n in range(2)]
    inky_down = [pg.transform.scale(pg.image.load(f'images/inky_down{n}.png'), (32, 32)) for n in range(2)]

    # initializing sprites for clyde
    clyde_right = [pg.transform.scale(pg.image.load(f'images/clyde_right{n}.png'), (32, 32)) for n in range(2)]
    clyde_left = [pg.transform.flip(n, True, False) for n in clyde_right]
    clyde_up = [pg.transform.scale(pg.image.load(f'images/clyde_up{n}.png'), (32, 32)) for n in range(2)]
    clyde_down = [pg.transform.scale(pg.image.load(f'images/clyde_down{n}.png'), (32, 32)) for n in range(2)]

    # initializing other sprites
    ghost_scared_images = [pg.transform.scale(pg.image.load(f'images/ghost_scared{n}.png'), (32, 32)) for n in range(2)]
    ghost_scared_end_images = [pg.transform.scale(pg.image.load(f'images/ghost_scared_end{n}.png'), (32, 32)) for n in range(20)]

    def __init__(self, game, image, node, speed, type):
        super().__init__(game, image, node, speed)

        self.directionNext = "UP"
        self.type = type
        self.scared = False
        self.speed *= 1.5
        self.scaredTime = 8000
        # self.scaredCutoff = 8000
        self.scaredSpeedMulti = 0.02
        self.startingSequence = True
        self.spawnNode = self.node

        self.score_time = self.settings.score_popup_time
        self.score_on = False

        self.previousPacmanNextNode = None
        self.calculatePath = True
        self.path, self.closed = list(), list()
        self.calcTimerDef = 5000
        self.calcTimer = 0
        self.randomizeDirection = False

        self.debugToggle = False

        # initializing image timers
        if self.type == 0:
            self.timer_bright = Timer(frames=Ghost.blinky_right)
            self.timer_bleft = Timer(frames=Ghost.blinky_left)
            self.timer_bup = Timer(frames=Ghost.blinky_up)
            self.timer_bdown = Timer(frames=Ghost.blinky_down)
            self.blinky_timer = self.timer_bright
        elif self.type == 1:
            self.timer_bright = Timer(frames=Ghost.pinky_right)
            self.timer_bleft = Timer(frames=Ghost.pinky_left)
            self.timer_bup = Timer(frames=Ghost.pinky_up)
            self.timer_bdown = Timer(frames=Ghost.pinky_down)
            self.pinky_timer = self.timer_bright
        elif self.type == 2:
            self.timer_bright = Timer(frames=Ghost.inky_right)
            self.timer_bleft = Timer(frames=Ghost.inky_left)
            self.timer_bup = Timer(frames=Ghost.inky_up)
            self.timer_bdown = Timer(frames=Ghost.inky_down)
            self.inky_timer = self.timer_bright
        elif self.type == 3:
            self.timer_bright = Timer(frames=Ghost.clyde_right)
            self.timer_bleft = Timer(frames=Ghost.clyde_left)
            self.timer_bup = Timer(frames=Ghost.clyde_up)
            self.timer_bdown = Timer(frames=Ghost.clyde_down)
            self.inky_timer = self.timer_bright

        self.timer_scared = Timer(frames=Ghost.ghost_scared_images)
        self.timer_scared_end = Timer(frames=Ghost.ghost_scared_end_images, looponce=True)

        self.ghost_timer = self.timer_bup

    def generateNextDirection(self):
        #if self.game.pacman.nextNode != self.previousPacmanNextNode or self.calcTimer <= 0:
        if self.calcTimer <= 0:
            self.calculatePath = True
        self.calcTimer -= 1

        if self.startingSequence:
            if self.node.actions[0] != "UP":
                self.directionNext = self.node.actions[random.randint(1, 2)]
                self.game.sound.play_siren()
                self.startingSequence = False
        elif self.calculatePath and self.atNode:
            self.path = list()
            self.calcTimer = self.calcTimerDef
##################### BEGIN A STAR SEARCH #####################
            goal = self.game.pacman.nextNode
            self.previousPacmanNextNode = goal

            open, closed = list(), list()

            self.nextNode.g, self.nextNode.f = 0, 0
            open.append(self.nextNode)
            self.path.append(self.nextNode)

            while len(open) > 0:
                minf = 100000
                q = open[0]
                qn = 0

                for n in range(0, len(open) - 1):
                    if open[n].f < minf:
                        minf = open[n].f
                        q = open[n]
                        qn = 0

                self.path.append(q)

                open.pop(qn)

                for adj in q.adjacent:
                    if adj == goal:
                        open = list()
                        self.closed = closed
                        break
                    else:
                        adj.g = q.g + 1

                        if self.type == 3:
                            # Manhattan Distance #
                            adj.h = (abs(adj.center.x - goal.center.x) + abs(adj.center.y - goal.center.y))
                            ######################
                        elif self.type == 2:
                            # Euclidean Distance #
                            adj.h = math.sqrt((adj.center.x - goal.center.x) ** 2 +  (adj.center.y - goal.center.y) ** 2)
                            ######################
                        else:
                            # Diagonal Distance # 
                            dx, dy = abs(adj.center.x - goal.center.x), abs(adj.center.y - goal.center.y)
                            adj.h = 1 * (dx + dy) + (math.sqrt(2) - 2 * 1) * min(dx, dy)
                            ####################

                        adj.f = adj.g + adj.h

                    skip = False
                    for n in open:
                        if n == adj and n.f < adj.f:
                            skip = True

                    for n in closed:
                        if n == adj and n.f <= adj.f:
                            skip = True

                    if not skip:
                        open.append(adj)

                closed.append(q)
            self.calculatePath = False
##################### END A STAR SEARCH #####################
        # PATHING #
        if self.atNode:
            self.randomizeDirection = False
        if self.atNode and random.randint(0, 5 * (self.type + 1)) == 0:
            dirInt = random.randint(0, len(self.node.actions) - 1)
            self.directionNext = self.node.actions[dirInt]
            self.randomizeDirection = True
        elif not self.randomizeDirection:
            isAdj = False
            while not isAdj:
                if len(self.path) > 0:
                    for n in self.node.adjacent:
                        if self.path[0] == n:
                            isAdj = True

                    if not isAdj:
                        self.path.pop(0)
                else:
                    break

            if len(self.path) > 0:
                self.moveTowards(self.path[0], self.speed)
                self.atNode = False
                if not self.scared:
                    if self.node.center.x > self.path[0].center.x:
                        self.ghost_timer = self.timer_bleft
                    elif self.node.center.x < self.path[0].center.x:
                        self.ghost_timer = self.timer_bright
                    elif self.node.center.y < self.path[0].center.y:
                        self.ghost_timer = self.timer_bdown
                    else:
                        self.ghost_timer = self.timer_bup
                if self.node.center.x == self.path[0].center.x and self.node.center.y == self.path[0].center.y:
                    self.node = self.path[0]
                    self.atNode = True
                    self.path.pop(0)
            elif self.atNode:
                self.calcTimer = 0

        # END PATHING #

        # DEBUG A STAR #
        if self.debugToggle:
            if self.type == 0:
                color1 = (180, 0, 0)
                color2 = (255, 0, 0)
            elif self.type == 1:
                color1 = (255, 51, 153)
                color2 = (255, 153, 204)
            elif self.type == 2:
                color1 = (0, 0, 180)
                color2 = (0, 0, 255)
            elif self.type == 3:
                color1 = (255, 102, 0)
                color2 = (255, 163, 102)

            for i in range(len(self.closed) - 1):
                pg.draw.circle(self.screen,  color1, (self.closed[i].center.x, self.closed[i].center.y), 6)
            for i in range(len(self.path) - 1):
                pg.draw.circle(self.screen, color2, (self.path[i].center.x, self.path[i].center.y), 3)
        # END DEBUG A STAR #

    def makeScared(self):
        self.scared = True
        self.speed += self.scaredSpeedMulti
        dirInt = random.randint(0, len(self.node.actions) - 1)
        self.directionNext = self.node.actions[dirInt]
        self.ghost_timer = self.timer_scared
        self.game.sound.stop_siren()
        self.game.sound.play_power_pellet()
    
    def adjustImageToDirection(self, direction):
        if self.atNode and self.directionNext != None and not self.scared and self.ghost_timer != self.timer_scared_end:
            if direction == "UP" or direction == None:
                self.ghost_timer = self.timer_bup
            elif direction == "DOWN":
                self.ghost_timer = self.timer_bdown
            elif direction == "LEFT":
                self.ghost_timer = self.timer_bleft
            elif direction == "RIGHT":
                self.ghost_timer = self.timer_bright

    def checkScared(self):
        # if self.scared:
        #     if self.scaredTimer >= self.scaredCutoff * 0.6:
        #         self.ghost_timer = Timer(frames=Ghost.ghost_scared_end_images)
        #     else:
        #         self.ghost_timer = Timer(frames=Ghost.ghost_scared_images)
        #     self.scaredTimer += 1
        #     if self.scaredTimer >= self.scaredCutoff:
        #         self.scaredTimer = 0
        #         self.scared = False
        #         self.speed -= self.scaredSpeedMulti
        if self.scared:
            if self.ghost_timer == self.timer_scared and self.scaredTime > 0:
                self.scaredTime -= 1
            elif self.ghost_timer == self.timer_scared and self.scaredTime <= 0:
                self.ghost_timer.reset()
                self.ghost_timer = self.timer_scared_end
            elif self.ghost_timer == self.timer_scared_end and self.ghost_timer.finished:
                self.scared = False
                self.speed -= self.scaredSpeedMulti
                self.ghost_timer.reset()
                self.ghost_timer = self.timer_bright
                self.scaredTime = 8000
                self.game.sound.stop_power_pellet()
                self.game.sound.play_siren()
            
    def die(self):
        self.game.scoreboard.increment_score(self.settings.ghost_points)
        self.game.sound.play_retreating()
        self.prep_score()
        self.score_on = True
        self.node = self.spawnNode
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y = self.node.center.x, self.node.center.y
        self.startingSequence = True
        self.directionNext = self.direction = "UP"
        self.scared = False
        self.ghost_timer.reset()
        self.ghost_timer = self.timer_bup
        self.scaredTime = 8000

    def prep_score(self):
        self.font = pg.font.SysFont(None, 24)
        self.text_color = (0, 255, 255)
        self.score_str = str(self.settings.ghost_points)
        self.score_image = self.font.render(self.score_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.rect.centerx
        self.score_rect.centery = self.rect.centery
    
    def draw_score(self):
        self.screen.blit(self.score_image, self.score_rect)

    def score_popup(self):
        if self.score_on and self.score_time >= 0:
            self.score_time -= 1
            self.draw_score()
        elif self.score_on and self.score_time <= 0:
            self.score_on = False
            self.score_time = self.settings.score_popup_time

    def update(self):
        self.checkTeleport()
        self.generateNextDirection()
        if self.startingSequence or self.randomizeDirection:
            self.nextDirection(self.directionNext, self.speed)
        self.checkScared()
        self.score_popup()
        self.draw()

    def draw(self):
        self.image = self.ghost_timer.imagerect()
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y
        self.screen.blit(self.image, self.rect)
