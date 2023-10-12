#!/usr/bin/python3
"""Defines a class TestMaxInteger for max_integer([...])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test class that defines test cases for the max_integer function.
    """
    def test_positive_integers(self):
        """
        Test for positive integers
        """
        test_list1 = [1, 2, 3, 4]
        test_list2 = [ 4, 1, 2, 3]
        test_list3 = [1, 2, 4, 2, 3]

        self.assertEqual(max_integer(test_list1), 4)
        self.assertEqual(max_integer(test_list2), 4)
        self.assertEqual(max_integer(test_list3), 4)

    def test_negative_integers(self):
        """
        Test for negative integers
        """
        test_list1 = [-91, -31, -4, -2]
        test_list2 = [-2, -91, -31, -4]
        test_list3 = [-91, -123, -2, -31, -4]

        self.assertEqual(max_integer(test_list1), -2)
        self.assertEqual(max_integer(test_list2), -2)
        self.assertEqual(max_integer(test_list3), -2)

    def test_pos_neg_integers(self):
        """
        Test for positive and negative integers
        """
        test_list = [-9, -14, 23, 98, 0, -9, -100, -1]
        self.assertEqual(max_integer(test_list), 98)

    def test_empty_list(self):
        """
        Test for an empty list
        """
        test_list = []
        self.assertIsNone(max_integer(test_list), None)
