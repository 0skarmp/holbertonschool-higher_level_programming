#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy_ls = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return new_list
    else:
        copy_ls[idx] = element
        return copy_ls
