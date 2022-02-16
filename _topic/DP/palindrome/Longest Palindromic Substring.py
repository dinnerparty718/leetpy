'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.


'''


# time O(n^2)
# space O(1) expand from middle

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0

        for i in range(len(s)):
            # odd len
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l + 1

                r += 1
                l -= 1
            # even len

            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l + 1

                r += 1
                l -= 1

        return res


# time O(n^2)
# space o(n^2)

# topdown
class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass


so = Solution()

s = "babad"
res = so.longestPalindrome(s)
print(res)
