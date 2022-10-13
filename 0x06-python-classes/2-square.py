#!/usr/bin/python3
class Square:
    """Show the definition and instantiation of a private attribute"""

    def __init__(self, size=0):
        """The private attribute 'size' is defined here.

            Args:
                 size (int): This represents the size of the square and is
                 passed from the module.
        """

        try:
            float(size).is_integer()
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
            print("size must be an integer")