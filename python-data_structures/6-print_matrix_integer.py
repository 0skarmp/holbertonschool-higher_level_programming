#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for number in matrix:
        for x, v in enumerate(number):
            if x != len(number) - 1:
                print("{:d}".format(v), end=" ")
            else:
                print("{:d}".format(v), end="")
        print()
