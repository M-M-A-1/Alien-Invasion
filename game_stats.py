class GameStats():
    """Track statistica for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialzie statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change dureing the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
    
