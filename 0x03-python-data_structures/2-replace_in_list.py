#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        for index, i in enumerate(my_list):
            if idx == index:
                my_list[index] = element
                break
    return my_list
