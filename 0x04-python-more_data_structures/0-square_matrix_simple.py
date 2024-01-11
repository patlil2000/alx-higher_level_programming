#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for item in matrix:
        for x in item:
            new_matrix.append(x**2)
    return new_matrix
