#!/usr/bin/python3
"""this class defines a Rectangle class."""


class Rectangle:
    """this class represent a rectangle.

    Attributes:
        number_of_instancesvrble (int variable): The number of Rectangle instances.
        print_symbol : any symbol used for string representation.
    """

    number_of_instancesvrble = 0
    print_symbolvrble = "#"

    def __init__(self, width=0, height=0):
        """this function initialize a new rectangle.

        Args:
            width (int variable): width of the new rectangle.
            height (int variable):height of the new rectangle.
        """
        type(self).number_of_instancesvrble += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """this function Gets or set sthe width of a rectangle."""
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
        """the function Get or sets the height of a rectangle."""
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
        """function returns the perimeter of  Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """function returns the rectangle with the area thats greater.

        Args: 
            rect_1 (Rectangle):  Rectangle1.
            rect_2 (Rectangle): Rectangle2.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """this function returns the printable representation of a rectangle.

        this represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectcv = []
        for ic in range(self.__height):
            [rect.append(str(self.print_symbolvrble)) for j in range(self.__width)]
            if ic != self.__height - 1:
                rectcv.append("\n")
        return ("".join(rectcv))

    def __repr__(self):
        """function returns string representation of a rectangle."""
        rectcv = "Rectangle(" + str(self.__width)
        rectcv += ", " + str(self.__height) + ")"
        return (rectcv)

    def __del__(self):
        """function prints a message for every rectangle deleted."""
        type(self).number_of_instancesvrble -= 1
        print("Bye rectangle...")
