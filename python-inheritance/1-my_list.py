#!/usr/bin/python3
"""
this method define a my list.
"""


class MyList(list):
    """
    this is a class list.
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
