#!/usr/bin/python3
"""A module that defines load_from_json_file"""
import json


def load_from_json_file(filename):
    """A function that creates an obj from a json file"""
    with open(filename, 'r') as f:
        return json.load(f)
