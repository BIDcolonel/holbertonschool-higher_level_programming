#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    resultMatrix = []
    for row in matrix:
        resultRow = []
        for value in row:
            resultRow.append(value ** 2)
        resultMatrix.append(resultRow)
    return resultMatrix
