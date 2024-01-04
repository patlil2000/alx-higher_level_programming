#!/usr/bin/python3
def print_last_digit(number):
    updated_num = abs(number)
    last_digit = updated_num % 10
    print(last_digit, end='')
    return last_digit

    
