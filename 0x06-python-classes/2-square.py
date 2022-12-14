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
