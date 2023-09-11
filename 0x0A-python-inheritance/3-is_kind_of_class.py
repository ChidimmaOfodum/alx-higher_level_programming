#!/usr/bin/python3

""" Module that defines a function"""


def is_kind_of_class(obj, a_class):
    """returns whether a class is an instance of an object
     Args:
        obj (any): object
        a_class (type): class
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    return isinstance(obj, a_class)
