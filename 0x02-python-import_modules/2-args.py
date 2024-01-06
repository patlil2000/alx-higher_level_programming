#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv) - 1
    i = 0
    if num_arg == 0:
        print("{:d} arguments.".format(num_arg))
    elif num_arg == 1:
        print("{:d} argument:".format(num_arg))
    else:
        print("{:d} arguments:".format(num_arg))
    arg = sys.argv[1:]
    for x in arg:
        i += 1
        print("{:d}: {}".format(i, x))
