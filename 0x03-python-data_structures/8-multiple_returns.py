#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first_ch = sentence[0] if sentence else None
    return length, first_ch
