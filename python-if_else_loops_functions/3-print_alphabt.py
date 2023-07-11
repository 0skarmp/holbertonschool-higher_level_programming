#!/usr/bin/python3
for letter in range(97, 123):
    if(chr(letter) != 'q' and chr(letter) != 'e'):
        print("{:s}".format(chr(letter)), end ="")
