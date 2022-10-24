class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        self.player_speed = 0.065
        self.initialize_speed_settings()

        self.lives_limit = 3

        self.ghost_points = 200
        self.pellet_points = 10
        self.power_pellet_points = 50
        self.fruit_points = 100

        self.pellet_size = 5
        
        self.initialize_speed_settings()

    def initialize_speed_settings(self):
        self.pacman_speed_factor = 2
        self.ghost_speed_factor = 2

