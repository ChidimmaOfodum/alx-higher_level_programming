#!/usr/bin/python3
"""Module that defines append_write"""


def append_write(filename="", text=""):
    """A function that appends to a file """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
