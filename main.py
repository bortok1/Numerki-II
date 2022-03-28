import numpy as np
import eliminacjaGaussa as elGauss
import copy
import czyNieoznaczonyLubSprzeczny as ns


def main():
    N = int(input("Podaj liczbe rownan: "))
    matrix = np.zeros((N, N + 1))
    path = input("Podaj sciezke do pliku: ")
    file = open(path, 'r')
    lines = file.readlines()
    count = 0
    for line in lines:
        numbers = line.split()
        for i in range(len(numbers)):
            matrix[count][i] = numbers[i]
        count += 1
    matrix = np.matrix(matrix)
    print(matrix)
    outputMatrix = elGauss.gaussStart(copy.copy(matrix))
    print(outputMatrix)
    print(ns.checkStart(matrix, outputMatrix))


if __name__ == '__main__':
    main()