from collections import Counter
from typing import List

# time O(m + n)
# space O(m + n)

# own can be optimiz , build the result while looping throught list2


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = {}
        for n in nums1:
            if n in m:
                m[n] = (m[n][0] + 1, 0)
            else:
                m[n] = (1, 0)

        for n in nums2:
            if n in m:
                m[n] = (m[n][0], m[n][1] + 1)

        res = []

        for key, value in m.items():
            if value[1] != 0:
                if value[0] == value[1]:
                    res.extend([key] * value[0])
                else:
                    res.extend([key] * min(value[0], value[1]))

        return res


# put smaller list in the hash
class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        counter = Counter(nums1)
        res = []

        for n in nums2:
            if n in counter and counter[n] != 0:
                res.append(n)
                counter[n] -= 1

        return res


        # return [key for key, value in m.items() if value > 0]
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]
nums1 = [43, 85, 49, 2, 83, 2, 39, 99, 15, 70, 39, 27, 71, 3, 88, 5, 19,
         5, 68, 34, 7, 41, 84, 2, 13, 85, 12, 54, 7, 9, 13, 19, 92]
nums2 = [10, 8, 53, 63, 58, 83, 26, 10, 58, 3, 61, 56, 55, 38, 81, 29, 69, 55, 86,
         23, 91, 44, 9, 98, 41, 48, 41, 16, 42, 72, 6, 4, 2, 81, 42, 84, 4, 13]

so = Solution()
res = so.intersect(nums1, nums2)


print(res)
