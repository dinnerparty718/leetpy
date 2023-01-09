from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]

        def get_nei(i: int, j: int):
            for i_diff, j_diff in directions:
                I = i + i_diff
                J = j + j_diff
                if 0 <= I < n and 0 <= J < n and grid[I][J] == 0:
                    yield (I, J)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        q = deque([(0, 0, 1)])
        visited = set((0, 0))

        target = (n-1, n-1)

        while q:
            i, j, distance = q.popleft()
            if (i, j) == target:
                return distance

            for I, J in get_nei(i, j):
                if (I, J) in visited:
                    continue
                visited.add((I, J))
                q.append((I, J, distance+1))

        return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]

so = Solution()

res = so.shortestPathBinaryMatrix(grid)

print(res)
