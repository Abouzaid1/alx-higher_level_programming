#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    result = 0
    for i in range(count+1):
        if i>0:
            result += int(sys.argv[i])
print(result)
