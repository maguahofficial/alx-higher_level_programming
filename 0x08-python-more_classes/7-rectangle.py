#!/usr/bin/python3
"""the class defines a rectangle class."""


class Rectangle:
    """this function represent a rectangle.

    Attributes:
        number_of_instances (int variable): The numb of rectangle instances.
        print_symbol : symbol used to represent  string.
    """

    number_of_instancesvrble = 0
    print_symbolvrble = "#"

    def __init__(self, width=0, height=0):
        """ this function initialize new rectangle.

        Args:
            width (int variable):width of the new rectangle.
            height (interger): height of the new rectangle.
        """
        type(self).number_of_instancesvrble += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """this function Gets or sets the width of a rectangle."""
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
        """this function Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function returns area of a Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """this function returns perimeter of a Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """this function returns the printable representation of a Rectangle.

        this represents the rectangle with # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbolvrble)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """this function returns string representation of a rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """function prints a message for every Rectangle deleted."""
        type(self).number_of_instancesvrble -= 1
        print("Bye rectangle...")
