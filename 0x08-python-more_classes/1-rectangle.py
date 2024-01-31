#!/usr/bin/python3
"""Define an empty class"""


class Rectangle:
    """Represent a rectangle."""


    def __init__(self, width=0, height=0):
        """Initialize the first instance of a Rectangle

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """this function get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """this function set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """this function get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """this function set the hight of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
