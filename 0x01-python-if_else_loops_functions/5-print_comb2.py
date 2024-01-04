#!/usr/bin/python3
for x in range(0, 99):
    formatted = str(x).zfill(2)
    print("{}, ".format(formatted), end='')
print("99")
