'''
115. Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.



base cae

if t == '' return 1

if s == '' return 0

'''
# Time Space O(m*n)
# top down with memo Slow


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        m = len(s)
        n = len(t)

        def dfs(i: int, j: int):
            if j == n:
                return 1
            if i == m:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                cache[(i, j)] = dfs(i+1, j+1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i+1, j)

            return cache[(i, j)]

        return dfs(0, 0)


# bottom up
# yass!
# the backward ways
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [[0] * (n+1) for _ in range(m+1)]

        #! base case
        #! column reach the end, t == '' return 1
        #! row reach the end, s == '' there is nothing else to match return 0

        for i in range(m+1):
            dp[i][n] = 1

        # filling backwards
        # bottom up , right to left

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]

        return dp[0][0]


so = Solution()

s = "rabbbit"
t = "rabbit"
res = so.numDistinct(s, t)


print(res)
