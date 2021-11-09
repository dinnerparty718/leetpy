# https://leetcode.com/problems/number-of-islands/discuss/345981/Python3Number-of-Islands-BFS-%2B-DFS
from typing import List
from collections import deque

# explicit stack
# visited set ? or flip the existing val from 1 to 0


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        stack = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    stack.append((i, j))
                    self.dfs(grid, stack)
                    count += 1
        return count

    def dfs(self, grid, stack):
        while stack:
            I, J = stack.pop()
            for i, j in (I + 1, J), (I - 1, J), (I, J+1), (I, J-1):
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    stack.append((i, j))
                    grid[i][j] = '0'


solution = Solution()


# grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

res = solution.numIslands(grid)


print(res)
