#!/usr/bin/python3

def no_c(my_string):
    output = my_string.translate({ord(i): None fori in 'cC'})
    return output
