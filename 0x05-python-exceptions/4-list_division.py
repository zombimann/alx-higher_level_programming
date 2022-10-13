#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element-wise"""
    results = []
    try:
        for i in range(list_length):
            result = 0
            try:
                result = my_list_1[i] / my_list_2[i]
            except (TypeError, ValueError):
                print("wrong type")
            except ZeroDivisionError:
                print("division by 0")
            finally:
                results.append(result)
    except IndexError:
        print("out of range")
    return results
