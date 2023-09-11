#!/usr/bin/python3

""" Module that defines a class Mylist"""


def is_same_class(obj, a_class):
    """returns whether a class is an instance of an object
     Args:
        obj (any): object
        a_class (type): class
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    return type(obj) == a_class
