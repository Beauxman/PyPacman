import pygame as pg
from pygame.sprite import Sprite
from node import Point
from random import randint

class Fruit(Sprite):
    # initialize fruit images
    cherry_image = pg.transform.scale(pg.image.load(f'images/cherry.png'), (32, 32))
    strawberry_image = pg.transform.scale(pg.image.load(f'images/strawberry.png'), (32, 32))
    orange_image = pg.transform.scale(pg.image.load(f'images/orange.png'), (32, 32))
    apple_image = pg.transform.scale(pg.image.load(f'images/apple.png'), (32, 32))
    melon_image = pg.transform.scale(pg.image.load(f'images/melon.png'), (32, 32))
    galaxian_flagship_image = pg.transform.scale(pg.image.load(f'images/galaxian_flagship.png'), (32, 32))
    bell_image = pg.transform.scale(pg.image.load(f'images/bell.png'), (32, 32))
    key_image = pg.transform.scale(pg.image.load(f'images/key.png'), (32, 32))

    def __init__(self, game, node):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.game = game
        self.scoreboard = game.scoreboard
        self.screen_rect = game.screen.get_rect()
        self.node = node
        self.sound = game.sound
        self.images = {0:Fruit.cherry_image, 1:Fruit.strawberry_image, 2:Fruit.orange_image, 3:Fruit.apple_image, 4:Fruit.melon_image, 5:Fruit.galaxian_flagship_image, 6:Fruit.bell_image, 7:Fruit.key_image}

        # first fruit
        self.choose_fruit()

        self.active = False
        self.fruit_spawn_timer = randint(self.settings.fruit_spawntime_min, self.settings.fruit_spawntime_max)
        self.fruit_availible_timer = self.settings.fruit_availible_time
        self.fruits_remaining = 2

    def choose_fruit(self):
        self.fruit_type = randint(0, 7)
        self.image = self.images[self.fruit_type]
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = self.node.center.x, self.node.center.y
        self.center = Point(self.rect.centerx, self.rect.centery)

    def check_fruit(self):
        if not self.active and self.fruit_spawn_timer >= 0:
            self.fruit_spawn_timer -= 1
        elif not self.active and self.fruit_spawn_timer <= 0 and self.fruits_remaining != 0:
            self.active = True
        elif self.active and self.fruit_availible_timer >= 0:
            self.fruit_availible_timer -= 1
            self.draw()
        elif self.active and self.fruit_availible_timer <= 0:
            self.despawn()

    def eaten(self):
        self.scoreboard.increment_score(self.settings.fruit_points[self.fruit_type])
        self.sound.play_eat_fruit()
        self.despawn()

    def despawn(self):
        self.fruits_remaining -= 1
        self.choose_fruit()
        self.fruit_spawn_timer = randint(self.settings.fruit_spawntime_min, self.settings.fruit_spawntime_max)
        self.fruit_availible_timer = self.settings.fruit_availible_time
        self.active = False

    def update(self):
        self.check_fruit()
        
    def draw(self):
        self.screen.blit(self.image, self.rect)