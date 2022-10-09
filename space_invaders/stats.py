class Stats():
    """Statistics tracking"""

    def __init__(self):
        """Statistics initialization"""
        self.reset_stats()

    def reset_stats(self):
        """Statistics that change during the game"""
        self.guns_left = 2  # Number of lives
