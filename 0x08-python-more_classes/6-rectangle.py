#!/usr/bin/python3
"""The Class defines a Rectangle."""


class Rectangle:
    """This class represents a rectangle.

    Attributes:
        number_of_instances (interger variable): numb of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Function initializes new Rectangle.

        Args:
            width (interger variable): The width of the new rectangle.
            height (interger variable): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """this function Gets or sets the width of a Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """this function Gets or sets the height of a rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function returns the area of a Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """this function returns the perimeter of a Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """function  returns the printable representation of a Rectangle.

        this basicaly represents the rectangle with # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """function returns string representation of a Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """This function prints a message for every rectangle deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
