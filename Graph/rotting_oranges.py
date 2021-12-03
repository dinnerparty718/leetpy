from typing import List
from collections import deque

# bfs
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.

# todo modify grid input directly


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        rotten = []
        numberOfFresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                if grid[i][j] == 1:
                    numberOfFresh += 1

        # there is no fresh left in the begining
        if numberOfFresh == 0:
            return 0

        q = deque(rotten)

        visited = set(rotten)

        minute = 0

        while q:
            size = len(q)
            minute += 1

            for _x in range(size):
                i, j = q.popleft()

                for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                    if 0 <= I < n and 0 <= J < m and grid[I][J] == 1 and (I, J) not in visited:
                        visited.add((I, J))
                        numberOfFresh -= 1
                        q.append((I, J))

        if numberOfFresh != 0:
            return -1

        return minute - 1


so = Solution()
grid = [[0, 2]]

res = so.orangesRotting(grid)


print(res)
