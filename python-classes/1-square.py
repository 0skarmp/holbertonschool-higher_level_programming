#!/usr/bin/python3
"""
This module defines an empty class Square that represents a square.
"""


class Square:
    """
    This is the Square class.
    It represents a square with private attributes.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
