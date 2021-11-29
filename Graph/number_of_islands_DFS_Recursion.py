# https://leetcode.com/problems/number-of-islands/discuss/345981/Python3Number-of-Islands-BFS-%2B-DFS
from typing import List


# time space O(M*N)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)

        return count

    def dfs(self, grid, i, j):
        grid[i][j] = 0  # mark visited

        for I, J in [(i + 1, j), (i - 1, j), (i, j+1), (i, j-1)]:
            if 0 <= I < len(grid) and 0 <= J < len(grid[0]) and grid[I][J] == '1':
                self.dfs(grid, I, J)


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
