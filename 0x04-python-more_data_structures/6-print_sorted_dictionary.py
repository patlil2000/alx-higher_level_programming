#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        print("No dictionary provided.")
        return
    sorted_dict =dict(sorted(a_dictionary.items()))
    for x in sorted_dict:
        value = a_dictionary[x]
        print("{}: {}".format(x, value))
