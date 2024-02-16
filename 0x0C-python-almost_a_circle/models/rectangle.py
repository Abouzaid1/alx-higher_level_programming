#!/usr/bin/python3
"""The rectangle moule"""
from models.base import Base


class Rectangle():
    def __init__(self, width, height, x=0, y=0, id=None):
        """Construct"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.width = value

    @property
    def height(self):
        """get the height"""
        return self.height

    @height.setter
    def height(self, value):
        self.height = value

    @property
    def x(self):
        """get the x"""
        return self.x

    @x.setter
    def x(self, value):
        self.x = value

    @property
    def y(self):
        """get the y"""
        return self.y

    @y.setter
    def y(self, value):
        self.y = value
