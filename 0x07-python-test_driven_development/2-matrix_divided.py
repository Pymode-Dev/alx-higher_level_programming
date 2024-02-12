#!/usr/bin/python3


def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError('div must be a number')
    if (matrix == [] or not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [item for row in matrix for item in row])):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    new_matrix = []
    for item in matrix:
        for i in item:
            t_mat = [round(i / div, 2) for i in item]
        new_matrix.append(t_mat)
    return new_matrix
