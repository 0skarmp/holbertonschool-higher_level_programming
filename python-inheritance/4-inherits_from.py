#!/usr/bin/python3
"""
this is module define a sub class.

"""


def inherits_from(obj, a_class):
    """
    this is a method
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)        
