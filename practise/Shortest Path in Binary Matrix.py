from typing import List
from collections import deque


# n * n
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        n = len(grid)

        # not possible
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        def neighbors(i: int, j: int):
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1):
                if 0 <= I < n and 0 <= J < n and grid[I][J] != 1:
                    yield I, J

        cnt = 0

        q = deque([(0, 0)])
        visited = set((0, 0))

        while q:
            cnt += 1
            size = len(q)

            for _ in range(size):
                (i, j) = q.popleft()
                if i == n-1 and j == n-1:
                    return cnt

                for I, J in neighbors(i, j):
                    if (I, J) not in visited:
                        q.append((I, J))
                        visited.add((I, J))

        return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
grid = [[0, 1], [1, 0]]

so = Solution()

res = so.shortestPathBinaryMatrix(grid)

print(res)
