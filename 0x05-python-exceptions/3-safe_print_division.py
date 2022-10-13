#!/usr/bin/python3


def safe_print_division(a, b):
    """Divides 2 integers and prints the result"""
    result = None
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return result
    finally:
        print("Inside result: {}".format(result))
