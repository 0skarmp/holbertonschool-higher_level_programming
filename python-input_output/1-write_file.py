#!/usr/bin/python3
"""
this function define an speciefic text file
"""


def write_file(filename="", text=""):
    """
    this is a method.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
