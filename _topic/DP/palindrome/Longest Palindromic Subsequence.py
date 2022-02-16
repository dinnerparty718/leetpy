'''
516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.



Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".


Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".



'''

#! todo

# https://leetcode.com/problems/longest-palindromic-subsequence/discuss/1096936/PYTHON-DP-FOR-DUMMIES


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}

        def dfs(s):
            if s not in memo:
                maxL = 0
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    maxL = max(maxL, 1 if i == j else 2 + dfs(s[i+1:j]))
                memo[s] = maxL
            return memo[s]

        return dfs(s)


so = Solution()

s = "bbbab"
res = so.longestPalindromeSubseq(s)

print(res)
