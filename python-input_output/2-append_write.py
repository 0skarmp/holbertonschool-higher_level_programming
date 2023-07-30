#!/usr/bin/python3
"""
this function define 'appends'
"""


def append_write(filename="", text=""):
    """
    this is a method that add text
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
