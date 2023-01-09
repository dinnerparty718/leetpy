# 1991. Find the Middle Index in Array

from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        total_sum = sum(nums)
        cur_sum = 0

        for i, num in enumerate(nums):
            left = cur_sum
            right = total_sum - left - num
            if left == right:
                return i

            cur_sum += num

        return -1
