from typing import List


# time O(m + n)
# space O(m + n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1.intersection(s2))


# two pointer
class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i, j = 0, 0

        res = []

        while i < len(nums1) and j < len(nums2):
            # remove duplicate

            while i + 1 < len(nums1) and nums1[i] == nums1[i+1]:
                i += 1
            while j + 1 < len(nums2) and nums2[j] == nums2[j+1]:
                j += 1

            if nums1[i] == nums2[j]:
                # optimzied only append if not (len(res) and num1[i] == res[len(res)-1])
                res.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return res

# two pointer from most vote


class Solution3:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if not (len(res) and nums1[i] == res[len(res)-1]):
                    res.append(nums1[i])
                i += 1
                j += 1

        return res


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]


# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]

so = Solution3()
res = so.intersection(nums1, nums2)


print(res)
