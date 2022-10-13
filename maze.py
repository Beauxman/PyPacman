import pygame as pg

class Maze:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.image = pg.image.load('images/maze.jpg')
        self.image = pg.transform.scale(self.image, (self.settings.screen_width, self.settings.screen_height))
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()

    def update(self):
        self.draw()
    
    def draw(self):
        rect = self.image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(self.image, rect)