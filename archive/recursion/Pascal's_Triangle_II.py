from typing import List
from functools import lru_cache


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex + 1
        res = [1] * n

        @lru_cache(maxsize=None)
        def getVal(i, j):
            if j == 1 or j == i:
                return 1
            if i == 1:
                return 1

            return getVal(i-1, j) + getVal(i-1, j-1)

        for i in range(1, n-1):
            res[i] = getVal(n, i+1)

        return res


so = Solution()
rowIndex = 24

res = so.getRow(rowIndex)


print(res)
