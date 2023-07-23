#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    numbers = 0
    for i in range(x):
        try:
            print(my_list[1], end="")
            numbers += 1
        except TypeError:
            break
    print()
    return numbers
    
