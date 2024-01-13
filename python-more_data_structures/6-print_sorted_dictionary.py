#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    pictionary = sorted(a_dictionary.keys())
    for dic in pictionary:
        print("{}: {}".format(dic, a_dictionary[dic]))
