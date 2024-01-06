#!/usr/bin/python3
def max_integer(my_list=[]):
    maxValue = 0
    if not my_list: return None
    else:
        for i in range(0, len(my_list)):
            if i < len(my_list) - 1:
                if my_list[i] >= my_list[i + 1]:
                    if maxValue >= my_list[i]:
                        continue
                    else:
                        maxValue = my_list[i]
                else:
                    maxValue = my_list[i + 1]
                    continue
        return maxValue
