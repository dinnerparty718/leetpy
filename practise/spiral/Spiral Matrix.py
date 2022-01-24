from typing import List


# https://www.youtube.com/watch?v=BJnMZNwUk1M

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        left = top = 0
        right = n-1  # 1
        bottom = m-1
        output = []

        while left <= right and top <= bottom:

            # top l -> r

            for col in range(left, right+1):
                output.append(matrix[top][col])

            top += 1

            # right t->b

            for row in range(top, bottom+1):
                output.append(matrix[row][right])

            right -= 1

            # bottom r -> l
            if not (top <= bottom and left <= right):
                break

            for col in reversed(range(left, right+1)):
                output.append(matrix[bottom][col])

            bottom -= 1

            for row in reversed(range(top, bottom+1)):
                output.append(matrix[row][left])

            left += 1

        return output


so = Solution()

#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix = [[1, 2], [3, 4]]

res = so.spiralOrder(matrix)


print(res)
