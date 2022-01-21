from typing import List


# intiilized 2d frist
# total number n*n
# set right, down, left, up boundaries
# while n>0  (last number is 1)
# left, right, top, down , update boundary


class Solution:
    def twoD_Array(self, n: int) -> List[List[int]]:
        res = [[None] * n for _ in range(n)]
        N = 1

        left, right = 0, n-1
        top, down = 0, n-1

        # print(res)

        while N <= n**2:
            # left->right
            for col in range(left, right + 1):
                res[top][col] = N
                N += 1

            # shrink top boundaries
            top += 1

            # top -> down
            for row in range(top, down+1):
                res[row][right] = N
                N += 1

            # shrink top boundaries
            right -= 1

            if top != down:
                # right -> left
                for col in reversed(range(left, right + 1)):
                    res[down][col] = N
                    N += 1

                down -= 1

            if left != right:
                # down -> top
                for row in reversed(range(top, down+1)):
                    res[row][left] = N

                    N += 1
                left += 1

        return res


so = Solution()

res = so.twoD_Array(4)


print(res)
