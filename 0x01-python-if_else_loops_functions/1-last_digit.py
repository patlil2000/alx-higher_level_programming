#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if digit > 5:
    print(f"Last digit of {number:d} is {digit:d} and is greater than 5")
elif digit == 0:
    print(f"Last digit of {number:d} is {digit:d} and 0")
else:
    print(f"Last digit of {number:d} is {digit:d} and is less than 6 and 0")
