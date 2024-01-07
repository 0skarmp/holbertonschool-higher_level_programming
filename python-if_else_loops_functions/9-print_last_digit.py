#!/usr/bin/python3
def print_last_digit(number):
    LastDigit = abs(number) % 10
    print("{}".format(LastDigit), end="")
    return LastDigit
