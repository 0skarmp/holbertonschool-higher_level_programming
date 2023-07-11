#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = ord(char) - 32
            upper += chr(char)
        else:
            upper += char
    print("{}".format(upper))
