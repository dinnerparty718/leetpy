from typing import List
from collections import defaultdict


'''
loop matric build hashmap

key = i+j
values = []

reverse list of values when key is even

'''


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        h = defaultdict(list)
        res = []

        for i in range(m):
            for j in range(n):
                h[i+j].append(mat[i][j])

        # print(h)

        for key, values in h.items():
            if key % 2 == 0:
                values.reverse()

            res.extend(values)

        return res


so = Solution()

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = [[1, 2], [3, 4]]

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

res = so.findDiagonalOrder(mat)


print(res)
