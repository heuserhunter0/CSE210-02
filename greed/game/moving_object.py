from game.common.color import Color
from game.common.coordinate import Coordinate
"""
This class is the Super class for all moving objects in the program.

gems = (*)
rocks = (o)
"""

class MovingObject:
    """A visible, moveable thing that participates in the game. 
        
        The responsibility of MovingObject class is to keep track of its appearance, position and velocity in 2d 
        space.

        Attributes:
            _text (string): The text to display
            _font_size (int): The font size to use.
            _color (Color): The color of the text.
            _position (Coordinate): The screen coordinates.
            _velocity (Coordinate): The speed and direction.
            _can_move_x (boolean) = If true, restricts horizontal movement 
            _can_move_y (boolean) = If true, restricts vertical movement
        """

    def __init__(self, can_move_x = True, can_move_y = True):
        """Constructs a new Actor.

        Args:
            can_move_x (bool): Allows or restricts the movement of the object vertically
            can_move_y (bool): Allows or restricts the movement of the object horizontally
        """
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Coordinate(0,0) #Point(0, 0)
        self._velocity = Coordinate(0,0) #Point(0, 0)
        self._can_move_x = can_move_x
        self._can_move_y = can_move_y

    def get_color(self):
        """Gets the moving object's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The moving object's text color.
        """
        return self._color

    def get_font_size(self):
        """Gets the moving object's font size.
        
        Returns:
            Coordinate: The moving object's font size.
        """
        return self._font_size

    def get_position(self):
        """Gets the moving object's position in 2d space.
        
        Returns:
            Coordinate: The moving object's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the moving object's textual representation.
        
        Returns:
            string: The moving object's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the moving object's speed and direction.
        
        Returns:
            Coordinate: The moving object's speed and direction.
        """
        return self._velocity
    
    def move_next(self, max_x, max_y):
        """Moves the object to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        # default values
        x = self._position.get_x()
        y = self._position.get_y()

        if self._can_move_x:
            x = (self._position.get_x() + self._velocity.get_x()) % max_x
        if self._can_move_y:
            y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Coordinate(x,y) #Point(x, y)

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Coordinate): The given position.
        """
        self._position = position
    
    def set_font_size(self, font_size):
        """Updates the font size to the given one.
        
        Args:
            font_size (int): The given font size.
        """
        self._font_size = font_size
    
    def set_text(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Coordinate): The given velocity.
        """
        self._velocity = velocity