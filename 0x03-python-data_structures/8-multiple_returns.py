#!/usr/bin/python3
def multiple_returns(sentence):
    """multiple_returns - pythone mulity returns"""
    length = len(sentence)
    first_char = sentence[0] if length > 0 else "None"
    tup = length, first_char
    return(tup)
