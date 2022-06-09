"""
Draws the rock (o)
Inherits from moving_objects
"""


from game.moving_object import MovingObject


class Rock(MovingObject):
    def __init__(self):
        super().__init__()
        super().set_text("o")


    def get_points(self):
        # return self._message
        return -1

    