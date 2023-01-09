# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element. # !important  preceding

# input without *


class Solution0:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}

        return first_match and self.isMatch(s[1:], p[1:])


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            # optoin1: remove the patter 0 or multiple
            # option2: delete current match one
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])


# bottom up
# https://leetcode-screenshot-yy.s3.us-west-1.amazonaws.com/regex_match.png
#
# time O(m*n)
# space O(m*n)
# initalize m*n array
class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[0][0] = True

        # row, col 0 are False, Except
        for j in range(1, len(dp[0])):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if p[j-1] in {s[i-1], '.'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] in {s[i-1], '.'}:
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]

        return dp[-1][-1]


# dp going right->left
# hard to understand
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:

        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]

        dp[-1][-1] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                # print(f'i: {i} j: {j}')
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]


so = Solution1()

s = 'aa'
p = 'a*'
# p = 'a'
# p = "c*a*b"
# p = ".*"
res = so.isMatch(s, p)

print(res)
