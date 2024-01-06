#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for char in my_string:
        if char.lower() != 'c':
            newString += char
        elif char.lower() == 'c':
            newString += ' '
    return newString
