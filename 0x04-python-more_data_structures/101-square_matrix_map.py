#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = [[] for i in range(len(matrix))]
    for i in range(len(matrix)):
        new_matrix[i] = list((map(lambda x: x * x, matrix[i])))
    return new_matrix
