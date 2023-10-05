#!/usr/bin/python3
def matrix_divided(matrix, div):
    if int(div) == 0:
        raise ZeroDivisionError("div must be a number")
    if (isinstance(div, int) or isinstance(div, float)) is False:
        raise TypeError("div must be a number")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row]):
        raise TypeError("matrix must be a matrix (list of lists) of"
                "integers/float")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
