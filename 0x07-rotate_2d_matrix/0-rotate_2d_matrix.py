#!/usr/bin/python3
'''2D Matrix rotation'''


def find_matrix_transpose(matrix):
    '''finds transpose of a given matrix'''
    size = len(matrix)
    for i in range(size):
        for j in range(i, size):
            if (i != j):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp


def rotate_2d_matrix(matrix):
    '''rotates a 2d matrix 9 degrees clockwise'''
    size = len(matrix)
    find_matrix_transpose(matrix)
    for row in range(size):
        start = 0
        end = size - 1
        while start < end:
            temp = matrix[row][start]
            matrix[row][start] = matrix[row][end]
            matrix[row][end] = temp
            start += 1
            end -= 1
