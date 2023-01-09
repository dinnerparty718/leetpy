
# backward dp
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[None] * n for _ in range(m)]

        # seen = set()

        def dp(i, j):
            # out of band
            if i < 0 or j < 0:
                return 0

            if i == 0 and j == 0:
                return 1

            if memo[i][j] != None:
                return memo[i][j]

            res = 0

            res += dp(i-1, j)
            res += dp(i, j-1)

            memo[i][j] = res

            return memo[i][j]

        return dp(m-1, n-1)


# forwards dp

# time O(m*n)
# space O(m*n)
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i-1][j] + d[i][j-1]

        return d[m-1][n-1]


m = 3
n = 2

so = Solution2()
res = so.uniquePaths(m, n)


print(res)
