#!/usr/bin/python3
a = 1
b = 2
func = __import__("add_0")
print("{:d} + {:d} = {:d}".format(a, b, func.add(a, b)))
