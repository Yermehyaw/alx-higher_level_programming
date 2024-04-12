#!/usr/bin/python3

"""
Module Imported: None
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix by a given value

    Attributes:
    matrix (list): A 2d matrix
    div (int): Value to divide matrix

    Return:
    A new matrix

    """

    # Gaurding div
    if div is None:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Guarding matrix
    # Check if matrix is a list
    if matrix is None or type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \
        integers floats")

    # Check if matrix is a list of lists
    for row in matrix:
        if not isinstance(row, list):  # is it a 2d matrix?
            raise TypeError("matrix must be a matrix (list of lists) of \
                    integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
                    integers/floats")

    #  Check if all rows are of equal length
    for i in range(len(matrix)):
        try:
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must \
                have the same size")
        except IndexError:  # matrix[i + 1] exceeded maximum matrix index
            pass

    # Divide matrix by div
    new_matrix = []
    for row in matrix:
        sub_matrix = []
        for element in row:
            sub_matrix.append(round(element / div, 2))
        new_matrix.append(sub_matrix)
    return new_matrix
