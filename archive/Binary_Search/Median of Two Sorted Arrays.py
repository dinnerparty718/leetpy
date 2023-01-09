from typing import List
import statistics
# hard
# https://www.youtube.com/watch?v=LPFhl65R7ww

# binary search on the smaller array. find a partition point of x, and derived the partition of y
# base on the formuarly   partition_x + partition_y = (len(x) + len(y) + 1) // 2, shifting to the right if it's even


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1)
        y = len(nums2)

        # making sure the nums1 is the smaller array
        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)

        if x == 0:
            mid = (y-1) // 2

            if y % 2 == 1:
                return nums2[mid]
            else:
                return (nums2[mid] + nums2[mid+1])/2

            # return statistics.median(nums2)

        # !important low, high is the partition point, not index
        low, high = 0, x

        # need to find that exacpt partition point
        while low <= high:

            partition_x = (low + high) // 2
            partition_y = (x + y + 1) // 2 - partition_x

            maxLeftX = float(
                '-inf') if partition_x == 0 else nums1[partition_x-1]
            minRightX = float(
                'inf') if partition_x == x else nums1[partition_x]

            maxLeftY = float(
                '-inf') if partition_y == 0 else nums2[partition_y-1]
            minRightY = float(
                'inf') if partition_y == y else nums2[partition_y]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partition_x - 1
            else:
                low = partition_x + 1


so = Solution()

# nums1 = [1, 2]
# nums2 = [3, 4]

nums1 = [2]
nums2 = []

res = so.findMedianSortedArrays(nums1, nums2)


print(res)
