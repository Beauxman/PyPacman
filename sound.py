import time
import pygame as pg

class Sound:
    def __init__(self):
        pg.mixer.init()
        pg.mixer.music.set_volume(0.1)
        gameover_sound = pg.mixer.Sound('sounds/death.wav')
        startup_sound = pg.mixer.Sound('sounds/pacman_beginning.wav')
        eat_pellet_sound = pg.mixer.Sound('sounds/waka.wav')
        eat_ghost_sound = pg.mixer.Sound('sounds/eat_ghost.wav')
        eat_fruit_sound = pg.mixer.Sound('sounds/eat_fruit.wav')
        power_pellet_sound = pg.mixer.Sound('sounds/power_pellet.wav')
        retreating_sound = pg.mixer.Sound('sounds/retreating.wav')
        siren_sound = pg.mixer.Sound('sounds/siren.wav')
        self.sounds = {'gameover': gameover_sound, 'startup': startup_sound,
                        'eat_ghost': eat_ghost_sound, 'eat_fruit': eat_fruit_sound,
                        'waka': eat_pellet_sound, 'power_pellet': power_pellet_sound,
                        'retreating': retreating_sound, 'siren': siren_sound}
    def play_startup(self):
        pg.mixer.Sound.play(self.sounds['startup'])

    def play_eat_pellet(self):
        pg.mixer.Sound.play(self.sounds['waka'])

    def play_eat_ghost(self):
        pg.mixer.Sound.play(self.sounds['eat_ghost'])

    def play_eat_fruit(self):
        pg.mixer.Sound.play(self.sounds['eat_fruit'])

    def play_power_pellet(self):
        pg.mixer.Sound.play(self.sounds['pacman_beginning.wav'])

    def play_retreating(self):
        pg.mixer.Sound.play(self.sounds['retreating'])

    def play_siren(self):
        pg.mixer.Sound.play(self.sounds['siren'])
        
    def gameover(self):
        self.stop_bg()
        pg.mixer.music.load('sounds/death.wav')
        self.play_bg()
        time.sleep(2.8)
    