#!/usr/bin/python3
"""Module for Base class"""
import json


class Base:
    """A representation of the base of our OOP hierarchy"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes instances

        Args:
            id (_type_, optional): id of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
# above this line: Task 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """List to JSON string"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
# above this line: Task 15

    @classmethod
    def save_to_file(cls, list_objs):
        """Save object in file"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))
# above this line: Task 16

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        if not json_string:
            return []
        return json.loads(json_string)
# above this line: Task 17

    @classmethod
    def create(cls, **dictionary):
        """Create an instance"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        if new:
            new.update(**dictionary)
        return new
# above this line: Task 18

    @classmethod
    def load_from_file(cls):
        """Return list of instance"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
# above this line: Task 19
