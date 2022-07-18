#!/usr/bin/python3

def safe_print_integer(value):
    """ ptthon printing integer"""
    try:
        print("{:d}".format(value))
    except:
        return False
    return True
