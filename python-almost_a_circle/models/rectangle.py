#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A representation of the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes instances

        Args:
            width (int): width of this Rectangle
            height (int): height of this Rectangle
            x (int, optional): x of this Rectangle. Defaults to 0.
            y (int, optional): y of this Rectangle. Defaults to 0.
            id (_type_, optional): id of the object. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width of this Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Height of this Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """X of this Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Y of this Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value
# above this line: Task 2

    def validate_integer(self, name, value, eq=True):
        """Method for validating the value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
# above this line: Task 3

    def area(self):
        """Returns area of this Rectangle"""
        return self.width * self.height
# above this line: Task 4

    def display(self):
        """Displays a Rectangle"""
        rectangle = self.y * "\n"
        for index in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"
        print(rectangle, end='')
# above this line: Task 5 and 7

    def __str__(self):
        """Return string info of this Rectangle"""
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)
        return str_rectangle + str_id + str_xy + str_wh
# above this line: Task 6

    def update(self, *args, **kwargs):
        """Update method"""
        if args is not None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for index in range(len(args)):
                setattr(self, list_atr[index], args[index])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
# above this line: Task 8 and 9

    def to_dictionary(self):
        """Returns dictionary representation of this class"""
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}
        for key in list_atr:
            dict_res[key] = getattr(self, key)
        return dict_res
# above this line: Task 13
