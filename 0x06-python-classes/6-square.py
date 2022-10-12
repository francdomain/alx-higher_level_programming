#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Display a square"""

    def __init__(self, size=0):
        """Initialize a square of attribute:
            size (int): size of the square"""
        self.size = size

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

    @property
    def position(self):
        """Get set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the current position of the square"""
        if type(value) is not tuple or len(value) != 2 or
        not all(isinstance(num, int) for num in value) or
        not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the current square"""
        return self.__size * self.__size

    def my_print(self):
        """print the square with # in stdout"""
        if self.__size == 0:
            print()
        for n in range(self.__size):
            [print("#", end="") for m in range(self.__size)]
