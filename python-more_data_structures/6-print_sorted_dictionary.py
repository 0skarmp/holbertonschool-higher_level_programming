#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    in_order = sorted(a_dictionary)
    for i in in_order:
        print(i+':'+' '+ str(a_dictionary[i]))
