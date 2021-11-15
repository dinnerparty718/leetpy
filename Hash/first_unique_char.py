from collections import Counter
# own solution


class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}

        # store the index

        for i, c in enumerate(s):
            if c in m:
                m[c] = (m[c][0], m[c][1]+1)
            else:
                m[c] = (i, 1)

        for i, count in m.values():
            if count == 1:
                return i

        return -1

# even faster


class Solution2:
    def firstUniqChar(self, s: str) -> int:
        m = Counter(s)

        for i, c in enumerate(s):
            if m[c] == 1:
                return i

        return -1


so = Solution()

s = "aabb"
print(so.firstUniqChar(s))
