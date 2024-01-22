#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value) >= 0 or int(value) < 0:
            print("{}".format(value))
            return True
    except ValueError:
        return False
