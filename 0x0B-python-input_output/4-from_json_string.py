#!/usr/bin/python3

"""A module that defines from_json_string"""
import json


def from_json_string(my_str):
    """A function that decodes a json string"""
    return json.loads(my_str)
