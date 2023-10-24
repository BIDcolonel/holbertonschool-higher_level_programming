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
