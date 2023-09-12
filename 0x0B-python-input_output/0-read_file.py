#!/usr/bin/python3
"""A module that reads a file"""


def read_file(filename=""):
    """A function that reads a file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
