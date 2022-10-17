#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing the dimension of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Represent the rectangle area"""
        area = self.width * self.height
        return area

    def perimeter(self):
        """Represent the rectangle perimeter"""
        perimeter = (self.width + self.height) * 2
        if self.width == 0 or self.height == 0:
            perimeter == 0
        return perimeter
