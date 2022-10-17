#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represent a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing the dimension of the rectangle"""
        self.width = width
        self.height = height
        Rectangle().number_of_instances += 1

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
        """Return the rectangle area"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Return the rectangle perimeter"""
        perimeter = (self.__width + self.__height) * 2
        if self.__width == 0 or self.__height == 0:
            perimeter == 0
            return 0
        return perimeter

    def __str__(self):
        """Return printable representation of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append('\n')
        return ("".join(rectangle))

    def __repr__(self):
        """Return a string representation of the rectangle to be able
        to recreate a new instance by using eval()"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle().number_of_instances -= 1
