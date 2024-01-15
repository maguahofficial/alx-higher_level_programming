#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """s is a base model.

    class represents the "base"for all other classes in project 0x0C*.

    private Class Attributes:
        __nb_objectvrb (int variable): Numb of instantiated bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """this function initializes a new Base.

        Args:
            id (int variable):identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """this function returns the (JSON) serialization of a list of dicts.

        Args:
            list_dictionaries (list variable):list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """this function prints the (JSON) serialization of a list of objects to a file.

        Args:
            list_objs (list variablw):list of inherited Base instances.
        """
        filenamex = cls.__name__ + ".json"
        with open(filenamex, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """this function returns the deserialization of a (JSON) string.

        Argments:
            json_string (str variable):(JSON) str representation of a list of dicts.
        Returns:
            if (json_string) is None/empty - an empty list.
            Otherwise - it returns python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """this function returns a class instantied from a dictionary
        of attributes.

        Args:
            **dictionary (dict variable): the Key/value pairs of
            attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """this function returns list of classes instantiated from a
        file of (JSON) strings.

        tjis reads from `<cls.__name__>.json`.

        Returns:
            If file does not exist - returns an empty list.
            Otherwise - returns a list of instantiated classes.
        """
        filenamex = str(cls.__name__) + ".json"
        try:
            with open(filenamex, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """this function writes the (CSV) serialization of a
        list ofobjects to a file.

        Args:
            list_objs (list variable): list of inherited base instances.
        """
        filenamex = cls.__name__ + ".csv"
        with open(filenamex, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """this function eturns a list of classes
        instantiated from a CSV file.

        reads from `<cls.__name__>.csv`.

        Returns:
            If file does not exist - it returns an empty list.
            Otherwise - it will return a list of instantiated classes.
        """
        filenamex = cls.__name__ + ".csv"
        try:
            with open(filenamex, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """this function draws a rectangle and Square using the turtle module.

        Args:
            list_rectangles (list variable):list of Rectangle objects to draw.
            list_squares (list variable):list of Square objects to draw.
        """
        turtx = turtle.Turtle()
        turtx.screen.bgcolor("#b7312c")
        turtx.pensize(3)
        turtx.shape("turtle")

        turtx.color("#ffffff")
        for rectx in list_rectangles:
            turtx.showturtle()
            turtx.up()
            turtx.goto(rectx.x, rectx.y)
            turtx.down()
            for ix in range(2):
                turtx.forward(rect.width)
                turtx.left(90)
                turtx.forward(rect.height)
                turtx.left(90)
            turtx.hideturtle()

        turtx.color("#b5e3d8")
        for sqx in list_squares:
            turtx.showturtle()
            turtx.up()
            turtx.goto(sqx.x, sqx.y)
            turtx.down()
            for ix in range(2):
                turtx.forward(sq.width)
                turtx.left(90)
                turtx.forward(sq.height)
                turtx.left(90)
            turtx.hideturtle()

        turtle.exitonclick()
