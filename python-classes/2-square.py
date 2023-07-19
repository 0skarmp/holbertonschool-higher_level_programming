#!/usr/bin/python3
"""
This module defines an empty class Square that represents a square.
"""


class Square:
    """
    This is the Square class.
    It represents a square with private attributes.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
