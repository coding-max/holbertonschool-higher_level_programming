#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    "prints a matrix of integers"

    row_len = len(matrix)
    col_len = len(matrix[0])

    for i in range(row_len):
        for j in range(col_len):
            if j != col_len - 1:
                print("{:d}".format(matrix[i][j]), end=' ')
            else:
                print("{:d}".format(matrix[i][j]), end='')
        print("")
