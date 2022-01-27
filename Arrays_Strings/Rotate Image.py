from typing import List

# rotate index change
# i, j -> j,(n-1-i)

# own
# swap 1 along forward /
# swap 2 along vertical, i, up->down


# leed code
# transposed via anti-diagonal
# reversed along j  left->right

# Time O(N) to transpose

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        def swapMirror(i: int, j: int):
            matrix[i][j], matrix[n-1-j][n-1 -
                                        i] = matrix[n-1-j][n-1-i], matrix[i][j]

        def swapHorizontal(i: int, j: int):
            matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

        # swap along diagonal

        end = n - 1
        row = 0

        while end > 0:
            for col in range(end):
                swapMirror(row, col)
            end -= 1
            row += 1

        # swap along mid row

        stop = n // 2

        for i in range(stop):
            for j in range(n):
                swapHorizontal(i, j)


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix = [[1, 2], [3, 4]]

so = Solution()

so.rotate(matrix)


for row in matrix:
    print(row)
