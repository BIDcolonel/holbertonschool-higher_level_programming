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

    def test_to_json_string_additional(self):
        """ Test additional cases for to_json_string """
        data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, '[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]')

        empty_data = []
        empty_json_str = Base.to_json_string(empty_data)
        self.assertEqual(empty_json_str, "[]")

    def test_from_json_string_additional(self):
        """ Test additional cases for from_json_string """
        json_str = '[{"name": "Alice", "age": 30}, 42, "Hello"]'
        data = Base.from_json_string(json_str)
        self.assertEqual(data, [{"name": "Alice", "age": 30}, 42, "Hello"])

    def test_create_additional(self):
        """ Test additional cases for create """
        rect_dict = {"id": 1, "width": 10, "height": 20, "x": 0, "y": 0}
        rect_instance = Rectangle.create(**rect_dict)
        self.assertIsInstance(rect_instance, Rectangle)
        self.assertEqual(rect_instance.id, 1)
        self.assertEqual(rect_instance.width, 10)
        self.assertEqual(rect_instance.height, 20)

        square_dict = {"id": 2, "size": 5, "x": 2, "y": 3}
        square_instance = Square.create(**square_dict)
        self.assertIsInstance(square_instance, Square)
        self.assertEqual(square_instance.id, 2)
        self.assertEqual(square_instance.size, 5)

    def test_load_from_file_additional(self):
        """ Test additional cases for load_from_file """
        with open("Rectangle.json", "w") as file:
            file.write('[{"id": 1, "width": 15, "height": 25, "x": 0, "y": 0}]')

        loaded_rectangles = Rectangle.load_from_file()
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertEqual(loaded_rectangles[0].id, 1)
        self.assertEqual(loaded_rectangles[0].width, 15)
        self.assertEqual(loaded_rectangles[0].height, 25)

        with open("Square.json", "w") as file:
            file.write('[{"id": 2, "size": 8, "x": 2, "y": 3}]')

        loaded_squares = Square.load_from_file()
        self.assertIsInstance(loaded_squares[0], Square)
        self.assertEqual(loaded_squares[0].id, 2)
        self.assertEqual(loaded_squares[0].size, 8)

    def test_save_to_file_exceptions(self):
        """ Test exception handling in save_to_file """
        with self.assertRaises(TypeError):
            Square.save_to_file(None)

        with self.assertRaises(TypeError):
            Square.save_to_file([None])
