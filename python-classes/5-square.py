#!/usr/bin/python3

"""a class Square that defines a
square by: (based on 1-square.py)"""


class Square:
    """Raise Error using conditionals"""

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#"*self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")
