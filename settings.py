class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        self.player_speed = 0.05
        self.initialize_speed_settings()

    def initialize_speed_settings(self):
        pass

    def increase_speed(self):
        pass
