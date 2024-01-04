#!/usr/bin/python3
def uppercase(input_str):
    for x in input_str:
        ascii_code = ord(x)
        if not (ascii_code >= 97 and ascii_code <= 122):
            print("{}".format(x), end='')
        else:
            upper_char = chr(ascii_code - ord('a') + ord('A'))
            print("{}".format(upper_char), end='')
    print()
