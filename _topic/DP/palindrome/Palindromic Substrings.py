'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.


Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        count = 0

        for i in range(n):
            # odd
            l, r = i, i
            while 0 <= l and r < n and s[l] == s[r]:
                count += 1

                l -= 1
                r += 1

            l, r = i, i+1
            while 0 <= l and r < n and s[l] == s[r]:
                count += 1

                l -= 1
                r += 1

        return count


so = Solution()

s = "aaa"

res = so.countSubstrings(s)

print(res)
