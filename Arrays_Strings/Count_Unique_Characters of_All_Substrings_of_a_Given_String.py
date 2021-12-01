
import string


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        res = 0

        for i, c in enumerate(s):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]

        for c in index:

            k, j = index[c]
            print(c, k, j)
            res += (len(s) - j) * (j - k)

        print(res)

        return res % (10**9 + 7)


s = "LEETCODE"

so = Solution()

res = so.uniqueLetterString(s)

print(res)
