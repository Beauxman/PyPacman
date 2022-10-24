import pygame as pg

class Scoreboard:
    def __init__(self, game):
        self.score = -100
        self.level = 0
        self.high_score = 0

        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (255, 255, 255)
        self.font = pg.font.SysFont(None, 48)

        self.score_image = None
        self.score_rect = None
        self.prep_score()

        self.imageScalePx = 32
        self.livesImg = pg.image.load('images/pacman0.png')
        self.livesImg = pg.transform.scale(self.livesImg, (self.imageScalePx, self.imageScalePx))
        self.livesRect = self.livesImg.get_rect()

    def increment_score(self, points):
        self.score += points
        self.prep_score()
    
    def prep_score(self):
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 5
    
    def reset(self):
        self.score = -100
        self.update()
    
    def update(self):
        self.draw()
    
    def draw(self):
        for i in range(self.game.lives + 1):
            self.livesRect.x = self.imageScalePx * i + 5
            self.livesRect.y = 5
            self.screen.blit(self.livesImg, self.livesRect)
        self.screen.blit(self.score_image, self.score_rect)