from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        i = 0
        j = len(s) - 1

        while i <= j:  # can be i < j in this case
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


so = Solution()

s = ["h", "e", "l", "l", "o"]

so.reverseString(s)

print(s)
