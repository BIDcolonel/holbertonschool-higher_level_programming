#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A representation of the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes instances

        Args:
            size (_type_): size of this Square
            x (int, optional): x of this Square. Defaults to 0.
            y (int, optional): y of this Square. Defaults to 0.
            id (_type_, optional): id of the object. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string info of this Square"""
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)
        return str_square + str_id + str_xy + str_size

    @property
    def size(self):
        """Size of this Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
# above this line: Task 10 and 11

    def update(self, *args, **kwargs):
        """Update method"""
        if args is not None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for index in range(len(args)):
                if list_atr[index] == 'size':
                    setattr(self, 'width', args[index])
                    setattr(self, 'height', args[index])
                else:
                    setattr(self, list_atr[index], args[index])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
# above this line: Task 12
