"""
    The responsibility of Coordinate is to hold and provide information about itself. Coordinate has a few 
    convenience methods for adding, scaling, and comparing them.
"""

class Coordinate:
    def __init__(self, x, y):
        ''' Constructs the new location with the given x and y values
        Args:
            x (int): the given x value
            y (int): the given y value
        '''
        self._x = x
        self._y = y

    def add(self, other):
        '''Gets a new location that is the sum of this 
        and the given one
        
        Args:
            other (coordinate): The coordinate to add.
        
        Returns:
            Coordinate: A new coordinate that is the sum.
            
        '''
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Coordinate(x, y)



    def equals(self, other):
        '''Whether or not this coordinate is equal to the given one.
        
        Args: 
            other (Coordinate): the Location to compare
        Returns:
            boolean: True if both x and y are equal; false if otherwise.
        '''
        #return abs(self._x - other.get_x()) < 3 and (self._y - other.get_y()) < 3
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        '''Gets the horizontal distance.
        
        Returns:
            interger: The horizontal distance
        '''
        return self._x

    def get_y(self):
        '''Gets the vertical distance.
        
        Returns:
            interger: The vertical distance'''
        return self._y

    def scale(self, factor):
        '''Scales the coordinates by the provided factor.
        
        Args:
            factor (int): The amount to scale.
            
        Returns: 
            Location: A new Location that is called'''
        return Coordinate(self._x * factor, self._y * factor)