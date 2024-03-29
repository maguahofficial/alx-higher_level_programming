#!/usr/bin/python3
"""this class defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """this class represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """this function initializes a new Rectangle.

        Args:
            width (int variable):width of the new rectangle.
            height (int variable):height of the new Rectangle.
            x (int variable):x coordinate of the new Rectangle.
            y (int variable):y coordinate of the new Rectangle.
            id (int variable): identity of the new Rectangle.
        Raises:
            TypeError: either of width or height is not an int.
            ValueError: either of width or height <= 0.
            TypeError:either of x or y is not an int.
            ValueError:either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """function setsorgets the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """function setsrgets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """function setsorgets the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """function setsorgets the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """this function returns the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """function prints the rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """this function updates the rectangle.

        Args:
            *args (ints variable): the new attribute values.
                - first args represents id attribute
                - second args represents width attribute
                - third args represent height attribute
                - fourth args represents x attribute
                - firth args represents y attribute
            **kwargs (dict variable):key or value pairs of attributes.
        """
        if args and len(args) != 0:
            ax = 0
            for arg in args:
                if ax == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif ax == 1:
                    self.width = arg
                elif ax == 2:
                    self.height = arg
                elif ax == 3:
                    self.x = arg
                elif ax == 4:
                    self.y = arg
                ax += 1

        elif kwargsx and len(kwargsx) != 0:
            for kx, vx in kwargsx.items():
                if kx == "id":
                    if vx is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = vx
                elif kx == "width":
                    self.width = vx
                elif kx == "height":
                    self.height = vx
                elif kx == "x":
                    self.x = vx
                elif kx == "y":
                    self.y = vx

    def to_dictionary(self):
        """this function returns dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """this returns print() and str() representation of the rectangle."""
        return .format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
