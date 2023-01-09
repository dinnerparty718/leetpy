

from typing import List


'''
1 2 3
2
3

'''


# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# i = j


def transpose_diagonal(matrix: List[List[int]]):
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


def transpose_anti_diagonal(matrix: List[List[int]]):
    n = len(matrix)
    for i in range(n):
        for j in range(n-1-i):
            matrix[i][j], matrix[n-1-j][n-1 -
                                        i] = matrix[n-1-j][n-1-i], matrix[i][j]
            # print([(i, j), (n-1-j, n-1-i)])


def reflect(matrix: List[List[int]]):
    n = len(matrix)

    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j],  matrix[i][j]


def reflect_h(matrix: List[List[int]]):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]


# transpose_diagonal(matrix)
# reflect(matrix)
transpose_anti_diagonal(matrix)
reflect_h(matrix)

for row in matrix:
    print(row)
