from itertools import zip_longest

# own


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        for n1, n2 in zip_longest(v1, v2, fillvalue=0):

            n1 = int(n1)
            n2 = int(n2)

            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1

        return 0

# leetcode


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        n1 = len(v1)
        n2 = len(v2)

        for i in range(max(n1, n2)):
            i1 = int(v1[i]) if i < n1 else 0
            i2 = int(v2[i]) if i < n2 else 0

            if i1 != i2:
                return 1 if i1 > i2 else -1

        return 0


so = Solution()

version1 = "1.01"
version2 = "1.001"


version1 = '1.0.1'
version2 = '1'

res = so.compareVersion(version1, version2)
print(res)
