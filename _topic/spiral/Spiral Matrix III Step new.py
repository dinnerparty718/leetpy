from typing import List


# step 1,1,2,2,3,3,4,4,5,5,6,6,

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        i, j = rStart, cStart

        res = [[i, j]]

        if rows * cols == 1:
            return res

        for k in range(1, 2*rows * cols, 2):
            for dr, dc, step in ((0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)):
                for _ in range(step):
                    i += dr
                    j += dc

                    # if on the grid
                    if 0 <= i < rows and 0 <= j < cols:
                        res.append([i, j])
                        if len(res) == rows*cols:
                            return res


so = Solution()

rows = 5
cols = 6
rStart = 1
cStart = 4
res = so.spiralMatrixIII(rows, cols, rStart, cStart)

print(res)
