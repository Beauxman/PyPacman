import pygame as pg
from consumable import Consumable

class Pellet(Consumable):
    def __init__(self, game, centerx, centery):
        super().__init__(game, centerx, centery)
        self.size = self.settings.pellet_size
        self.points = self.settings.pellet_points

    def eaten(self):
        if not self.consumed:
            self.consumed = True
            self.scoreboard.increment_score(self.settings.pellet_points)
    
    def update(self):
        self.draw()

    def draw(self):
        pg.draw.circle(self.screen, self.color, (self.centerx, self.centery), self.size)
