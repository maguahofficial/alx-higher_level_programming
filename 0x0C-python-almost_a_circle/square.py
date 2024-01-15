#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this class represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """this function nitializes a new Square.

        Args:
            size (int variable): The size of the new Square.
            x (int variable): x coordinate of the new Square.
            y (int variable): y coordinate of the new Square.
            id (int variable):identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """function Gets or sets the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """this function updates the Square.

        Args:
            *args (ints variable): New attribute values.
                - first args represents id attribute
                - second args represents size attribute
                - third args represents x attribute
                - fourth argument represents y attribute
            **kwargs (dict array): the new key/value pairs of attributes.
        """
        if args and len(args) != 0:
            ax = 0
            for arg in args:
                if ax == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif ax == 1:
                    self.size = arg
                elif ax == 2:
                    self.x = arg
                elif ax == 3:
                    self.y = arg
                ax += 1

        elif kwargsx and len(kwargsx) != 0:
            for kx, vx in kwargsx.items():
                if kx == "id":
                    if vx is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = vx
                elif kx == "size":
                    self.size = vx
                elif kx == "x":
                    self.x = vx
                elif kx == "y":
                    self.y = vx

    def to_dictionary(self):
        """function returns the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """function returns print() and str() representations of a Square."""
        return .format(self.id, self.x, self.y,
                                                 self.width)
