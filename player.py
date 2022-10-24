import pygame as pg
from node import Point
from character import Character
from timer import Timer

class Player(Character):

    # initializing sprites for pacman
    pacman_right_images = [pg.transform.scale(pg.image.load(f'images/pacman{n}.png'), (32, 32)) for n in range(4)]
    pacman_left_images = [pg.transform.flip(n, True, False) for n in pacman_right_images]
    pacman_up_images = [pg.transform.rotate(n, 90) for n in pacman_right_images]
    pacman_down_images = [pg.transform.flip(n, False, True) for n in pacman_up_images]
    pacman_death_images = [pg.transform.scale(pg.image.load(f'images/pacman_death{n}.png'), (32, 32)) for n in range(20)]

    def __init__(self, game, image, node, speed):
        super().__init__(game, image, node, speed)

        self.game = game

        # initializing image timers
        self.timer_normal_right = Timer(frames=Player.pacman_right_images)
        self.timer_normal_left = Timer(frames=Player.pacman_left_images)
        self.timer_normal_up = Timer(frames=Player.pacman_up_images)
        self.timer_normal_down = Timer(frames=Player.pacman_down_images)
        self.timer_death = Timer(frames=Player.pacman_death_images, looponce=True)
        self.timer = self.timer_normal_right

    def adjustImageToDirection(self, direction):
        if self.atNode and self.directionNext != None:
            if direction == "UP" or direction == None:
                self.timer = self.timer_normal_up
            elif direction == "DOWN":
                self.timer = self.timer_normal_down
            elif direction == "LEFT":
                self.timer = self.timer_normal_left
            elif direction == "RIGHT":
                self.timer = self.timer_normal_right

    def checkCollisions(self):
        toX, toY = self.nextNode.center.x, self.nextNode.center.y
        rDistanceX, rDistanceY = toX - self.rect.centerx, toY - self.rect.centery
        if rDistanceX <= self.nextNode.size / 2 or rDistanceY <= self.nextNode.size / 2:
            if self.nextNode.type == 3:
                self.game.blinky.makeScared()
                self.game.pinky.makeScared()
                self.game.inky.makeScared()
                self.game.clyde.makeScared()
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

    def draw(self):
        self.image = self.timer.imagerect()
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y
        self.screen.blit(self.image, self.rect)
