from typing import List


# https://leetcode.com/problems/compare-version-numbers/solution/

# todo don't need to convert to number
#


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        def version_array(ver: str):
            res = ver.split('.')
            return [int(val) for val in res]

        def num_array_to_decimal(nums: List[int]):
            result = 0
            for num in nums:
                result = result*10 + num
            return result

        v1 = version_array(version1)
        v2 = version_array(version2)

        if len(v1) > len(v2):
            # pad v2
            v2 = v2 + [0] * (len(v1) - len(v2))
        else:
            # pad v2
            v1 = v1 + [0] * (len(v2) - len(v1))

        # print(v1, v2)
        # conver to decimal numbers

        ver1 = num_array_to_decimal(v1)
        ver2 = num_array_to_decimal(v2)

        if ver1 > ver2:
            return 1
        elif ver1 < ver2:
            return -1
        else:
            return 0


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')

        n1, n2 = len(nums1), len(nums2)

        # compare version

        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1

        return 0


so = Solution()


version1 = "0.1"
version2 = "1.1"
# version2 = "1.0.0"

res = so.compareVersion(version1, version2)

print(res)
