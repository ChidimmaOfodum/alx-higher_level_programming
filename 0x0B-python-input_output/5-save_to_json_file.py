#!/usr/bin/python3
"""A module that defines save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """A function that saves to a file using json"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
