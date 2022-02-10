'''
https://leetcode.com/problems/consecutive-characters/
'''


class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        stack = []

        next_diff_char = [n] * n

        for i, char in enumerate(s):
            while stack and s[stack[-1]] != char:
                idx = stack.pop()
                next_diff_char[idx] = i
            stack.append(i)

        res = 0

        for i in range(n):
            res = max(res, next_diff_char[i] - i)

        return res
