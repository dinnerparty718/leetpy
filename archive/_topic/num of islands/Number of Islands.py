from typing import List
from collections import deque

# bfs
# dfs


# BFS
# time O(m*n)
# space O (min(m, n)) size of the queue  diagonal

# DFS
# time O(m*n)
# space O (m*n)) all island


# todo disjoint set but need to pivit the grid to 1D


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        cnt = 0

        def bfs(row: int, col: int):
            q = deque([(row, col)])

            while q:
                size = len(q)
                for _ in range(size):
                    i, j = q.popleft()

                    for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                        if 0 <= I < m and 0 <= J < n and grid[I][J] == "1":
                            q.append((I, J))
                            grid[I][J] = "0"

        def dfs(i: int, j: int):
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < m and 0 <= J < n and grid[I][J] == '1':
                    grid[I][J] = "0"
                    dfs(I, J)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "0"

                    dfs(i, j)
                    cnt += 1

        return cnt


so = Solution()

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


res = so.numIslands(grid)


print(res)
