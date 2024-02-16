#!/usr/bin/python3
"""The rectangle module"""
from models.base import Base


class Rectangle(Base):
    """the rectangle class"""

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """The area"""
        return self.__width * self.__height

    def display(self):
        """The stdout of the rectangle"""
        s = '\n' * self.__y + \
            (' ' * self.__x + '#' * self.__width + '\n') * self.__height
        print(s, end='')

    def __str__(self):
        """srt"""
        return "[{}] ({}) {}/{} - {}/{}". \
            format(type(self).name, self.id, self.__width,
                   self.__height, self.__x, self.__y)
