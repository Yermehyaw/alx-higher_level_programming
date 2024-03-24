#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Squares all elements in a matrix
    Arguments:
    matrix: Matrix

    Return:
    mew_matrix:Edited copy of @matrix
    """
    if matrix is None:
        return None
    new_matrix = matrix[:]
    i = 0
    while i < len(matrix):
        new_matrix[i] = list(map(lambda x: x**2, new_matrix[i]))
        i += 1
    return new_matrix
