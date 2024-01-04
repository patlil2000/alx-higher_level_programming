#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        updated_num = abs(number)
        return updated_num % 10
    else:
        return number % 10
