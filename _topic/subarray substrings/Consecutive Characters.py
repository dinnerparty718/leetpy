'''
https://leetcode.com/problems/consecutive-characters/

The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

 

find right boundary using stack

r = [ n ] * n  default to n if not found



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
