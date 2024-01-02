#!/usr/bin/python3
def islower(c):
    if c == '' and c == ' ':
        return 0
    else:
        return 'a' <= c <= 'z'
