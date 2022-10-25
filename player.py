import pygame as pg
import time
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
        self.sound = game.sound
        self.dead = False
        self.deathTimer = 0
        self.deathLength = 3000
        self.speed = self.speed * self.settings.pacman_speed_factor # had to change his default speed to get the iconic wakawaka

        # initializing image timers
        self.timer_normal_right = Timer(frames=Player.pacman_right_images)
        self.timer_normal_left = Timer(frames=Player.pacman_left_images)
        self.timer_normal_up = Timer(frames=Player.pacman_up_images)
        self.timer_normal_down = Timer(frames=Player.pacman_down_images)
        self.timer_death = Timer(frames=Player.pacman_death_images, wait=75, looponce=True)
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
        # CHECK COLLISIONS WITH PELLETS
        toX, toY = self.nextNode.center.x, self.nextNode.center.y
        rDistanceX, rDistanceY = toX - self.rect.centerx, toY - self.rect.centery
        if rDistanceX <= self.nextNode.size / 2 or rDistanceY <= self.nextNode.size / 2:
            if self.nextNode.type == 1:
                self.game.scoreboard.increment_score(self.settings.pellet_points)
                self.sound.play_eat_pellet()
            if self.nextNode.type == 3:
                self.game.scoreboard.increment_score(self.settings.power_pellet_points)
                self.sound.play_eat_pellet()
                self.game.blinky.makeScared()
                self.game.pinky.makeScared()
                self.game.inky.makeScared()
                self.game.clyde.makeScared()
            self.nextNode.type = 0

        # CHECK COLLISIONS WITH GHOST
        if pg.Rect.colliderect(self.rect, self.game.blinky.rect) and not self.dead:
            if self.game.blinky.scared:
                self.game.blinky.die()
                self.sound.play_eat_pellet()
                self.sound.play_eat_ghost()
            else:
                self.die()
        elif pg.Rect.colliderect(self.rect, self.game.pinky.rect) and not self.dead:
            if self.game.pinky.scared:
                self.game.pinky.die()
                self.sound.play_eat_pellet()
                self.sound.play_eat_ghost()
            else:
                self.die()
        elif pg.Rect.colliderect(self.rect, self.game.inky.rect) and not self.dead:
            if self.game.inky.scared:
                self.game.inky.die()
                self.sound.play_eat_pellet()
                self.sound.play_eat_ghost()
            else:
                self.die()
        elif pg.Rect.colliderect(self.rect, self.game.clyde.rect) and not self.dead:
            if self.game.clyde.scared:
                self.game.clyde.die()
                self.sound.play_eat_pellet()
                self.sound.play_eat_ghost()
            else:
                self.die()
        
        # CHECK COLLISIONS WITH FRUIT
        if pg.Rect.colliderect(self.rect, self.game.fruit.rect) and not self.dead and self.game.fruit.active:
            self.game.fruit.eaten()
        

    def checkTeleport(self):
        if self.atNode:
            if self.node == self.game.nodes.nodeList[14][0]:
                self.node = self.game.nodes.nodeList[14][26]
                self.rect.centerx, self.rect.centery = self.center.x, self.center.y = self.node.center.x, self.node.center.y
                self.directionNext = self.direction = "LEFT"
            elif self.node == self.game.nodes.nodeList[14][27]:
                self.node = self.game.nodes.nodeList[14][1]
                self.rect.centerx, self.rect.centery = self.center.x, self.center.y = self.node.center.x, self.node.center.y
                self.directionNext = self.direction = "RIGHT"

    def die(self):
        self.sound.stop_power_pellet()
        self.sound.stop_siren()
        self.dead = True
        self.speed = 0
        self.game.blinky.speed = 0
        self.game.pinky.speed = 0
        self.game.inky.speed = 0
        self.game.clyde.speed = 0
        self.game.sound.gameover()
        self.timer = self.timer_death

    def checkDead(self):
        # if self.dead:
        #     self.deathTimer += 1
        #     if self.deathTimer == self.deathLength:
        #         self.game.reset()
        if self.timer == self.timer_death and self.timer.finished:
            time.sleep(0.5)
            self.game.reset()

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
        self.checkDead()
        self.checkTeleport()
        self.checkInput()
        self.checkCollisions()
        self.nextDirection(self.directionNext, self.speed)
        self.draw()

    def draw(self):
        self.image = self.timer.imagerect()
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y
        self.screen.blit(self.image, self.rect)
