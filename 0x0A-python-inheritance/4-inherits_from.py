#!/usr/bin/python3

""" Module that defines a function"""


def inherits_from(obj, a_class):
    """returns whether a class is an instance of an object
     Args:
        obj (any): object
        a_class (type): class
    Returns:
        If obj is exactly an subclass of a_class - True.
        Otherwise - False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
