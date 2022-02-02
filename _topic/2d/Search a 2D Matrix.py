from curses.ascii import SO
from typing import List


# todo check binary search

# https://leetcode.com/problems/search-a-2d-matrix/solution/

# own zig zag

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i, j = m-1, 0

        while 0 <= i < m and 0 <= j < n:
            curr = matrix[i][j]

            if curr == target:
                return True

            elif curr > target:
                i -= 1
            else:
                # curr < target
                j += 1

        return False


so = Solution()


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13

res = so.searchMatrix(matrix, target)

print(res)
