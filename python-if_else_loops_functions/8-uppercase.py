#!/usr/bin/python3
def uppercase(str):
    str_upper = ""
    if ord(str) >= 97 and ord(str) <= 122:
        str_upper += chr(ord(str)-32)
    else:
        str_upper += str
    print(str_upper)
