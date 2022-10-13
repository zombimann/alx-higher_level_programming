#!/usr/bin/python3
""" This is a module with one class"""


class Square:
    """Show the definition and instantiation of a private attribute"""

    def __init__(self, size=0):
        """The private attribute 'size' is defined here.

            Args:
                 size (int): This represents the size of the square and is
                 passed from the module.
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """gets the value of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of __size

           Args:
                value (int): the new value representing the size
                   of the square.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
