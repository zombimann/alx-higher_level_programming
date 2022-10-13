#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """ prints the first x elements of a list and only integers"""

    j = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            pass
        else:
            j += 1
    print()

    return j
