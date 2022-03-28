import numpy as np
import eliminacjaGaussa as elGauss


def main():
    N = 3 # int(input("Podaj liczbe rownan: "))
    matrix = np.zeros((N, N + 1))
    print(matrix)
    path = "Test10" # input("Podaj sciezke do pliku: ")
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
    matrix = elGauss.gaussStart(matrix)
    print(matrix)


if __name__ == '__main__':
    main()