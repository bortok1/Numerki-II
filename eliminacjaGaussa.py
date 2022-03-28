import basicMatrixFunctions as mf
import math


def gaussStart(inputMatrix):
    for column in range(0, len(inputMatrix)):
        inputMatrix = getOneInColumn(inputMatrix, column)
        inputMatrix = getZerosInColumn(inputMatrix, column)
    return inputMatrix


def getOneInColumn(inputMatrix, column):
    for row in range(column, len(inputMatrix)):
        if not math.isclose(0, math.fabs(inputMatrix.item(row, column)), abs_tol=1e-14):
            if row != column:
                inputMatrix = mf.swapRow(inputMatrix, column, row)
            return mf.getOneInColumn(inputMatrix, column)
    print("")
    print("Układ może być nieoznaczony!")
    print("")
    return inputMatrix


def getZerosInColumn(inputMatrix, column):
    for row in range(0, len(inputMatrix)):
        if row != column:
            inputMatrix = mf.subtractionOfRows(inputMatrix, column, row)

    return inputMatrix
