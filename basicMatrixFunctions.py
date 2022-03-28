import numpy as np


def swapRow(inputMatrix, row1, row2):
    matrixRow = inputMatrix[row1]
    inputMatrix[row1] = inputMatrix[row2]
    inputMatrix[row2] = matrixRow
    return inputMatrix


def getOneInColumn(inputMatrix, column, row):
    inputMatrix[row] = np.true_divide(inputMatrix[row], inputMatrix.item(row, column))
    return inputMatrix


def subtractionOfRows(matrix, minuend, subtrahend):
    matrix[subtrahend] = np.subtract(matrix[subtrahend], np.multiply(matrix[minuend], matrix.item(subtrahend, minuend)))
    return matrix

