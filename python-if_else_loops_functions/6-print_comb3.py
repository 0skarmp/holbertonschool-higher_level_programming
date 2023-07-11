#!/usr/bin/python3
for i in range(9):
    for j in range(i+1, 10):
        if i == 8 and j == 9:
            print("{:02d}".format(i * 10 + j))
        else:
            print("{:02d}, ".format(i * 10 + j), end="")
