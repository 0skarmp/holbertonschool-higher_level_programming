#!/usr/bin/python3
"""
read and print the contents of the specified text file.
"""


def read_file(filename=""):
    """give the permission for read the file"""

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
