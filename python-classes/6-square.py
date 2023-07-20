#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0, 0)):
        self._size = size
        self._position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if i <= 0:
                raise ValueError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        return self._size * self._size

    def my_print(self):
        if self._size == 0:
            print("")
        else:
            for i in range(self._size):
                for _ in range(self.position[1]):
                    print(" ", end="")
                for j in range(self._size):
                    if i == 0 or i == self._size - 1 or j == 0 or j == self._size - 1:
                        print("#", end="")
                    else:
                        if self.position[0] > 0:
                            print(" ", end="")
                        if self.position[1] > 0:
                            print(" ", end="")
                print("")
