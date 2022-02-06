from typing import List


# find max 1 max2
import heapq


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        # edge cases

        if len(nums) == 1:
            if nums[0] == 0:
                return -1
            if nums[0] == 1:
                return 0

            return -1

        # max1 = 0
        # max2 = 0

        # for idx, n in enumerate(nums):
        #     if n >= nums[max1]:
        #         max2 = max1
        #         max1 = idx
        #     elif n >= nums[max2]:
        #         max2 = idx

        # print(nums[max1], nums[max2])

        # if nums[max1] >= nums[max2]*2:
        #     return max1
        # else:
        #     return -1

        max_heap = [(-num, idx) for idx, num in enumerate(nums)]

        heapq.heapify(max_heap)

        max1, idx1 = heapq.heappop(max_heap)
        max2, idx2 = heapq.heappop(max_heap)

        max1 = -max1
        max2 = -max2

        if max1 >= 2 * max2:
            return idx1

        else:
            return -1


so = Solution()

nums = [3, 6, 1, 0]

nums = [1, 0]

res = so.dominantIndex(nums)

print(res)
