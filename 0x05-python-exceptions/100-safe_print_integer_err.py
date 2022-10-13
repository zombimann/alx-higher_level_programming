#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """prints an integer"""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        print(f"Exception: {err}", file=sys.stderr)
        return False