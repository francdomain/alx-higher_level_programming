#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Display a square"""

    def __init__(self, size=0):
        """Initialize a square of attribute:
            size (int): size of the square"""

    @property
    def size(self):
        """Get the current square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set current square size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Display current square area"""
    def area(self):
        return self.__size *__self.size
