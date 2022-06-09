"""
imports 
Ends game loop, inherits from moving_objects.py
"""

from Greed_game.greed_classes.moving_objects import Moving_objects


class Mine(Moving_objects):
    def __init__(self):
        super().__init__()