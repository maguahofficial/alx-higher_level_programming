#!/usr/bin/python3
"""class Defines a Rectangle"""


class Rectangle:
    """this class represent a rectangle.

    Attributes:
        number_of_instancesvrble (int variable): The numb of rectangle instances.
        print_symbolvrble : any symbol used for string representation.
    """

    number_of_instancesvrble = 0
    print_symbolvrble = "#"

    def __init__(self, width=0, height=0):
        """this function initialize a new Rectangle.

        Args:
            width (int variable): width of the new rectangle.
            height (int variable):height of the new rectangle.
        """
        type(self).number_of_instancesvrble += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """this function Gets or sets the width of the Rectangle."""
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
        """function Gets or sets the height of a Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function returns the area of a rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """this function returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """function returns the rectangle with the greater area.

        Args:
            rect_1 (Rectangle): Rectangle1.
            rect_2 (Rectangle): Rectangle2.
        Raises:
            TypeError:either the rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """function returns new rectangle with width and height equal to the size.

        Args:
            size (int variable): width andheight of the new rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """function returns the printable representation of the Rectangle.

        this represents the rectangle with # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectvrble = []
        for ix in range(self.__height):
            [rectvrble.append(str(self.print_symbolvrble)) for j in range(self.__width)]
            if ix != self.__height - 1:
                rectvrble.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """function returns string representation of the Rectangle."""
        rectvrble = "Rectangle(" + str(self.__width)
        rectvrble += ", " + str(self.__height) + ")"
        return (rectvrble)

    def __del__(self):
        """function prints a message for every rectangle deleted."""
        type(self).number_of_instancesvrble -= 1
        print("Bye rectangle...")
