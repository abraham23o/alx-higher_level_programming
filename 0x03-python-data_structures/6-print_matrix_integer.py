#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elem in range(len(row)):
            if elem == len(row) - 1:
                print(row[elem], end="")
            else:
                print(row[elem], end=" ")
        print()
