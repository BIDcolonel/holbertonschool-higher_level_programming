#!/usr/bin/python3
""" Module for test Base class """
import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO

class TestBaseMethods(unittest.TestCase):
    """ Suite to test Base class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test assigned id """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """ Test default id """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """ Test nb object attribute """
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """ Test nb object attributes and assigned id """
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        """ Test string id """
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """ Test accessing to private attributes """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_1(self):
        """ Test JSON file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_to_json_string_empty_list(self):
        """ Test to_json_string with an empty list """
        empty_list = []
        json_string = Base.to_json_string(empty_list)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_non_empty_list(self):
        """ Test to_json_string with a non-empty list """
        data = [{"key": "value"}, {"key2": "value2"}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json_string, '[{"key": "value"}, {"key2": "value2"}]')

    def test_save_to_file_empty_list(self):
        """ Test save_to_file with an empty list of objects """
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:
            json_data = file.read()
            self.assertEqual(json_data, "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass

    def test_from_json_string_empty_string(self):
        """ Test from_json_string with an empty JSON string """
        json_string = ""
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_valid_string(self):
        """ Test from_json_string with a valid JSON string """
        json_string = '[{"key": "value"}, {"key2": "value2"}]'
        result = Base.from_json_string(json_string)
        expected = [{"key": "value"}, {"key2": "value2"}]
        self.assertEqual(result, expected)

    def test_create_rectangle(self):
        """ Test create method with a dictionary to create a Rectangle instance """
        dictionary = {"width": 5, "height": 10, "x": 2, "y": 3, "id": 1}
        rectangle_instance = Rectangle.create(**dictionary)
        self.assertEqual(rectangle_instance.width, 5)
        self.assertEqual(rectangle_instance.height, 10)
        self.assertEqual(rectangle_instance.x, 2)
        self.assertEqual(rectangle_instance.y, 3)
        self.assertEqual(rectangle_instance.id, 1)

    def test_create_square(self):
        """ Test create method with a dictionary to create a Square instance """
        dictionary = {"size": 4, "x": 2, "y": 3, "id": 1}
        square_instance = Square.create(**dictionary)
        self.assertEqual(square_instance.size, 4)
        self.assertEqual(square_instance.x, 2)
        self.assertEqual(square_instance.y, 3)
        self.assertEqual(square_instance.id, 1)

    def test_load_from_file_non_existing_file(self):
        """ Test load_from_file with a non-existing JSON file """
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_empty_file(self):
        """ Test load_from_file with an empty JSON file """
        with open("Rectangle.json", "w") as file:
            file.write("")

        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

        try:
            os.remove("Rectangle.json")
        except:
            pass

    def test_create_with_empty_dictionary(self):
        """ Test create method with an empty dictionary """
        dictionary = {}
        new_instance = Base.create(**dictionary)
        self.assertIsNone(new_instance)
