#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    result = 0
    for i in my_list:
        result += i
    return result

