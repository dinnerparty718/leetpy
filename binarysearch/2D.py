'''
1. 2D to 1D, binary search, standard template
lo, hi = 0, m*n -1


create helper function go translate mid back to i,j

i , j = mid // n , mid % n

time O(log(m*n))
space  O(1)

2. search from bottom left (m-1, 0)

time O(log(m + n))
space O(1)

'''


from typing import List


class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + ((right - left) >> 1)

            if matrix[mid // n][mid % n] < target:
                left = mid + 1
            elif matrix[mid // n][mid % n] > target:
                right = mid - 1
            else:
                return True

        return False


so = Solution()
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

target = 3

res = so.searchMatrix(matrix,  target)

print(res)


class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        i, j = m-1, 0

        while 0 <= i < m and j <= 0 < n:
            if matrix[i][j] < target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False


so = Solution()
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

target = 3

res = so.searchMatrix(matrix,  target)

print(res)
