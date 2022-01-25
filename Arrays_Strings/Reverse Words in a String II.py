from typing import List


# https://leetcode.com/problems/reverse-words-in-a-string-ii/solution/

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def resverseChar(i: int, j: int):
            s[i], s[j] = s[j], s[i]

        def reverseWord(start: int, end: int):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        l = 0
        r = len(s)-1

        while l < r:
            resverseChar(l, r)
            l += 1
            r -= 1

        start = 0

        for end in range(len(s)):
            if s[end] == ' ':
                l = start
                r = end - 1
                reverseWord(l, r)
                start = end + 1

        if start < len(s):
            l = start
            r = len(s)-1
            reverseWord(l, r)


so = Solution()

s = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
#s = ["a"]
res = so.reverseWords(s)

print(s)
