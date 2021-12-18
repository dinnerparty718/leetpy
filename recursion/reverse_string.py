from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(l: int, r: int, s: List[str]):

            if l >= r:
                return

            s[l], s[r] = s[r], s[l]

            reverse(l+1, r-1, s)

        reverse(0, len(s)-1, s)


so = Solution()

s = ["h", "e", "l", "l", "o"]


so.reverseString(s)


print(s)
