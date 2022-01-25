from typing import List

# own
# time O(MN)
# space O(M+N)


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zero = set()
        col_zero = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M = len(matrix)
        N = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
so = Solution()

so.setZeroes(matrix)


print(matrix)
