#!/usr/bin/python3
"""The rectangle module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Construct"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """srt"""
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
