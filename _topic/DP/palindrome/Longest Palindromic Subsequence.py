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


# https://www.youtube.com/watch?v=_nCsPn7_OgI

'''
does not need to be continous

dp = [ [0] * n for _ in range(n) ]

# todo

#! basecase
    
    1 0 0 0 
    0 1 0 0
    0 0 1 0
    0 0 0 1

    
    for sub_l in range(1, n+1):
        #! len == 1
        dp[i][i] = 1

#! recurrence
    len 1 - n
    
    
    for right in range(n):
        for left in range(right)

        
        
            if right - left <=2   #! len 2 or len 3
                dp[left][right] = s[left] == s[right]
            else:
                dp[left][right] =  s[right] == s[left] and dp[left + 1][right - 1]
                
            if dp[right][left]:
                cnt+=1
                
#! return dp[0][-1]  top row rightmost col



'''


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}

        def dfs(s):
            if s not in memo:
                maxL = 0
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    maxL = max(maxL, 1 if i == j else 2 + dfs(s[i+1:j]))  # dp[i+1][j-1]
                memo[s] = maxL
            return memo[s]

        return dfs(s)


so = Solution()

s = "bbbab"
res = so.longestPalindromeSubseq(s)

print(res)
