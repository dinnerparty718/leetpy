from typing import List


# reduce serach space
# Time O(m+n)
# space O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i, j = m-1, 0

        while j < n and i >= 0:

            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                j += 1

            else:
                i -= 1

        return False

# Divide and Conquer

# todo


class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        def search(left, up, right,  down):
            # invalid matrix
            if left > right or up > down:
                return False

            # impossible
            elif target > matrix[down][right] or target < matrix[up][left]:
                return False

            mid = left + (right-left) // 2

            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            return search(left, row, mid-1, down) or search(mid+1, up, right, row-1)

        return search(0, 0, n-1, m-1)


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

target = 24


so = Solution2()


res = so.searchMatrix(matrix, target)


print(res)
