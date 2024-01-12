#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list)  # Use a set to keep only unique elements
    result = sum(unique_numbers)
    return result
