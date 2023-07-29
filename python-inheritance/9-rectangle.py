#!/usr/bin/python3
"""
this module define a class geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    this class is inherits of BaseGeometry.
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        return self.__width * self.__height
