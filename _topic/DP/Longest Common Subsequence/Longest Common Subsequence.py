'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.


bottom up

text1 = abcde   m
text2 = ace     n

dp = [[0] * (n+1) for _ in range(m+1)] 


#! basecase
    0000
    0000
    0000
    
from right -> left  bottom -> up


#! recurrence
    if text1[i] = text2[j]
        dp[i][j] = dp[i+1][j+1]
    else:
    #! look for max(right, down)
        dp[i][j] = max(dp[i][j+1], dp[i+1][i]])

#! return dp[0][0]


'''


# own! yass
# recurrence relationship and intialize one more col and rows

# Time O(m*n)
# Space O(m*n)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    # look for the, right and down
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]


# own topdown with memo. Yas!


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        if m == 0 or n == 0:
            return 0

        memo = {}

        def dfs(i: int, j: int):

            if i == m or j == n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            cnt = 0

            if text1[i] == text2[j]:

                cnt += dfs(i+1, j+1) + 1
            else:
                cnt += max(dfs(i+1, j),  dfs(i, j+1))

            memo[(i, j)] = cnt
            return memo[(i, j)]

        return dfs(0, 0)


so = Solution()


text1 = "abcde"
text2 = "ace"


# text1 = "abc"
# text2 = "abc"


# text1 = "abc"
# text2 = "def"


# text1 = "bl"
# text2 = "yby"


res = so.longestCommonSubsequence(text1, text2)


print(res)
