from typing import List
from functools import lru_cache

# wihtout cach
# time O(m*n)
# space O(1) use input array

# leet code


class Solution0:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

         # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1, m):
            obstacleGrid[i][0] = int(
                obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row
        for j in range(1, n):
            obstacleGrid[0][j] = int(
                obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + \
                        obstacleGrid[i][j-1]

        return obstacleGrid[m-1][n-1]


# turing planet
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        memo = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(grid: List[List[int]], i: int, j: int):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == 1:
                return 0

            if i == 0 and j == 0:
                return 1

            if memo[i][j]:
                return memo[i][j]

            res = 0

            res += dfs(grid, i-1, j)
            res += dfs(grid, i, j-1)

            memo[i][j] = res

            print(memo)

            return memo[i][j]

        return dfs(obstacleGrid, m-1, n-1)


class Solution2:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])

        @lru_cache(maxsize=None)
        def dp(r: int, c: int) -> int:
            if r == R - 1 and c == C - 1 and obstacleGrid[r][c] == 0:
                return 1
            if r >= R or c >= C or obstacleGrid[r][c] == 1:
                return 0
            return dp(r + 1, c) + dp(r, c + 1)

        return dp(0, 0)


so = Solution()

obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

res = so.uniquePathsWithObstacles(obstacleGrid)

print(res)
