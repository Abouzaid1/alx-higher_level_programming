#!/usr/bin/python3
"""Defines a square by: (based on 2-square.py)"""


class Square:
    """Square representation"""

    def __init__(self, size=0):
        """Initialize a square
        
        Args:
            size (int): size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")  
        self.__size = size  #: size of the square

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)
