# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element. # !important  preceding


# dp[i][j] -> i is s j = pattern

# O((T+P)2^(t + P/2)
#
#
# m = row

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = s and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            # '' matches 'a*'
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))

        else:
            return first_match and self.isMatch(s[1:], p[1:])
