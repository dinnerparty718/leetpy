from typing import List
from collections import defaultdict


# native bfs or bellman ford
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        edges = []

        def neighbors(i: int, j: int):
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < m and 0 <= J < n:
                    yield (I, J)

        # for i in range(m):
        #     for j in range(n):
        #         for I, J in neighbors(i, j):
        #             diff = abs(heights[I][J] - heights[i][j])
        #             edges.append([(i, j), (I, J), diff])

        # for s, t, cost in g:
        #     print(s, t, cost)

        prev = [[float('inf')] * n for _ in range(m)]

        cur = [[float('inf')] * n for _ in range(m)]

        prev[0][0] = cur[0][0] = 0

        # for i in range(m*n - 1):
        #     for src, target, cost in edges:

        #         cur[target[0]][target[1]] = min(
        #             cur[target[0]][target[1]], max(prev[src[0]][src[1]], cost))

        #         # prev[src[0]][src[1]], cost

        #     prev = [row[:] for row in cur]

        for k in range(m*n - 1):
            for i in range(m):
                for j in range(n):
                    for I, J in neighbors(i, j):
                        cur[I][J] = min(cur[I][J], max(
                            prev[i][j], abs(heights[i][j] - heights[I][J])))
            prev = [row[:] for row in cur]

        return cur[m-1][n-1]


so = Solution()

#heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]

res = so.minimumEffortPath(heights)

print(res)
