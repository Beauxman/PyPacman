class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0, 38, 78)
        
        self.player_speed = 0.065
        self.initialize_speed_settings()

        self.lives_limit = 3

        self.ghost_points = 200
        self.pellet_points = 10
        self.power_pellet_points = 50
        self.fruit_points = {0:100, 1:300, 2:500, 3:700, 4:1000, 5:2000, 6:3000, 7:5000}

        self.fruit_spawntime_min = 2000
        self.fruit_spawntime_max = 4000
        self.fruit_availible_time = 2000
        
        self.initialize_speed_settings()

    def initialize_speed_settings(self):
        self.pacman_speed_factor = 2
        self.ghost_speed_factor = 2

