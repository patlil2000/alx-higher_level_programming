#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv[1:]
    result = 0
    for x in arg:
        result += int(x)
    print("{:d}".format(int(result)))
