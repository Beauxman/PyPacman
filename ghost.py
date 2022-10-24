import pygame as pg
from node import Point
from character import Character
import random
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
        self.scaredTimer = 0
        self.scaredCutoff = 10000

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
            self.timer_scared_end = Timer(frames=Ghost.ghost_scared_end_images)

    def generateNextDirection(self):
        AIMultiplier = 1000 * (self.type + 1)
        if random.randint(0, AIMultiplier) == 0:
            dirInt = random.randint(0, len(self.node.actions) - 1)
            self.directionNext = self.node.actions[dirInt]

    def makeScared(self):
        self.scared = True
        self.speed += 0.01
    
    def adjustImageToDirection(self, direction):
        if self.atNode and self.directionNext != None:
            if direction == "UP" or direction == None:
                self.ghost_timer = self.timer_bup
            elif direction == "DOWN":
                self.ghost_timer = self.timer_bdown
            elif direction == "LEFT":
                self.ghost_timer = self.timer_bleft
            elif direction == "RIGHT":
                self.ghost_timer = self.timer_bright

    def checkScared(self):
        if self.scared:
            self.ghost_timer = Timer(frames=Ghost.ghost_scared_images)
            self.scaredTimer += 1
            if self.scaredTimer >= self.scaredCutoff:
                self.scaredTimer = 0
                self.scared = False
                self.speed -= 0.01
            
    def update(self):
        self.generateNextDirection()
        self.nextDirection(self.directionNext, self.speed)
        self.checkScared()
        self.draw()

    def draw(self):
        self.image = self.ghost_timer.imagerect()
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y
        self.screen.blit(self.image, self.rect)
