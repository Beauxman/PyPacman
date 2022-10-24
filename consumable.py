import pygame as pg
from pygame.sprite import Sprite, Group
from timer import Timer


class Consumable(Sprite):
    def __init__(self, game, centerx, centery):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.scoreboard = game.scoreboard
        self.centerx = centerx
        self.centery = centery
        self.size = 5
        self.color = 255, 255, 255

        self.consumed = False
    
    def eaten(self):
        if not self.consumed:
            self.consumed = True
            self.scoreboard.increment_score()

    def update(self):
        self.draw()

    def draw(self):
        pg.draw.circle(self.screen, self.color, (self.center.x, self.center.y), self.size)