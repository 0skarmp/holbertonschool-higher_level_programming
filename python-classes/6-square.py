#!/usr/bin/python3
"""
This module defines an empty class Square that represents a square.
"""


class Square:
    """
    This is the Square class.
    It represents a square with private attributes.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.
        Args:
            size (int): The size of the square.
            position (int): the position of the square.
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(x, int) for x in value) or not all(x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for post0 in range(self.__position[1]):
                print()
            for column in range(self.__size):
                for colum in range(self.__position[0]):
                    print(" ", end="")
                for reglones in range(self.__size):
                    print("#", end="")
                print()
