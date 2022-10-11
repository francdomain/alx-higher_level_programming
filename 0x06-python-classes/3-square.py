#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Display a square"""

    def __init__(self, size=0):
        """Initialize a square of attribute:
            size (int): size of the square"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.current_area = current_area

    """Display current square area"""
    def area(self):
        """Return the area of the current square"""
        return (self.size * self.size)
