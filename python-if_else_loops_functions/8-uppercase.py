#!/usr/bin/python3
def uppercase(str):
    str_upper = ""
    for char in str:
         if ord('a') <= ord(char) <= ord('z'):
            char = ord(char) - 32
            str_upper += chr(char)
         else:
            str_upper += char
    print("{}".format(str_upper))
