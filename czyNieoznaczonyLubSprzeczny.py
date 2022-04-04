import copy
import math


def checkStart(matrix, outputMatrix):
    for row in matrix:
        if not countEquation(copy.copy(row), outputMatrix):
            return "Układ równań jest sprzeczny."

    for n in range(0, math.floor(math.sqrt(outputMatrix.size))):
        if outputMatrix.item(n, math.floor(math.sqrt(outputMatrix.size))) == 0:
            return "Układ równań jest nieoznaczony."

    i = 0
    for row in outputMatrix:
        i += 1
        print("x", i, "=", round(row.item(0, row.size - 1), 10))
    return "Rozwiązane prawidłowo."


def countEquation(equation, xes):
    resoult = 0
    for number in range(0, equation.size - 1):
        resoult += (equation.item(0, number) * xes.item(number, equation.size - 1))

    # Default value of difference is 1e-09
    return math.isclose(resoult, equation.item(0, equation.size - 1))

