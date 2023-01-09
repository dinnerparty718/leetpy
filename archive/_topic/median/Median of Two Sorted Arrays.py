from typing import List


# navive approach
# merge list and find middle

# binary search on the larger list
# calculation

# Time O(log m + n)

# find mid point
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        # nums1 is the longers

        x = len(nums1)
        y = len(nums2)

        if x == 0:
            mid = (y - 1) // 2

            if y % 2 == 1:
                return nums2[mid]
            else:
                return (nums2[mid] + nums2[mid+1]) / 2

        lo, hi = 0, x  # not index, insertion point

        while lo <= hi:
            partition_x = lo + (hi - lo) // 2

            # ! shift to the right
            # if odd left side has one more item
            partition_y = (x + y + 1) // 2 - partition_x

            maxLeftX = float(
                '-inf') if partition_x == 0 else nums1[partition_x - 1]
            minRightX = float(
                'inf') if partition_x == x else nums1[partition_x]

            maxLeftY = float(
                '-inf') if partition_y == 0 else nums2[partition_y - 1]
            minRightY = float(
                'inf') if partition_y == y else nums2[partition_y]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)

            elif maxLeftX > minRightY:

                hi = partition_x - 1
            else:
                lo = partition_x + 1


class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def mergeList(l1: List[int], l2: List[int]):
            p1 = 0
            p2 = 0
            n1 = len(l1)
            n2 = len(l2)

            new_list = []

            while p1 < n1 and p2 < n2:
                if l1[p1] < l2[p2]:
                    new_list.append(l1[p1])
                    p1 += 1
                else:
                    new_list.append(l2[p2])
                    p2 += 1

            for i in range(p1, n1):
                new_list.append(l1[i])

            for i in range(p2, n2):
                new_list.append(l2[i])

            return new_list

        l = mergeList(nums1, nums2)

        mid = (len(l) - 1) // 2

        if len(l) % 2 == 1:
            return float(l[mid])
        else:

            return (l[mid] + l[mid+1])/2


so = Solution()


nums1 = [1, 3]
nums2 = [2]


# nums1 = [1, 2]
# nums2 = [3, 4]

res = so.findMedianSortedArrays(nums1, nums2)


print(res)
