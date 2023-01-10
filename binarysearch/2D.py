'''
1. 2D to 1D, binary search
lo, hi = 0, m*n -1


create helper function go translate mid back to i,j

i , j = mid // n , mid % n

time O(log(m*n))
space  O(1)

2. bottom left, top right

'''


from typing import (
    List,
)


class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        # write your code here
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m * n - 1

        while l < r:
            mid = l + (r - l) // 2
            value = matrix[mid // n][mid % n]
            if value == target:
                return True
            elif value > target:
                r = mid - 1
            else:
                l = mid + 1

        if matrix[r // n][r % n] == target:
            return True
        return False
        # end condition l == r


so = Solution()
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

target = 3

res = so.search_matrix(matrix,  target)
