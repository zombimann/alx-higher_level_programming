#!/usr/bin/python3
""" This is a module with one class"""


class Square:
    """Show the definition and instantiation of a private attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """The private attribute 'size' is defined here.

            Args:
                 size (int): This represents the size of the square and is
                 passed from the module.
        """

        self.__size = size
        self.__position = position

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
        try:
            if type(value) != int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        except TypeError as err:
            pass
        except ValueError as err:
            pass
        finally:
            return err

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" " * (self.__position[0]) + "#" * self.__size)
