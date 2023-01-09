# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.


from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = top = 0
        right = bottom = n - 1

        output = [[None]*n for _ in range(n)]

        N = 1

        while left <= right and top <= bottom:

            # top, left -> right
            for col in range(left, right+1):
                output[top][col] = N
                N += 1

            top += 1

            # right, top -> bottom

            for row in range(top, bottom+1):
                output[row][right] = N
                N += 1

            right -= 1

            # bottom right -> left
            if top <= bottom:
                for col in reversed(range(left, right+1)):
                    output[bottom][col] = N
                    N += 1

                bottom -= 1

            # left bottom -> top
            if left <= right:
                for row in reversed(range(top, bottom+1)):
                    output[row][left] = N
                    N += 1
                left += 1

        return output


so = Solution()

n = 3

res = so.generateMatrix(3)

print(res)
