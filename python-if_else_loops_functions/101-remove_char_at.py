#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n <= len(str):
        remove = list(str)
        del remove[n]
        return ''.join(remove)
    else:
        return str
