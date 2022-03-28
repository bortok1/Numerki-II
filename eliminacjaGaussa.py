import numpy as np
import basicMatrixFunctions as mf


def gaussStart(inputMatrix):
    if isPossible(inputMatrix):
        for column in range(0, len(inputMatrix)):
            inputMatrix = getOneInColumn(inputMatrix, column)
            inputMatrix = getZerosInColumn(inputMatrix[0], column)
    return inputMatrix


def isPossible(inputMatrix):
    return True


def getOneInColumn(inputMatrix, column):
    for row in range(column, len(inputMatrix)):
        if inputMatrix.item(row, column) != 0:
            if row != column:
                inputMatrix = mf.swapRow(inputMatrix, column, row)
            return mf.getOneInColumn(inputMatrix, column, row), row
    print("ZERA WIDZE :O")


def getZerosInColumn(inputMatrix, column):
    for row in range(0, len(inputMatrix)):
        if row != column:
            inputMatrix = mf.subtractionOfRows(inputMatrix, column, row)

    return inputMatrix
