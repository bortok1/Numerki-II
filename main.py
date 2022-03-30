import numpy as np
import eliminacjaGaussa as elGauss
import copy
import czyNieoznaczonyLubSprzeczny as ns


def main():

    # path = input("Podaj sciezke do pliku: ")
    for i in range(1, 11):
        path = "Test" + str(i)
        file = open(path, 'r')
        lines = file.readlines()
        N = lines[0].count(' ')
        matrix = np.zeros((N, N + 1))

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
