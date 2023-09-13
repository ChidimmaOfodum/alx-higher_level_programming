#!/usr/bin/python3
"""A module that defines class_to_json"""


def class_to_json(obj):
    result = {}
    for i in dir(obj):
        attr = getattr(obj, i)
        if i[:2] != '__' and not callable(attr):
            result[i] = attr
    return result
