from typing import List


# exceee limit

# todo

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        res = []
        cur = []

        for idx_sum in range(m + n - 1):

            cur.clear()

            #! how to figure out the head
            for i in range(m + n - 1):
                j = idx_sum - i
                if 0 <= i < m and 0 <= j < n:
                    cur.append(mat[i][j])

            if idx_sum % 2 == 0:

                res.extend(cur[::-1])
            else:
                res.extend(cur)

        return res


so = Solution()

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = [[1, 2], [3, 4]]

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

res = so.findDiagonalOrder(mat)


print(res)
