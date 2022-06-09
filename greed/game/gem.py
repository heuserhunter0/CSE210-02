"""
Import moving_objects.py
This class will draw the gems for the game
Inherit from moving_object
"""
from game.moving_object import MovingObject
class Gem(MovingObject):
    def __init__(self):
        super().__init__()
        super().set_text("*")

    def get_points(self):
        # return self._message
        return 1
