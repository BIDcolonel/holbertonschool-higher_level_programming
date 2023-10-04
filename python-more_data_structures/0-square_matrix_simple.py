#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    resultMatrix = []
    for row in matrix:
        result_row = []
        for value in row:
            result_row.append(value ** 2)
        resultMatrix.append(result_row)
    return resultMatrix
