#!/usr/bin/python3
def max_integer(my_list=[]):
    """max_integer - maxmumm integer"""
    if len(my_list) == 0:
        return ("None")
    x = my_list[0]
    for i in my_list:
        if i > x:
            x = i
            return (x)
