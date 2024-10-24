import numpy as np

def separator(x):
    for i in range(x):
        if i % 2 == 0:
            print("=", end="")
        else:
            print("-", end="")
    print()


def perform_matrix_operations():
    matrix = np.array([ [0.1, 0, 0, 0.4],
                        [0.2, 0, 0, 0],
                        [0, 0.1, 0, 0.1],
                        [0, 0, 0.1, 0]])

    row_sums = np.sum(matrix, axis=1)
    row_probs = row_sums / np.sum(row_sums)
    test = np.cumsum(row_probs)
    #print(test)

    Y = np.copy(matrix)
    for row in range(4):
        row_sum = 0
        for col in range(4):
            row_sum += matrix[row][col]
        for col in range(4):
            Y[row][col] = Y[row][col] / row_sum

    for row in range(4):
        for col in range(3, -1, -1):
            if Y[row][col] > 0:
                col_sum = 0
                for i in range(col):
                    col_sum += Y[row][i]
                Y[row][col] += col_sum

    result = [[0 for _ in range(4)] for _ in range(4)]
    for _ in range(100000):
        rand = np.random.random()
        for row in range(4):
            if rand < test[row]:
                rand = np.random.random()
                for col in range(4):
                    if rand < Y[row][col]:
                        result[row][col] += 1
                        break
                break

    print("     >> Output:")
    for line in result:
        print("     >>", line)

def main():
    x = 135
    print()
    separator(x)
    print("[INFO] LABORATORY 4")
    separator(x)
    print("[INFO] 1. Matrix Operations")
    perform_matrix_operations()


if __name__ == '__main__':
    main()



"""
import random
import numpy as np

def separator(x):
    for i in range(x):
        if i % 2 == 0:
            print("=", end="")
        else:
            print("-", end="")
    print()


def perform_matrix_operations():
    iterations = 100000
    counts = [[0 for _ in range(4)] for _ in range(4)]

    for _ in range(iterations):
        r = random.random()
        if r < 0.5:
            x = random.random()
            if x < 0.1 / 0.5:
                counts[0][0] += 1
            else:
                counts[0][3] += 1
        elif r < 0.7:
            x = random.random()
            if x < 0.2 / 0.2:
                counts[1][0] += 1
        elif r < 0.9:
            x = random.random()
            if x < 0.1 / 0.2:
                counts[2][1] += 1
            else:
                counts[2][3] += 1
        else:
            x = random.random()
            if x < 0.1 / 0.1:
                counts[3][2] += 1

    for i in counts:
        print("     >> ", i)

def main():
    x = 135
    print()
    separator(x)
    print("[INFO] LABORATORY 4")
    separator(x)
    print("[INFO] 1. Matrix Operations")
    perform_matrix_operations()


if __name__ == '__main__':
    main()
"""