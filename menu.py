import sys
from threading import Timer
import pygame as pg
from pygame import mixer
from pygame.sprite import Sprite

import game_functions as gf
from button import Button
from timer import Timer

class Menu:
    def __init__(self, game):
        self.game = game

        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (252, 186, 3)

        font = pg.font.Font(None, 160)
        self.text = font.render("PAC-MAN", True, self.text_color)
        self.text_rect = self.text.get_rect(center=(self.settings.screen_width/2, self.settings.screen_height/10))

        font2 = pg.font.Font(None, 100)
        self.text2 = font2.render("Play Game: Press Enter", True, self.text_color)
        self.text_rect2 = self.text2.get_rect(center=(self.settings.screen_width/2, self.settings.screen_height/4.5))

        font3 = pg.font.Font(None, 100)
        self.text3 = font3.render("Highscore: " + str(self.game.highscore), True, self.text_color)
        self.text_rect3 = self.text_rect3 = self.text3.get_rect(center=(self.settings.screen_width/2, self.settings.screen_height/3.0))

        blinky_font = pg.font.Font(None, 80)
        self.blinky_text = blinky_font.render("Blinky", True, (255, 0, 0))
        self.blinky_rect = self.blinky_text.get_rect(center=(self.settings.screen_width/2 + 100, self.settings.screen_height/2.4))

        inky_font = pg.font.Font(None, 80)
        self.inky_text = inky_font.render("Inky", True, (0, 191, 255))
        self.inky_rect = self.inky_text.get_rect(center=(self.settings.screen_width/2 + 100, self.settings.screen_height/2.1))

        pinky_font = pg.font.Font(None, 80)
        self.pinky_text = pinky_font.render("Pinky", True, (255, 192, 203))
        self.pinky_rect = self.pinky_text.get_rect(center=(self.settings.screen_width/2 + 100, self.settings.screen_height/1.7))

        clyde_font = pg.font.Font(None, 80)
        self.clyde_text = clyde_font.render("Clyde", True, (255, 165, 0))
        self.clyde_rect = self.clyde_text.get_rect(center=(self.settings.screen_width/2 + 100, self.settings.screen_height/1.4))

        pacman_font = pg.font.Font(None, 80)
        self.pacman_text = pacman_font.render("Pac-man", True, (255, 215, 0))
        self.pacman_rect = self.pacman_text.get_rect(center=(self.settings.screen_width/2 + 100, self.settings.screen_height/1.1))


        self.image = pg.image.load('images/blinky_down0.png')
        self.rect = self.image.get_rect(center=(self.settings.screen_width/2 - 140, self.settings.screen_height/2.4))
        
        self.image2 = pg.image.load('images/inky_down0.png')
        self.rect2 = self.image2.get_rect(center=(self.settings.screen_width/2 - 140, self.settings.screen_height/2.1))

        self.image3 = pg.image.load('images/pinky_down0.png')
        self.rect3 = self.image3.get_rect(center=(self.settings.screen_width/2 - 140, self.settings.screen_height/1.7))

        self.image4 = pg.image.load('images/clyde_down0.png')
        self.rect4 = self.image4.get_rect(center=(self.settings.screen_width/2 - 140, self.settings.screen_height/1.4))

        self.image5 = pg.image.load('images/pacman0.png')
        self.rect5 = self.image5.get_rect(center=(self.settings.screen_width/2 - 140, self.settings.screen_height/1.1))

    def reset(self):
        self.update()
    
    def update(self):
        if gf.check_menu_events():
            self.game.scene = 2
        self.draw()
    
    def draw(self):
        self.screen.fill((50, 50, 50))
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.text2, self.text_rect2)
        self.screen.blit(self.text3, self.text_rect3)
        self.screen.blit(self.blinky_text, self.blinky_rect)
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.inky_text, self.inky_rect)
        self.screen.blit(self.image2, self.rect2)
        self.screen.blit(self.pinky_text, self.pinky_rect)
        self.screen.blit(self.image3, self.rect3)
        self.screen.blit(self.clyde_text, self.clyde_rect)
        self.screen.blit(self.image4, self.rect4)
        self.screen.blit(self.pacman_text, self.pacman_rect)
        self.screen.blit(self.image5, self.rect5)