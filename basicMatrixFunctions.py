import numpy as np
import copy


def swapRow(inputMatrix, row1, row2):
    matrixRow = copy.copy(inputMatrix[row1])
    inputMatrix[row1] = inputMatrix[row2]
    inputMatrix[row2] = matrixRow
    return inputMatrix


def getOneInColumn(inputMatrix, column):
    inputMatrix[column] = np.true_divide(inputMatrix[column], inputMatrix.item(column, column))
    return inputMatrix


def subtractionOfRows(matrix, minuend, subtrahend):
    matrix[subtrahend] = np.subtract(matrix[subtrahend], np.multiply(matrix[minuend], matrix.item(subtrahend, minuend)))
    return matrix

