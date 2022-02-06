import heapq
from typing import List

#! because of negative number
# min1 * min2 * max1    or
# max1 * max2 * max3

# sort ot heap

# sort
# Time O(nlogn)
# space O(n) for python


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # if len(nums) == 3:
        #     return nums[0] * nums[1] * nums[2]

        heapq.heapify(nums)

        min1, min2 = heapq.nsmallest(2, nums)
        max1, max2, max3 = heapq.nlargest(3, nums)

        return max(min1*min2*max1, max1*max2*max3)

# using simple scan
# time O(n)
# space O(1)


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = float('inf')
        min2 = float('inf')

        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')

        for n in nums:

            # handle min
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:
                min2 = n

            # handle max
            if n >= max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:
                max3 = max2
                max2 = n
            elif n >= max3:
                max3 = n

        return max(min1*min2*max1, max1 * max2 * max3)


so = Solution()

nums = [1, 2, 3]


res = so.maximumProduct(nums)


print(res)
