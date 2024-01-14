#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    pictionary = {}
    for k, v in a_dictionary.items():
        if v % 2 == 0:
            pictionary[k] = v * 2
    return pictionary
