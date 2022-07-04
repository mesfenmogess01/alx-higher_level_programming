#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Makes copy of a list, replce element at certain index in copy
    while leaving originial unmodified.
    """
    tmp_list = my_list[:]
    if 0 <= idx < len(my_list):
        tmp_list[idx] = element
        return(tmp_list)
    return(my_list)
