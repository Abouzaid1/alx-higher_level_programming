#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if chr(c) == "q" or chr(c) == 'e':
        continue
    else:
   		print(chr(c), end='')
