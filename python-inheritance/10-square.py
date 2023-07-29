#!/usr/bin/python3
"""
this module is a Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this class define a Rectangle.
    and have to method area size.
    """

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size ** 2
