#!/usr/bin/python3
def no_c(my_string):
    listString = list(my_string)
    while "c" in listString:
        listString.remove('c')
    while "C" in listString:
        listString.remove('C')
    return "".join(listString)
