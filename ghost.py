import pygame as pg
from node import Point
from character import Character
import random
from timer import Timer

class Ghost(Character):
    # initializing sprites for blinky
    blinky_right = [pg.transform.scale(pg.image.load(f'images/blinky_right{n}.png'), (32, 32)) for n in range(2)]
    blinky_left = [pg.transform.flip(n, True, False) for n in blinky_right]
    blinky_up = [pg.transform.scale(pg.image.load(f'images/blinky_up{n}.png'), (32, 32)) for n in range(2)]
    blinky_down = [pg.transform.scale(pg.image.load(f'images/blinky_down{n}.png'), (32, 32)) for n in range(2)]

    # initializing sprites for pinky

    # initializing sprites for inky

    # initializing sprites for clyde

    # initializing other sprites
    ghost_scared_images = [pg.transform.scale(pg.image.load(f'images/ghost_scared{n}.png'), (32, 32)) for n in range(2)]
    ghost_scared_end_images = [pg.transform.scale(pg.image.load(f'images/ghost_scared_end{n}.png'), (32, 32)) for n in range(20)]

    def __init__(self, game, image, node, speed):
        super().__init__(game, image, node, speed)

        # initializing image timers
        self.timer_bright = Timer(frames=Ghost.blinky_right)
        self.timer_bleft = Timer(frames=Ghost.blinky_left)
        self.timer_bup = Timer(frames=Ghost.blinky_up)
        self.timer_bdown = Timer(frames=Ghost.blinky_down)
        self.blinky_timer = self.timer_bright

        self.timer_scared = Timer(frames=Ghost.ghost_scared_images)
        self.timer_scared_end = Timer(frames=Ghost.ghost_scared_end_images)

        self.directionNext = "UP"

    def generateNextDirection(self): #VERY BASIC AI -- CHANGE LATER
        if random.randint(0, 2000) == 0:
            dirInt = random.randint(0, len(self.node.actions) - 1)
            self.directionNext = self.node.actions[dirInt]
    
    def adjustImageToDirection(self, direction):
        if self.atNode and self.directionNext != None:
            if direction == "UP" or direction == None:
                self.blinky_timer = self.timer_bup
            elif direction == "DOWN":
                self.blinky_timer = self.timer_bdown
            elif direction == "LEFT":
                self.blinky_timer == self.timer_bleft
            elif direction == "RIGHT":
                self.blinky_timer == self.timer_bright
        
    def update(self):
        self.generateNextDirection()
        self.nextDirection(self.directionNext, self.speed)
        self.draw()

    def draw(self):
        self.image = self.blinky_timer.imagerect()
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y
        self.screen.blit(self.image, self.rect)
