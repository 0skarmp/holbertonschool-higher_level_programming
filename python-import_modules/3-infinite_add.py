#!/usr/bin/python3
import sys
if __name__ == "__main__":
    infinite = 0
    for i in range(1, len(sys.argv)):
        infinite = infinite + int(sys.argv[i])
    print("{}".format(infinite))
